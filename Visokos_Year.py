# -*- encoding: utf-8 -*-
g = input("Введите год:")
if type(g) != int:
  print "Введите число!"
else:
  if g%400==0:
    print("Високосный")
  elif g%100==0:
    print("Не високосный")
  elif g%4==0:
    print("Високосный")
  else:
    print("Не високосный")
