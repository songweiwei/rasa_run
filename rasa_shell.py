import requests
import json
from flask import request

def requestRasabotServer(content):
    """
        访问rasa服务
    :param userid: 用户id
    :param content: 自然语言文本
    :return:  json格式响应数据
    """
    params = {'content': content}
    # rasa使用rest channel
    # https://rasa.com/docs/rasa/user-guide/connectors/your-own-website/#rest-channels
    # POST /webhooks/rest/webhook
    rasaUrl = "http://127.0.0.1:8088/ai"
    # print(rasaUrl)


    reponse = requests.post(
        rasaUrl,
        data=json.dumps((params)),
        headers={'Content-Type': 'application/json'}
    )
    # print(type(json.loads(reponse.text,strict=False)["reply"]))
    return json.loads(reponse.text,strict=False)["reply"]


while (True):
    usrInput=input()
    print("用户：",usrInput)
    botReply=requestRasabotServer(usrInput)
    print("bot:",botReply)
