#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
*add_nodeint - adds a nouv node at the beginning of a listint_t list
*@head: head of listint_t
*@n: int to add in listint_t list
*Return: address of the nouv element, or NULL if it failed
*/
listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *nouv;

	nouv = malloc(sizeof(listint_t));
	if (nouv == NULL)
		return (NULL);
	nouv->n = n;
	nouv->next = *head;
	*head = nouv;
	return (nouv);
}
/**
*is_palindrome - identify if a syngle linked list is palindrome
*@head: head of listint_t
*Return: 1 if it is palindrome else 0
*/
int is_palindrome(listint_t **head)
{
	listint_t *head_rev = *head;
	listint_t *a = NULL, *b = NULL;

	if (*head == NULL || head_rev->next == NULL)
		return (1);
	while (head_rev != NULL)
	{
		add_nodeint(&a, head_rev->n);
		head_rev = head_rev->next;
	}
	b = a;
	while (*head != NULL)
	{
		if ((*head)->n != b->n)
		{
			free_listint(a);
			return (0);
		}
		*head = (*head)->next;
		b = b->next;
	}
	free_listint(a);
	return (1);
}
