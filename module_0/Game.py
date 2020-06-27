#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
count = 0                            # счетчик попыток
number = np.random.randint(1,101)    # загадали число


# In[7]:


def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print("Ваш алгоритм угадывает число в среднем за {0} попыток".format(score)) 
    


# In[1]:


def game_core_v5(number):
    lowest = 1
    highest = 100
    count = 1
    
    while True: # Используем метод двоичного поиска
        count += 1
        predict = (lowest+highest)//2
        if predict==number:
            break
        elif predict<number:
            lowest = predict + 1
        else:
            highest = predict - 1
            
    return(count)


# In[8]:


score_game(game_core_v5)


# In[ ]:




