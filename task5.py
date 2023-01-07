def __get_string(element):
    return element[1] + element[0]

def meeting(s: str) -> str:
    persons = s.upper().split(';')
    persons_names = []
    for it in persons:
        persons_names.append(list(it.split(':')))
    persons_names.sort(key=__get_string)
    print(persons_names)
    for i in persons_names:
        i[0], i[1] = i[1], i[0]

    for i in range(len(persons_names)):
        persons_names[i] = tuple(persons_names[i])
    string = ''.join(map(str, persons_names))
    string = string.replace("'", '')
    return string

print(meeting('Fred:Corwill;Wilfred:Corwill;Barney:Tornbull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill'))
