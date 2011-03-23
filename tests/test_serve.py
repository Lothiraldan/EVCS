import os.path
import sys
sys.path.insert(0, os.path.realpath('../'))

from evcs.backends.hg import MercurialRepository
from os.path import join
import tempfile
import unittest2
import random
import socket

class MercurialServeTest(unittest2.TestCase):
    def setUp(self):
        #Create the repo
        self.repo = MercurialRepository('sample_hg')

    def test_serve_and_pull(self):
        temppath = tempfile.mkdtemp()

        repo_new = MercurialRepository(temppath, create = True)
        self.assertTrue(len(self.repo.revisions) > len(repo_new.revisions))

        server = self.repo.serve()
        try:
            repo_new.pull(server.http_address)
        finally:
            server.shutdown()

        repo_new = MercurialRepository(temppath)
        self.assertTrue(len(self.repo.revisions) == len(repo_new.revisions))

    def test_set_port_and_adress(self):
        temppath = tempfile.mkdtemp()
        repo_new = MercurialRepository(temppath, create = True)
        self.assertTrue(len(self.repo.revisions) > len(repo_new.revisions))

        port = random.randint(5000, 10000)
        host = 'localhost'

        server = self.repo.serve(host = host, port = port)
        try:
            repo_new.pull(server.http_address)
        finally:
            server.shutdown()

        self.assertEquals(port, server._port)
        self.assertEquals(socket.getfqdn(), server.host)

        repo_new = MercurialRepository(temppath)
        self.assertTrue(len(self.repo.revisions) == len(repo_new.revisions))
