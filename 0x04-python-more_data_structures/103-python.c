#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes - Prints Python bytes.
 * @p: PyObject list object.
 */
void print_python_bytes(PyObject *p)
{
	long int size, i, limit;
	char *string;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = ((PyVarObject *)p)->ob_size;
	string = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", string);

	limit = size >= 10 ? 10 : size + 1;

	printf("  first %ld bytes:", limit);

	for (i = 0; i < limit; i++)
		printf(" %02x", (unsigned char)string[i]);

	printf("\n");
}

/**
 * print_python_list - Prints Python list.
 * @p: PyObject list object.
 */
void print_python_list(PyObject *p)
{
	PyObject *obj;
	PyListObject *list;
	long int size, i;

	printf("[*] Python list info\n");

	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	size = Py_SIZE(p);
	list = (PyListObject *)p;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		obj = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(obj)->tp_name);

		if (PyBytes_Check(obj))
			print_python_bytes(obj);
	}
}
