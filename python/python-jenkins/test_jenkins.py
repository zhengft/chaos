#!/usr/bin/env python3

import json

import click
import jenkins
from lxml import etree


def get_server():
    server = jenkins.Jenkins('http://localhost:8080', username='root', password='secret')
    return server


class Cli:
    
    @staticmethod
    def aaa():
        pass

    @staticmethod
    def bbb():
        pass


@click.group()
def cli():
    pass


@cli.command()
def test_main():
    server = get_server()
    user = server.get_whoami()
    version = server.get_version()
    print('Hello %s from Jenkins %s' % (user['fullName'], version))

@cli.command()
def test_get_jobs():
    server = get_server()
    jobs = server.get_jobs()
    for job in jobs:
        print('job name: {0}'.format(job['name']))


@cli.command()
def test_get_job_info():
    server = get_server()
    job_info = server.get_job_info('simple-compile')
    print('buildable: {0}'.format(job_info['buildable']))
    print('description: {0}'.format(job_info['description']))
    print(json.dumps(job_info, indent='    '))


@cli.command()
def test_get_job_info_not_exists():
    server = get_server()
    job_info = server.get_job_info('job-not-exists')


@cli.command()
def test_enable_job():
    server = get_server()
    server.enable_job('simple-compile')


@cli.command()
def test_disable_job():
    server = get_server()
    server.disable_job('simple-compile')
    

@cli.command()
def test_get_job_config():
    server = get_server()
    job_config = server.get_job_config('simple-compile')
    root = etree.fromstring(job_config.encode())
    description = root.find('./description')
    print(description.text)


def reconfig_job(desc_text):
    server = get_server()
    job_config = server.get_job_config('simple-compile')
    root = etree.fromstring(job_config.encode())
    description = root.find('./description')
    description.text = desc_text
    # print(description.text)
    config_xml = etree.tostring(root).decode('utf-8')
    # print(config_xml)
    server.reconfig_job('simple-compile', config_xml)
    

@cli.command()
def test_reconfig_job():
    reconfig_job('test reconfig job')


@cli.command()
def test_reconfig_job_others():
    reconfig_job('test reconfig job others')


@cli.command()
def test_parse_fromstring():
    root = etree.fromstring('<root>data</root>')
    print(root)


@cli.command()
def test_view_class():
    for key, value in Cli.__dict__.items():
        pass


@cli.command()
def test_datetime():
    pass


if __name__ == '__main__':
    cli()
