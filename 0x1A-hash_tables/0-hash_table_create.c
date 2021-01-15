#include "hash_tables.h"

/**
 *hash_table_create - creates a hash table
 *@size: size of the array
 *Return: pointer to the newly created hash table
 */
hash_table_t *hash_table_create(unsigned long int size)
{
hash_table_t *table;

if (size < 1)
return (NULL);

table = malloc(sizeof(hash_table_t));

if (table == NULL)
return (NULL);

table->array = (hash_node_t**)malloc(size * sizeof(hash_node_t));
if (table->array == NULL)
return (NULL);

memset(table->array, 0, size * sizeof(hash_node_t));
table->size = size;
return table;
}
