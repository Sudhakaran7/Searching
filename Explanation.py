Write an efficient algorithm that searches for a value in an RxC matrix. This matrix has the following properties:
Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.

Input Description:
First line contains, R,C,target. R-> rows, C-> coloumns. (1<R,c,target<100).
Second line contains, RxC elements of matrix in a single line.

Output Description:
Print True or False.

Sample Input:
3 4 3
1 3 5 7 10 11 16 20 23 30 34 50

Sample Output:
True

Explanation:
The given target is 3, the matrix has 3 and also it satisfies the given condition.

Sample Input:
2 3 4
1 2 3 4 5 6

Sample Output:
True

Sample Input:
4 3 5
1 2 3 5 4 6 7 8 9 12 13 14

Sample Output:
False

Sample Input:
2 3 1
2 3 4 1 5 4

Sample Output:
False

Sample Input:
2 4 203
103 117 234 334 201 202 203 204

Sample Output:
False

Sample Input:
2 3 55
22 27 34 37 47 55

Sample Output:
True
