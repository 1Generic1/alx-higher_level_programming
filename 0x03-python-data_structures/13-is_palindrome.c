#include <stdio.h>
#include <stdlib.h>
#include "list.h"

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
		return 1;
	}
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *prev_slow = NULL;
	listint_t *mid = NULL;
	listint_t *second_half = NULL;
	int is_palindrome = 1;
	listint_t *prev = NULL;
	listint_t *current = second_half;
	listint_t *next_node;
	listint_t *list1 = *head;
	listint_t *list2 = second_half;

	/* Find the middle of the linked list using slow and fast pointers */
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		prev_slow = slow;
		slow = slow->next;
	}
	/* Handle odd length by moving slow to the next node */
	if (fast != NULL)
	{
		mid = slow;
		slow = slow->next;
	}
	/* Reverse the second half of the linked list */
	second_half = slow;
	prev_slow->next = NULL;
	while (current != NULL)
	{
		next_node = current->next;
		current->next = prev;
		prev = current;
		current = next_node;
	}
	second_half = prev;
	/* Compare the first and second halves of the linked list */
	while (list1 != NULL && list2 != NULL)
	{
		if (list->n != list2->n)
		{
			is_palindrome = 0;
			break;
		}
		list1 = list1->next;
		list2 = list2->next;
	}
	/* Restore the reversed second half */
	prev = NULL;
	current = second_half
		while (current != NULL)
		{
			next_node = current->next;
			current->next = prev;
			prev = current;
			current = next_node;
		}
	/* Reconnect the first and second halves */
	prev_slow->next = second_half;
	if(mid != NULL)
	{
		mid->next = prev_slow->next;
		prev_slow->next = mid;
	}
	return is_palindrome;
}
