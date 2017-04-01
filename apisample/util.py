#!/usr/bin/env python
# -*- coding: UTF-8 -*-


import signal


class Struct(object):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


def set_timeout(handler=None, latency=5, param=None):
    def signal_handler(*args):
        handler(param)
    signal.signal(signal.SIGALRM, signal_handler)
    signal.setitimer(signal.ITIMER_REAL, latency)
