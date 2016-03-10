import unittest
from hooks import common
from unittest.mock import MagicMock


def perform_mock_request(url, message, success_log_message, color=None):
    print(url, message, success_log_message, color)


class TestStringMethods(unittest.TestCase):

    def test(self):
        common.perform_request = MagicMock(side_effect=perform_mock_request)


if __name__ == '__main__':
    unittest.main()
