#ABCD ABCD ABCD ABCD
n = int(input())
i=1
p=1
while i<= n:
    j=1
    while j<=i:
        print(p, end="")
        j=j+1
        p=p+1
    print()
    i=i+1