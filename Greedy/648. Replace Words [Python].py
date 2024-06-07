class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionary = set(dictionary)
        sentence = sentence.split()
        n_sent = list()

        for i in sentence:
            for j in range(len(i)+1):
                pref = i[:j]
                if pref in dictionary:
                    n_sent.append(pref)
                    break
            else:
                n_sent.append(i)
                
        return ' '.join(n_sent)
