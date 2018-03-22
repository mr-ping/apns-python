# apns-python package

**apns-python** is a package to help you to commmunicate with Apple Push Notification Service (APNs).


It support the HTTP2.0 protocol with APNs.

## Precondition

- Python 2.7.9 and later
- Python 3.5 and later


## Installation

Make sure you have pip installed.
If not, **install pip**

```
$ wget https://bootstrap.pypa.io/get-pip.py
$ python get-pip.py
```

**Install apns-python:**

```
$ pip install apns-python
```


## Demo

```python
from apns_python import Alert, APS, Payload, Headers, Client


alert = Alert(
    title='Notification Title',
    body='A preview content from apn-python')

aps = APS(
    alert=alert,
    badge=1,
    sound='sound.mp3')

payload = Payload(
    aps=aps,
    custom_fields=dict(
        customized_field='some data'))

headers = Headers(
    custom_fields={"Content-Type": "application/json; charset=utf-8"})

client = Client(
    push_mode='dev',
    secure=True,
    cert_location='/your/apns/certfile.pem',
    cert_password='APNsCertPassword')

result = client.send(target_device_token, headers, payload)

print result
```
