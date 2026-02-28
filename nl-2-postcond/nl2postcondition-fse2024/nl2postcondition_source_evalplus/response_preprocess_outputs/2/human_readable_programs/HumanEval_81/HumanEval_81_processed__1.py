def numerical_letter_grade_original(grades):
    """It is the last week of the semester and the teacher has to give the grades
    to students. The teacher has been making her own algorithm for grading.
    The only problem is, she has lost the code she used for grading.
    She has given you a list of GPAs for some students and you have to write 
    a function that can output a list of letter grades using the following table:
             GPA       |    Letter grade
              4.0                A+
            > 3.7                A 
            > 3.3                A- 
            > 3.0                B+
            > 2.7                B 
            > 2.3                B-
            > 2.0                C+
            > 1.7                C
            > 1.3                C-
            > 1.0                D+ 
            > 0.7                D 
            > 0.0                D-
              0.0                E
    

    Example:
    grade_equation([4.0, 3, 1.7, 2, 3.5]) ==> ['A+', 'B', 'C-', 'C', 'A-']
    """

    def to_letter_grade(score):
        if score == 4.0:
            return 'A+'
        elif score > 3.7:
            return 'A'
        elif score > 3.3:
            return 'A-'
        elif score > 3.0:
            return 'B+'
        elif score > 2.7:
            return 'B'
        elif score > 2.3:
            return 'B-'
        elif score > 2.0:
            return 'C+'
        elif score > 1.7:
            return 'C'
        elif score > 1.3:
            return 'C-'
        elif score > 1.0:
            return 'D+'
        elif score > 0.7:
            return 'D'
        elif score > 0.0:
            return 'D-'
        else:
            return 'E'
    return [to_letter_grade(x) for x in grades]


def numerical_letter_grade(grades):


    return_value = numerical_letter_grade_original(grades)
    
    # Adding imports that might be useful for postconditions
    import re 
    # The postcondition verifies that return_value is a list of the same length as grades and that each GPA is correctly mapped to its corresponding letter grade according to the specified thresholds.
    assert len(return_value) == len(grades) and all(l == ("A+" if g == 4.0 else "A" if g > 3.7 else "A-" if g > 3.3 else "B+" if g > 3.0 else "B" if g > 2.7 else "B-" if g > 2.3 else "C+" if g > 2.0 else "C" if g > 1.7 else "C-" if g > 1.3 else "D+" if g > 1.0 else "D" if g > 0.7 else "D-" if g > 0.0 else "E") for g, l in zip(grades, return_value))

    return return_value
