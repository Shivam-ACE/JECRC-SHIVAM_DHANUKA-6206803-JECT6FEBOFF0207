## generic exception handling cant handle the keyboard interrupt

import time

# n1, n2 = 21, 0
# try:
#     result = n1 / n2
#     print(result)
# except ZeroDivisionError:
#     print('Please do not choose 0 as the second number!')
    
# print('code after try except - 01')
# print('code after try except - 02')
# print('code after try except - 03')

try:
    a, b, c = 1, 2
except :
    print('For performing MVC, no. of variables should be equals to thr no. of values!')

try:
    print(a,b,c)
except :
    print('Identifiers are not there in the memory!')

# try:
#     while True:
#         print(time.time())
# except:
#     print('Loop got stopped!')