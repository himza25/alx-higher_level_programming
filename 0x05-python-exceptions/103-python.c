#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - Prints basic info about Python lists
 * @p: PyObject list pointer
 */
void print_python_list(PyObject *p)
{
	long int size, i;
	PyObject *item;

	printf("[*] Python list info\n");
	if (!PyList_Check(p))
	{
	printf("  [ERROR] Invalid List Object\n");
	return;
	}

	size = PyList_GET_SIZE(p);
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
	item = PyList_GetItem(p, i);
	printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	if (PyBytes_Check(item))
	print_python_bytes(item);
	else if (PyFloat_Check(item))
	print_python_float(item);
	}
}

/**
 * print_python_bytes - Prints basic info about Python bytes
 * @p: PyObject bytes pointer
 */
void print_python_bytes(PyObject *p)
{
	long int size, i;
	char *str;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
	printf("  [ERROR] Invalid Bytes Object\n");
	return;
	}

	size = PyBytes_GET_SIZE(p);
	str = PyBytes_AsString(p);
	printf("  size: %ld\n  trying string: %s\n  first 10 bytes:", size, str);

	for (i = 0; i < size && i < 10; i++)
	{
	printf(" %02hhx", str[i]);
	}
	printf("\n");
}

/**
 * print_python_float - Prints basic info about Python floats
 * @p: PyObject float pointer
 */
void print_python_float(PyObject *p)
{
	double value;

	printf("[.] float object info\n");
	if (!PyFloat_Check(p))
	{
	printf("  [ERROR] Invalid Float Object\n");
	return;
	}

	value = PyFloat_AsDouble(p);
	printf("  value: %0.16g\n", value);
}
