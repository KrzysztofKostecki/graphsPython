#include <iostream>
#include "graph.h"
#include <Python.h>
#include "IncidenceMatrix.h"
#include <memory>




int main(int argc, char* argv[])
{
	std::auto_ptr<graphs::Graph> ptr = graphs::Graph::getRandomGraph();
	ptr->printAdjacencyList();
	std::cout << std::endl;
	ptr->printAdjacencyMatrix();
	std::cout << std::endl;
	ptr->printIncidenceMatrix();
	std::cin.get();
	return 0;
}