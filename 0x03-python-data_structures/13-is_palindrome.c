#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * reverse_list - Reverses a singly linked list.
 * @head: Pointer to the head of the linked list.
 *
 * Return: Pointer to the new head of the reversed linked list.
 */
listint_t *reverse_list(listint_t *head)
{
	listint_t *prev = NULL;
	listint_t *current = head;
	listint_t *next_node;

	while (current != NULL)
	{
		next_node = current->next;
		current->next = prev;
		prev = current;
		current = next_node;
	}
	return (prev);
}

/**
 * find_middle - Finds the middle node of a linked list.
 * @head: Pointer to the head of the linked list.
 *
 * Return: Pointer to the middle node.
 */
listint_t *find_middle(listint_t *head)
{
	listint_t *slow = head;
	listint_t *fast = head;

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		slow = slow->next;
	}
	return (slow);
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: Double pointer to the head of the list.
 *
 * Return: 1 if the list is a palindrome, 0 otherwise.
 */


int is_palindrome(listint_t **head)
{
	if (*head == NULL)
	{
		return (1);
	}
	listint_t *fast = *head;
	listint_t *slow = *head;
	listint_t *prev_slow = NULL;
	listint_t *mid = NULL;
	listint_t *second_half = NULL;
	int is_palindrome = 1;
	listint_t *list1 = *head;
	listint_t *list2 = second_half;

	/* Find the middle of the linked list using slow and fast pointers */
	mid = find_middle(*head);
	prev_slow = NULL;
	slow = mid;
	if (fast != NULL)
	{
		mid = slow;
		slow = slow->next;
	}
	/* Reverse the second half of the linked list */
	second_half = reverse_list(second_half);
	/* Compare the first and second halves of the linked list */
	while (list1 != NULL && list2 != NULL)
	{
		if (list1->n != list2->n)
		{
			is_palindrome = 0;
			break;
		}
		list1 = list1->next;
		list2 = list2->next;
	}
	/* Restore the reversed second half */
		second_half = reverse_list(second_half);
	/* Reconnect the first and second halves */
	prev_slow->next = second_half;
	return (is_palindrome);
}
