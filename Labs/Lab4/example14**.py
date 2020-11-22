s1 = input("Enter a string: ")
for c in range(1, len(s1)+1):
    for pos in range(0, len(s1)-c+1):
        print(s1[pos:pos+c])
