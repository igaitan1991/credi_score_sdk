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
from swagger_client.api.predictor_scoring_api import PredictorScoringApi  # noqa: E501
from swagger_client.rest import ApiException


class TestPredictorScoringApi(unittest.TestCase):
    """PredictorScoringApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.predictor_scoring_api.PredictorScoringApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_cancel_and_delete_batch_execution(self):
        """Test case for cancel_and_delete_batch_execution

        Cancels and deletes all batch executions for predictor_scoring.  # noqa: E501
        """
        pass

    def test_get_batch_execution_file(self):
        """Test case for get_batch_execution_file

        Gets a specific file from an execution in predictor_scoring.  # noqa: E501
        """
        pass

    def test_get_batch_execution_files(self):
        """Test case for get_batch_execution_files

        Gets all files from an individual execution in predictor_scoring.  # noqa: E501
        """
        pass

    def test_get_batch_execution_status(self):
        """Test case for get_batch_execution_status

        Gets all batch executions for predictor_scoring.  # noqa: E501
        """
        pass

    def test_get_batch_executions(self):
        """Test case for get_batch_executions

        Gets all batch executions for predictor_scoring.  # noqa: E501
        """
        pass

    def test_predictor_scoring(self):
        """Test case for predictor_scoring

        """
        pass

    def test_start_batch_execution(self):
        """Test case for start_batch_execution

        """
        pass


if __name__ == '__main__':
    unittest.main()
