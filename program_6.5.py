# Kevin Lee
# assign 2

def gcd(int1 , int2):
    #if first input is larger then 2nd
    if int1 > int2:
        remainder = int1 / int2
        clean_remainder = int( remainder )
        remainder = int1 - int2 * clean_remainder
        #if clean div happens then, original int is the largest GCD
        if remainder == 0 :
            remainder = int2
    else:
        #incase 2nd int is larger than 1st int
        remainder = int2 / int1
        clean_remainder = int( remainder )
        remainder = int2 - int1 * clean_remainder
        if remainder == 0 :
            remainder = int2
    print(remainder)
    return remainder

#change whatever number you would like to test
remain = gcd( 102 , 24 )
secondgcd = gcd( 24 , remain )
# print(secondgcd)
if remain == secondgcd:
    print( "GCD is ==" , secondgcd )
else:
    #incase it doesn't have any other than just 1
    print("GCD is ==", 1)
