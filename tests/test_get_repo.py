import os.path
import sys
sys.path.insert(0, os.path.realpath('../'))

import unittest2
from evcs.backends.hg import MercurialRepository
from evcs import get_backend, get_repo

class TestGetRepo(unittest2.TestCase):

    def test_get_hg_backend(self):
        hg = get_backend('hg')
        self.assertEqual(hg, MercurialRepository)

    def test_get_hg_repo(self):
        repo = get_repo('sample_hg')
        self.assertTrue(isinstance(repo, MercurialRepository))
