"""
В быстрых шахматах на принятие решений для всех ходов игроку даётся 30 минут. Программа должна:
Предлагать ввод хода (например, E2–E4) и считать потраченное время.
После получения хода печатать оставшееся время в минутах.
Если 30 минут закончились или игрок вводит «off» — завершать работу.
Оформить в виде функции.
"""


def chess():
 from time import time
 start = time()
 total_time = 1800
 while True:
  move = input("Введите ход (по типу E2-E4): ")
  if move == "off" or time() - start >= total_time:
   break
  else:
   time_left = round((total_time - (time() - start)) / 60, 2)
   print('Времени осталось:', time_left, 'мин')

 print("Game over :(")


chess()