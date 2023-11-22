import time

#Converts a positive number to a binary represented as a list of 0s and 1s.
#using the algorithm of divide by 2 and put the remainder in the small column then start again with the quotient as input
def pos_dec_to_binary(decimal,bit_list):
    if decimal<=1:
        bit_list.append(decimal%2)
        return list(reversed(bit_list))
    else:
        bit_list.append(decimal%2)
        return pos_dec_to_binary(decimal//2,bit_list)
    
#why does this not work? Fix it! - ok don't shout :(
def countdown(number):
    # Base Case
    if number == -1:
        return
    print(number)
    time.sleep(1)
    # Recursive case
    countdown(number-1)


#try to complete this - I've changed it quite a bit but it still functions as should
def fibonacci(n):  # Actual sequence
  if n <= 1:  # Base case
    return n
  else:  # Recursive case
    return (fibonacci(n - 1) + fibonacci(n - 2))


def full_seq():  # Used as a safe holder so the sequence doesn't count continuously
  nterms = int(input("Enter the number of terms: "))
  if nterms <= 0:
    print("There can only be positive integers. ")
  else:
    print("Fibonacci sequence: ")
    for i in range(nterms):
      print(fibonacci(i))


#triangular numbers
def triangular(n):
    #base case
    #recursive case
    pass

#try to complete this - ok - done
def factorial(number):
    # Base Case
    if number < 0:
        return "Numbers below 0 cannot be in a factorial" # checks if a number is 0 or negative
    else:
        if not str(number).isdigit():
            return "Numbers given must be whole" # checks if number is a decimal
        else:
            if (number == 1) or (number == 0):
                return 1
            # Recurssive Case
            else:
                return number * factorial(number - 1)

def is_palendromic(string):
    """
    A recursive palendrome subroutine; it checks if the word is the same when reversed
    """
    if len(string) < 2:
       return True
    if string[0] != string[-1]:
       return False
    else:
       return is_palendromic(string[1:-1])

#try to complete a recursive linear search, returning the index of the item, or -1
def linear_search_recursive(items, start_index, end_index, search_item):
    """
    A Linear search using recursion to go through the list, if the selected item is the search item - output the index of the item
    """
    #base cases
    if start_index > end_index:
       return -1
    #recursive case:
    if search_item == items[start_index]:
       return start_index
    else:
       return linear_search_recursive(items, start_index + 1, end_index, search_item)



def binary_search_recursive(items,start_index, end_index, search_item): # RE-used code :) - should still work :?
    """
    A Binary search using recursion, returning the index of the item in the list or -1 if not in the list.
    The start index should be 0 and the end index should be 1 less than the length of the list.
    """
    # Base cases for if the item isn't in the list or if the item has been found
    if start_index > end_index:
        return -1
    middle_index = (start_index + end_index) // 2
    current_item = items[middle_index]
    if current_item == search_item:
        return middle_index
    # Recursive cases
    elif current_item < search_item:
        return binary_search_recursive(items, middle_index + 1, end_index, search_item)
    else:
        return binary_search_recursive(items, start_index, middle_index - 1, search_item);


"""EXTENSION: Euclid's algorithm. The greatest common divisor (gcd) of two positive integers is the largest integer
that divides evenly into both of them. For example, the gcd(102, 68) = 34.
We can efficiently compute the gcd using the following property, which holds for positive integers p and q:

If p > q, the gcd of p and q is the same as the gcd of q and p % q."""

#tests
#print(pos_dec_to_binary(1234,[]))
##or, neater (using a generator expression (outside scope of A-level CS))
#print("".join(str(i) for i in pos_dec_to_binary(1234,[])))
#print (factorial(5))
#print (full_seq())
#countdown(10)
#print(linear_search_recursive([1,2,3,4,54,56,58],0,6,1))
print(is_palendromic("racecar"))