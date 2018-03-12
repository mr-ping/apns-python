# apns-python package


## Demonstration

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

CHEM_APNS_CLIENT = Client(
    push_mode='dev',
    secure=True,
    cert_location='/your/apns/certfile.pem',
    cert_password='APNsCertPassword')

result = client.send(device_token, headers, payload)

print result
'''
