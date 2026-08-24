#check if the given string is pallindrome or not
def pallindrome(st):
    reverse=""
    for i in range(len(st)-1,-1,-1):
        reverse=reverse+st[i]
    if reverse==st:
        print(f"{st} is a pallindrome")
    else:
        print(f"{st} is not a pallindrome")

pallindrome("NAMAN")
pallindrome("CURSOR")