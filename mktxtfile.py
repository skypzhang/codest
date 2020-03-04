#!/usr/bin/env python3
import os
def get_fname():
    while 1:
        filename = input('请输入文件名: ')
        if not os.path.exists(filename):
            break
        print('s% 已存在，请重试。' % filename)
    return filename
def get_contents():
    contents = []
    print('请输入内容，结束请输入end。')
    while True:
        line = input('> ')
        if line == 'end':
            break
        contents.append(line)
    return contents
def wfile(fname, contents):
    with open(fname, 'w') as fobj:
        fobj.writelines(contents)

if __name__ == '__main__':
      fname = get_fname()
      contents = get_contents()
      contents = ['%s\n' % line for line in contents]
      wfile(fname, contents)
