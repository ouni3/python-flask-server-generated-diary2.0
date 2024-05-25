# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.diary_entry import DiaryEntry  # noqa: E501
from swagger_server.models.error import Error  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_diaries_date_get(self):
        """Test case for diaries_date_get

        Get diary entry by date
        """
        response = self.client.open(
            '/v1/diaries/{date}'.format(_date='2013-10-20'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_diaries_date_patch(self):
        """Test case for diaries_date_patch

        Update a diary entry
        """
        body = DiaryEntry()
        response = self.client.open(
            '/v1/diaries/{date}'.format(_date='2013-10-20'),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_diaries_get(self):
        """Test case for diaries_get

        Get all diary entries
        """
        response = self.client.open(
            '/v1/diaries',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_diaries_post(self):
        """Test case for diaries_post

        Create a new diary entry
        """
        body = DiaryEntry()
        response = self.client.open(
            '/v1/diaries',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
