#include "lists.h"
#include <stdlib.h>

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the head of the list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp = *head;
	int len = 0, i = 0, arr[2048];

	if (!*head || !(*head)->next)
		return (1);

	while (temp)
	{
		arr[len++] = temp->n;
		temp = temp->next;
	}

	for (i = 0; i < len / 2; i++)
	{
		if (arr[i] != arr[len - i - 1])
			return (0);
	}

	return (1);
}
