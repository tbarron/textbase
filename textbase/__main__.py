"""
Usage:
    textbase edit [-d]
    textbase new [-d]
    textbase version [-d]
    textbase browse [-d]
    textbase find [-d]

textbase edit
    Edit an existing file

textbase new
    Create a new file (allow for naming it later)

textbase version
    Report the version of textbase

textbase browse
    Browse the available files

textbase find
    Search through available files for particular keywords
"""
from docopt_dispatch import dispatch
import os
import pdb
import textbase as tb


@dispatch.on('version')
def tb_version(**kw):
    """
    Report the version of textbase
    """
    if kw['d']:
        pdb.set_trace()
    print("textbase {} (TEXTBASE_ROOT='{}')"
          .format(tb.version(), os.getenv("TEXTBASE_ROOT")))


if __name__ == "__main__":
    dispatch(__doc__)
