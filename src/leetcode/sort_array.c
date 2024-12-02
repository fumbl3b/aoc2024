#include <stdio.h>
#include <stdlib.h>

// Function prototype
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* sortArray(int* nums, int numsSize, int* returnSize);

void printArray(int* arr, int size) {
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

int main() {
    // Test case 1
    int test1[] = {5, 3, 8, 6, 2, 7, 4, 1};
    int size1 = sizeof(test1) / sizeof(test1[0]);
    int returnSize1;
    printf("Original array (Test 1): ");
    printArray(test1, size1);
    int* sorted1 = sortArray(test1, size1, &returnSize1);
    printf("Sorted array (Test 1): ");
    printArray(sorted1, returnSize1);
    free(sorted1); // Free the allocated memory

    // Test case 2
    int test2[] = {12, 45, 23, 51, 19, 8};
    int size2 = sizeof(test2) / sizeof(test2[0]);
    int returnSize2;
    printf("Original array (Test 2): ");
    printArray(test2, size2);
    int* sorted2 = sortArray(test2, size2, &returnSize2);
    printf("Sorted array (Test 2): ");
    printArray(sorted2, returnSize2);
    free(sorted2); // Free the allocated memory

    return 0;
}

void quickSort(int* arr, int low, int high) {
	if (low < high) {
		int pivot = arr[high];
		int i = low - 1;

		for (int j = low; j < high; j++) {
			if (arr[j] <= pivot) {
       				i++;
       				int temp = arr[i];
       				arr[i] = arr[j];
       				arr[j] = temp;
			}
		}

		int temp = arr[i + 1];
		arr[i + 1] = arr[high];
		arr[high] = temp;

		int pi = i + 1;

		quickSort(arr, low, pi - 1);
		quickSort(arr, pi + 1, high);
	}
}

// Function to sort an array (to be implemented by you)
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* sortArray(int* nums, int numsSize, int* returnSize) {
    // Allocate memory for the sorted array
    int* sorted = (int*)malloc(numsSize * sizeof(int));
    if (!sorted) {
        fprintf(stderr, "Memory allocation failed\n");
        exit(EXIT_FAILURE);
    }

    // Copy input array to sorted array
    for (int i = 0; i < numsSize; i++) {
        sorted[i] = nums[i];
    }
    
    // Set returnSize to numsSize
    *returnSize = numsSize;

    // Implement your sorting algorithm here
    // Example: You can fill in with your sorting logic.

    return sorted;
}
