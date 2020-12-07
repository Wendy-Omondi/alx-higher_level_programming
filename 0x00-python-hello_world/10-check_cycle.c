#include "lists.h"
/**
 *check_cycle - checks if a singly linked list has a cycle
 *@list: singly linked list being checked
 *Return: Always 0
 */
int check_cycle(listint_t *list)
{
listint_t *s = list, *f = list;
s = f = list;

while (s && f && f->next)
{
s = s->next;
f  = f->next->next;
if (s == f)
{
printf("Linked List has a cycle\n");
return (0);
}
}
printf("Linked List has no cycle \n");
return (0);
}
