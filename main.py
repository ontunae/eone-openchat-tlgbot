import requests
import telegram
from apscheduler.schedulers.blocking import BlockingScheduler


#진짜: 1372299266:AAHY6XiAyzzp5Hw54CzgzZ4csQzNGNhRi-w
#진짜: 1215804711

#테스트: 1261968915:AAENDB7nRG5_zLFcqrkkaaJwfepo-F07BYQ
#테스트:1215804711

bot = telegram.Bot(token='1372299266:AAHY6XiAyzzp5Hw54CzgzZ4csQzNGNhRi-w')
#test = telegram.Bot(token='1261968915:AAENDB7nRG5_zLFcqrkkaaJwfepo-F07BYQ')


def currentNum():
    headers = {
        'Content-Type': 'application/json',
    }

    params = (
        #고강방1
        ('query', 'https://open.kakao.com/o/gYSBYqF'),
        #캐럿방
        #('query', 'https://open.kakao.com/o/gVIIm6Yb'),
        ('type', 'm'),
        ('page', '1'),
        ('count', '30'),
    )

    response = requests.get('https://api.develope.kr/search/room/list', headers=headers, params=params)
    result = response.json()['result']['lists'][0]
    desc = result['desc']

    #test.sendMessage(chat_id=1215804711, text='10초 간격 체크 가능 여부 테스트입니다. 양해 바랍니다.')
    if result['headcount'] < 1500:
        #진짜
        bot.sendMessage(chat_id=1215804711, text=result['name'] + '\n에 자리가 났습니다! 서두르세요!!\n' + desc[:desc.find(']') + 1])
        #테스트
        #test.sendMessage(chat_id=1215804711, text=result['name'] + '\n에 자리가 났습니다! 서두르세요!!')


sched = BlockingScheduler()
sched.add_job(currentNum, 'interval', seconds=10, max_instances=6)
sched.start()
