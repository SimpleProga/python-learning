#def compute_surface(radius):
    #from math import pi
    #return pi * radius * radius

#def variable_len(*args):
#    print(type(args))
#    print(args)       
#    for x in args:
#        print(x)
#        print(type(x))
#variable_len(2,3,4)  

#product = lambda x,y: x*y
#print(product(2,3))

#def variable_len(**args):
#    print(type(args))
#    print(args.items())
#   for x, value in args.items():
#      print(x, value)

#variable_len(apple = "яблоко", bread = "хлеб")

#def print_mean_sequences(**kwargs):
#    def mean(data):
#        return sum(data)/float(len(data))
#    for k, v in kwargs.items():
#        print(k, mean(v))

#print_mean_sequences(x=[1,2,3], y=[3,3,0])

#def greet(name):
#    """  Функция выводит приветственное сообщение для имени name """
#    print("Hello, " + name + ". Good morning!")
#greet("Amir")
#print(greet.__doc__)

#def e():
#    x = 5
#    def inner_e():
#        nonlocal x
#        x = x + 1
#        return x
#    return inner_e()
#print(e())

#val1 = "my global"
#val2 = "another global"
#def example():
#    print(val1) # Выведет my global
#    global val2
#    val2 = "change another global"
#example()
#print(val2) # Выведет change another global

#num = 42
#def some_function(n):
#    res = n + num
#    return res
#print(some_function(1))
#print(num)

#def calculate(num1, num2):
#    return num1 + num2, num1 - num2, num1 * num2
# для так называемой распаковки нескольких значений 
# их следует присвоить равному количеству аргументов
#res1 ,res2, res3 = calculate(7, 6)
#print(res1, res2, res3)

#lambda_test = lambda a, b: pow(a, b)
#print(lambda_test(2, 4))

#def prod(a: int, b: int) -> int:
#    return a * b
#print(prod(2, 4))

#def linear(a, b):
#    if (a == 0 and b == 0):
#        print("Бесконечное количество решений.")
#    if (a == 0 and b != 0):
#        print("Нет решений.")   
#    if (a != 0):
#        sol = -b/a
#        print(sol)
# Это процедура!
#linear(1,1)

#def sum_from_one(num):
#    if num == 1:
#        return 1
#    return num + sum_from_one(num - 1)
#print(sum_from_one(5))

#def multiplicator(x):
#    global k
#    k = 2
#    print("Значение локальной переменной k:", k)
#    return k*x
#k = 20
#multiplicator(4)
#print("Значение внешней переменной k:", k)   

#def print_kwargs(**kwargs):
#    for key in kwargs:
#        print("key = {0}, value = {1}".format(key, kwargs[key])) 
#print_kwargs(a = 2, b = 10)

#def sum_arg(a, **kwargs):
#    print(a, kwargs)
#    return a + sum(kwargs.values())
#print(sum_arg(10, c = 10, b = 5, d = 30))