import json
import urllib

from edgar import logger


def _decode_response(response):
    raw, decoded, parsed = None, None, None
    try:
        logger.debug('decoding response from %s', response.geturl())
        raw = response.read()
        logger.debug('read raw response %s', raw)
        encoding = response.info().get_content_charset('utf-8')
        logger.debug('decoding response using %s', encoding)
        decoded = raw.decode(encoding)
        logger.debug('decoded response, decoded=%s', decoded)
        parsed = json.loads(decoded)
        logger.debug('parsed decoded response, parsed=%s', parsed)
        return response.getcode(), parsed
    except json.JSONDecodeError:
        best = parsed or decoded or raw
        logger.debug('could not parse response, leaving as %s', type(best))
        return best


def _make_request(url, method='GET', params={}, data={}, headers={}):
    logger.info('creating %s request for %s', method, url)

    if params:
        url += f'?{urllib.parse.urlencode(params)}'
        logger.debug('encoding params=%s into url=%s', params, url)

    headers.update({
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    })

    logger.debug('using headers=%s', headers)

    if data:
        data = json.dumps(data).encode('utf8')
        logger.debug('using data=%s', data)

    request = urllib.request.Request(
        url=url, method=method,
        headers=headers, data=data
    )

    try:
        with urllib.request.urlopen(request) as response:
            return _decode_response(response)
    except urllib.request.HTTPError as e:
        logger.error('request to %s returned a %s', e.geturl(), e.getcode())
        return _decode_response(e)


def post(url, data={}, params={}, headers={}):
    return _make_request(
        url, method='POST', params=params,
        data=data, headers=headers
    )


def get(url, params={}, headers={}):
    return _make_request(
        url, method='GET', params=params, headers=headers
    )
