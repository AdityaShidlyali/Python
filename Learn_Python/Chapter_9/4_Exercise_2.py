def convert(l):
    return [str(i) for i in l if type(i) == (int) or type(i) == (float)]


l = ["Aditya", True, False, 1, 2.342, '1', '2']
print(convert(l))