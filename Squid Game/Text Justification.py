class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        count=j=0
        lst=[]
        curr=[]
        space=False
        over=False
        while j<len(words):
            word=words[j]
            # print(word,count)
            if count+len(word)>maxWidth or over:
                if space:
                    i=0
                    # print(curr)
                    while count<maxWidth:
                        if curr[i][0]==" ":
                            curr[i][1]+=1
                            count+=1
                        i+=1
                        if i>=len(curr):
                            i=0
                else:
                    curr.append([" ",maxWidth-count])
                count=0
                lst.append(curr)
                curr=[]
                space=False
                over=False
            else:
                if curr:
                    if count+len(word)+1<=maxWidth:
                        curr.append([" ",1])
                        curr.append(word)
                        count+=1+len(word)
                        space=True
                        j+=1
                    else:
                        over=True
                else:
                    curr.append(word)
                    count+=len(word)
                    j+=1
        # print(curr,lst)
        if curr:
            curr.append([" ",maxWidth-count])
            lst.append(curr)
        # print(lst)
        curr2=[]
        output=[]
        for curr in lst:
            for word in curr:
                if word[0]==" ":
                    new=" "*word[1]
                    curr2.append(new)
                else:
                    curr2.append(word)
            sent="".join(curr2)
            output.append(sent)
            curr2=[]
        return output