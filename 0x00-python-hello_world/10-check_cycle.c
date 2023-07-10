/*
 * task 10 File: 10-check_cycle.c
 */

#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - Checks if a singly-linked list contains a cycle.
 * @list: A singly-linked list.
 *
 * Return: If there is no cycle - 0.
 *         If there is a cycle - 1.
 */
int check_cycle(listint_t *list)
{
	listint_t *tl, *hr;

	if (list == NULL || list->next == NULL)
		return (0);

	tl = list->next;
	hr = list->next->next;

	while (tl && hr && hr->next)
	{
		if (tl == hr)
			return (1);

		tl = tl->next;
		hr = hr->next->next;
	}

	return (0);
}
