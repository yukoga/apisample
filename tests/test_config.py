#!/usr/bin/env python
# -*- coding: UTF-8 -*-


import pytest
from warnings import warn
from .context import apisample
from apisample.config import Config


@pytest.fixture
def config():
    try:
        config = Config('./config.ini')
        return config
    except Exception as e:
        warn('Failed to instantiate Config. {}'.format(e))


def test_init(config):
    test_config = {
        'max_task': 10,
        'max_retry': 3,
        'interval': 300
    }
    assert config.max_task == test_config['max_task']
    assert config.max_retry == test_config['max_retry']
    assert config.interval == test_config['interval']
