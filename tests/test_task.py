#!/usr/bin/env python
# -*- coding: UTF-8 -*-


import pytest
from warnings import warn
from .context import apisample
from apisample.config import Config
from apisample.task import Task


@pytest.fixture
def data():
    try:
        data = dict()
        config = Config('./config.ini')
        task = Task(name='MyTask', config=config)
        data['config'] = config
        data['task'] = task
        return data
    except Exception as e:
        warn('Failed to instantiate Task. {}'.format(e))


def test_name(data):
    assert data['task'].name == 'MyTask'


def test_put(data):
    assert data['task'].put() == 'success'


def test_fetch(data):
    t = data['task'].fetch()
    assert t() == 'Fetch data.'
    assert t() == 'Fetch data.'
    assert t() == 'Fetch data.'
    assert t() == 'Log.'


def test_log(data):
    assert data['task'].log() == 'Log.'


def test_raise_my_exception(data):
    with pytest.raises(ValueError, message='This is my exception.'):
        data['task'].raise_my_exception()
