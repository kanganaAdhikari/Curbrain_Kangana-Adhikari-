
#include <stdio.h>

int main()
{
    int n, i;
    int suffixSum = 0;

    printf("Enter the size of array: ");
    scanf("%d", &n);

    int arr[n > 0 ? n : 1];

    printf("Enter array elements: ");
    for (i = 0; i < n; i++)
    {
        scanf("%d", &arr[i]);
    }

    // Traverse from right to left
    for (i = n - 1; i >= 0; i--)
    {
        int original = arr[i];

        arr[i] = suffixSum;

        suffixSum = suffixSum + original;
    }

    printf("Array after suffix sum: ");
    for (i = 0; i < n; i++)
    {
        printf("%d ", arr[i]);
    }

    return 0;
}
