# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import paratranz_client
from paratranz_client.paths.projects_project_id_issues_issue_id import put  # noqa: E501
from paratranz_client import configuration, schemas, api_client

from .. import ApiTestMixin


class TestProjectsProjectIdIssuesIssueId(ApiTestMixin, unittest.TestCase):
    """
    ProjectsProjectIdIssuesIssueId unit test stubs
        修改讨论  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = put.ApiForput(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()