#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to head of list
 * Return: 1 if it is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
    listint_t *slow, *fast, *prev_slow = NULL, *mid = NULL;
    listint_t *second_half, *prev = *head;
    int res = 1;

    if (*head == NULL || (*head)->next == NULL)
        return (1);

    slow = *head;
    fast = *head;

    /* Find the middle of the list */
    while (fast != NULL && fast->next != NULL)
    {
        fast = fast->next->next;
        prev_slow = slow;
        slow = slow->next;
    }

    /* If the list has odd number of nodes, ignore the middle node */
    if (fast != NULL)
    {
        mid = slow;
        slow = slow->next;
    }

    /* Reverse the second half of the list */
    second_half = slow;
    prev_slow->next = NULL;
    while (second_half != NULL)
    {
        listint_t *next = second_half->next;
        second_half->next = prev;
        prev = second_half;
        second_half = next;
    }

    /* Compare the first and second halves of the list */
    while (*head != NULL && prev != NULL)
    {
        if ((*head)->n != prev->n)
        {
            res = 0;
            break;
        }
        *head = (*head)->next;
        prev = prev->next;
    }

    /* Restore the original list */
    second_half = prev;
    prev = NULL;
    while (second_half != NULL)
    {
        listint_t *next = second_half->next;
        second_half->next = prev;
        prev = second_half;
        second_half = next;
    }
    if (mid != NULL)
    {
        prev_slow->next = mid;
        mid->next = prev;
    }
    else
        prev_slow->next = prev;

    return res;
}
