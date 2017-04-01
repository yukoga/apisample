#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Task(object):
    def __init__(self, name, config):
        self.config = config
        self._name = name

    @property
    def name(self):
        return self._name

#    def fetch(self):
#        return 'Fetch data.'

    def put(self):
        return 'success'

    def fetch(self):
        retry = 0

        def do_task():
            nonlocal retry
            if retry < self.config.max_retry:
                msg = self.fetch()
                retry += 1
                return 'Fetch data.'
            else:
                msg = self.log()
                return msg
        return do_task

    def log(self):
        return 'Log.'

    def raise_my_exception(self):
        raise ValueError('This is my exception.')
