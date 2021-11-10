from cs50 import get_string, get_int
import re
import array as arr
import sys

#promp user for a number and count the numbers of digits
#print INVALID if is not a valid lenght cc number
number = get_int ("Number:")
numberstr = str(number)
length = len(numberstr)
if (length != 13 and length != 15 and length != 16):
    print("INVALID")
    sys.exit(1)

#calculate the sum of the digit according to luhn's algorthm
#add the string to an list
ccnumber = []
ccnumber.extend(numberstr)

n = number
sum1 = 0
sum2 = 0
while (n > 0):
    s1 = n % 10
    n = n // 10
    sum1 = sum1 + s1

    s2 = n % 10
    n = n // 10
    tos2 = s2 * 2
    if tos2 > 9:
        a = tos2 % 10
        b = tos2 // 10
        sum2 = sum2 + a + b
    else:
        sum2 = sum2 + tos2

sumtotal = sum1 + sum2
firstdigit1 = ccnumber[0]
firstdigit = int(firstdigit1)
first2digit = []
first2digit.extend(ccnumber[0])
first2digit.extend(ccnumber[1])
first2 = [str(integer) for integer in first2digit]
a_string = "".join(first2)
twodigits = int(a_string)
lastdigit = sumtotal % 10

if lastdigit != 0:
    print("INVALID")
elif firstdigit == 4 and (length == 13 or 16):
    print("VISA")
elif (twodigits == 34 or 37) and length == 15:
    print("AMEX")
elif (twodigits > 50 and twodigits < 56) and length == 16:
    print("MASTERCARD")
else:
    print("INVALID")





