import time, threading
def calc_square(n):
    print('Calculating Square')
    for i in n:
        time.sleep(0.2)
        print('Square', i**2)

def cal_cube(n):
    print('Calculating Cube')
    for i in n:
        time.sleep(0.2)
        print('Cube', i**3)

arr = [2,4,6,8]
# t = time.time()
# calc_square(arr)
# cal_cube(arr)
# print('completion time ', time.time() - t)

#threading
t1 = threading.Thread(target=calc_square, args=(arr,))
t2 = threading.Thread(target=cal_cube, args=(arr,))
ti = time.time()
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print('completion time', time.time() - ti)


for i in range(5):
    time.sleep(1)
    print(time.asctime())
