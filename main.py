import numpy as np

def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)


def game_core_v1(number):
    '''Просто угадываем на random, никак не используя информацию о больше или меньше.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 0
    while True:
        count+=1
        predict = np.random.randint(1,101) # предполагаемое число
        if number == predict:
            return(count) # выход из цикла, если угадали

        
def game_core_v2(number):
    '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 1
    predict = np.random.randint(1,101)
    while number != predict:
        count+=1
        if number > predict:
            predict += 1
        elif number < predict:
            predict -= 1
    return(count) # выход из цикла, если угадали
        
      
def game_core_v3(number):
    '''Ищем искомое число методом половинного деления за log2(N).
       Функция принимает загаданное число и возвращает число попыток'''
    count = 1
    
    #Установка границ и середины интервала поиска
    left = 1
    right = 100
    predict = (left + right) // 2
    
    while predict != number:
        #Корректировка интервала поиска
        if predict < number:
            left = predict + 1
        elif predict > number:
            right = predict - 1
        
        #Очередная попытка угадать число
        predict = (left + right) // 2
        count +=1
    
    return count

def game_core_v4(number):
    '''Читерский вариант за O(1).
       Функция принимает загаданное число и возвращает число попыток'''
    predict = number
    return 1



score_game(game_core_v1) #random-force
score_game(game_core_v2) #random base, sequential
score_game(game_core_v3) #bisection 
score_game(game_core_v4) #cheating