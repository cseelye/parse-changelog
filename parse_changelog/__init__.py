import os

def get_version():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    try:
        with open(os.path.join(dir_path, "VERSION")) as vf:
            version = vf.read().strip()
    except Exception:
        version = "0.0.0"

    return version
