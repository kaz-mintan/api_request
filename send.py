# ライブラリのインポート
import requests
import json

# APIに接続するための情報
url_login = "https://management-api.xaiml.docomo-dialog.com/login"
url = "https://api-sunaba.xaiml.docomo-dialog.com/dialogue"

# APIに送信する情報
headers = {"Content-Type": "application/json;charset=utf-8"}

body = {"language": "ja-JP", "botId": "KATARAI_Chatting", "appId": "705f15b5-d457-4782-b198-59da2757def0", "voiceText": "こんにちは", "clientData": { "option": { "nickname": "太郎", "nicknameY": "たろう", "sex": "男", "bloodtype": "A", "birthdateY": "1989", "birthdateM": "1", "birthdateD": "1", "age": "31", "constellations": "山羊座", "place": "東京" } }, "appRecvTime": "2017-01-01 12:00:00", "appSendTime": "2017-01-01 12:01:00"}

body_account = {
  "accountName":**,
  "password":**
}

body3 = {
  "appId": "7f141696-1e0a-47c0-8296-e01c2cbd7834",
  "botId": "1928_b56vbrkeywrg0yp",
  "voiceText": "やあこんにちは",
  "initTalkingFlag": "false",
  "initTopicId": "s56vbrymc9us09h",
  "language": "ja-JP"
}

# API接続の実行
result = requests.post(url_login,params=body_account,headers=headers)
#result = requests.post(url, params=body, headers=headers2)
#result = requests.post(url, params=body, headers=headers2)
print(result)
