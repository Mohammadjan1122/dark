# Decompiled By RandiSr
# Github : https://github.com/RANDIOLOY
# uncompyle6 version 3.7.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.18 (default, Jan  8 2021, 21:22:37) 
# [GCC 4.2.1 Compatible Android (6454773 based on r365631c2) Clang 9.0.8 (https:/
# Embedded file name: Sumarr ID
import os, time
from app import config
from app import login
from app import crack
from src import friends_list
from src import friends
from src import search_name
from src import likes
from bs4 import BeautifulSoup as parser

class Brute(object):

    def __init__(self, url):
        self.url = url
        self.config = config.Config()
        self.cookie = self.config.loadCookie()
        self.menu = ''
        self.menu += ' \x1b[0;97m[\x1b[0;96m01\x1b[0;97m] Dump Id Frind\n'
        self.menu += ' \x1b[0;97m[\x1b[0;96m02\x1b[0;97m] Dump Id publick id \n'
        self.menu += ' \x1b[0;97m[\x1b[0;96m03\x1b[0;97m] Dump Id Pencarian Nama\n'
        self.menu += ' \x1b[0;97m[\x1b[0;96m04\x1b[0;97m] Dump Id  Like post\n'
        self.menu += ' \x1b[0;97m[\x1b[0;96m05\x1b[0;97m] Start Crack\n'
        self.menu += ' \x1b[0;97m[\x1b[0;96m06\x1b[0;97m] Hapus Cookies\n'
        self.menu += ' \x1b[0;97m[\x1b[0;96m07\x1b[0;97m] Update Tools\n'
        self.menu += ' \x1b[0;97m[\x1b[0;91m00\x1b[0;97m] Exit\n'
        self.menu += '\x1b[0;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
        if self.cookie == False:
            login.loginFb(self, self.url, self.config)
            self.cookie = self.config.loadCookie()

    def start(self):
        response = self.config.httpRequest(self.url + '/profile.php', self.cookie).encode('utf-8')
        if 'mbasic_logout_button' in str(response):
            self.main(response)
        else:
            os.remove('log/cookies.log')
            print '\n\x1b[0;91m[WARNING] Cookies invalids, please login again.\x1b[0m'
            raw_input('\n[ Press Enter]')
            login.loginFb(self, self.url, self.config)
            self.cookie = self.config.loadCookie()
            self.start()
            exit()

    def main(self, response):
        os.system('clear')
        print self.config.banner()
        html = parser(response, 'html.parser')
        print '\x1b[0;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
        print ('\x1b[0;97m [\x1b[0;95m\xc3\x97\x1b[0;97m] \x1b[0;96mNama Akun \x1b[0;91m:\x1b[0;93m ').decode('utf-8') + html.title.text.upper()
        print '\x1b[0;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
        print self.menu
        try:
            choose = int(raw_input('\x1b[1;97m [\x1b[1;94m\xe2\x80\xa2\x1b[1;91m\xe2\x80\xa2\x1b[1;97m] \x1b[90m\xe2\x96\xba\x1b[1;93m '))
        except ValueError:
            print '\n\x1b[0;97m [\x1b[0;91m!\x1b[0;97m]\x1b[0;91m Lihat Menu Dong Ajg'
            os.system('python2 crack.py')

        if choose == 1 or choose == 1:
            exit(friends_list.main(self, self.cookie, self.url, self.config))
        elif choose == 2 or choose == 2:
            exit(friends.main(self, self.cookie, self.url, self.config))
        elif choose == 3 or choose == 3:
            exit(search_name.main(self, self.cookie, self.url, self.config))
        elif choose == 4 or choose == 4:
            exit(likes.main(self, self.cookie, self.url, self.config))
        elif choose == 5 or choose == 5:
            ngentod = raw_input('\n\x1b[0;97m [\x1b[0;91mWARNING\x1b[0;97m] Sebelum Mulai Crack Anda Diharuskan Nge\n dump Id Terlebih Dahulu...\n \x1b[0;97m[\x1b[0;91m?\x1b[0;97m] Apakah Kamu Mengerti [y/n]\x1b[0;91m :\x1b[0;92m ')
            print '\x1b[0;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
            if ngentod.lower() == '':
                exit('\n  \x1b[0;91mTinggal Ketik y Atau n Apa Susahnya Sih Tlol!')
            elif ngentod.lower() == 'y':
                exit(crack.Brute().main())
            elif ngentod.lower() == 'n':
                os.system('python2 crack.py')
            else:
                exit('  \x1b[0;91mTinggal Ketik y Atau n Apa Susahnya Sih Tlol!')
        elif choose == 7 or choose == 7:
            print '\n\n\x1b[0;92m   [ \x1b[0;96mMohon Tunggu Sedang Meng Update Tools \x1b[0;92m]\n'
            time.sleep(2)
            os.system('git pull')
            print ' \n\x1b[0;97m[\x1b[0;92m\xe2\x9c\x93\x1b[0;97m]\x1b[0;92m Succesfull Di Update!\n'
            time.sleep(2)
            os.system('python2 crack.py')
        elif choose == 0 or choose == 0:
            print '\x1b[0;92m\n Terimakasih Sudah Memakai Tools Saya Jangan Lupa\n Subscribe My YouTube Channel...\n'
            time.sleep(2)
            os.system('xdg-open https://youtube.com/channel/UC6PezjDN1ofLSXn3onPxzpQ')
            os.system('exit')
            os.system('exit')
        elif choose == 6 or choose == 6:
            ask = raw_input('\n\x1b[0;97mApakah Kamu Yakin \nIngin Menghapus Cookies? [y/n]\x1b[0;91m :\x1b[0;92m ')
            if ask.lower() == 'y':
                print '\n \x1b[0;97m  [\x1b[0;95m\xe2\x80\xa2\x1b[0;97m] Mengahapus cokiies\x1b[0;92m...'
                time.sleep(2)
                os.remove('log/cookies.log')
                print '\n\x1b[0;97m  [\x1b[0;92m\xe2\x88\x9a\x1b[0;97m] \x1b[0;92mCookiis Succesfull Terhapus!'
                time.sleep(2)
                login.loginFb(self, self.url, self.config)
                self.cookie = self.config.loadCookie()
                self.start()
            else:
                self.cookie = self.config.loadCookie()
                print '\n\x1b[0;97m  [\x1b[0;91m!\x1b[0;97m] \x1b[0;91mBatal Terhapus'
                self.start()
        else:
            print '\n \x1b[0;97m[\x1b[0;91m!\x1b[0;97m] \x1b[0;91mLihat Menu Dong Ajg'
            os.system('python2 crack.py')