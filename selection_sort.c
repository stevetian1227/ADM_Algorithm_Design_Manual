#include <string.h>
#include <stdio.h>

void selection(int *arr,int size)
{
    int i,j,min,tmp;
    for (i=0;i<size;i++)
    {
        min = i;
        for (j=i+1;j<size;j++)
        {
            if (arr[j]<arr[min])
            {
                min = j;
            }
        }
        tmp = arr[i];
        arr[i] = arr[min];
        arr[min] = tmp;
    }
    for (i=0;i<size;i++)
    {
        printf("%d ",arr[i]);
    }
}

int main(int argc, char **argv)
{
    int arr[] = {6,5,8,1,4,9};
    selection(arr,6);
}