numbers = [3,5,6,2,8,9]

#linear searching searches in a linear way

def linearsearching(n):
    for i in numbers:
        if i == n:
            return("item found")
            break
    
    return("item not found")      

print(linearsearching(7))