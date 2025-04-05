import pyttsx3
from datetime import datetime

import requests
import speech_recognition as sr
from random import choice
from utils import opening_text, stop_text
from os_ops import open_spotify, open_cmd, open_browser, open_calc, open_telegram, open_dota
from online_ops import find_my_ip, search_on_wikipedia, play_on_youtube, search_on_google, send_email, contacts, get_weather_report
from cities_game import cities

engine = pyttsx3.init('sapi5')

#rate
engine.setProperty('rate', 190)

#volume
engine.setProperty('volume', 1.0)

#voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


#text to speech conversio
def speak(text):
    engine.say(text)
    engine.runAndWait()


#greetings
def greetings():
    hour = datetime.now().hour
    if (hour >= 6) and (hour <= 12):
        speak(f'Доброе утро, сэр')
    elif (hour > 12) and (hour <= 18):
        speak(f'Добрый день, сэр')
    elif (hour > 18) and (hour <= 21):
        speak(f'Добрый вечер, сэр')
    elif (hour > 21) or (hour < 6):
        speak(f'Доброй ночи, сэр')
    speak(f'Я голосовой ассистент Мира, чем могу вам помочь?')


def take_user_input(assistant_name="мира"):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Ожидаю активации...')
        r.pause_threshold = 2
        audio = r.listen(source)
        
    try:
        print('Распознаю вашу речь...')
        query = r.recognize_google(audio, language='ru-RU').lower()
        
        # Проверяем, содержит ли запрос имя ассистента
        if assistant_name.lower() not in query:
            return "None"
            
        # Удаляем имя ассистента из запроса для дальнейшей обработки
        query = query.replace(assistant_name.lower(), "").strip()
        
        if not any(word in query for word in stop_text):
            speak(choice(opening_text))
        else:
            hour = datetime.now().hour
            if ((hour >= 6) and (hour <= 12)) or ((hour > 12) and (hour <= 18)):
                speak('Хорошего дня, сэр!')
            elif ((hour > 18) and (hour <= 21)) or ((hour > 21) or (hour < 6)):
                speak('Доброй ночи, сэр')
            else:
                speak('До встречи, хорошего времени суток, сэр!')
            exit()
            
    except Exception:
        speak('Извините, я вас не понимаю, повторите пожалуйста еще раз')
        query = 'None'
        
    return query


if __name__ == '__main__':
    greetings()
    while True:
        query = take_user_input().lower()
        print(query)

        if 'открой spotify' in query or 'открой спотифай' in query:
            open_spotify()

        elif 'открой browser' in query or 'открой браузер' in query:
            open_browser()

        elif 'открой командную строку' in query or 'открой консоль' in query:
            open_cmd()

        elif 'открой калькулятор' in query:
            open_calc()

        elif 'открой telegram' in query or 'открой телеграм' in query or 'открой телегу' in query:
            open_telegram()

        elif 'jarvis протокол yagul' in query or 'jarvis протокол я гуль' in query: #не работает, надо фиксить
            open_spotify()
            open_dota()

        elif 'найди мой айпи' in query or 'найди мой ip' in query:
            ip_address = find_my_ip()
            speak(f'Ваш айпи адрес {ip_address}, ради вашей безопасности я выведу его на экран')
            print(f'Ваш IP-адрес {ip_address}')

        elif 'википедия' in query or 'wikipedia' in query:
            speak('Что вы желаете найти на википедии?')
            search_query = take_user_input().lower()
            results = search_on_wikipedia(search_query)
            speak(f'Как написано в википедии, {results}')
            speak('для вашей безопасности я выведу это на экран')
            print(results)

        elif 'ютуб' in query or 'youtube' in query:
            speak('Что вы хотите найти на ютубе?')
            video = take_user_input().lower()
            play_on_youtube(video)

        elif 'google' in query or 'гугл' in query:
            speak('Что вы хотите найти в гугле?')
            query = take_user_input().lower()
            search_on_google(query)

        elif 'отправь письмо' in query:
            speak('Вы хотите ввести адрес электронной почты в консоль? или выбрать из своего списка контактов?')
            query = take_user_input().lower()
            if 'я введу вручную' in query or 'ручной ввод' in query:
                receiver_address = input('Введите адрес электронной почты: ')
            if 'я хочу выбрать из списка контактов' in query or 'выбери из списка контактов' in query:
                speak("Кому пишем письмо, сэр? ")
                query = take_user_input().lower()
                if 'лене' in query or 'лена' in query:
                    receiver_address = contacts['лена']
                elif 'на мою вторую почту' in query or 'моя вторая почта' in query:
                    receiver_address = contacts['вторая почта']
            speak('Какая тема письма, сэр?')
            subject = take_user_input().capitalize()
            speak('Что вы хотите написать сэр?')
            message = take_user_input().capitalize()
            if send_email(receiver_address, subject, message):
                speak('Я отправила письмо, сэр')
            else:
                speak('Что-то пошло не так, проверьте отчет об ошибке')

        elif 'давай сыграем в города' in query or 'города' in query:
            cities()

        elif 'скажи прогноз погоды' in query or 'какая сейчас погода' in query or 'скажи погоду' in query:
            ip_address = find_my_ip()
            city = requests.get(f"https://ipapi.co/{ip_address}/city/").text
            speak(f'Получаю информацию о вашем городе {city}')
            weather, temperature, feels_like = get_weather_report(city)
            speak(f'Текущая температура воздуха {temperature}, ощущается как {feels_like}')
            speak(f'Также в отчете о погоде {weather}')
            speak('Для вашей безопасности, я выведу это на экран, Сэр')
            print(f'Отчет: {weather}\nТемпература: {temperature}\nОщущается как: {feels_like}')