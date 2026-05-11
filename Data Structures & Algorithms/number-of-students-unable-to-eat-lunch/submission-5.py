class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        loop = 0
        i,j= 0, 0
        while students and loop < len(students):
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                loop = 0
            else:
                students.append(students.pop(0))
                loop = loop +1
        return len(students)