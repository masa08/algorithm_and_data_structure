def fizzBuzz(number):
    string = '1'
    for n in range(2, number+1):
        if n % 3 == 0 and n % 5 == 0:
            string += "-FizzBuzz"
        elif n % 3 == 0:
            string += "-Fizz"
        elif n % 5 == 0:
            string += "-Buzz"
        else:
            string += "-{}".format(n)
    return string
