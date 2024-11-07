from bs4 import BeautifulSoup as bs
from googletrans import Translator
import requests

def get_eng_word():
    url = 'http://randomword.com/'
    try:
        response = requests.get(url)
        soup = bs(response.content, 'html.parser')
        word = soup.find('div', id='random_word').text.strip()
        definition = soup.find('div', id='random_word_definition').text.strip()

        return {'word': word,
                'definition': definition}
    except: print('Что-то не так...')

def game():
    print('Добро пожаловать в игру!')
    translator = Translator()
    def rus(text):
        return translator.translate(text, dest='ru').text
    while True:
        word_dict = get_eng_word()
        word = word_dict.get('word')
        rus_word = rus(word)
        definition = word_dict.get('definition')

        print(f'Значение слова: {rus(definition)}')
        print(f'({definition})')
        user = input('Угадай что это? (можно на английском;) - ').strip().lower()
        if user == word or user == rus_word: print('Верно!')
        else:
            print(f'Неверно! Правильное слово: {rus_word}')
            print(f'({word})')

        play_again = input('Попробовать ещё? y(н)/n')
        if play_again not in 'yн':
            print('Ладно, пока!')
            break

game()