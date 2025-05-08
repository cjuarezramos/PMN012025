L = [1,40,3,5,6,89,2,4,7,8,9,10]
for i in range(len(L)):
    for j in range(i+1, len(L)):
        if L[i] > L[j]:
            L[i], L[j] = L[j], L[i]
print(L)