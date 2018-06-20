import sys
from urllib.request import Request, urlopen
from datetime import datetime


def crawling(
        url='',
        encoding='utf-8',
        proc = lambda html : html,
        store =lambda html : html,
        err=lambda e: print('%s : %s' % (e, datetime.now()), file=sys.stderr)):
    try:
        request = Request(url)
        resp = urlopen(request)

        try:
            receive = resp.read()
            result = store(proc(receive.decode(encoding)))
            # proc = proc(result)
            # if store is not None:
            #     store(result)
            #if proc is not None:
             #   result =proc(result)

        except UnicodeDecodeError:
            result = receive.decode(encoding, 'replace')
        print('%s: success for request [%s]' % (datetime.now, url))
        return result

    except Exception as e:
        err(e)