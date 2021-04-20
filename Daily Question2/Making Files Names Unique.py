class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        
        # print(names)
        
        di={}
        output=[]
        
        for i in names:
            if i in di:
                new=i+"("+str(di[i]+1)+")"
                di[i]+=1
                if new in di:
                    # print(new)
                    word=self.check(di,new,i)
                    # print(word)
                    output.append(word)
                    di[word]=0
                    
                else:
                    output.append(new)
                    di[new]=0
                    
            else:
                di[i]=0
                output.append(i)
                
                
        return output
    
    
    def check(self,di,word,original):
        if word in di:
            # print(word,di[original])
            new=original+"("+str(di[original]+1)+")"
            # print(new)
            di[original]+=1
            word=self.check(di,new,original)
            
        return word