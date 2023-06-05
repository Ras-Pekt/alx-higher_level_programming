#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle
 * @list: pointer to the first node
 * Return: 1 if there is s cycle. 0 otherwise
*/
int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	if (list == NULL)
		return (0);
	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
			return (1);
	}
	return (0);
}
