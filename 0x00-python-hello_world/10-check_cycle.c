#include "lists.h"

int check_cycle(listint_t *list)
{
    listint_t *per_one = list;
    listint_t *per_two = list;

if (list == NULL)
return(0);

    while (per_two && per_two->next)
    {
        per_one = per_one->next;
        per_two = per_two->next->next;

        if (per_one == per_two)
            return(1);
    }
return(0);
}