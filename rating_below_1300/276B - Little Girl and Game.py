def solve():
    string=input()
    if len(string)%2:
        print("First")
    else:
        freq={}
        for i in string:
            freq[i]=freq.get(i,0)+1
        flag=0
        for k,v in freq.items():
            if v%2:
                flag=1
                break
        if flag:
            print("Second")
        else:
            print("First")
            
        

def main():
    # for i in range(int(input())):
    solve()
if __name__== "__main__":
    main()
    