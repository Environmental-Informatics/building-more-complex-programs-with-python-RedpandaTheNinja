# Kevin Lee
# assign 2

import math
def mysqrt(a):
    #creadting arbitrary num it cannot be 1 less, then it explode
    x = a-0.1
    while True:
        # same code as the book
        y = (x + a / x) / 2
        if y == x:
            break
        x = y
    return x

def test_square_root():
    a = 1
    print('\na      mysqrt(a)     math.sqrt(a)     diff')
    print('-----------------------------------------------------')
    #make a loop to 1 to 9
    while a in range(10):
        sec_col = mysqrt(a)
        third_col = math.sqrt(a)
        diff = abs(third_col - sec_col)
        #display proper floating points
        print('{0:0.1f}   {1:.11f}      {2:.11f}    {3}'.format(a,sec_col,third_col,diff))
        a+=1

test_square_root()