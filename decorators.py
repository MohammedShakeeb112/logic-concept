import time
#for calculating time is not efficient ways 
# def cal_square(numbers):
#     start = time.time()
#     result = []
#     for num in numbers:
#         result.append(num**2)
#     end = time.time()
#     print('Square Completion ' + str((end-start)*1000) + str(' milli seconds'))
#     return result

# def cal_cube(numbers):
#     start = time.time()
#     result = []
#     for num in numbers:
#         result.append(num**3)
#     end = time.time()
#     print('Cube Completion ' + str((end-start)*1000) + str(' milli seconds'))
#     return result

# arr = range(1,100000)
# sq_out = cal_square(arr)
# cube_out = cal_cube(arr)

def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__ + ' Completion time ' + str((end-start)*1000) + ' milli seconds')
        return result
    return wrapper

# @time_it
# def cal_square(numbers, s=[]):
#     result = []
#     for num in numbers:
#         result.append(num**2)
#     return result

# @time_it
# def cal_cube(numbers):
#     result = []
#     for num in numbers:
#         result.append(num**3)
#     return result

# arr = range(1, 100000)
# sq_out = cal_square(arr, s=36)
# cube_out = cal_cube(arr)

# def funcret(num):
#     if num == 0:
#         return print
#     if num == 1:
#         return int
# a = funcret(0)
# print(a)

def executor(fun,s):
    ar = [i for i in range(1,11)]
    fun('it works')
    return fun(s(ar))
# executor(print, sum)


# def decor(fun):
#     def wrapper():
#         a = fun()
#         return a+15
#     return wrapper

# @decor
# def num():
#     return 15
# without writing @decor
# res = decor(num)
# print(res())

# with @decor
# print(num())

def decor1(num):
    def inner():
        a = num()
        multi = a * 5
        return multi
    return inner

def decor2(num):
    def inner():
        a = num()
        add = a + 5
        return add
    return inner

# without @decor_function
# def num():
#     return 10
# num = decor2(decor1(num))
# print(num())

# with @decor_function
@decor2
@decor1
def num():
    return 10
# print(num())