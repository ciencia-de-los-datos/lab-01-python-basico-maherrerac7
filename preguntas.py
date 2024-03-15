"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    with open ('data.csv', 'r') as f:
        sum_seg_colm=0
        for row in f:
            row = row.split("\t")
            sum_seg_colm= sum_seg_colm + float(row[1])

    return sum_seg_colm


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    with open('data.csv', 'r') as archivo_csv:
        lines = archivo_csv.readlines()
        lines.count

    for line in lines:
        values =line.strip()  

    dict=[]      
    sum_a = 0 ; sum_b = 0 ; sum_c = 0 ; sum_d = 0 ; sum_e = 0
    for row in lines:
        if row[0] == "A":
            sum_a = sum_a + 1
        if row[0] == "B":
            sum_b = sum_b + 1
        if row[0] == "C":
            sum_c = sum_c + 1
        if row[0] == "D":
            sum_d = sum_d + 1  
        if row[0] == "E":
            sum_e = sum_e + 1  

    dict = [("A", sum_a),("B", sum_b),("C", sum_c),("D", sum_d),("E", sum_e)]

    return dict


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    with open ('data.csv', 'r') as f:
        f = [x.replace("\n", "") for x in f]
        f = [y.split("\t") for y in f]

        ext_letters = [t[0][0] for t in f]
        numbers = [int(t[1]) for t in f]

        sum_ext_letters = {}
        
        for letter, value in zip(ext_letters, numbers):
            if letter in sum_ext_letters:
                sum_ext_letters[letter] += value
            else:
                sum_ext_letters[letter] = value
        
        result = sorted([(letter,add) for letter, add in sum_ext_letters.items()])

    return result


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    with open ('data.csv', 'r') as f:
        f = [x.replace("\n", "") for x in f]
        f = [y.split("\t") for y in f]

        date_month = [t[2].split("-")[1] for t in f]

        result = [(month, date_month.count(month)) for month in sorted(set(date_month))]

    return result


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    with open ('data.csv', 'r') as f:
        f = [x.replace("\n", "") for x in f]
        f = [y.split("\t") for y in f]

        letters = [t[0][0] for t in f]
        numbers = [int(t[1][0]) for t in f]
        lista = list(zip(letters, numbers))

        max_min = {}

        for letter, value in lista:
            if letter not in max_min:
                max_min[letter] = {"maximo": value, "minimo": value}
            else:
                if value > max_min[letter]["maximo"]:
                    max_min[letter]["maximo"] = value
                if value < max_min[letter]["minimo"]:
                    max_min[letter]["minimo"] = value
        
        result = [(letter, max_min[letter]["maximo"], max_min[letter]["minimo"]) for letter in max_min]
        result = sorted(result, key =lambda result: result[0])

    return result


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    with open ('data.csv', 'r') as f:
        f = [x.replace("\n", "") for x in f]
        f = [y.split("\t") for y in f]

        min_max = {}

        for row in f:
            col5_dict = row[4]
            for key_number in col5_dict.split(","):
                key , number = key_number.split(":")
                number = int(number)
                if key in min_max:
                    min_max[key].append(number)
                else:
                    min_max[key]= [number]
            
            result =[]
            for key, numbers in sorted((min_max.items())):
                result.append((key,min(numbers), max(numbers)))
                    
    return result


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    with open ('data.csv', 'r') as f:
        f = [x.replace("\n", "") for x in f]
        f = [y.split("\t") for y in f]

        result =[]
        list_letter_number = [(int(t[1]), t[0]) for t in f]

        for ext_number in sorted(set(t[0] for t in list_letter_number)):
            letters =[t[1] for t in list_letter_number if t[0]==ext_number]
            result.append((ext_number, letters))

        result = sorted(result, key = lambda x: x[0])

    return result 


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    with open ('data.csv', 'r') as f:
        f = [row_1.replace("\n", "") for row_1 in f]
        f = [row_1.split("\t") for row_1 in f]

        result = []
        list_letter_number = [(int(t[1]), t[0]) for t in f]

        for ext_number in sorted(set(t[0] for t in list_letter_number)):
            letters = sorted(set([t[1] for t in list_letter_number if t[0] == ext_number]))
            result.append((ext_number, letters))

        result = sorted(result, key = lambda x: x[0])

    return result   


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    with open ('data.csv', 'r') as f:
        dict_letters_values ={}
        f = [x.replace("\n", "") for x in f]
        f = [y.split("\t") for y in f]

        for row in f:
            col5_dic = row[4]
            for key_value in col5_dic.split(","):
                key , value = key_value.split(":")
                value = int(value)
                if key in dict_letters_values:
                    dict_letters_values[key].append(value)
                else:
                    dict_letters_values[key] = [value]

        result = {key:len(values) for key, values in sorted(dict_letters_values.items())}

    return result


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    with open ('data.csv', 'r') as f:
        f = [x.replace("\n", "") for x in f]
        f = [y.split("\t") for y in f]

        col_0 = [t[0] for t in f]
        col_4 =[len(t[3].split(",")) for t in f]
        col_5 =[len((t[4]).split(",")) for t in f]

        result = list(zip(col_0, col_4, col_5 ))

    return result


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    with open ('data.csv', 'r') as f:
        f = [x.replace("\n", "") for x in f]
        f = [y.split("\t") for y in f]

        col_2=[int(t[1]) for t in f]
        col_4=[t[3] for t in f]
        result_dict = {}

        for i in range (len(col_2)):
            keys = col_4[i].split(",")
            for key in keys:
                if key in result_dict:
                    result_dict[key] += col_2[i]
                else:
                    result_dict[key] = col_2[i]
        
        sorted_dict = dict (sorted(result_dict.items()))

        format_dict = {}

        for key, value in sorted_dict.items():
            format_dict[key] = value
        
    return format_dict


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    with open ('data.csv', 'r') as f:
        result = {}

        for line in f:
            items = line.strip().split("\t")
            column1 , column5 = items[0], items[4]
            total =0

            for pair in column5.split(","):
                total += int(pair.split(":")[1])
            if column1 in result:
                result[column1] += total
            else:
                result[column1] = total
            
        result = dict(sorted(result.items()))

    return result