#include <iostream>
#include "graph.h"
#include <Python.h>
#include "IncidenceMatrix.h"
#include "AdjacencyMatrix.h"

#include <memory>




int main(int argc, char* argv[])
{
	//std::auto_ptr<graphs::Graph> ptr = graphs::Graph::getRandomGraph();

	graphs::AdjacencyMatrix inc = graphs::Graph::getAdjacencyMatrixFromFile();
	graphs::Graph g (inc);
	
	g.printAdjacencyList();
	std::cout<<std::endl;

	g.printIncidenceMatrix();
	std::cout<<std::endl;
	g.printAdjacencyMatrix();
	std::cout<<std::endl;
	
	/*graphs::Graph::TransformToDiGraph(ptr);
	
	std::cout<<std::endl<<"PO PRZEMIANIE"<<std::endl<<std::endl;
	
	std::auto_ptr<graphs::Graph> ptr1 = graphs::Graph::getRandomGraph1();
	
	
	ptr1->printAdjacencyList();
	std::cout << std::endl;
	ptr1->printIncidenceMatrix();
	std::cout<<std::endl;
	ptr1->printAdjacencyMatrix();
	std::cout<<std::endl;*/
	
	std::cin.get();
	return 0;
}