from setuptools import setup
from parse_changelog import get_version

try:
    version = get_version()
except Exception:
    version = "unknown"
try:
    with open("README.md") as readme_file:
        readme = readme_file.read()
except Exception:
    readme = ""

setup(
    name="parse-changelog",
    version=version,
    description="A very simplistic changelog parser/updater",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/cseelye/parse-changelog",
    author="Carl Seelye",
    author_email="cseelye@gmail.com",
    license="MIT",
    scripts=["bin/parse-changelog"],
    packages=["parse_changelog"],
    package_data={"": ["parse_changelog/VERSION", "LICENSE"]},
    include_package_data=True
)
