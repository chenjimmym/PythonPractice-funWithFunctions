# Print odd and even numbers
for i in range(0,2001):
    if i%2 == 0:
        print "Number is {}. This is an even number".format(i)
    else:
        print "Number is {}. This is an odd number".format(i)

#multiply by 5
a = [2,4,10,16]

def multiply (a, mult):
    b = []
    for data in a:
        b.append(data * mult)
    return b

b = multiply(a, 5)
print b

#hacker challenge
def layered_multiples(arr):
    new_array = []
    for data in arr:
        temp = []
        for i in range(0, data):
            temp.append(1)
        new_array.append(temp)
    return new_array
x = layered_multiples(multiply([2,4,5],3))
print x