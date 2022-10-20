from setuptools import setup, find_packages

# with open(os.path.join(mypackage_root_dir, 'VERSION')) as version_file:
#     version = version_file.read().strip()
try:
    with open("parse_changelog/VERSION") as version_file:
        version = version_file.read().strip()
except Exception:
    version = "unknown"

setup(
    name="parse-changelog",
    version=version,
    description="A very simplistic changelog parser/updater",
    url="https://github.com/cseelye/parse-changelog",
    author="Carl Seelye",
    author_email="cseelye@gmail.com",
    license="MIT",
    scripts=["bin/parse-changelog"],
    packages=["parse_changelog"],
    package_data={"": ["parse_changelog/VERSION", "LICENSE"]},
    include_package_data=True
)
