"""
Test signal_handler
"""

import signal
from unittest import TestCase
from unittest.mock import patch

from aempsconn.utils.signal_handler import signal_handler


class TestSignalHandler(TestCase):
    @patch("sys.exit")  # Mock the exit function
    def test_signal_handler(self, mock_exit):
        # Call the Ctrl + C with its system signal
        signal_handler(signal.SIGINT, None)

        # Check if sys.exit() is called and exits with code = 0
        mock_exit.assert_called_once_with(0)
