# coding: utf-8


'''
 정규식
  . : 문자 1개(개행문자 제외)
  ^ : 문자열의 시작
  $ : 문자열의 종료
  [] : 문자 집합, [^a]: a를 제외한 모든문자 가능
   | : OR 연산
  () : 정규식 그룹
  * : 문자 0번이상 반복
  + : 문자 1번이상 반복
  ? : 문자 0 or 1번
  {m} : 문자가 m번 반복
  {m, n} : 문자가 m번부터 n번까지 반복
  {m, } : 문자가 m번부터 무한 반복

  \w : [a-zA-Z0-9_] 모든 언어
  \W : \w의 반대 [^a-zA-Z0-9_]
  \d : [0-9] 숫자
  \D : \d의 반대 [^0-9]
  \s : 공백 [\t\r\n\f\v]
  \S : \s의 반대  [^\t\r\n\f\v]
  \b : 단어의 시작, 끝이 빈 공백
  \B : 단어의 사작, 끝이 아닌 빈 공백
  \\ : \ 문자 자체
  \[숫자] : 지정된 숫자만틈 일치하는 문자열
  \A : 문자열의 시작
  \Z : 문자열의 끝

'''


import re


print(bool(re.match('[0-9]*th', '35th')))  # match()는 문자열 시작부터 검색(Match객체 리턴)
print(bool(re.match('[0-9]*th', '###35th')))

print(bool(re.search('[0-9]*th', '35th'))) # search()는 문자열 전체에서 검색(Match객체 리턴)
print(bool(re.search('[0-9]*th', '###35th')))

# rwa 문자 표기법(\를 이스케이프 문자열이 아닌 일반 문자열로 처리)
print(bool(re.search('\\\\\w+', '\\apple')))
print(bool(re.search(r'\\\w+', r'\apple')))

print(re.split('[:. ]+', 'apple Orange:banana  :. tomato'))
print(re.split('([:. ])+', 'apple Orange:banana  :. tomato'))  # ()를 사용할 경우 분리 문자도 결과에 포함

print(re.findall(r'app\w*', 'application orange apple')) ## 리스트 반환

print(re.sub('-', '', '010-1234-9876')) ## 패턴과 매칭되는 문자열 변경
print(re.sub(r'[:,|\s]', '; ', 'Apple:Orange Banana|Tomato', 2))  # 2번만 변경 설정 경우, 2번째 매개변구'; '에 함수명으로 함수 호출 가능


######## Compile  ###########

c = re.compile(r'app\w*')
print(c.findall('application orange apple'))
print(c.findall('so many apple'))

s = 'Apple is a big company and apple is delicious'
c = re.compile(r'app\w*', re.I)  ## re.I 대소문자 구분없음(IgnoreCase)
print(c.findall(s))

s = '''Gee Gee Gee Gee Gee Gee
 Oh 너무 부끄러워

 쳐다볼 수 없어
 '''
c = re.compile('^.+')
print(c.findall(s))
c = re.compile('^.+', re.M)  ## 빈 라인을 제외하고 라인별로 처리(Multiline)
print(c.findall(s))


######## Match 객체(match(), search() 메소드 결과)  ###########
telchk = re.compile('(\d{2,3})-(\d{3,4})-(\d{4})')
m = telchk.match('02-123-4567')
print(m.groups())
print(m.group())
print(m.group(1)) # 1번째로 매칭된 문자열
print(m.group(2, 3))  # 2, 3번째로 매칭된 문자열
print(m.start(2)) # 2번째로 매칭된 문자열의 시작 인덱스
print(m.end(2)) # 2번째로 매칭된 문자열의 종료 인덱스
print(m.string) # 전체 String
print(m.string[m.start(2):m.end(3)])

m = re.match(r'(?P<area_code>\d+)-(?P<exchange_number>\d+)-(?P<user_number>\d+)', '02-123-4567')
print(m.groupdict())
print(m.group('user_number'))


