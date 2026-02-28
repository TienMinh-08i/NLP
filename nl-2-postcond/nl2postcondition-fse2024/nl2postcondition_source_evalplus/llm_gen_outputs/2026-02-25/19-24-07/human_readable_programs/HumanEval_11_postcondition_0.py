# This postcondition checks that the returned string has the same length as the input strings, consists only of '0's and '1's, and that each character is the result of the binary XOR operation on the corresponding characters of the input strings.
assert len(return_value) == len(a) and all(c in '01' for c in return_value) and all(int(return_value[i]) == (int(a[i]) ^ int(b[i])) for i in range(len(a)))


