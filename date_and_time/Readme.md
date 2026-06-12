<!-- THIS is for maths  -->
 Great choice. The **`math` module** is one of the most important Python modules for problem solving, DSA, HackerRank, and real-world programming.

We'll follow your preferred learning pattern:

# 1. Simple Explanation

The **`math` module** provides mathematical functions that Python doesn't include by default.

First import it:

```python
import math
```

---

# Topic 1: Absolute Value

Returns the distance from zero.

```python
print(abs(-10))
print(abs(10))
```

Output:

```python
10
10
```

---

# Topic 2: Power

### Method 1

```python
print(2 ** 3)
```

Output:

```python
8
```

### Method 2

```python
import math

print(math.pow(2, 3))
```

Output:

```python
8.0
```

Notice: `math.pow()` returns a float.

---

# Topic 3: Square Root

```python
import math

print(math.sqrt(25))
```

Output:

```python
5.0
```

---

# Topic 4: Ceiling

Rounds upward.

```python
import math

print(math.ceil(4.1))
print(math.ceil(4.9))
```

Output:

```python
5
5
```

---

# Topic 5: Floor

Rounds downward.

```python
import math

print(math.floor(4.1))
print(math.floor(4.9))
```

Output:

```python
4
4
```

---

# Topic 6: Factorial

Very important for mathematics and probability.

```python
import math

print(math.factorial(5))
```

Output:

```python
120
```

Because:

```text
5! = 5 × 4 × 3 × 2 × 1
   = 120
```

---

# Topic 7: Greatest Common Divisor (GCD)

Very important for DSA.

```python
import math

print(math.gcd(12, 18))
```

Output:

```python
6
```

---

# Topic 8: Constants

### π (Pi)

```python
import math

print(math.pi)
```

Output:

```python
3.141592653589793
```

### e

```python
import math

print(math.e)
```

Output:

```python
2.718281828459045
```

---

# Topic 9: Logarithms

```python
import math

print(math.log(8, 2))
```

Output:

```python
3.0
```

Because:

```text
2³ = 8
```

---

# Topic 10: Trigonometry

```python
import math

print(math.sin(math.pi/2))
print(math.cos(0))
print(math.tan(0))
```

Output:

```python
1.0
1.0
0.0
```

---

# 2. Important Diagram

```text
math module
│
├── math.sqrt()
├── math.pow()
├── math.factorial()
├── math.gcd()
├── math.floor()
├── math.ceil()
├── math.log()
├── math.sin()
├── math.cos()
├── math.tan()
│
├── math.pi
└── math.e
```

---

# 3. Revision Notes

```text
1. import math

2. Square root:
   math.sqrt(n)

3. Power:
   math.pow(a,b)
   a ** b

4. Ceiling:
   math.ceil(x)

5. Floor:
   math.floor(x)

6. Factorial:
   math.factorial(n)

7. GCD:
   math.gcd(a,b)

8. Log:
   math.log(x,base)

9. Trigonometry:
   math.sin()
   math.cos()
   math.tan()

10. Constants:
    math.pi
    math.e
```

# Practice Questions

Try these without looking at the answers:

1. Find the square root of 144.
2. Find 5⁴.
3. Find the factorial of 6.
4. Find the GCD of 24 and 36.
5. Round 7.2 upward.
6. Round 7.9 downward.
7. Print the value of π.
8. Find log₂(32).

After you solve these, we'll move to **advanced math module topics**:

* `lcm()`
* `comb()` (nCr)
* `perm()` (nPr)
* `isqrt()`
* `prod()`
* `dist()`
* `degrees()`
* `radians()`
* precision and floating-point issues

These are the functions most useful in competitive programming and HackerRank.
