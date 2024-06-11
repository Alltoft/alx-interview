#!/usr/bin/python3
"""retreives the min number of operations to reach a given number."""
# import math


# prime_list = [2, 3, 5, 7]


# def isprime(n):
#     """
#     Check if a number is prime.

#     Args:
#         n (int): The number to check.

#     Returns:
#         bool: True if the number is prime, False otherwise.
#      float: The quotient of the number divided by the smallest prime factor.
#         int: The smallest prime factor of the number.
#     """
#     if n in prime_list:
#         return True
#     squaroot = math.sqrt(n)
#     for i in prime_list:
#         if n % i == 0 or n == 1:
#             return False, n / i, i
#     if squaroot.is_integer():
#         if isprime(squaroot):
#             return False
#     else:
#         return True


# def minOperations(n):
#     """
#     Calculate the minimum number of operations required
#     to reach a given number.

#     Args:
#         n (int): The target number.

#     Returns:
#         int: The minimum number of operations required.
#     """
#     if n <= 0:
#         return 0

#     if isprime(n)[0]:
#         return n
#     else:
#         gather_list = []
#         gather_list.append(isprime(n)[2])
#         number = isprime(n)[1]
#         while number != 1:
#             for i in prime_list:
#                 if number % i == 0:
#                     gather_list.append(i)
#                     number = number / i
#     minOperations = sum(gather_list)
#     return minOperations


def minOperations(n):
    """function minOperations"""
    if n <= 1:
        return 0
    for op in range(2, n+1):
        if n % op == 0:
            return minOperations(int(n/op)) + op
