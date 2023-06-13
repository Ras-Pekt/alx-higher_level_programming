#include <Python.h>
#include <stdio.h>
/**
 * print_python_list_info - prints some basic info about Python lists
 * @p: python list
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	long int idx = 0, size = PyList_Size(p);
	PyObject *item;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	while (idx < size)
	{
		item = PyList_GET_ITEM(p, idx);
		printf("Element %ld: %s\n", idx, Py_TYPE(item)->tp_name);
		idx++;
	}
}
