# Solution 2
# O(nLog(n)) time | 0(1) space

def two_number_sum(array, target_sum):

   # first let's sort the array
   # from ascending order
   array.sort()

   # initialize our left pointer to 0
   # which is the first value in our array
   left = 0

   # initialize our right pointer to
   # the last index value in array
   right = len(array) - 1

   # while the two pointers don't overlap
   # or while the left not pass the right pointer
   while left < right:
       # add the value of left pointer & right pointer
       # add store it to current_sum
       current_sum = array[left] + array[right]

       # check if the current_sum is == target_sum
       if current_sum == target_sum:
           # if so, return the those two numbers
           return [array[left], array[right]]

       # if the current_sum is less than our target_sum
       elif current_sum < target_sum:
           # move our pointer to the right by 1
           # increment left pointer by 1
           left += 1

        # if the current_sum is greater than our target_sum
       elif current_sum > target_sum:
           # move the right pointer to the left
           # by decrementing the right pointer
           right -= 1

   # if none add up to target sum then
   # just return my empty array
   return[]
    
array = [3, 5, -4, 8, 11, 1, -1, 6]
target_sum =10
print(two_number_sum(array, target_sum))
