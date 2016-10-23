# coding: utf-8

print('CAPITALIZE'.capitalize())

print('python is powerful'.count('p'))
print('python is powerful'.count('p', 5,11))

print('가나다'.encode('utf-8'))  ## byte로 인코딩

print('python is powerful'[5:-1])
print('python is powerful'.endswith('ful',5,-1))  ## [startwith()]

print('python is powerful'.find('p', 1, 11)) # 찾지 못할 경우 -1 리턴 [rfind()]
print('python is powerful'.index('p', 1, 11)) # 찾지 못할 경우 Error 발생 [rindex()]

print('python3000'.isalnum())
print('python30.00'.isalnum()) ## 알파벳 숫자 인경우 True

print('.'.join('HOT'))

print('\t python'.lstrip())  ## 왼쪽 공백제거 [rstrip()]
print('### ### python'.lstrip('#'))

tramsmap = str.maketrans('p', 'P', 'is')  # 번역(대체)용 맵(1,2번째 매개변수 글자 길이가 같아야함, 3번 매개변수는 제거할 문자)
print(tramsmap)
print('python is powerful!!!'.translate(tramsmap))


print('python is powerful'.partition('is'))  ## 3튜플 반환(앞부분, separator, 뒷부분) [rpartition]

print('python is powerful'.replace('p', 'T'))
print('python is powerful'.replace('p', 'T', 1))

print('python is powerful'.split())  ## 매개변수 없을 경우 공백으로 분리 [rsplit()]
print('python is powerful'.split('p'))


print('python\r\nis\npowerful'.splitlines())
print('python\r\nis\npowerful'.splitlines(True))

print('   python   '.strip())  # 문자열 양쪽 끝 제거
print('## #python# ###'.strip('#'))