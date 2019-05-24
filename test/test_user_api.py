# coding: utf-8

"""
    predictor_scoring

    Credit Score Predictor  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.user_api import UserApi  # noqa: E501
from swagger_client.rest import ApiException


class TestUserApi(unittest.TestCase):
    """UserApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.user_api.UserApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_login(self):
        """Test case for login

        Logs the user in  # noqa: E501
        """
        pass

    def test_renew_token(self):
        """Test case for renew_token

        The user renews access token and refresh token  # noqa: E501
        """
        pass

    def test_revoke_refresh_token(self):
        """Test case for revoke_refresh_token

        The user revokes a refresh token  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
