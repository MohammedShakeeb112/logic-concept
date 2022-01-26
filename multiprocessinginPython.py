import time, multiprocessing

def square(n):
    for i in n:
        time.sleep(1)
        print(f'square {i}', i**2)

def cube(n):
    for i in n:
        time.sleep(1)
        print(f'cube {i}', i**3)

if __name__ == '__main__':
    arr = [2,4,6,8]
    t = time.time()
    p1 = multiprocessing.Process(target=square, args=(arr,))
    p2 = multiprocessing.Process(target=cube, args=(arr,))

    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print('Completed time', time.time() - t)