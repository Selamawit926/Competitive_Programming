class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        di={}
        
        for i in strs:
            # print(''.join(sorted(i)))
            if ''.join(sorted(i)) in di:
                di[''.join(sorted(i))].append(i)
                
            else:
                di[''.join(sorted(i))]=[i]
                
        return di.values()
    