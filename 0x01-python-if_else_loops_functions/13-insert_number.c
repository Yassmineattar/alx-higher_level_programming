#include "lists.h"

/**
 * insert_node - function that inserts a number into a sorted singly-linked list.
 * @head: pints the head of the list.
 * @number: input
 *
 * Return: address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
        listint_t *node = *head, *nouv;

        nouv = malloc(sizeof(listint_t));
        if (nouv == NULL)
                return (NULL);
        nouv->n = number;

        if (node == NULL || node->n >= number)
        {
                nouv->next = node;
                *head = nouv;
                return (nouv);
        }

        while (node && node->next && node->next->n < number)
                node = node->next;

        nouv->next = node->next;
        node->next = nouv;

        return (nouv);
}
