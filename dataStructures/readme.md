### Abstract DataTypes

Abstract DataTypes or ABTs are logical representations of complex data structures.

### Big-O notation gives an upper bound to worst case scenario.

1. Constant Time: O(1)
2. Logarithimic Time: o(log(n))
3. Linear Time: O(n)
4. Linearithmic Time: O(n log(n))

### Recursion

1. Understand the importance of **base** case. This is the case where no recursive call is made.
2. To implement recursion there should be at least one base case.
3. The chain of recursion calls should eventually reach a base case.

### Formula for Factorial 

* Factorial(n) = n * Factorial(n-1)

### How Factorial Evaluates:

1. Factorial(5) = 5 * factorial(4) __returns(4*6)__

2. Factorial(4) = 4 * factorial(3) __returns(3*2)__

3. Factorial(3) = 3 * factorial(2) __returns(2*1)__

4. Factorial(2) = 2 * factorial(1) __returns(1*1)__

5. Factorial(1) = 1 * factorial(0) __returns(1)__  <mark>Breaks the chain of recursion.</mark>

6. If n == 0 return 1 <mark>This is the base case!</mark>
