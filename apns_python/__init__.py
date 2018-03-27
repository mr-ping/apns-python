"""
Version: 0.1.2-beta

apns-python is a package to commmunicate with Apple Push Notification Service (APNs).
It support the HTTP2.0 protocol with APNs.

PYPI:
    https://pypi.python.org/pypi/apns-python

Project Home:
    GitHub: https://github.com/mr-ping/apns-python

Project Documents:
    readthedocs: http://apns-python.readthedocs.io

You can use either Alert, APS, Payload, Headers and Client objects directly or
use them with their module prefix like notification.Alert
"""

from notification import Alert, APS, Payload, Headers
from client import Client
