# -*- coding: utf-8 -*-
"""
    evcs
    ~~~~

    Extended Various version Control System (vcs) is an overlayer over vcs, an
    scm abstraction layer written in python.

    :created_on: March 23, 2011
    :copyright: (c) 2010-2011 by Marcin Kuzminski, Lukasz Balcerzak, Boris Feld.
"""

__all__ = [
    'get_version', 'get_repo', 'get_backend', 'BACKENDS',
    'VCSError', 'RepositoryError', 'ChangesetError']

from vcs import get_version
from evcs.backends import get_repo, get_backend, BACKENDS
from vcs.exceptions import VCSError, RepositoryError, ChangesetError
