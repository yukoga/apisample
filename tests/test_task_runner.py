#!/usr/bin/env python
# -*- coding: UTF-8 -*-


import pytest
from warnings import warn
from .context import apisample
from apisample.config import Config
from apisample.task import Task
from apisample.task_runner import TaskRunner


@pytest.fixture
def data():
    try:
        data = dict()
        config = Config('./config.ini')
        runner = TaskRunner()
        data['config'] = config
        data['runner'] = runner
        return data
    except Exception as e:
        warn('Failed to instantiate TaskRunner. {}'.format(e))


def test_append(data):
    runner = data['runner']
    len_tasks = len(runner.tasks)
    config = data['config']
    task = Task('append_test', config)
    runner.append(task)
    assert task.name == 'append_test'
    assert len(runner.tasks) == len_tasks + 1


def test_pop(data):
    runner = data['runner']
    config = data['config']
    runner.append(Task('left', config))
    runner.append(Task('middle', config))
    runner.append(Task('right', config))
    len_tasks = len(runner.tasks)
    popped = runner.pop()
    assert isinstance(popped, Task)
    assert popped.name == 'right'
    assert len(runner.tasks) == len_tasks - 1


def test_popleft(data):
    runner = data['runner']
    config = data['config']
    runner.append(Task('left', config))
    runner.append(Task('middle', config))
    runner.append(Task('right', config))
    len_tasks = len(runner.tasks)
    popped = runner.popleft()
    assert isinstance(popped, Task)
    assert popped.name == 'left'
    assert len(runner.tasks) == len_tasks - 1


def test_run(data):
    assert data['runner'].run() == 'Run task.'
