import os

def get_version():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    try:
        with open(os.path.join(dir_path, "VERSION"), encoding="utf-8") as vf:
            version = vf.read().strip()
    except Exception: #pylint: disable=broad-exception-caught
        version = "0.0.0"

    return version
