/* The maximum difference for a pair of elements in some array 
a is defined as the largest difference between any a[i] and a[j] where i < j and a[i] < a[j].
 
The declaration for a function named maxDifference (which takes array a as a parameter) is provided for you in the editor. 
Complete the function so that it calculates and returns the maximum difference for a; if no such number exists 
(e.g.: if a is in descending order and all a[j] < a[i]), return -1.
 
Input Format
The task of reading input (defined below) from stdin, assembling it into array a, 
and and calling maxDifference(a) is already handled for you by the locked code in the editor.
 
The first line contains N (the number of elements in array a).
The N subsequent lines each contain a single element of a; the ith line of input 
(where 0 < i < N-1) contains element a[i].
 
Constraints
1 ≤ N ≤ 106
−10^6 ≤ a[i] ≤ 10^6 ∀ i ∈ [0, N-1]
 
Output Format
Your maxDifference function should return the maximum difference in a. 
Printing to stdout is handled for you by the locked code in the editor.
 
Sample Input 0
7
2
3
10
2
4
8
1
 
Sample Output 0
Sample Input 1
6
7
9
5
6
3
2
 
Sample Output 1
2
  Explanation
Sample Case 0: n = 7, a = {2, 3, 10, 2, 4, 8, 1}
As a[2] = 10 is largest element in the array, we must find the smallest a[i] where 0 ≤ i < 2. 
This ends up being 2 at index 0.
We then calculate the difference between the two elements: a[2] − a[0] = 10 − 2 = 8, 
and return the result (8).
 
Note: While the largest difference between any two numbers in this array is 9 (between a[2] = 10 and a[6] = 1), 
this cannot be our maximum difference because the element having the smaller value (a[6]) must be of a lower 
index than the element having the higher value (a[2]). As 2 is not less than 6, 
these elements cannot be used to calculate our maximum difference.
 
Sample Case 1: n = 6, a = {7, 9, 5, 6, 3, 2}
The maximum difference returned by our function is a[1] − a[0] = 9 − 7 = 2, because 2 is the largest 
difference between any a[i] and a[j] satisfying the conditions that a[i] < a[j] and i < j.
*/

#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

/*
 * Complete the function below.
 */
int maxDifference(int a_size, int* a) {
    int largest  = -1000000, smallest = 1000000, li = 0;
    int i;
    for(i = 0; i < a_size; i++){
        if(a[i] > largest){
            largest = a[i];
            li = i;
        }
    }
    for(i = 0; i < li; i++){
        if(a[i] < smallest){
            smallest = a[i];
        }
    }
    return largest - smallest;

}
int main() {
    FILE *f = fopen(getenv("OUTPUT_PATH"), "w");
    int res;
    
    int _a_size = 0;
    int _a_i;
    scanf("%d\n", &_a_size);
    int _a[_a_size];
    for(_a_i = 0; _a_i < _a_size; _a_i++) {
        int _a_item;
        scanf("%d", &_a_item);
        
        _a[_a_i] = _a_item;
    }
    
    res = maxDifference(_a_size, _a);
    fprintf(f, "%d\n", res);
    
    fclose(f);
    return 0;
}

