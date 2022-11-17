import unittest
from unittest.mock import patch, Mock

from api import get_user_info


class TestAPI(unittest.TestCase):
    # @patch('api.requests')
    # def test_get_user_info(self, mock_requests):
    #     response_mock = Mock()
    #     response_mock.status_code = 200
    #     response_mock.json.return_value = {'login': 'test'}

    #     mock_requests.get.return_value = response_mock

    #     assert get_user_info('test') == {'login': 'test'}
    #     assert mock_requests.get.call_count

    def test_get_user_info_context_manager(self):
        response_mock = Mock()
        response_mock.status_code = 200
        response_mock.json.return_value = {'login': 'test'}

        with patch('api.requests') as mock_requests:
            mock_requests.get.return_value = response_mock

            assert get_user_info('test') == {'login': 'test'}
            assert mock_requests.get.call_count

    def test_get_user_info_context_manager_github_error(self):
        response_mock = Mock()
        response_mock_2 = Mock()
        response_mock.status_code = 500

        with patch('api.requests') as mock_requests:
            mock_requests.get.return_value = response_mock

            assert get_user_info('test') is None
            assert mock_requests.call_count == 1


unittest.main()
