%Персонажи
character(assassin).
character(thief).
character(sorcerer).
character(king).
character(pontiff).
character(merchant).
character(architect).
character(condottiere).

%Цвет персонажей
color(king, gold).
color(pontiff, blue).
color(merchant, green).
color(condottiere, red).

%Игроки
player(masha).
player(gleb).
player(max).
player(sanek).
player(me).

%Деньги игроков
money_player(masha, 3).
money_player(gleb, 2).
money_player(max, 2).
money_player(sanek, 1).
money_player(me, 2).

%Количество кварталов на руках у игроков
quarter_player(masha, 2).
quarter_player(gleb, 3).
quarter_player(max, 4).
quarter_player(sanek, 3).
quarter_player(me, 3).

%Построенные кварталы игроков (игрок, цвет, цена)
built_player(masha, red, 2).
built_player(gleb, gold, 3).
built_player(max, green, 1).
built_player(sanek, blue, 2).
built_player(me, gold, 4).

%Кварталы на руке (цвет квартала, стоимость)
quarter(red, 2).
quarter(green, 5).
quarter(blue, 4).
quarter(red, 1).

%Мои построенные кварталы (цвет, стоимость)
my_built(gold, 4).
my_built(green, 2).
my_built(blue, 3).
my_built(gold, 3).


%Предикат для подсчета общей стоимости построенных кварталов
my_points(Total) :-
    %Находим все стоимости и помещаем их в список
    findall(Cost, my_built(_, Cost), Costs),
    %Суммируем элементы списка
    sum_list(Costs, Total).

%Функция для суммирования элементов списка
sum_list([], 0).
sum_list([Head|Tail], Sum) :-
    sum_list(Tail, X),
    Sum is Head + X.

%Мой Персонаж
:- dynamic my_character/1.
my_character(assassin).

%Список персонажей
list_character() :-
    character(X),
    write(X).

%Смена на нового персонажа
new_character(Name) :-
    retract(my_character(_)),
    assert(my_character(Name)),
    write("your new character is the "), 
    write(Name).

%Могу ли построить квартал
can_built() :-
    money_player(me, X),
    quarter(_, Y), 
    X >= Y.

%Могу ли разрушить Кварталы
can_destroy() :- 
    my_character(condottiere), 
    money_player(me, X),
    built_player(_, _, Y),  
    X >= Y - 1.

%Могу ли получить доп монеты
can_get_coins() :- 
    my_character(condottiere), 
        my_built(red, _); 
    my_character(king), 
        my_built(gold, _); 
    my_character(pontiff), 
        my_built(blue, _);
    my_character(merchant), 
        my_built(green, _).

%Могу ли убить
can_kill() :- 
    my_character(assassin).

%Могу ли своровать
can_still() :- 
    my_character(thief), 
    money_player(_, X), X > 0.

%Могу ли обменять кварталы
can_exchange_quarter() :- 
    my_character(sorcerer), 
    quarter_player(_, X), 
    X > 0.

%Могу ли получить доп кварталы
can_get_quarter() :- 
    my_character(architect).