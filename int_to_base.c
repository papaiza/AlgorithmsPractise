#include <stdio.h>
#include <string.h>

char digitToChar(int digit){
    while (digit > 36){
        digit %= 36;
    }
    if (digit < 10){
        return digit + '0';
    }else{
        return digit - 10 + 'A';
    }
}

char* reverseArray(char str[]){
    char temp[100] ;
    int i ;
    int j;
    int size = strlen(str);
    for(i = 0, j = size - 1; j >= 0; i++, j--){
        temp[i] = str[j];
    }
    temp[i] = '\0';
    return temp;
}

char* displayAsBase(int x, int base)
{
    char arr[10];
    int i = 0;
    while(x != 0)
    {
        arr[i] = digitToChar(x % base);
        i ++;
        x = x/base;
    }
    arr[i] = '\0';
    return reverseArray(arr);
}



main()
{
  printf("%s\n", displayAsBase(42, 16));
  printf("%s\n", displayAsBase(257, 8));
    printf("%c\n", digitToChar(10));
    printf("%c\n", digitToChar(38));
    char *str = "String";
    printf("%s\n", reverseArray(str));

}