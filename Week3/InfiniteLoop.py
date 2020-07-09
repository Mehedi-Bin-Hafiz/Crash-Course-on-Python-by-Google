# x=0
# while x % 2 == 0:
#     print(x)
#     x = x / 2

# x = 0
# while x <= 10:
#     print(x)

def print_range(start, end):
	# Loop through the numbers from start to end
	n = start
	while n <= end:
		print(n)
		n += 1

print_range(1, 5)  # Should print 1 2 3 4 5 (each number on its own line)

def sum_divisors(n):
  if n == 0:
    return 0
  sum = 0
  m = 1
  # Return the sum of all divisors of n, not including n
  while m < n:
      if( n % m == 0 ):
        sum = sum + m
      m = m + 1
  return sum

print(sum_divisors(0))
# 0
print(sum_divisors(3)) # Should sum of 1
# 1
print(sum_divisors(36)) # Should sum of 1+2+3+4+6+9+12+18
# 55
print(sum_divisors(102)) # Should be sum of 2+3+6+17+34+51
# 114
