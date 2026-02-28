
# Response 0
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


