import os

# List RELATIVE paths (from this file) to story files here.
_STORY_FILES = [
    "slant.markdown",
    "stc.markdown",
    "data.markdown",
    "seattle_stage.markdown",
    "thehub.markdown",
    ]

_DIRECTORY_PATH = os.path.dirname(os.path.abspath(__file__))

# files is the public-facing part of the directory. It should be an iterable
# object that contains the ABSOLUTE PATHS to all of the files.
files = [os.path.join(_DIRECTORY_PATH, f) for f in _STORY_FILES]
