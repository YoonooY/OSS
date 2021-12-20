import requests
import datetime
from bs4 import BeautifulSoup

isAbroad = False

def ask_keep_going():
    keep_going = input('계속 하시겠습니까? y/n : ')
    if keep_going == 'n':
        return True
    else:
        return False

def today_weather(): 
  print(nowDate)
  print('--> ', where, ' 날씨 : ',  today_temps.get_text())
  print('\n')
  print(today_cast.get_text())
  print('\n')

now = datetime.datetime.now()
nowDate = now.strftime('%Y년 %m월 %d일 %H시 %M분 입니다.')

print('      오늘의 주요 정보를 요약해 드리겠습니다.\n')

# 오늘의 날씨
while True:
  where = input('어디 날씨를 알아볼까요? ex) 국가/도시/구/동/면/읍/동 : ')
  html = requests.get('https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query=' + where + '날씨')

  print(' >>  오늘의 날씨 요약 \n')

  soup = BeautifulSoup(html.text, 'html.parser')
  today_temps = soup.find('div',"temperature_text")
  today_cast = soup.find('div',"temperature_info")

  today_weather()
  if ask_keep_going():
    print('프로그램 종료')
    break
