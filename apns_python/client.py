import os
import ujson

from hyper import tls, HTTP20Connection


class Client(object):
    """The client for APNs provider."""
    dev_apns_host = 'api.development.push.apple.com:443'
    prd_apns_host = 'api.push.apple.com:443'
    apns_method = 'POST'
    apns_path = '/3/device/'
    def __init__(
            self, push_mode='dev', secure=True, cert_location=None,
            cert_password=None):
        if push_mode == 'dev':
            self.apns_host = Client.dev_apns_host
        elif push_mode == 'prd':
            self.apns_host = Client.prd_apns_host
        else:
            err_msg = (
                'The push_mode param must be "dev" or "prd", not {0}'.format(
                    push_mode))
            raise ValueError(err_msg)
        if cert_location:
            ssl_context_obj = tls.init_context(
                cert=cert_location, cert_password=cert_password)
        else:
            ssl_context_obj = None
        self.conn = HTTP20Connection(
            self.apns_host, secure=secure, ssl_context=ssl_context_obj)

    def send(self, device_token, headers, payload):
        body = ujson.dumps(payload)
        complete_apns_path = os.path.join(Client.apns_path, device_token)
        session_id = self.conn.request(
            method=Client.apns_method, url=complete_apns_path, body=body,
            headers=headers)
        resp = self.conn.get_response()
        status_code = resp.status
        apns_id = resp.headers.get('apns-id')
        if status_code == 200:
            result = dict(
                session_id=session_id,
                apns_id=apns_id,
                status_code=resp.status)
        else:
            resp_body = ujson.loads(resp.read())
            result = dict(
                session_id=session_id,
                apns_id=apns_id,
                status_code=status_code,
                reason=resp_body.get('reason'),
                timestamp=resp_body.get('timestamp'))
        return result
