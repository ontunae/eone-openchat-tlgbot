import requests
import telegram
from apscheduler.schedulers.blocking import BlockingScheduler


bot = telegram.Bot(token='TELEGRAM_TOKEN')


def currentNum():
    headers = {
        'Content-Type': 'application/json',
    }

    params = (
        ('query', 'OPENCHAT_LINK'),
        ('type', 'm'),
        ('page', '1'),
        ('count', '30'),
    )

    response = requests.get('https://api.develope.kr/search/room/list', headers=headers, params=params)
    result = response.json()['result']['lists'][0]
    desc = result['desc']

    if result['headcount'] < OPENCHAT_MAX_HEADCOUNT:
        bot.sendMessage(chat_id=CHAT_ID, text=result['name'] + '\n에 자리가 났습니다! 서두르세요!!\n' + desc[:desc.find(']') + 1])


sched = BlockingScheduler()
sched.add_job(currentNum, 'interval', seconds=10, max_instances=6)
sched.start()
