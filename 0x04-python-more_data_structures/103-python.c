#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>

void print_python_bytes(PyObject *p)
{
    long int length;
    int index;
    char *attempt_str = NULL;

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    PyBytes_AsStringAndSize(p, &attempt_str, &length);

    printf("  size: %li\n", length);
    printf("  attempting string: %s\n", attempt_str);
    if (length < 10)
        printf("  first %li bytes:", length + 1);
    else
        printf("  first 10 bytes:");
    for (index = 0; index <= length && index < 10; index++)
        printf(" %02hhx", attempt_str[index]);
    printf("\n");
}

void print_python_list(PyObject *p)
{
        long int length = PyList_Size(p);
        int index;
        PyListObject *list = (PyListObject *)p;
        const char *data_type;

        printf("[*] Python list info\n");
        printf("[*] Size of the Python List = %li\n", length);
        printf("[*] Allocated = %li\n", list->allocated);
        for (index = 0; index < length; index++)
        {
                data_type = (list->ob_item[index])->ob_type->tp_name;
		        printf("Element %i: %s\n", index, data_type);
                if (!strcmp(data_type, "bytes"))
                        print_python_bytes(list->ob_item[index]);
        }
}
