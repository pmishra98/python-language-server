# NB: posixpath.pyi, ntpath.pyi, and macpath.pyi must remain consistent!
# Stubs for os.path
# Ron Murawski <ron@horizonchess.com>

# based on http://docs.python.org/3.2/library/os.path.html
import sys
from typing import Any, List, Tuple, IO

# ----- os.path variables -----
supports_unicode_filenames = False

# ----- os.path function stubs -----
def abspath(path: str) -> str: ...
def basename(path) -> str: ...
def commonprefix(list: List[str]) -> str: ...
def dirname(path: str) -> str: ...
def exists(path: str) -> bool: ...
def lexists(path: str) -> bool: ...
def expanduser(path: str) -> str: ...
def expandvars(path: str) -> str: ...
def getatime(path: str) -> int:
    ...  # return float if os.stat_float_times() returns True
def getmtime(path: str) -> int:
    ...  # return float if os.stat_float_times() returns True
def getctime(path: str) -> int:
    ...  # return float if os.stat_float_times() returns True
def getsize(path: str) -> int: ...
def isabs(path: str) -> bool: ...
def isfile(path: str) -> bool: ...
def isdir(path: str) -> bool: ...
def islink(path: str) -> bool: ...
def ismount(path: str) -> bool: ...
def join(path: str, *paths: str) -> str: ...
def normcase(path: str) -> str: ...
def normpath(path: str) -> str: ...
def realpath(path: str) -> str: ...
def relpath(path: str, start: str = ...) -> str: ...
def samefile(path1: str, path2: str) -> bool: ...

def sameopenfile(fp1: IO[Any], fp2: IO[Any]) -> bool: ...

# def samestat(stat1: stat_result, stat2: stat_result) -> bool:
#    ...  # Unix only
def split(path: str) -> Tuple[str, str]: ...
def splitdrive(path: str) -> Tuple[str, str]: ...
def splitext(path: str) -> Tuple[str, str]: ...
if sys.version_info < (3, 7) and sys.platform == 'win32':
    def splitunc(path: str) -> Tuple[str, str]: ...
