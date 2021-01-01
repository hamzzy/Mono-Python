import os
from pymono import Mono

os.environ['MONO-SEC-KEY'] = ""

mono = Mono(code=" ")


def get_auth():
    (data, status) = mono.Auth()
    return data


if __name__ == '__main__':
    get_auth()