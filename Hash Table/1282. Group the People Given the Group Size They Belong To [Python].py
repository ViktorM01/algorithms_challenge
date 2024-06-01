class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        n = range(len(groupSizes))
        key_dic = {key: [i for i, _ in enumerate(groupSizes) if _ == key] for key in set(groupSizes)}
        lst = []
        for key, indx in key_dic.items():
            for i in range(0, len(indx), key):
                lst.append(indx[i:i+key])
        return lst
            
