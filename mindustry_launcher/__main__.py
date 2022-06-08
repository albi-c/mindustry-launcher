import argparse

from .launcher import Launcher
from ._version import __version__

parser = argparse.ArgumentParser(description="mindustry launcher", prog="mindustry_launcher")

parser.add_argument("version", help="version to launch")

parser.add_argument("-V", "--version", action="version", version=f"mindustry_launcher {__version__}")

args = parser.parse_args()

if args.version == "GUI":
    pass
else:
    Launcher.launch(args.version)
