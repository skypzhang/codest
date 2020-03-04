#!/usr/bin/env python3
#coding=gbk
import sys
import subprocess
import random
import string

all_chs = string.digits + string.ascii_letters

def gen_pass(n=8):
    result = ''
    for i in range(n):
        ch = random.choice(all_chs)
        result += ch
    return result


def add_user(username, password, fname):
    result = subprocess.run('id %s &> /dev/null' % username, shell=True)
    if result.returncode == 0:
        print('用户已存在')
        return
    subprocess.run('useradd %s' % username, shell=True)
    subprocess.run('echo %s | passwd --stdin %s ' % (password, username), shell=True)
    info = """user information:
username: %s
password: %s
""" % (username, password)
    with open(fname, 'a') as fobj:
        fobj.write(info)
if __name__ == '__main__':
    username = sys.argv[1]
    password = gen_pass()
    fname = sys.argv[2]
    add_user(username, password, fname)
