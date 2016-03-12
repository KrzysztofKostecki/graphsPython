#include <iostream>
#include "graph.h"
#include <Python.h>
#include "IncidenceMatrix.h"
#include <memory>




int main(int argc, char* argv[])
{
	std::auto_ptr<graphs::Graph> ptr = graphs::Graph::getRandomGraph();
	ptr->printAdjacencyList();
	//ptr->printAdjacencyMatrix();
	//ptr->printIncidenceMatrix();
	std::cin.get();
	return 0;
}