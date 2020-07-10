'''
    this is a test file
'''
def prime_no(n):
    '''
        this is a function to check if a no. is a prime no. or not
    '''
    n = int(input("enter the number 'n' "))
    if n > 1:
        for i in range(2, n):
            if(n%i) == 0:
                print("not a prime no: ", n)
                break
            else:
                print("it's a prime no. ",n)
    else:
        print(" not a prime no: ", n)
                
