from random import  *
from string import  *
 # collections : Tableaux, listes, tuples
list = ['jean', 'jack', 'rouseau', 'yassine']
tupple = ('jean', 'jack', 'rouseau', 'yassine')
# ---------------------------------------------------------TUPPLES

# tupple is with [] and is it fixed that is the princpal diffrence betwwen list and tupple

for i in range(len(tupple)):
    print(tupple[i])
print(tupple[-1])
print(tupple)
print(len(tupple))
value = range(0, 10)
print(value[0])

# ---------------------------------------------------------LIST
list = ['jean', 'jack', 'rouseau', 'yassine']

new_list = "ali"
print(list)
list.append(new_list)
print(list)
del list[0]
print(list)
def display_list(c):
    for i in c:
        print(i)

display_list(list)
def update_value(a):
    a[0]=40

test=[1,2,3,4]
print(test)
update_value(test)
print(test)
# ---------------------------------------------------------FUNCTION AND LIST
def get_information():
    return "boubacar", 37, 1.60


def display_information(name, old, heigth):
    print(f"new= name : {name}, old : {old}, heigth : {heigth}")


info = get_information()
# display_information(*info) inpact tupple
print(f"name : {info[0]}")
print(f"old : {info[1]}")
print(f"heigth : {info[2]}")
# ---------------------------------------------------------SLICES

for i in list[::-2]:
    print(i)

variable = "kayak"
def retour(variable3):
    variable3[::-1]
    print(variable3)
retour(variable)

# ---------------------------------------------------------LISTES - EXERCICES
# EXERCISE1 =
# --> Ans the name of the person
# --> create a infinite loop and this loop is break when name it's empty'
while True:
    name = input("Please enter a name : ")
    list.append(name)
    if name == "":
        break


print("\n\t names of persons")
list.sort()
for name in list:
    print("\t"+name)

# EXERCISE2 =
# -->  algorithme permit us to return the smaller value

# -------------------------verion1-------------------------
name_driver = ['Baba', 'Ali', 'Cheikh', 'Daoud', 'Emir']
distance_car_km = [10, 12, 20, 2, 4]
index_min = 0
distance_min = distance_car_km[0]
for i in range(len(distance_car_km)):
    distance = distance_car_km[i]
    if distance < distance_min:
        distance_min = distance
        index_min = i

print(f"The smaller value of distance and the position is : {distance_min},{index_min},{name_driver[index_min]}")

# -------------------------verion2-------------------------
name_and_distance = [('Baba', 10), ('Ali', 12), ('Cheikh', 20), ('Daoud', 2), ('Emir', 4)]
name_and_distance_min = name_and_distance[0]

for distances in name_and_distance:
    if distances[1] < name_and_distance_min[1]:
        name_and_distance_min = distances
print(name_and_distance_min)

Generator_Password
def generator_password():
    pass_min= 6
    pass_max = 12
    varChar= digits + punctuation + ascii_letters
    password1="".join(choice(varChar) for i in range(randint(pass_min,pass_max)))
    return password1
print(generator_password())