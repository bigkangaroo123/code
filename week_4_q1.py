N = 1216
x = 0
while N > 0:
    x = x + N % 10
    N = N/10
    #end
print(x)

#program adds all the digits that make the number N
#By dividing by 10 and getting the remainder, it kinda exculdes the ones digit and adds it to x 
