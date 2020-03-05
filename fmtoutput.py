#!/usr/bin/env python3
def get_contents():
    contents = []
    print('请输入内容，结束请输入end。')
    while True:
        line = input('> ')
        if line == 'end':
            break
        contents.append(line)
    return contents
contents2 = get_contents()
print('+%s+' %('*' * 48))
for line in contents2:
    print('+{:^48}+'.format(line))
print('+%s+' %('*' * 48))

