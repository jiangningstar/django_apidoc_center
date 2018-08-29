#!/usr/bin/env python
# -*- coding:utf8 -*-

import commands
import os
import logging
import time
from watchdog.events import LoggingEventHandler, PatternMatchingEventHandler
from watchdog.observers import Observer
from django.conf import settings


class ApiDoc(object):
    def __init__(self, monitor_path, output):
        self.monitor_path = monitor_path
        self.output = output

    def run(self):
        (status, output) = commands.getstatusoutput('apidoc -i %s -o %s' % (self.monitor_path, self.output))
        return status, output


INIT_FILE = os.path.join(os.path.dirname(__file__), '__init__.py')

try:
    paths_to_watch = [{'path': './aiops_core', 'patterns': ['*.py'], 'ignore_directories': True}]
except AttributeError:
    try:
        paths_to_watch = [{'path': './aiops_core', 'patterns': ['*.py'], 'ignore_directories': True}]
    except AttributeError:
        message = """
            paths_to_watch is error
        """
        raise message


class EventHandler(PatternMatchingEventHandler):
    def process(self, event):
        """
        event.event_type
            'modified' | 'created' | 'moved' | 'deleted'
        event.is_directory
            True | False
        event.src_path
            path/to/observed/file
        """
        api_doc = ApiDoc(monitor_path=monitor_path, output=output)
        print (api_doc.run())
        print (event.src_path, event.event_type)

    def on_created(self, event):
        self.process(event)


def work_apidoc(paths_to_watch_d):
    observer = Observer()

    for path in paths_to_watch_d:
        event_handler = EventHandler(
            patterns=path.get('patterns', ['*.py']),
            ignore_directories=path.get('ignore_directories', True),
        )

        observer.schedule(
            event_handler,
            path['path'],
            recursive=path.get('recursive', True),
        )

    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    event_handler2 = LoggingEventHandler()
    observer.add_handler_for_watch(event_handler2, observer)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


def test():
    while True:
        time.sleep(1)


if __name__ == '__main__':
    monitor_path = settings.GIT_PULL_FILE_PATH
    output = '/data/apidoc'
    apidoc = ApiDoc(monitor_path, output)
    apidoc.run()
    paths_to_watch[0]["path"] = monitor_path
    work_apidoc(paths_to_watch)
