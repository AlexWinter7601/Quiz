score = 0
print("Добро пожаловать в квиз по стартапам!")
print("Ответь на следующие вопросы:")
questions = ["1. Как называется компания, которая создается для развития новой идеи или инновационного продукта?",
             "2. Как назвается человек или компания, который вкладывает деньги в бизнес с целью получения прибыли?",
             "3. Как называется капитал, который дают инвесторы на развитие стартапа?",
             "4. Как пишется минимально жизнеспособный продукт, который создается для тестирования идей и концепций?",
             "5. Какой план создают перед тем, как открывать стартап и занимать деньги?",
             "6. Как называются другие компании на рынке, которые предлагают аналогичные товары или услуги?",
             "7. Как называется разница между выручкой и затратами компании?"]
answers = ["Стартап", "Инвестор", "Инвестиция", "MVP", "Бизнес-план", "Конкуренты", "Прибыль"]
print(questions[0])

# Напиши код вместо ""
user_input = input("Ваш ответ: ")

# Проверка правильного ответа ,

if user_input.lower() ==  answers[0].lower():
    print("Правильно!")
    score +=1
else:
    print("Неправильно.")
print(questions[1])

# Напиши код вместо ""
user_input = input("Ваш ответ: ")

# Проверка правильного ответа ,

if user_input.lower() ==  answers[1].lower():
    score += 1
    print("Правильно!")
else:
    print("Неправильно.")

print(questions[2])

# Напиши код вместо ""
user_input = input("Ваш ответ: ")

# Проверка правильного ответа ,

if user_input.lower() == answers[2].lower():
    score += 1
    print("Правильно!")
else:
    print("Неправильно.")
print(questions[3])

# Напиши код вместо ""
user_input = input("Ваш ответ: ")

# Проверка правильного ответа ,

if user_input.lower() == answers[3].lower():
    score += 1
    print("Правильно!")
else:
    print("Неправильно.")

print(questions[4])

# Напиши код вместо ""
user_input = input("Ваш ответ: ")

# Проверка правильного ответа

if user_input.lower() == answers[4].lower():
    score += 1
    print("Правильно!")
else:
    print("Неправильно.")

print(questions[5])

# Напиши код вместо ""
user_input = input("Ваш ответ: ")

# Проверка правильного ответа ,

if user_input.lower() == answers[5].lower():
    score += 1
    print("Правильно!")
else:
    print("Неправильно.")

print(questions[6])

# Напиши код вместо ""
user_input = input("Ваш ответ: ")

# Проверка правильного ответа ,

if user_input.lower() == answers[6].lower():
    score += 1
    print("Правильно!")
else:
    print("Неправильно.")

if score > 5:
    print("Это отличный результат! Ты много знаешь о стартапах.")
elif score > 3:
    print("Неплохой результат! Как здорово, что тебе предстоит узнать ещё так много о стартапах.")
else:
    print("Видимо, ты только начинаешь свой путь к стартапам! Ты ещё много чего узнаешь о мире, где мы живём.")