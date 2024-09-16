from pyswip import Prolog

prolog = Prolog()

def query(msg: str) -> bool:
    a = list(prolog.query(msg))
    if (len(a) == 1 and a[0] == {}):
        return "true"
    if (len(a) == 0):
        return "false"
    return a

prolog.consult("lab.pl")
characters = query("character(X)")
flag = False
while (True):
    print("Введите имя персножа чтобы я мог порекомендовать правильно применить способность и дальнейший план на игру")
    name = input()
    for i in characters:
        if (i['X'] == name):
            flag = True
            break
    if (flag):
        break
    else:
        print("Такго персонажа нет. Вот их список")
        for i in characters:
            print(i['X'])

built = query("built_player(X, Z, Y)")
maxx = -1
namek = ""
color = ""
arr_name = {}
for i in built:
    arr_name[i['X']] = i['Z']
    if (i['Y'] > maxx):
        maxx = i['Y']
        namek = i['X']
        color = i['Z']
name_color_kill = query(f"color(X, {color})")
nc = name_color_kill[0]['X']
my_built = query("my_built(X,_)")
my_red = 0
my_blue = 0
my_green = 0
my_gold = 0
for mblt in my_built:
    if (mblt['X'] == "red"):
        my_red += 1
    elif (mblt['X'] == "gold"):
        my_gold += 1
    elif (mblt['X'] == "blue"):
        my_blue += 1
    elif (mblt['X'] == "green"):
        my_green += 1
if (name == "assassin"):
    print(f"На данном ходу стоит убить игрока {namek} так как он впереди всех и надо ухудшить ему игру")
    print(f"Так как его квартал цвета {color} вам стоит попытаться убить {nc}")
elif (name == "thief"):
    maxxm = 0
    namem = ''
    money_player = query("money_player(X,Y)")
    for i in money_player:
        if (i['Y'] > maxxm):
            maxxm = i['Y']
            namem = i['X']
    name_color_still = query(f"color(X, {arr_name[namem]})")
    nm = name_color_still[0]['X']
    print(f"Больше всего денег у игрока {namem} поэтому обокрасть нужно именно его")
    print(f"Так как его квартал цвета {arr_name[namem]} вам стоит попытаться обокрасть {nm}")
elif (name == "sorcerer"):
    quarter_player = query("quarter_player(X,Y)")
    maxxq = 0
    nameq = ''
    for i in quarter_player:
        if (i['Y'] > maxxq):
            maxxq = i['Y']
            nameq = i['X']
    print("Так как ваш персонаж чародей вы можете обменять свои кварталы")
    print(f"Советую поменяться с игроком {nameq} так как у него больше всего кварталов а именно {maxxq}")
elif (name == "king"):
    print(f"Так как ваш персонаж король возьмите 1 золотой за каждый ваш построенный золотой квартал а именно {my_gold}")
    print("Хорошая новость на следующем ходу вы сможете выбрать персонажа самым первым")
elif (name == "pontiff"):
    print(f"Так как ваш персонаж епископ возьмите 1 золотой за каждый ваш построенный синий квартал а именно {my_blue}")
    print("Также поните что ваши кварталы не может трогать кондатьер и вы в безопасности")
elif (name == "merchant"):
    print(f"Так как ваш персонаж купец возьмите 1 золотой и еще плюс 1 золотой за каждый ваш построиный зеленый квартал а именно {my_green}")
elif (name == "architect"):
    quarter = query("quarter(X, 1)")
    count = 0
    for i in quarter:
        count += 1
    print("Возьмите две карты кварталов")
    print(f"Так как вы зодчий вам стоит попытаться построить за ход как можно больше кварталов желательно за одну монету их вас есть в количестве: {count}")
else:
    print(f"На данном ходу стоит разрушить квартал игрока {name} так как он впереди всех и надо ухудшить ему игру")
    print(f"Также не забудьте взять золотой за каждый ваш построенный красный квартал а именно {my_red}")
my_money = query("money_player(me,X)")
my_money_count = my_money[0]['X']
if (my_money_count <= 2):
    print(f"У вас мало монет ({my_money_count}) возьмете вора или купца")
else:
    print(f"У вас достаточно монет({my_money_count}) советую не держать их долго у себя так как вор может вас обокрасть")

my_quarter = query("quarter(_,_)")
n = 0
for i in my_quarter:
    n += 1
if (n <= 2):
    print(f"У вас маловато кварталов ({n}) советую взять вам зодчиго или чародея")
else:
    print(f"У вас достаточно кварталов ({n}) советую не брать зодчиго или чародея")