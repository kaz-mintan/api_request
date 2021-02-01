import requests
import json
from requests.exceptions import Timeout

url = 'https://api-sunaba.xaiml.docomo-dialog.com/dialogue'
headers2 = {"x-api-key": "", "Content-Type": "application/json;charset=utf-8"}

def send_msg(user_utt):
    data = {
      "appId": "",
      "botId": "",
      "voiceText": user_utt,
      "initTalkingFlag": "false",
      "initTopicId": "s56vbrymc9us09h",
      "language": "ja-JP"
    }
    return data

while(True):
    print("input message")
    msg = input()
    try:
        r = requests.post(url, data=json.dumps(send_msg(msg)),headers=headers2, timeout=1)
        print("ユーザ:",msg)
        print("かたらい:",r.json()['systemText']['utterance'])
    except Timeout:
        print(Timeout)
        pass
