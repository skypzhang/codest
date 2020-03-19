import base64
import sys


def b64_decode(bstring):
    code = base64.b64decode(bstring)
    return code


if __name__ == '__main__':
    print(b64_decode(sys.argv[1]))
