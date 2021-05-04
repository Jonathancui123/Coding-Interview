Next Permutation:
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).

The replacement must be in place and use only constant extra memory.

1. Modify numbers from the end of the sequence

Ex 1
1 2 3 4
1 2 4 3
1 3 2 4
1 3 4 2
1 4 2 3
1 4 3 2
(2 4 3 1)
2 1 3 4
2 1 4 3
(2 3 4 1)
2 3 1 4
2 3 4 1
(2 4 3 1)
2 4 1 3
2 4 3 1
(3 4 2 1)
3 1 2 4

swap: i----j
reverse: [i+1, end] (to the end)


Ex 2
1
1

Ex 3
1 1 5
1 5 1