import time
def martin(num):
    while num > 0:
        print(f'{num} Seconds!!!!')
        num-=1
        time.sleep(1)
    print('Happy rich day punk!!!')
martin(5)
