#reverse a number

def rev(n):

    print(n)
    re=0
    while n>0:
        re = re*10 + n%10
        #print(re)
        n=n//10
    return re
myNumber =9876
print(rev(myNumber))