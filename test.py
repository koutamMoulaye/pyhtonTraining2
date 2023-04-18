from random import  *
import  string
#------------------------------------------------------------------EXERCISE--1
#Return the smaller value of distance withthe name of driver

# name_driver = ["Paul","Jymmy","Ali","Abdallah","Karim","Francis"]
# distance_car_km = [12, 0.2,0.2,11,15,0.1]
# distance_car_km_min = distance_car_km[0]
# for i in range(len(distance_car_km)):
#     index=i
#     distances = distance_car_km[i]
#     if distances < distance_car_km_min:
#         distance_car_km_min = distances
#         index
# print(f"the small value is {distance_car_km_min}, and name driver is {name_driver[index]}")


#------------------------------------------------------------------EXERCISE--2
# GENERATOR PASSWORD
# height1=6
# height2=12
# all_chars= string.digits + string.digits + string.ascii_letters
# def genarator_password():
#     password = "".join(choice(all_chars) for i in range(randint(height1,height2)))
#     return password
# print(genarator_password())


#------------------------------------------------------------------EXERCISE--3 form ask you a capital of country
#
# score = 0
# def form(question,r1, r2, r3, r4, good_choice):
#    global score
#     print("Welcome to this part")
#     print(f"\t {question}")
#     print(f"\t (a) {r1}")
#     print(f"\t (b) {r2}")
#     print(f"\t (c) {r3}")
#     print(f"\t (d) {r4}")
#     enter = input("please enter your answer : ")
#     if enter == good_choice:
#          print("You're RIGTH !!!")
#          score += 1
#      else:
#          print("Bad answer !!")
# print(form("What's the capital ofUSA","Paris", "Bamako", "Riyad", "Washington DC", "Washington DC"))
# print(form("What's the capital of Australia","Paris", "Bamako", "Riyad", "Gamberra", "Gamberra"))
# print("You're score : " ,score)


