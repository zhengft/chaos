#!/usr/bin/env python3

import argparse
from typing import List


class MockScript:
    def __init__(self, script: str, result: bool):
        self._script = script
        self._result = result

    def __call__(self):
        print('mock script {0}, result is {1}'.format(self._script, self._result))


class MockScripts:
    def __init__(self, scripts: List[str], result: bool):
        self._scripts = scripts
        self._result = result

    def __call__(self):
        for script in self._scripts:
            print('mock script {0}, result is {1}'.format(script, self._result))


class ProcessNode:
    def __init__(self, name, parser, arg_commands):
        # name for debug
        self.name = name
        self.parser = parser
        self.arg_commands = arg_commands


def set_parser_args_commands(parser: argparse.ArgumentParser, args_commands_dict):
    process_queue = [ ProcessNode('__root__', parser, args_commands_dict) ]

    for node in process_queue:
        if isinstance(node.arg_commands, dict):
            node.parser.set_defaults(func=node.parser.print_help)

            subparsers = node.parser.add_subparsers()
            for subarg in node.arg_commands.keys():
                subparser = subparsers.add_parser(subarg)
                pending_node = ProcessNode(subarg, subparser, node.arg_commands[subarg])
                process_queue.append(pending_node)
        else:
            node.parser.set_defaults(func=node.arg_commands)


def main():
    args_commands_dict = {
        'mock': {
            'firmware': {
                'success': MockScript('firmware', True),
                'failed': MockScript('firmware', False),
            },
            'driver': {
                'success': MockScript('driver', True),
                'failed': MockScript('driver', False),
            },
            'runtime': {
                'success': MockScript('runtime', True),
                'failed': MockScript('runtime', False),
            },
        },
    }
    parser = argparse.ArgumentParser()
    set_parser_args_commands(parser, args_commands_dict)
    args = parser.parse_args()
    args.func()


if __name__ == '__main__':
    main()
