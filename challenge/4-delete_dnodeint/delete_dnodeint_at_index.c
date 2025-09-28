#include "lists.h"
#include <stdlib.h>

/**
 * delete_dnodeint_at_index - deletes the node at index of a dlistint_t list
 * @head: pointer to pointer to the head node
 * @index: index of the node that should be deleted (0-based)
 *
 * Return: 1 if it succeeded, -1 if it failed
 */
int delete_dnodeint_at_index(dlistint_t **head, unsigned int index)
{
	dlistint_t *node;
	unsigned int i;

	if (head == NULL || *head == NULL)
		return (-1);

	node = *head;

	/* move to the node at given index */
	for (i = 0; node != NULL && i < index; i++)
		node = node->next;

	if (node == NULL)
		return (-1);

	/* bridge neighbors around 'node' */
	if (node->prev != NULL)
		node->prev->next = node->next;
	else
		*head = node->next;

	if (node->next != NULL)
		node->next->prev = node->prev;

	free(node);
	return (1);
}
