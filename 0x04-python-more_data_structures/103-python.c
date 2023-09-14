#include <Python.h>

/**
 * print_python_bytes - prints some basic info about Python bytes objects.
 * @p: Python object
 */
void print_python_bytes(PyObject *p)
{
	PyBytesObject *bytes;
	int size, i;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	bytes = (PyBytesObject *)p;
	size = PyBytes_Size(p);
	printf("  size: %d\n", size);
	printf("  trying string: %s\n", bytes->ob_sval);
	printf("  first %d bytes:", (size < 10 ? size + 1 : 10));
	for (i = 0; i < (size < 10 ? size + 1 : 10); i++)
		printf(" %02x", bytes->ob_sval[i]);
	printf("\n");
}

/**
 * print_python_list - prints some basic info about Python lists.
 * @p: Python object
 */
void print_python_list(PyObject *p)
{
	PyListObject *list;
	Py_ssize_t size, i;

	printf("[*] Python list info\n");
	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	list = (PyListObject *)p;
	size = PyList_Size(p);
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);
	for (i = 0; i < size; i++)
	{
		printf("Element %ld: %s\n", i, Py_TYPE(list->ob_item[i])->tp_name);
		if (PyBytes_Check(list->ob_item[i]))
			print_python_bytes(list->ob_item[i]);
	}
}

