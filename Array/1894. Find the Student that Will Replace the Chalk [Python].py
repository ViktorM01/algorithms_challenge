class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        total_chalk = sum(chalk)
        rem_chalk = k % total_chalk

        for idx, student_use in enumerate(chalk):
            if rem_chalk < student_use:
                return idx
            rem_chalk -= student_use
        
        return 0
