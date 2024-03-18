#include <Python.h>

void print_python_list_info(PyObject *p) {
	int size, i;
	PyObject *item;

	if (!PyList_Check(p)) {
		fprintf(stderr, "Invalid argument: not a Python list\n");
		return;
	}

	size = PyList_Size(p);

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++) {
		item = PyList_GetItem(p, i);
		printf("Element %d: %s\n", i, Py_TYPE(item)->tp_name);
	}
}

