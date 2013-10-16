#!/usr/bin/env python
import requests
from gnupg import GPG
passphrase = None

if __name__ == "__main__":
    gpg = GPG()
    url = 'http://127.0.0.1:8000/students/crypto/'
    r = requests.get(url)
    print 'cifrado', r.text
    content = gpg.decrypt(r.text, always_trust=True, passphrase=passphrase)
    print 'decifrado'
    if not content:
        print 'No se pudo descifrar'
    else:
        print content
