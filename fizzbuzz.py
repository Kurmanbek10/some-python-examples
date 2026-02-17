#Print numbers from 1 to 100 but: 'range(1,101)'

for n in range(1, 101):
    # for numbers which are multiples of both 3 and 5, print "FizzBuzz"
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    # for multiples of 3, print "Fizz" instead of the number.
    elif n % 3 == 0:
        print("Fizz")
    # for multiples of 5, print "Buzz" instead of the number.
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)