#include "lists.h"
#include <stdlib.h>

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer of first node of listint_t list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp = *head;
	int len = 0, i;
	int *array;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (temp != NULL)
	{
		len++;
		temp = temp->next;
	}

	array = malloc(sizeof(int) * len);
	if (array == NULL)
		return (0);

	temp = *head;
	for (i = 0; i < len; i++)
	{
		array[i] = temp->n;
		temp = temp->next;
	}

	for (i = 0; i < len / 2; i++)
	{
		if (array[i] != array[len - i - 1])
		{
			free(array);
			return (0);
		}
	}

	free(array);
	return (1);
}
