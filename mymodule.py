def add(*args):
    sum = 0
    for i in args:
        sum +=i
    return sum

def fact(*agrs):
    # res = []

    for i in agrs:
        fact =1

        for j in range(1,i+1):
            fact *=j
        print(f"factorial of {i} = {fact}")