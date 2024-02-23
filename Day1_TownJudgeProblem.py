class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        #We are taking n+1 elements, having value 0 (means nobody is trusted and trusting initially)
        #As here in this list, our index elements which represents the person label and their respective values to determine how many people trust them. Hence, we need to leave 0th index because there is no person called 0.
        new = [0 for x in range(n+1)]

        for i in trust:
            trustor = i[0] #For all trustors
            trustee = i[1] #For all trustees

            new[trustor]-=1
            new[trustee]+=1
        
        for i in range(1,len(new)):
            if new[i]==n-1:
                return i
        return -1
