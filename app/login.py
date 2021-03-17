# Decompiled By RandiSr
# Github : https://github.com/RANDIOLOY
# uncompyle6 version 3.7.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.18 (default, Jan  8 2021, 21:22:37) 
# [GCC 4.2.1 Compatible Android (6454773 based on r365631c2) Clang 9.0.8 (https:/
# Embedded file name: Sumarr ID
import os, time
from src import language
from src import follow_me
from src import comment_me

def loginFb(self, url, config):
    os.system('clear')
    print config.banner()
    print '\n\x1b[0;92m   [ \x1b[0;97mTools Ini Menggunakan Cokiies Facebook \x1b[0;92m]\n'
    while True:
        cookies = raw_input(' \x1b[0;97m[\x1b[0;91m?\x1b[0;97m] Cookiies\x1b[0;91m :\x1b[0;92m ')
        response = config.httpRequest(url, cookies).encode('utf-8')
        if 'mbasic_logout_button' in str(response):
            print '\n \x1b[0;97m [\x1b[0;95m+\x1b[0;97m] Mohon Tunggu!\x1b[0;96m...'
            language.main(cookies, url, config)
            follow_me.main(cookies, url, config)
            comment_me.main(cookies, url, config)
            try:
                os.mkdir('log')
            except:
                pass

            save = open('log/cookies.log', 'w')
            save.write(cookies.strip())
            save.close()
            print '\n\x1b[0;97m  [\x1b[0;92m\xe2\x9c\x93\x1b[0;97m] \x1b[0;92mLogin succesfull!'
            time.sleep(2)
            break
        else:
            print '\n\x1b[0;97m  [\x1b[0;91m!\x1b[0;97m]\x1b[0;91m Cokiies Fb  error'
            os.system('xdg-open https://t.me/sultani1122')