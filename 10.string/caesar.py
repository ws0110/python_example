# coding: utf-8

'''
 ord(), chr() 메소드를 활용한 '카이사르' 암호화 예제
'''

SHIFT = 1

def encrypt(raw):
    ret = ''
    for i in raw:
        ret += chr(ord(i) + SHIFT)
    return ret


def decrypt(raw):
    ret = ''
    for i in raw:
        ret += chr(ord(i) - SHIFT)
    return ret


if __name__ == '__main__':
    raw = input('input: ')
    encrypted = encrypt(raw)
    print('encrypted: ', encrypted)

    decrypted = decrypt(encrypted)
    print('decrypted: ', decrypted)