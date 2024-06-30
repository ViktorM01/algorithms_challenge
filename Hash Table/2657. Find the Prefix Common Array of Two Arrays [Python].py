class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        lst = [0] * len(A)
        sub_list = set()

        for i in range(len(A)):
            sub_list.add(A[i])
            sub_list.add(B[i])
            lst[i] = 2 * (i + 1) - len(sub_list)


        return lst
