class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats, students = sorted(seats), sorted(students)
        return sum([abs(students[i] - seats[i]) for i in range(len(seats))])
