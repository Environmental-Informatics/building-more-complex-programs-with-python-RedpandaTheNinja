# Kevin Lee
# assign 2

# a =4
# x = 3
import math
def mysqrt(a):
    x = a-0.1
    while True:
        # print( x )
        y = (x + a / x) / 2
        if y == x:
            break
        x = y
    return x

def test_square_root():
    a = 1
    print('\na      mysqrt(a)     math.sqrt(a)     diff')
    print('-----------------------------------------------------')
    while a in range(10):
        sec_col = mysqrt(a)
        third_col = math.sqrt(a)
        diff = abs(third_col - sec_col)
        print('{0:0.1f}   {1:.11f}      {2:.11f}    {3}'.format(a,sec_col,third_col,diff))
        # print('\n')
        a+=1

test_square_root()