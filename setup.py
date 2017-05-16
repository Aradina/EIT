import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(name = "EIT", 
      version = "0.1",
      description = "Eve Intel Tool",
      executables = [Executable("EIT.py", base=base)]
    )