#include <stdio.h>
#include <string.h>

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

int main(){
	char* str = "Hello";
	char* cu = "String";
	printf("%s\n", reverseArray(str));
	printf("%s\n", reverseArray(cu));
	return 1;
}