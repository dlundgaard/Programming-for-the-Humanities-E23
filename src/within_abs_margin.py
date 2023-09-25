# Using `abs`, write some conditions that print `True` if the variable a is within 10% of the variable b and `False` otherwise. Compare your implementation with your partner's: do you get the same answer for all possible pairs of numbers?
def within_margin(a, b):
    print(abs(a - b) <= 0.1 * abs(b))

within_margin(1, 1.05)
within_margin(1.05, 1)
within_margin(1.11, 1)
within_margin(1, 1.15)
within_margin(-1, 1)
