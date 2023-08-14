#include <Python.h>
#include <stdio.h>

void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, i;
	PyObject *item;

	size = PyList_Size(p);
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
	for (i = 0; i < size; i++)
	{
		item = PyListObject *)p)->allocated);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
int main(void)
{
	return 0;
}