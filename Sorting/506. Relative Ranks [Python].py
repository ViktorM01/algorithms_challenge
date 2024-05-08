class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sort_scores = sorted(score, reverse=True)
        medals = ['Gold Medal', 'Silver Medal', 'Bronze Medal']

        rank_map = {score: medals[i] if i < 3 else str(i+1) for i, score in enumerate(sort_scores)}
        return [rank_map[score] for score in score]
