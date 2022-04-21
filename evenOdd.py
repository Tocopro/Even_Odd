# even numbers

def even_numeral(a, b):
    result = []
    for i in range(a, b, 1):
        if i % 2 == 0:
            result.append(i)

    print(result)


even_numeral(4, 30)
print(list(range(4, 30, 2)))
