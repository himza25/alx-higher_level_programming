#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>

void print_python_bytes(PyObject *p)
{
	long int taille;  // changed from size
	int indice;  // changed from i
	char *chaine_essai = NULL;  // changed from trying_str

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	PyBytes_AsStringAndSize(p, &chaine_essai, &taille);

	printf("  taille: %li\n", taille);
	printf("  chaine d'essai: %s\n", chaine_essai);
	if (taille < 10)
		printf("  premiers %li octets:", taille + 1);
	else
		printf("  premiers 10 octets:");
	for (indice = 0; indice <= taille && indice < 10; indice++)
		printf(" %02hhx", chaine_essai[indice]);
	printf("\n");
}

void print_python_list(PyObject *p)
{
        long int taille = PyList_Size(p);
        int indice;
        PyListObject *liste = (PyListObject *)p;
        const char *type;

        printf("[*] Python list info\n");
        printf("[*] Taille de la liste Python = %li\n", taille);
        printf("[*] Alloué = %li\n", liste->allocated);
        for (indice = 0; indice < taille; indice++)
        {
                type = (liste->ob_item[indice])->ob_type->tp_name;
		printf("Element %i: %s\n", indice, type);
                if (!strcmp(type, "bytes"))
                        print_python_bytes(liste->ob_item[indice]);
        }
}
