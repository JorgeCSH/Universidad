import numpy as np

def transpose(x, a, n):
    if a[0] == x:
        return a
    
    for i in range(0 ,n):
        if a[i] == x:
            a[i] = a[i-1]
            a[i-1] = x 
            return a
    a[n] = a[n-1]
    a[n-1] = x
    return a

a = [1, 2, 5, 11, 66, 4, None]
x = 4 
n = len(a)-1

completo_italiano = transpose(x, a, n)

print(completo_italiano)

def move_to_front(x, a, n):
    if a[0] == x:
        return a

    for i in range(0, n):
        if a[i] == x:
            while i != 0:
                a[i] = a[i-1]
                i -= 1
            a[0] = x
            return a

    for j in range(0, n):
        a[n-j] = a[n-j-1]
    a[0] = x

    return a

y = 1 

a = [1, 2, 5, 11, 66, 4, None]
print(move_to_front(y, a, n))
print(np.full(5, None))


def transpose2(x, a, n):
    pos = 0
    while pos < n:
        if a[pos] == x:
            break
        pos += 1
    if pos == n:
        a[pos] = x
        
    if pos != 0:
        a[pos], a[pos-1] = a[pos-1], a[pos]
    return a

aa = np.array([1, 4, 6, 2, 8, 69, None])
x1 = 1
x2 = 8
x3 = 420
nigeria = len(aa)-1

print(f"{aa}\n" )

#print(transpose2(x1, aa, nigeria))
#print(transpose2(x2, aa, nigeria))
#print(transpose2(x3, aa, nigeria))

def move_to_front2(x, a, n):
    pos = 0
    while pos < n:
        if a[pos] == x:
            break
        pos += 1
    if pos == n:
        a[pos] = x
        
    while pos > 0:
        a[pos], a[pos-1] = a[pos-1], a[pos]
        pos -= 1
    return a

aa = np.array([1, 4, 6, 2, 8, 69, None])
print()
#print(move_to_front2(x1, aa, nigeria))
#print(move_to_front2(x2, aa, nigeria))
#print(move_to_front2(x3, aa, nigeria))


