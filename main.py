import speech_recognition as sr
import os
from gtts import gTTS
import datetime, warnings, calendar, wikipedia, random

warnings.filterwarnings('ignore')

def recordAudio():

    while True:
        rec = sr.Recognizer()

        with sr.Microphone() as source:
            print('Fala tu')
            audio = rec.listen(source)

            data = ''
        try:
            data = rec.recognize_google(audio)
            if 'data' in data:
                print(dataAtual())
            elif 'Neymar' or 'neymar' in data:
                os.system('start notepad.exe')

            print('Tu falo: ' + data + '???!?')
            wiki = wikipedia.summary(data, sentences=2)
        except sr.UnknownValueError:
            print("Tendi foi nada")

        except sr.RequestError as e:
            print(e)

        return data

def jarvisTalk(txt):


    print(txt)
    myobj = gTTS(text=txt, lang='pt-BR', slow=False)

    myobj.save('jarvisAmigao.mp3')

    os.system('start jarvisAmigao.mp3')


def wakeWords(txt):
    WAKER_WORDS = ['Flamengo ola', 'Oi Flamengo', 'Gabigol Amigo']

    txt = txt.lower()

    for i in WAKER_WORDS:
        if i in txt:
            return True

    return False

def dataAtual():

    now = datetime.datetime.now()
    myDate = datetime.datetime.today()
    semana = calendar.day_name[myDate.weekday()]
    mes = now.month
    ano = now.year
    dia = now.day

    meses = ['Janeiro', 'Fevereiro', 'Março','Abril','Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    dias = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19","20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"]

    return 'Hoje é ' + semana + ' de ' + meses[mes - 1] + ' dia ' + dias[dia - 1]


if __name__ == "__main__":

    txt = recordAudio()
    jarvisTalk(txt)

