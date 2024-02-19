# n-th Catalan Number

Catalan numbers are defined as a mathematical sequence that consists of positive integers, which can be used to find the number of possibilities of various combinations. 
The nth term in the sequence denoted $C_n$, is found in the following formula: 
$\frac{(2n)!}{((n + 1)! n!)}$

    The first few Catalan numbers for n = 0, 1, 2, 3, … are : 1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, …  

Catalan numbers occur in many interesting counting problems like the following.

1. Count the number of expressions containing n pairs of parentheses that are correctly matched. For $n = 3$, possible expressions are ((())), ()(()), ()()(), (())(), (()()).
2. Count the number of possible Binary Search Trees with n keys (See this)
3. Count the number of full binary trees ($A$ rooted binary tree is full if every vertex has either two children or no children) with $n+1$ leaves.
4. Given a number $n$, return the number of ways you can draw n chords in a circle with $2 x n$ points such that no $2$ chords intersect.