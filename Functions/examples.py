#Type 1: No Arguments & No Return
def print_numbers():
    for i in range(1, 6):
        print(i)

print_numbers()

#Type 2: With Arguments & No Return
def check_even_odd(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")

check_even_odd(4)
#Type 3: No Arguments & With Return
def return_value():
    return 50
x = return_value()
print(x)
#Type 4: With Arguments & With Return
def larger(a, b):
    if a > b:
        return a
    else:
        return b

print(larger(10, 20))



