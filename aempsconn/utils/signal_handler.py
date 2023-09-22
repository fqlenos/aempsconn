"""
Utility for handling: "Ctrl + c"
"""

import signal
import sys


def signal_handler(sig, frame):
    print("Handling exit...")
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)
