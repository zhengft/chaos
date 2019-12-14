#!/usr/bin/env python3

from datetime import datetime

import click


class JenkinsInfo:
    def __init__(self, url, username, password):
        self.url = url
        self.username = username
        self.password = password


class JenkinsJob:
    def __init__(self, url, job_name):
        self.url = url
        self.job_name = job_name


class TenantData:
    pass


class JenkinsOperator:
    pass


class JenkinsManager:

    def __init__(self, jenkins_info: JenkinsInfo, tenant_data: TenantData, operator: JenkinsOperator):
        self._jenkins_info = jenkins_info
        self._tenant_data = tenant_data
        self._operator = operator

    def disable_job(self, job_name):
        now = datetime.now()
        date_str = now.strftime('%Y-%m-%d')
        time_str = now.strftime('%H:%M')

        description = '禁用工程, zhengfeiteng, {0}, {1}'.format(date_str, time_str)

        self._tenant_data.add_disable_info(self._jenkins_info.url, job_name, description)
        self._operator.disable_job(self._jenkins_info, job_name)
        self._operator.set_job_description(self._jenkins_info, job_name, description)
            

class FakeTenantData:
    def add_disable_info(self, url, job_name, description):
        print('add_disable_info')
        print('url : {0}'.format(url))
        print('job_name : {0}'.format(job_name))
        print('description : {0}'.format(description))
        print('-----')


class FakeJenkinsOperator:
    def disable_job(self, jenkins_info, job_name):
        print('disable_job')
        print('url : {0.url}'.format(jenkins_info))
        print('job_name : {0}'.format(job_name))
        print('-----')

    def set_job_description(self, jenkins_info, job_name, description):
        print('set_job_description')
        print('url : {0.url}'.format(jenkins_info))
        print('job_name : {0}'.format(job_name))
        print('description : {0}'.format(description))
        print('-----')


@click.group()
def cli():
    pass

@cli.command()
def test():
    jenkins_info = JenkinsInfo('http://localhost:8080', username='root', password='1199a58f1a1857c69425979228d20899e1')
    tenant_data = FakeTenantData()
    operator = FakeJenkinsOperator()

    jenkins_manager = JenkinsManager(jenkins_info, tenant_data, operator)
    jenkins_manager.disable_job('simple-compile')


if __name__ == '__main__':
    cli()
