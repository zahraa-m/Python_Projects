#while

i=5

while i>0:
    print(i)
    i-=1


#break
i=5
while i>0:
    print(i)
    i-=1
    break


#skipping num 3
i=6
while i>0:
    i-=1
    if i == 3:
        continue
    if i==1:
        print(i)
        print("Breaking")
        break
    print(i)

print("finished")


