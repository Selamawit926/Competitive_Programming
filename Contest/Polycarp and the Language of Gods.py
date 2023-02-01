def count(di,word,count):
    # print("here: ,", count)
    for i in range(len(word)):
        if word[i] in di:
            di[word[i]].append(i)
        else:
            di[word[i]]=[i]

    # print(di)
    for letter in di:
        if letter=="w":
            count+=len(di[letter])
        else:
            if len(di[letter])>1:
                diff=1
                for i in range(1,len(di[letter])):
                    if di[letter][i]-di[letter][i-1]==1:
                        diff+=1
                    
                    else:
                        count+=diff//2
                        diff=1
                # print(diff)
                count+=(diff//2)
    
    print(count)

n= eval(input())
lst=[]
for i in range(n):
    word= input()
    lst.append(word)
di={}
for word in lst:
    count({},word,0)