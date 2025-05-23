import smtplib

import requests
import wikipedia
import pywhatkit as kit
from email.message import EmailMessage

EMAIL = ('garimil86@gmail.com')
PASSWORD = ('xqzrndfmotmdaufd')
OPENWEATHER_APP_ID = ('9fa98b106528c93a28111462d039acf5')

contacts = {
    'Лена': "height_atisuto@mail.ru",
    'вторая почта': "videow492@gmail.com"
}

def find_my_ip():
    ip_address = requests.get('https://api64.ipify.org?format=json').json()
    return ip_address['ip']


def search_on_wikipedia(query):
    results = wikipedia.summary(query, sentences=2)
    return results


def play_on_youtube(video):
    kit.playonyt(video)


def search_on_google(query):
    kit.search(query)


def send_email(receiver_address, subject, message):
    try:
        email = EmailMessage()
        email['To'] = receiver_address
        email['Subject'] = subject
        email['From'] = EMAIL
        email.set_content(message)
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(EMAIL, PASSWORD)
        s.send_message(email)
        s.close()
        return True
    except Exception as e:
        print(e)
        return False


def get_weather_report(city):
    res = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_APP_ID}&units=metric").json()
    weather = res['weather'][0]['main']
    temperature = res['main']['temp']
    feels_like = res['main']['feels_like']
    return weather, f'{temperature}℃', f'{feels_like}℃'