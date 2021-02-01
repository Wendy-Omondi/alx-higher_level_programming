#include "lists.h"

/**
 * reverse_list - Reverses a singly-linked list.
 * @head: A pointer to head of the list to reverse.
 *
 * Return: A pointer to the head of the reversed list.
 */
listint_t *reverse_list(listint_t **head)
{
listint_t *node = *head, *next, *prev = NULL;

while (node)
{
next = node->next;
node->next = prev;
prev = node;
node = next;
}

*head = prev;
return (*head);
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: A pointer to the head of the linked list.
 *
 * Return: If not a palindrome - 0.
 *         If is a palindrome - 1.
 */
int is_palindrome(listint_t **head)
{
listint_t *tmp, *rev, *x;
size_t size = 0, i;

if (*head == NULL || (*head)->next == NULL)
return (1);

tmp = *head;
while (tmp)
{
size++;
tmp = tmp->next;
}

tmp = *head;
for (i = 0; i < (size / 2) - 1; i++)
tmp = tmp->next;

if ((size % 2) == 0 && tmp->n != tmp->next->n)
return (0);

tmp = tmp->next->next;
rev = reverse_list(&tmp);
x = rev;

tmp = *head;
while (rev)
{
if (tmp->n != rev->n)
return (0);
tmp = tmp->next;
rev = rev->next;
}
reverse_list(&x);

return (1);
}
