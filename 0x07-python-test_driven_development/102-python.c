#include "Python.h"

/**
 * print_python_string - Show details about Python string objects.
 * @p: A PyObject string object.
 */
void print_python_string(PyObject *p)
{
	long int str_length;

	fflush(stdout);

	printf("[.] string object info\n");

	if (!PyUnicode_Check(p))
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	str_length = ((PyASCIIObject *)(p))->length;

	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");

	printf("  length: %ld\n", str_length);
	printf("  value: %ls\n", PyUnicode_AsWideCharString(p, &str_length));
}
