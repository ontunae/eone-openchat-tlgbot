# eone-openchat-tlgbot
이원 카카오톡 오픈채팅방 공석 알림봇 @ 텔레그램

제작: 이원(트위터 [@on_tuna_e](https://twitter.com/on_tuna_e))


카카오톡 오픈채팅방에 자리가 났는지 실시간으로 체크, 공석이 생기면 알림을 보내주는 텔레그램 봇 소스코드입니다.  
python 패키지 중 bs4(beautiful soup)를 이용하면 약간의 수정 후 각종 크롤링 & 알리미에 이용할 수 있습니다. 

예시: <https://twitter.com/on_tuna_e/status/1300113505350164480?s=20>

&nbsp;  

# 파일 설명
1. PROCFILE: 헤로쿠(heroku) 서버 업로드를 위한 용도
2. requirements.txt: 헤로쿠에 어떤 서드파티 패키지가 필요하니 pip을 통해 설치하라 명령하는 용도
3. main.py: 알리미 실행 메인 소스코드 (대문자로 된 변수명은 임의 수정 필요)
