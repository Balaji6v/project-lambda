# Generate Fibonacci series using lambda and iteration
fibonacci = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]], range(n - 2), [0, 1])

# Import reduce from functools
from functools import reduce

# Generate the first 50 Fibonacci numbers
fib_series = fibonacci(50)
print(fib_series)
