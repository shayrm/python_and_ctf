def is_prime(num):
    prime_list = []
    for x in range(1, num):
        for y in range(2, x):
            if x%y==0:
                break
            else:
                prime_list.append(x)
                #print (x,sep=' ', end=' ')
    return prime_list
number = int(input("enter number for prime range: "))
print(is_prime(number))
