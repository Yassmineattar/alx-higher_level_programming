#include "lists.h"
/**
 * check_cycle-function that checks if a list has a cycle in it
 * @list: the linked list to be checked
 * Return: 1 if it has a cycle, 0 otherwise
*/
int check_cycle(listint_t *list)
{
	listint_t *s = NULL, *f = NULL;

	s = list;
	f = list;

	while (f && f->next)
	{
		s = s->next;
		f = f->next->next;
		if (s == f)
			return (1);
	}
	return (0);
}
