def filter_list(array):  
    output = []
    for el in array:  
        if type(el) != str and el >= 0:  
            output.append(el)  
    return output

print(filter_list([1, 2, 'a', 'b']))
print(filter_list([1,'a', 'b', 0, 15]))
print(filter_list([1, 2, 'aasf', '1', '123', 123]))
