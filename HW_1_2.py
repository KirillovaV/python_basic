"""
2. Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
"""

time_sec = input('Введите время в секундах:\n>>>')

while not time_sec.isdigit():
    time_sec = input("Неверный воод. Необходимо ввести целое число!\n>>>")
time_sec = int(time_sec)

second = time_sec % 60
minute = time_sec // 60
if minute >= 60:
    hour = minute // 60
    minute = minute % 60
else:
    hour = 0

print(f"{time_sec} секунд это {hour}:{minute}:{second}")
