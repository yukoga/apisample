#!/usr/bin/env python
# -*- coding: UTF-8 -*-


from collections import deque


class TaskRunner(object):
    def __init__(self):
        self.tasks = deque([])

    def append(self, task):
        self.tasks.append(task)

    def pop(self):
        return self.tasks.pop()

    def popleft(self):
        return self.tasks.popleft()

    def run(self):
        return 'Run task.'
