# -*- coding: utf-8 -*-
from os import getenv as get


class Config(object):
    def __init__(self):
        self.redis_conn = get('REDIS_CONN', 'redis://:pythonrq@127.0.0.1:6666/0')


app_config = Config()
