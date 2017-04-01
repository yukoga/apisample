#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import configparser


class Config(object):
    def __init__(self, file=None):
        config = configparser.ConfigParser()
        config._interpolation = configparser.ExtendedInterpolation()
        config.read(file)
        sections = config.sections()
        items = config.items(sections[0])
        for item in items:
            setattr(self, item[0], int(item[1]))
