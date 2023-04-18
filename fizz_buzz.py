def fizz_buzz(i):
    output = ''
    if i % 3 == 0 or i % 5 == 0:
        if i % 3 == 0:
            output += 'Fizz'
        if i % 5 == 0:
            output += 'Buzz'
    else:
        output = str(i) 
    return output   

