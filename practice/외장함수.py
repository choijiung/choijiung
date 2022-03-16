#직접 import를 해야 하는 함수
#glob : 경로 내에 폴더 / 파일 목록 조회(윈도우 dir)
# import glob
# print(glob.glob("*.py"))#확장자가 py인 모든 파일
#
# #os : 운영체제에서 제공하는 기본 기능
import os
# print(os.getcwd())#현재 디렉터리
#
# folder = "samplr_dir"
#
# if os.path.exists(folder):
#     print("이미 존재하는 폴더입니다")
#     os.rmdir(folder)
#     print(folder, "폴더를 삭제하였습니다")
# else:
#     os.makedirs(folder)
#     print("폴더를 생성하였습니다")

#print(os.makedirs())

#time: 시간관련함수
#import time
#print(time.localtime())
#print(time.strftime("%Y-%m-%d %H:%M:%S"))
#print(time.strftime("%Y-%m-%d %H:%M:%S"))
#print(time.strftime("%Y-%m-%d %H:%M:%S"))

import datetime
#print("오늘날짜는", datetime.date.today())

today = datetime.date.today()
td = datetime.timedelta(days=100)
print("우리가 만난지 100일은", today + td)