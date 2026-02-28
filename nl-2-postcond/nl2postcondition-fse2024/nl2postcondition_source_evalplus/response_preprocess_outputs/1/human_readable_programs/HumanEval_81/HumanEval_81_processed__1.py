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
    # This postcondition asserts that the length of the returned list of letter grades matches the length of the input list of GPAs.
    # It then verifies that each letter grade in the `return_value` list correctly corresponds to its GPA in the `grades` list,
    # following the specified grading scale in the problem description.
    assert len(return_value) == len(grades) and all(
        (gpa == 4.0 and letter_grade == "A+") or
        (gpa > 3.7 and letter_grade == "A") or
        (gpa > 3.3 and letter_grade == "A-") or
        (gpa > 3.0 and letter_grade == "B+") or
        (gpa > 2.7 and letter_grade == "B") or
        (gpa > 2.3 and letter_grade == "B-") or
        (gpa > 2.0 and letter_grade == "C+") or
        (gpa > 1.7 and letter_grade == "C") or
        (gpa > 1.3 and letter_grade == "C-") or
        (gpa > 1.0 and letter_grade == "D+") or
        (gpa > 0.7 and letter_grade == "D") or
        (gpa > 0.0 and letter_grade == "D-") or
        (gpa == 0.0 and letter_grade == "E")
        for gpa, letter_grade in zip(grades, return_value)
    )

    return return_value
