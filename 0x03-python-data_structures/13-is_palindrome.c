#include<stdio.h>
#include<stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer to the head of the linked-list
 * Return: 1 if a palindrome. 0 otherwise
*/
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *rev = NULL;
	listint_t *temp;

	/*
	* by moving fast by 2 steps and slow by 1
	* when fast reaches the end, slow will be at the midpoint
	* having reversed the first half of the list
	*/
	while (fast && fast->next)
	{
		fast = fast->next->next; /*moves fast two steps*/
		temp = slow; /*sets temp to slow*/
		slow = slow->next; /*moves slow one step*/
		temp->next = rev; /*reverses temp's pointer*/
		rev = temp; /*sets rev_node as the new temp*/
	}
	/*
	* fast moves by two steps i.e 0, 2, 4, 6....
	* slow moves by one step i.e 0, 1, 2, 3....
	* if list is odd numbered, fast will not have reached the end and
	* slow will not have reached the midpoint, hence the need for this step
	*/
	if (fast)
		slow = slow->next;
	/*
	* at this point, slow is at the beginning of the 2nd half of the list
	* rev is at the beginning of the first, now reversed, half of the list
	*/
	while (slow && rev)
	{
		if (slow->n != rev->n)
			return (0);
		slow = slow->next;
		rev = rev->next;
	}
	return (1);
}
