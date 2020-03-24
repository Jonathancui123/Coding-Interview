/*
 * IsUnique.c
 *
 *  Created on: Dec. 27, 2019
 *      Author: Jonathan Cui
 */

#include <stdbool.h>
#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#define CHARSET 128

bool bitVectorGet(int * bitVector, int index){
	bitVector += index / (sizeof(int) * 8);
	index %= (sizeof(int) * 8);
	return (*bitVector) & (1 << index);
}

bool bitVectorSetTrue(int * bitVector, int index){
	int setterbit = 1;
	bitVector += index / (sizeof(int) * 8);
	index %= sizeof(int) * 8;
	*bitVector = (*bitVector) | (setterbit << index);
	return setterbit;
}

//First solution using a bit vector
bool isUnique(char * str){
	if (strlen(str) > CHARSET) return false;
	int numInts = (CHARSET + sizeof(int) - 1)/ sizeof(int);
	int * bitVector = calloc(numInts, 8);

	for(int i = 0; i < strlen(str); i++){
		char letter = str[i];
		if(bitVectorGet(bitVector, letter)) return false;
		bitVectorSetTrue(bitVector, letter);
	}
	return true;
}



int main(void){
	printf("isUnique of AaBbCcDdEe12093845 is: %d\n",isUnique("AaBbCcDdEe12093845"));
	printf("isUnique of asdf is: %d\n",isUnique("asdf"));
	printf("isUnique of tes123 is: %d\n",isUnique("tes123"));
	printf("isUnique of abcdefghijklmnopqrs is: %d\n",isUnique("abcdefghijklmnopqrs"));
}
