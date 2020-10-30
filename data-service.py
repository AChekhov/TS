"""Модуль призначено для роботи з вхідними даними
"""


def get_clients():
    """повертає список клієнтів з файла "dovidnik.txt"
    
    Returns:
       dovidnik_list : довідник
    """
    
    from_file = [
       "10;Яловичина;25,5",
       "20;Свинина;26,5",
       "30;Сало;15,0"
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
        print("код: {} назва: {} адреса: {}".format(dovidnik[0], dovidnik[1], dovidnik[2]))
    
dovidnik = get_clients()
    
for c in dovidnik:
    print(c)