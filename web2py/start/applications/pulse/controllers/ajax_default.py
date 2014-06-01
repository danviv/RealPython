import requests
import json

def index(): return dict()

def pulse():
    session.m=[]
    if request.vars.sentiment:
        text = request.vars.sentiment
        text = text.split('_')
        text = ' '.join(text)
        url = 'http://text-processing.com/api/sentiment/'
        data = {'text': text}
        r = requests.post(url, data=data)
        session.m.append(r.content)
    session.m.sort()
    return text, TABLE(*[TR(v) for v in session.m]).xml()
