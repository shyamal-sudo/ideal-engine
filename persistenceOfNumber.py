def per(n):
    if len(str(n))==1:
        print(n)
        return "Done"

    digits=[int(i) for i in str(n)]

    result=1
    for j in digits:
        result *=j
    print(result)
    per(result)

while True:
    a = int(input("num plz"))
    per(a)
