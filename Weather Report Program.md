Weather Report Program

*오픈소스소프트웨어 강의 프로젝트*

건설시스템공학과 17100709 김재윤

## 작품 소개
- 웹 크롤링을 통한 지역의 실시간 날씨 정보를 알려주는 프로그램
- 네이버 날씨정보를 받음
- 시 뿐만 아니라 국내의 시/구/동/면/읍 까지 가능

## TODO list
- [x] 아이디어 구상
- [x] 날씨 데이터 갖고 오기
- [x] 날씨 데이터 분석
- [x] 결과 도출



# 개요 

**크롤링**(crawling) : 웹사이트(website), [하이퍼링크](https://terms.naver.com/entry.naver?docId=861505&ref=y)(hyperlink), 데이터(data), 정보 자원을 [자동화](https://terms.naver.com/entry.naver?docId=815815&ref=y)된 방법으로 수집, 분류, 저장하는 것.                                                                                         출처 -  [네이버 지식백과](https://terms.naver.com/entry.naver?docId=6470952&cid=42346&categoryId=42346)

 웹  사이트는 기본적으로 HTML 이라는 형식으로 쓰여진 문서이다. 우리는 HTML 문서에 담긴 내용을 가져 오도록 request(요청)해야 한다.  크롤링을 이용해 웹 사이트의 HTML 코드  정보를 저장 할 수 있다.  이 과정에서 BeautifulSoup 라는 라이브러리를 사용한다.



# 상세설명

#### 웹크롤링을 하기 위한 모듈 import 하기.

<img src="C:\Users\jaeyo\Desktop\새 폴더\1.PNG" alt="1"  /> 

 다른 환경에서는 라이브러리를 다운받아야 하므로 [Colaboratory(Colab)](https://colab.research.google.com/?utm_source=scs-index) 사용을 권장한다.

#### 현재 시간을 불러오기 위한 변수 now 정의

![2](C:\Users\jaeyo\Desktop\새 폴더\2.PNG) 

​    import 를 했다면 현재 시간을 나타내는 now를 정의한다.



#### <code>today_weather</code> 함수 정의하기

![3](C:\Users\jaeyo\Desktop\새 폴더\3.PNG)



- input 으로 받은 값을 <code>location</code> 변수로 저장하여 네이버 날씨의 주소를 <code>get</code> 요청하여 html을 받아오는 것으로 시작한다. 
- <code>soup = BeautifulSoup(html.text, 'html.parser')</code> 받아온 html을 텍스트 형태로 변환하고, <code>html.parser</code> 을 통해 <code>beautifulsoup</code> 가 처리할 수 있는 데이터로 변환해 준다.



![6](C:\Users\jaeyo\Desktop\새 폴더\6.png)

- 네이버 날씨 웹 페이지에서 **F12** 키를 누르면 개발자 도구를 볼 수 있다. 여기서 개발자  도구 좌측 상단의 **Select an element in the page to inspect it** 버튼을 누르면 현재 페이지의 코드들을 확인할 수 있다.

   

  이를 통해  좌측 현재온도를 클릭하게 되면 개발자도구에서 `<div class="temperature_text">` 부분이 강조된다. `today_temps = soup.find('div',"temperature_text")` 의 의미는 `temperature_text `라는 이름의 `div`를 찾아 `today_temps`에 저장해준다는 뜻이다. 

  

  이런식으로  

  `today_temps = soup.find('div',"temperature_text")` 

   ` today_cast = soup.find('div',"temperature_info")` 를 작성해준다.

  

- `try`/`except` 를 사용 한 이유는 지역명이 잘못 입력 됐을 경우 오류가 발생하기 때문이다.

  이 때, `today_temp_Data = today_temps.get_text()`에서 오류가 발생한다면 `except` 부분으로 넘어갈 것이고 그렇지 않다면 남은 코드를 실행 할 것이다.

  

#### 프로그램의 종료 여부를 묻는 <code>ask_keep_going</code> 함수 정의

![4](C:\Users\jaeyo\Desktop\새 폴더\4.PNG) 

  

- 한 지역의 날씨를 알아본 후 계속해서 다른 지역의 날씨를 알아볼 지 결정하는 함수이다.



#### 날씨 출력하기

![5](C:\Users\jaeyo\Desktop\새 폴더\5.PNG) 

- `while` 루프를 사용하여 프로그램 종료전까지 무한반복한다.



# 결과

#### ![7](C:\Users\jaeyo\Desktop\새 폴더\7.PNG)

- 프로그램 실행 시 다음과 결과를 얻을 수 있다.