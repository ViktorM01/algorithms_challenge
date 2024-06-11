class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse = True) 
        weight = 0
        for i in boxTypes:
            if truckSize <= 0:
                return weight
            weight += min(i[0], truckSize) * i[1]
            truckSize -= i[0]
        return weight

                
