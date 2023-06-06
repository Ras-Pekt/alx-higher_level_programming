#include <stdio.h>
#include<stdlib.h>
#include<string.h>
#include "lists.h"
/**
 * insert_node - inserts a node in a sorted linked list
 * @head: pointer to head node
 * @number: number to be inserted
 * Return: pointer to new node. NULL otherwise
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp_head, *temp_prev, *new_node;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	if (*head == NULL)
	{
		new_node->next = NULL;
		return (new_node);
	}

	temp_head = *head;
	while (temp_head)
	{
		if (temp_head->n > number)
			break;
		temp_prev = temp_head;
		temp_head = temp_head->next;
	}
	new_node->n = number;
	new_node->next = temp_head;
	temp_prev->next = new_node;

	return (new_node);
}
