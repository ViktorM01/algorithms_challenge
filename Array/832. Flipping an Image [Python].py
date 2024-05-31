class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        tab = list()
        for i in image:
            lst = i[::-1]
            for l in range(len(lst)):
                if lst[l] == 1:
                    lst[l] = 0
                else:
                    lst[l] = 1
            tab.append(lst)
        return tab
