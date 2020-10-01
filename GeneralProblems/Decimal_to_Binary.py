n = (input('Enter a Number: '))
try:
    n = int(n)    
    binary = ''
    while n:
        reminder = n % 2
        binary = str(reminder)+binary
        n = int(n/2)
    print(binary)

except:
    print("Invalid input ")
