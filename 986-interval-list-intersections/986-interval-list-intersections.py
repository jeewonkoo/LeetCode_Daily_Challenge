class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if not firstList or not secondList: return []
        output = []
        i, j = 0, 0
        
        while i < len(firstList) and j < len(secondList) :
            start_1, end_1 = firstList[i]
            start_2, end_2 = secondList[j]
            
            max_ = max(start_1, start_2)
            min_ = min(end_1, end_2)
            if max_ <= min_:
                output.append([max_, min_])
                
            if end_2 > end_1: 
                i +=1 
            else: 
                j +=1
                
        return output