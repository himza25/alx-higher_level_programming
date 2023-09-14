#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - prints some basic info about Python lists.
 * @p: A Python object.
 */
void print_python_list(PyObject *p)
{
    int size, alloc, i;
    const char *type;
    PyListObject *list = (PyListObject *)p;

    size = (int)PyList_Size(p);
    alloc = (int)(list->allocated);
    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %d\n", size);
    printf("[*] Allocated = %d\n", alloc);

    for (i = 0; i < size; i++)
    {
        type = (list->ob_item[i])->ob_type->tp_name;
        printf("Element %d: %s\n", i, type);
        if (strcmp(type, "bytes") == 0)
        {
            print_python_bytes(list->ob_item[i]);
        }
    }
}

/**
 * print_python_bytes - prints some basic info about Python bytes objects.
 * @p: A Python object.
 */
void print_python_bytes(PyObject *p)
{
    int size, i;
    char *string;

    printf("[.] bytes object info\n");

    if (strcmp(p->ob_type->tp_name, "bytes") != 0)
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = (int)PyBytes_Size(p);
    string = (char *)PyBytes_AsString(p);
    printf("  size: %d\n", size);
    printf("  trying string: %s\n", string);
    printf("  first %d bytes:", (size < 10) ? size + 1 : 10);

    for (i = 0; i < ((size < 10) ? size + 1 : 10); i++)
    {
        printf(" %02hhx", string[i]);
    }
    printf("\n");
}
