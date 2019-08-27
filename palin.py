
#code contrtibuted bt shyamal bhatt

while True:
    a,j,k=str(input()),-1,0

    for i in range(0,len(a)):
        if a[i]==a[j]:
            j=j-1
            k=k+1
        else:
            break
        
    if k==len(a):
        print('it is a palindron')
    else:
        print('it is not palindron')


