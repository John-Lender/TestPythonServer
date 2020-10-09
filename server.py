#https://flask-russian-docs.readthedocs.io/ru/latest/quickstart.html
#https://ru.wikibooks.org/wiki/%D0%A3%D1%87%D0%B5%D0%B1%D0%BD%D0%B8%D0%BA_Python/%D0%94%D0%B0%D1%82%D0%B0_%D0%B8_%D0%B2%D1%80%D0%B5%D0%BC%D1%8F

from flask import Flask
from datetime import datetime
app = Flask(__name__)

answer = {"time": datetime.strftime(datetime.now(), "%H:%M"), "date": datetime.strftime(datetime.now(), "%d.%m.%Y"), "hello":  "Привет, "}

@app.route('/<msg>')
def getAnswer(msg):
    if (msg == 'time' or msg == 'date'):
        return answer[msg]
    elif (msg.find('hello') > -1):
        return answer[msg[0:5]] + msg[6::]
    return msg

if __name__ == '__main__':
    app.run()