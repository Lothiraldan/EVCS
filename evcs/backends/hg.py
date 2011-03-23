from mercurial import hgweb
from vcs.backends.hg import MercurialRepository
import threading

class MercurialRepository(MercurialRepository):

    def serve(self, host = None, port = None):

        if host is not None:
            self.baseui.setconfig('web', 'adress', host)

        if port is not None:
            self.baseui.setconfig('web', 'port', port)

        return MercurialServer(self._repo, self.baseui)

class MercurialServer(object):
    """
    Mercurial Repository Server.
    """
    def __init__(self, repository, ui):

        #Create the server
        app = hgweb.hgweb(repository.root, ui)
        self.httpd = hgweb.server.create_server(ui, app)

        #Compute address
        if self.httpd.prefix:
            self.prefix = self.httpd.prefix.strip('/') + '/'
        else:
            self.prefix = ''

        self._port = self.httpd.port
        self.port = ':%d' % self.httpd.port
        if self.port == ':80':
            self.port = ''

        self.host = self.httpd.fqaddr
        if ':' in self.host:
            self.host = '[%s]' % fqaddr

        self.http_address = 'http://%s%s/%s' % (self.host, self.port,
                                                self.prefix)

        #Start server
        self.thread_server = threading.Thread(target = self.httpd.serve_forever)
        self.thread_server.start()

    def shutdown(self):
        """
        Ask server to stop
        """
        self.httpd.shutdown()
        self.thread_server.join()
