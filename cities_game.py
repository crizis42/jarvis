def cities():
    from main import take_user_input, speak

    cities_old = []
    symbols_bad = {'ь', 'ъ', 'ы', 'ц', 'й'}

    text1 = open('cities.txt', encoding='utf8')
    cities = []
    for i in text1:
        cities.append(i)

    for i in range(len(cities)):
        if cities[i][-1] == '\n':
            cities[i] = cities[i][:-1]
    cities_all = cities.copy()

    game_over = False

    speak('Давайте сыграем в города! Если вы хотите прекратить игру, скажите стоп')


    # Первый ход - делает компьютер
    city = 'Москва'
    print(city)
    s_end = 'а'
    step = 'human'
    cities_old.append(city)
    s_end = city[-1]

    while game_over == False:

        if step == 'human':
            correct = False

            while correct == False:
                speak('Назовите город, который начинается с последней буквы предыдущего города')
                query = take_user_input().lower()
                city = query
                if "стоп" in query or 'stop' in query:
                    game_over = True
                    correct = True
                else:
                    correct = True
                    #Проверить что город на нужную букву
                    if city[0].lower () != s_end:
                        correct = False
                        speak('Неправильно. Назовите город на нужную букву')
                    #Проверить существование города
                    if city in set(cities_all):
                        pass
                    else:
                        correct = False
                        speak('Неправильно. Такого города не существует')
                    #Проверить был ли этот город
                    if city in set(cities_old):
                        correct = False
                        speak('Неправильно. Этот город уже был назван')

            step = 'AI'
        else:
            city = ''
            for city_next in cities:
                if city_next[0].lower() == s_end:
                    city = city_next
            if city == '':
                print('Вы победили')
                speak('Вы победили')
                print('Не найден город на букву', s_end)
                speak('Я не могу найти город, который начинается на последнюю букву вашего города')
                game_over = True
            else:
                print(city)
                step = 'human'

        if game_over == False:
            cities.remove(city)
            cities_old.append(city)

            s_end = city[-1]
            if s_end in symbols_bad:
                s_end = city[-2]

            if s_end in symbols_bad:
                s_end = city[-3]
            else:
                pass

    speak('Игра окончена')
    print('Назвали', len(cities_old), 'городов из', len(cities_all))