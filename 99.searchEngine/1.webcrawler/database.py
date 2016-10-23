# coding: utf-8

'''
  웹크롤러 DB 클래스 소스
'''

import sqlite3

class DB:
    'SQLITE3 wrapper class'

    def __init__(self):
        self.conn = sqlite3.connect('crawlerDB')
        self.cursor = self.conn.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS urls(url text, state int)')
        self.cursor.execute('CREATE UNIQUE INDEX IF NOT EXISTS IDX001 ON urls(url)')
        self.cursor.execute('CREATE INDEX IF NOT EXISTS IDX002 ON urls(state)')

    def __del__(self):
        self.conn.commit()
        self.cursor.close()

    # URL 등록
    def insertURL(self, url, state=0):
        try:
            self.cursor.execute('INSERT INTO urls VALUES("%s", "%d")' % (url, state))
        except:
            return 0
        else:
            return 1

    # 수집되지 않은 URL 조회
    def selectUncrawledURL(self):
        self.cursor.execute('SELECT * FROM urls WHERE state=0')
        return [row[0] for row in self.cursor.fetchall()]  # url 리스트만 리턴

    # URL 상태 수정(수집된 것으로)
    def updateURL(self, url, state=1):
        self.cursor.execute('UPDATE urls SET state="%d" WHERE url="%s" ' % (state, url))

    # 수집된 URL인지 체크
    def isCrawledURL(self, url):
        self.cursor.execute('SELECT COUNT(1) FROM urls WHERE url="%s" AND state=1 ' % (url))
        ret = self.cursor.fetchone()
        return ret[0]

