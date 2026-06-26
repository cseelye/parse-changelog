import os
import pathlib
import subprocess
import sys
import tempfile
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]
CLI = ROOT / "bin" / "parse-changelog"


class SecurityTests(unittest.TestCase):
    def test_add_change_does_not_follow_fixed_tempfile_symlink(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            workdir = pathlib.Path(tmpdir)
            changelog = workdir / "CHANGELOG.md"
            changelog.write_text(
                "# Changelog\n\n"
                "## [Unreleased]\n"
                "### Fixed\n"
                "* Existing fix\n",
                encoding="utf-8",
            )
            victim = workdir / "victim.txt"
            victim.write_text("do not change\n", encoding="utf-8")
            os.symlink(victim, workdir / ".CHANGELOG.md.new")

            subprocess.run(
                [
                    sys.executable,
                    str(CLI),
                    "--changelog",
                    str(changelog),
                    "--add-change",
                    "Safe temp files",
                    "--type",
                    "fixed",
                ],
                cwd=workdir,
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )

            self.assertEqual(victim.read_text(encoding="utf-8"), "do not change\n")
            self.assertFalse(changelog.is_symlink())
            self.assertIn("Safe temp files", changelog.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
