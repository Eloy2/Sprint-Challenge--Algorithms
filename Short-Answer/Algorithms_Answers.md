#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)If n is 1 then the while loop condition is while a < 1:
    After the first loop a will be 1.
    Our function has finished.
If n is 4 then the while loop condition is while a < 64:
    After the first loop a will be 16.
    After the second loop a will be 80.
    Our function has finished.
If n is 500 then the while loop condition is while a < 125,000,000:
    After the first loop a will be 250,000.
    After the second loop a will be 125,250,000.
    Our function has finished.
This is either O(c) or O(n).
Taking this into account I think this function is O(n). Why? because even though the number of loops remain the same. The amount of space required does not. 



b) As the input sizes increase the amount of operations will increase slightly faster than linear. So I think this is O(n log n).


c) O(n) As input increases so does the amount of operations we need to perform. It will increase linearly. If I add one bunny it will make one recursive call. If I add two bunnies then it will make two recursive calls. etc...

## Exercise II

I would use a binary search for this. I would start at the middle and if the egg breaks then I would set my new middle in between the 
bottom floor and one floor lower of the previous middle point. If the egg does not break then I would set my new middle in between one 
more than previous middle and top floor. I would then repeat. This runtime is O(log(n)) since we are halving the number of floors each time.

Depending on the size of the building we could use an iterative solution. We could simply start at the bottom and keep moving up until an egg breaks. 
Then we would have found f and only one egg would have been broken. This runtime is O(n) since we are halving the number of floors each time.
