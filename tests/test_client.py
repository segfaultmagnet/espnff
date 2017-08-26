import json
import unittest
import requests_mock
from espnff.client import ESPNFF
from espnff.exception import AuthorizationError


class ESPNFFTestCase(unittest.TestCase):
    """Test ESPNFF Client"""
    @requests_mock.Mocker()
    def test_authorize(self, m):
        m.post(
            'https://registerdisney.go.com/jgc/v5/client/ESPN-FANTASYLM-PROD/api-key?langPref=en-US',
            status_code=200, headers={'api-key': '<API_KEY>'}
        )

        with open('tests/test_client.json') as f:
            data = json.load(f)

        m.post(
            'https://ha.registerdisney.go.com/jgc/v5/client/ESPN-FANTASYLM-PROD/guest/login?langPref=en-US',
            status_code=200, json=data
        )

        espnff = ESPNFF('<username>', '<password>')

        try:
            espnff.authorize()
        except AuthorizationError:
            self.fail('authorize() raised AuthorizationError unexpectedly')
