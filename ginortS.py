# You are given a string .
#  contains alphanumeric characters only.
#  Your task is to sort the string  in the following manner:

# All sorted lowercase letters are ahead of uppercase letters.
# All sorted uppercase letters are ahead of digits.
# All sorted odd digits are ahead of sorted even digits.
# Input Format

# A single line of input contains the string .

# Constraints

# Output Format

# Output the sorted string .

# Sample Input

# Sorting1234
# Sample Output

# ginortS1324

import re
S= input()
series="[a-z]","[A-Z]","[13579]","[02468]"
print("".join(map(lambda x: "".join(sorted(re.findall(x, S))),series)))
