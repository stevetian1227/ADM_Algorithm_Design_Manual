#include <stdio.h>
#include <string.h>

void insertion(int *array,int size)
{
    int i,j,tmp;
    for (i=0;i<size;i++)
    {
        j = i;
        while(j>0 && array[j-1]> array[j])
        {
            tmp = array[j];
            array[j] = array[j-1];
            array[j-1] = tmp;
            j=j-1;
        }
    }
    for (i=0;i<size;i++)
    {
        printf("%d\n",array[i]);
    }
}



int main(int argc, char **argv)
{
    int arr[] = {5,3,6,1,9};
    insertion(arr,5);
}