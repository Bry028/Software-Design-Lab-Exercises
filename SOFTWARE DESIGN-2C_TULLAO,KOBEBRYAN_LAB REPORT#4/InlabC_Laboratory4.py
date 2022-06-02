def reverse_string(s):
    if len(s)<=0:
        #print("<=0")
        return 0
    elif len(s)==1:
        #print("==1", s)
        return s
    else:
        #print(">1", s)
        return s[-1] + reverse_string(s[:-1])

if __name__=="__main__":
    s = input("Enter word to reverse: ")
    print(reverse_string(s))