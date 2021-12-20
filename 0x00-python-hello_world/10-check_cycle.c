#include "lists.h"
/**
 * check_cycle - check if linked list have a cycle or no
 * per_one: goes one by one through the linked list
 * per_two: goes two by two through the linked list
 * @list: linked list
 * Return: 0 if success or 1 if not
 */

int check_cycle(listint_t *list)
{
	listint_t *per_one = list;
	listint_t *per_two = list;

	if (list == NULL)
		return (0);

	while (per_two && per_two->next)
	{
		per_one = per_one->next;
		per_two = per_two->next->next;

		if (per_one == per_two)
			return (1);
	}
	return (0);
}
