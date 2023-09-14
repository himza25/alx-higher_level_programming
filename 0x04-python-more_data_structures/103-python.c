#include <Python.h>

/**
 * print_python_list - prints some basic info about Python lists
 * @p: pointer to the python object
*/
void print_python_list(PyObject *p)
{
	int size, alloc, i;
	PyObject *item;

	printf("[*] Python list info\n");

	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	size = PyList_Size(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %d: %s\n", i, Py_TYPE(item)->tp_name);
		if (PyBytes_Check(item))
			print_python_bytes(item);
	}
}

/**
 * print_python_bytes - prints some basic info about Python bytes
 * @p: pointer to the python object
*/
void print_python_bytes(PyObject *p)
{
	char *str;
	int i, size;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	str = PyBytes_AsString(p);

	printf("  size: %d\n", size);
	printf("  trying string: %s\n", str);
	printf("  first %d bytes:", size + 1 < 10 ? size + 1 : 10);

	for (i = 0; i < size + 1 && i < 10; i++)
		printf(" %02hhx", str[i]);

	printf("\n");
}
