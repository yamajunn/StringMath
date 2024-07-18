The program internally represents floating-point numbers in binary, and some fractional numbers cannot be represented accurately.
  
This may cause incorrect results to be output when calculating with a small number of numbers.
  
In the case of Python, the following is the result of the following
  
0.1 + 0.2 = 0.30000000000000004
  
which is the same as the following.
  
To get rid of it,
  
{"0+0": "0", "0+1": "1", ....... "9+8": "17", "9+9": "18"}
  
Prepare a dictionary as above, and use the concept of written arithmetic to repeatedly add one digit to one digit to derive the answer.
