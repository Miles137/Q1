# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.

nums = list(range(2000,3201))
## did not need to make this list separately: can just iterate through them in the for loop
## do not need to make a list of the numbers: can just return them with comma separation via join

for num in nums:
#    print('anynum = ', num, 'bool = ', (num%7 != 0) or (num%5 == 0))
    if (num%7 != 0) or (num%5 == 0):
#        print('num = ', num, 'bool = ', (num%7 != 0) or (num%5 == 0))
        nums.remove(num)
#adding a line from vim to test pushing from cloned directory
#
       
print (nums)
