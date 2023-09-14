#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - Prints Python bytes information
 * @p: Python object
 * Return: no return
 */
void print_python_bytes(PyObject *p)
{
	long int size, i, limit;
	char *str;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = ((PyVarObject *)p)->ob_size;
	str = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str);

	limit = size + 1;
	if (limit > 10)
		limit = 10;

	printf("  first %ld bytes:", limit);

	for (i = 0; i < limit; i++)
	{
		printf(" %02x", (unsigned char)str[i]);
	}

	printf("\n");
}

/**
 * print_python_list - Prints Python list information
 * @p: Python object
 * Return: no return
 */
void print_python_list(PyObject *p)
{
	PyListObject *list;
	PyObject *item;
	long int size, i;

	printf("[*] Python list info\n");
	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	list = (PyListObject *)p;
	size = PyList_GET_SIZE(p);

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GET_ITEM(list, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
		if (PyBytes_Check(item))
			print_python_bytes(item);
	}
}
