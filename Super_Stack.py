Implement a simple stack that accepts the following commands and performs the operations associated with them:

push k: Push integer k onto the top of the stack.
pop: Pop the top element from the stack.
inc e k: Add k to each of the bottom e elements of the stack.
 

Function Description 

Complete the function superStack in the editor below. The function must create an empty stack and perform each of the operations in order. After performing each operation, print the value of the stack's top element on a new line. If the stack is empty, print EMPTY instead.

 

superStack has the following parameter(s):

    operations[operations[0],...operations[n-1]]:  an array of strings

 

Constraints

1 ≤ n ≤ 2 × 105
-109 ≤ k ≤ 109
1 ≤ e ≤ |S|, where |S| is the size of the stack at the time of the operation.
It is guaranteed that pop is never called on an empty stack.
 

Input Format for Custom Testing
Input from stdin will be processed as follows and passed to the function.

 

The first line contains an integer n, the size of the array operations.

The next n lines each contain an element operations[i] .

Sample Case 0
Sample Input 0

12
push 4
pop
push 3
push 5
push 2
inc 3 1
pop
push 1
inc 2 2
push 4
pop
pop
 

Sample Output 0

4
EMPTY
3
5
2
3
6
1
1
4
1
8
 

Explanation 0

The diagram below depicts the stack after each operation:


After each operation, we print the value denoted by Current Top on a new line.

 

In other words, we have an empty stack, S, we express as an array where the leftmost element is the bottom of the stack and the rightmost element is its top. We perform the following sequence of n = 12 operations as given in the operations array:

push 4: Push 4 onto the top of the stack, so S = [4]. We then print the top (rightmost) element, 4, on a new line.
pop: Pop the top element from the stack, so S = []. Because the stack is now empty, we print EMPTY on a new line.
push 3: Push 3 onto the top of the stack, S = [3]. Print 3, and the top of the stack after each of the following operations.
push 5: Push 5 onto the top of the stack, S = [3, 5]. 
push 2: Push 2 onto the top of the stack, S = [3, 5, 2]. 
inc 3 1: Add k = 1 to bottom e = 3 elements of the stack, S = [4, 6, 3]. 
pop: Pop the top element from the stack, S = [4, 6]. 
push 1: Push 1 onto the top of the stack, S = [4, 6, 1]. 
inc 2 2: Add k = 2 to bottom e = 2 elements of the stack,  S = [6, 8, 1]. 
push 4: Push 4 onto the top of the stack, S = [6, 8, 1, 4]. 
pop: Pop the top element from the stack, S = [6, 8, 1]. 
pop: Pop the top element from the stack, S = [6, 8].
