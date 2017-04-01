#!/usr/bin/env python
# -*- coding: UTF-8 -*-


import pytest
from warnings import warn
from .context import apisample
from apisample.util import set_timeout
from apisample.util import Struct


@pytest.fixture
def data():
    try:
        data = dict()
        args = {'a': 1, 'b': 10, 'c': 'This is my message.'}
        data['struct'] = Struct(**args)
        return data
    except Exception as e:
        warn('Failed to instantiate. {}'.format(e))


def test_init_struct(data):
    struct = data['struct']
    assert struct.a == 1
    assert struct.b == 10
    assert struct.c == 'This is my message.'


def test_set_timeout(data):
    set_timeout(lambda x: x**2, 3)
