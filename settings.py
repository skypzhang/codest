#coding=u8
# -*- coding: UTF-8 -*-

from globall import global_variable
import main
import sys
import base64


res = main.reading_conf(sys.argv[2])
src,host,user,password,port,dumper_method,separ = res[0][:7]
def b64_decode(bstring):
    code = base64.b64decode(bstring).decode('utf-8')
    return code

#mysql_connect = {'host': host, 'user': b64_decode(user), 'password': b64_decode(password), 'port': b64_decode(port)}

mysql_connect = {'host': host, 'user': user, 'password': password, 'port': port}

print(mysql_connect)

delimiter_dict = {src: separ}
print(delimiter_dict)

if __name__ == '__main__':
    global_variable.variable_name()
    


    
