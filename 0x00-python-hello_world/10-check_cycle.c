#include "lists.h"
/**
*check_cycle - that checks if a singly linked list has a cycle in it.
*@list: linked list
*Return:0 if there is no cycle, 1 if there is a cycle
*/
int check_cycle(listint_t *list)
{
	listint_t *faster, *slower;

	if (list == NULL)
		return (0);
	faster = list;
	slower = list;
	if (faster == NULL || slower == NULL)
		return (0);
	while (faster != NULL && slower != NULL)
	{
		faster = faster->next;
		if (faster != NULL)
			faster = faster->next;
		slower = slower->next;
		if (faster == slower)
		{
			return (1);
		}
	}
	return (0);
}
