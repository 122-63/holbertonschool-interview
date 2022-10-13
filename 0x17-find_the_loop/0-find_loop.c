#include "lists.h"
#include <stdio.h>
/**
 * find_listint_loop - function that finds the loop in a linked list.
 * @head: pointer to the head in linked list to test
 * Return: The address of the node where the loop starts,
 * or NULL if there is no loop
 */
listint_t *find_listint_loop(listint_t *head)
{
	listint_t *a = head;
	listint_t *b = head;

	while (b && b->next != NULL)
	{
		a = a->next;
		b = b->next->next;

		if (a == b)
			break;
	}

	if (a != b)
		return (NULL);

	a = head;

	while (a != b)
	{
		a = a->next;
		b = b->next;
	}

	return (a);
}
