import requests
import datetime
from bs4 import BeautifulSoup

now = datetime.datetime.now()
nowDate = now.strftime('%Y년 %m월 %d일 %H시 %M분 입니다.')


def today_weather():
  location = input('어디 날씨를 알아볼까요? ex) 시/구/동/면/읍 : ')
  print('\n')
  html = requests.get('https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query=' + location + '날씨')
  soup = BeautifulSoup(html.text, 'html.parser')
  today_temps = soup.find('div',"temperature_text")
  today_cast = soup.find('div',"temperature_info")

  try:
    today_temp_Data = today_temps.get_text() #exception 잡기

    print('====================================오늘의 날씨 요약================================ \n')
    print(nowDate)
    print('--> ', location, ' 날씨 : ',  today_temp_Data)
    print(today_cast.get_text())
    print('=====================================================================================')
    print('\n')
  
  except Exception : 
    print('해당 지역을 찾을 수 없습니다.')
    print('\n')

def ask_keep_going():
    keep_going = input('계속 하시겠습니까? y/n : ')
    print('\n')
    if keep_going == 'n':
        return True
    else:
        return False

print(' 오늘의 주요 날씨 정보입니다.\n')

while True:
  today_weather()
  
  if ask_keep_going():
    print('프로그램 종료')
    break