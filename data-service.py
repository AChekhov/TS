"""Модуль призначено для роботи з вхідними даними
"""


def get_clients():
    """повертає список клієнтів з файла "dovidnik.txt"
    
    Returns:
       dovidnik_list : довідник
    """
    
    from_file = [
       "1;Масло",
       "2;Сир_твердий",
       "3;Молоко",
       "4;Сир",
       "5;Маргарин",
       "6;М'ясо",
       "7;Ковбаса",
       "8;Фарш_м'ясний",
       "9;М'ясо_кістки"
    ]
 
     # накопичувач
    dovidnik_list = []
    
    for line in from_file:
        line_list = line.split(';')
        dovidnik_list.append((line_list))
    
    return dovidnik_list

def show_dovidnik(dovidnik):
    """виводить на екран список довідника по заданій умові
 
    Args:
        dovidnik (list): список довідника
    """
    for dovidnik in dovidnik:
        print("код: {2} назва: {Сир_твердий}".format(dovidnik[0], dovidnik[1], dovidnik[2]))
    
dovidnik = get_clients()
    
for c in dovidnik:
    print(c)