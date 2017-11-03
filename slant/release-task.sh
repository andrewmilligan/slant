#!/bin/bash

DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )

# RELOAD THE PORTFOLIO PROJECTS
python "$DIR/manage.py" loadportfolio
if [[ $? -ne 0 ]]; then
  echo "Failure loading portfolio stories."
  exit 1
fi

# RELOAD THE SLANT STORIES
python "$DIR/manage.py" dvloadstories
if [[ $? -ne 0 ]]; then
  echo "Failure loading dataviz stories."
  exit 1
fi

# Everything worked, so exit cleanly
exit 0
