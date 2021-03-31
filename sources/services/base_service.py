

class BaseService(object):
    BASE = ''

    def __init__(self, conf):
        self.BASE = '{}/'.format(conf['server_url'])