calc_score = []
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
sort_score = sorted(students)

calc_score = {
    sort_score[0]: (sum(grades[0])) / len(grades[0]),
    sort_score[1]: (sum(grades[1])) / len(grades[1]),
    sort_score[2]: (sum(grades[2])) / len(grades[2]),
    sort_score[3]: (sum(grades[3])) / len(grades[3]),
    sort_score[4]: (sum(grades[4])) / len(grades[4])
}
print(calc_score)
