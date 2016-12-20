
# from datetime import datetime
#
# print(datetime.now().second)
#
#
# if datetime.now().second%2 == 0:
#     print("짝")
# else :
#     print("홀")


array = [1,2,3,4,5,6,7,8,9,10,11,12]
tub = (1,2,3,4,5,6,7,8,9,10, 11, 12)
dic = {"one":1, "two":2, "three":3, "msg":"hoho"}

# print(type(array))
# print(type(tub))
# print(type(dic))
# count=0
#
# for i in array:
#     count+=1
#     print (i)
#     if count==10:
#         break

#
#
# count=0
#
# while count <10:
#     print (array[count])
#     count+=1
#
#-------- 가변인자 위치인자의 가변인자 키워드인자의 가변인자-----------
# def say(tray):
#     for i in tray:
#         print(i)
#
# def mul(tray):
#     for i in tray:
#         print(i+10)
#
# def wrapper(func, tray):
#     func(tray)
#
# def onebyone(*args, **kwargs):
#
#     if len(args)>0:
#         for i in args:
#             print (i)
#
#     for key in kwargs:
#         if key == "msg":
#             print (key, kwargs[key])
#
# onebyone(1,2,3,4,5,6,7,8,9,10,11,12, one=1, two=2, three=3, msg="hoho")

#------------generator-------------------
#
# def gengerator():
#     var =[1,2,3,4,5,6,7,8]
#     i=0
#
#     while True:
#         if i>len(var):
#             raise StopIteration
#         else:
#             yield var[i]
#             i+=1
#
# gen=gengerator()
# print(next(gen))
# print(next(gen))
# print(next(gen))

#------------interator------------------

# emty_array =[]
# print(type(emty_array))
# print(dir(emty_array))
#
# iter_emty_array=iter(emty_array)
# print(iter_emty_array)
# print(type(iter_emty_array))
# print(dir(iter_emty_array))

#------------expection------------------

# try :
#     result = 1/0
# except ZeroDivisionError:
#     print ("영으로 나누지 마세여. 그래여? 성격 이상하네")


# def add_100(text):
#
#     number=int(text)+100
#     return number
#
# try :
#     print(add_100("200"))
# except ValueError:
#     print("숫자가 없다니까여")
# except TypeError:
#     print("문자열은 안되요")
# except Exception:
#     print("으악 이건 무슨 에러지")
# else :
#     print("잘더했어요")
# finally:
#     print("어쨋든 수고 했어요 빠이 빠이")
#------------import------------------
# from wow import msg
#
# msg01 = msg
#
# print (msg01)


#------------name_space------------------
# number = 1023
#
# l_number =locals()["number"]
# print(l_number)
#
# def func():
#
#     number=221
#     print(number)
#
#     g_number=globals()["number"]
#     print (g_number)
#
# func()


# ak_41="old gun"
# k2="new gun"
#
# oldest=locals()["k2"]
# madeby=globals()["k2"]
#
# print (oldest)
# print (madeby)
# def func():
#     k2 = "korea gun"
#     ak_41="russia gun"
#     oldest = locals()["k2"]
#     madeby = globals()["k2"]
#     print (oldest)
#     print (madeby)
#
# func()
# name ="hi"
#
# def func():
#     name="hello"
#     print (name)
#
# func()
#
#
# def func2(name):
#     print (name)
#     name="hello"
#     print(name)
#
# func2(name)
#------------class, type------------------

class Card(object):
    name =""
    suit = ""
    number = None
    is_opened = False

    def put(self):
        print("카드를 놓았습니다")

    def get(self):
        print("카드를 받았습니다")

    def flip(self):
        print("카드를 뒤짚었습니다")


class Spade(Card):

    name="스페이드"
    suit = 'spade'
    number = 'None'

class Joker(Card):

    name='조커'
    suit='joker'
    number=None

    def change_card(self, card):
        self.suit