#include <stdio.h> 

long rproduct(long start,long count){
    if (count <= 1){
        return 1;
    }
    return start rproduct(start+1,count-1);
}

int main()
{
    val = rproduct(4,2);
    printf("Value: %d\n",val);
    return 0;
}
