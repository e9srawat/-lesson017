# Limitations
1. Prefix and suffix cannot be the same values, it will lead to infinite loop, a solution to this could be using regular expression instead of just string manipulation

2. Prefix or suffix cannot be the empty values it will either give an error or will run infinitely, this can be fixed by adding checks in the function

3. The function is case sensitive but can be made case insensitive using .lower() method of string