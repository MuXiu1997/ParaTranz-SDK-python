# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import paratranz_client
from paratranz_client.paths.projects_project_id_terms import post  # noqa: E501
from paratranz_client import configuration, schemas, api_client

from .. import ApiTestMixin


class TestProjectsProjectIdTerms(ApiTestMixin, unittest.TestCase):
    """
    ProjectsProjectIdTerms unit test stubs
        创建术语  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = post.ApiForpost(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200






if __name__ == '__main__':
    unittest.main()
