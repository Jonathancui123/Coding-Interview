/*
 * hashmap.c
 *
 *  Created on: Dec. 18, 2019
 *      Author: Jonathan Cui
 */

//Keys will be strings and values will be an integer

#include <assert.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

typedef struct ll{
	struct llnode* head;
}ll;

typedef struct llnode{
	char* key;
	int val;
	struct llnode* next;
}llnode;


void print_hm(ll* hm, int n){
	for (int i = 0; i<n; i++){
		printf("a[%d]: ", i);
		if(hm[i].head){
			llnode* curr = hm[i].head;
			while(curr){
				printf("(%s, %d)",curr->key, curr->val);
				if(curr->next) printf(", ");
				curr = curr->next;
			}
		}else{
			printf("EMPTY");
		}
		printf("\n");
	}
	printf("--------------\n");
}

int hashFunc(char* name, int arrLen){
	int hashVal = 0;
	while(*name){
		hashVal += *name;
		name++;
	}
	return hashVal % arrLen;
}

struct ll* hm_create(int n){
	struct ll* hm = calloc(n, sizeof(struct ll));
	assert(hm);
	return hm;
}

//Fail to create a deep copy of the string

int hm_input(struct ll* hm, int n, char* key, int val){
	int index = hashFunc(key, n);
	if(!hm[index].head){
		//The index of the array is still empty
		llnode* new = malloc(sizeof(llnode));
		hm[index].head= new;
		new->key = key;
		new->val = val;
		new->next = NULL;
		assert(new);
		return 0;
	}else{
		//Not empty - already resided by another key-val pair
		llnode* curr = hm[index].head;
		llnode* prev = curr;
		do{
			//Check if the key already exists inside of the LL --> change the value if it does
			if(!strcmp(curr->key, key)){
				curr->val = val;
				return 0;
			}
			prev = curr;
			curr = curr->next;
		}while(curr);
		llnode* new = malloc(sizeof(llnode));
		prev->next = new;
		new->key = key;
		new->val = val;
		new->next = NULL;
		assert(new);
		return 0;
	}
}

struct ll* hm_dump(struct ll* hm, int n){
	for (int i = 0; i < n; i++){
		if(hm[i].head){
			llnode* curr = hm[i].head;
			llnode* prev = curr;
			while(curr){
				prev = curr;
				curr = curr->next;
				free(prev);
			}
		}
	}
	free(hm);
	return NULL;
}

int hm_retrieve(struct ll* hm, int n, char* key){
	int index = hashFunc(key, n);
	llnode* curr = hm[index].head;
	while(curr){
		if(!strcmp(curr->key, key)){
			printf("Value is: %d\n", curr->val);
			return curr->val;
		}
		curr = curr->next;
	}
	printf("Key not found\n");
	return -1;
}

int main(void){
	struct ll* hm = hm_create(5);
	print_hm(hm, 5);
	hm_input(hm, 5, "grak", 18);
	hm_input(hm, 5, "b", 20);
	hm_input(hm, 5, "c", 22);
	hm_input(hm, 5, "d", 392);
	hm_input(hm, 5, "j", 19);
	hm_input(hm, 5, "e", 238);
	hm_input(hm, 5, "abcdefm", 6969696);

	print_hm(hm, 5);
	hm_retrieve(hm, 5, "d");
	hm_retrieve(hm, 5, "grak");
	hm_retrieve(hm, 5, "peepee");
	hm_dump(hm, 5);
}

