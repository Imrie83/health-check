#!/usr/bin/env python3

import os
import sys

def check_rebood():
    """Returns True if the computer has a pending rebood."""
    return os.path.exists("/run/reboot-required")

def main():
    if check_rebood():
        print('Pending Reboot.')
        sys.exit(1)
    print('Everything ok.')
    sys.exit(0)

main()
