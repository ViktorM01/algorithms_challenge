class Solution {
public:
    int mostWordsFound(vector<string>& sentences) {
        int length = 0;
        for(string &sentence:sentences){
            int wordsCount = 1;
            for(int i = 0 ;i < sentence.size(); i++){
                if(sentence[i] == ' '){
                    wordsCount++;
                }
            }
            if(wordsCount>length){
                length = wordsCount;
            }
        }
        return length;
    }
};
