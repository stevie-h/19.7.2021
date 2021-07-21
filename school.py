# ex22

def calculate_average(*gr):
    sum_grades = 0
    for n in gr:
        sum_grades += n
    return sum_grades / len(gr)


def add_bonus(*gr):
    grades_bonus = []
    for n in gr:
        grades_bonus.append(n + 5)
    return grades_bonus


def get_result(gr):
    if gr == 100:
        return 'Excellent'
    elif gr >= 80:
        return 'Very Good'
    elif gr >= 70:
        return 'Good'
    elif gr >= 60:
        return 'Pass'
    else:
        return 'Fail'


