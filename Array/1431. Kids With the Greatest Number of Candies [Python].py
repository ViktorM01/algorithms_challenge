class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        lst = []
        max_value = max(candies)

        for i in candies:
            if i + extraCandies >= max_value:
                lst.append(True)
            else:
                lst.append(False)

        return lst
