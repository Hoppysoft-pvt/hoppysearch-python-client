# coding: utf-8

"""
    SearchHS

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.general_api import GeneralApi  # noqa: E501
from swagger_client.rest import ApiException


class TestGeneralApi(unittest.TestCase):
    """GeneralApi unit test stubs"""

    def setUp(self):
        self.api = GeneralApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_v1_clear_index_delete(self):
        """Test case for v1_clear_index_delete

        /clearIndex  # noqa: E501
        """
        pass

    def test_v1_delete_post(self):
        """Test case for v1_delete_post

        /delete  # noqa: E501
        """
        pass

    def test_v1_index_post(self):
        """Test case for v1_index_post

        /index  # noqa: E501
        """
        pass

    def test_v1_search_get(self):
        """Test case for v1_search_get

        /search (simple search)  # noqa: E501
        """
        pass

    def test_v1_search_post(self):
        """Test case for v1_search_post

        /search  # noqa: E501
        """
        pass

    def test_v1_stats_get(self):
        """Test case for v1_stats_get

        /stats  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
