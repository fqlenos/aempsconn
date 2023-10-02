"""
Test signal_handler
"""

import unittest
from unittest.mock import patch
import signal
from aempsconn.utils.signal_handler import signal_handler


class TestSignalHandler(unittest.TestCase):
    @patch("sys.exit")  # Mock the exit function
    def test_signal_handler(self, mock_exit):
        # Call the Ctrl + C with its system signal
        signal_handler(signal.SIGINT, None)

        # Check if sys.exit() is called and exits with code = 0
        mock_exit.assert_called_once_with(0)
