#pragma once
#include <iostream>
#include <memory>
#include <vector>
#include <list>
#include "Vertex.h"
#include "Edge.h"
#include "AdjacencyMatrix.h"
#include "IncidenceMatrix.h"
#include <Python.h>
#include <string>


namespace graphs {
	using AdjacencyList = std::vector<std::list<int>>;

	class Graph
	{
	public:
		//Constructors
		Graph(){}
		Graph(const AdjacencyList& adj);
		Graph(const AdjacencyMatrix& adj); 
		Graph(const IncidenceMatrix& inc); 
		explicit Graph(const Graph& graph);

		//Destructor
		~Graph(){}

		//drawing the graph
		void draw();

		//random graph generator
		static std::auto_ptr<Graph> getRandomGraph()
		{
			Py_Initialize();
			std::string t = "import sys\nsys.path.append('..')\nimport generating as gen\ngen.run()";
			PyRun_SimpleString(t.c_str());
			Py_Finalize();
			AdjacencyList tt = Graph::getAdjListFromFile("adjList.txt");
			return std::auto_ptr<Graph>(new Graph(tt));
		}

		//getters
		const AdjacencyList& getAdjacencyList() const{ return *_adjacencyList; }
		const AdjacencyMatrix& getAdjacencyMatrix() const{ return *_adjacencyMatrix; }
		const IncidenceMatrix& getIncidenceMatrix() const{ return *_incidenceMatrix; }
		
		//printers
		void printAdjacencyList() const;
		void printAdjacencyMatrix() const;
		void printIncidenceMatrix() const;
	private:
		
		void adjacencyListToIncidenceMatrix() const;
		void adjacencyMatrixToAdjacencyList() const;
		void incidenceMatrixToAdjacencyMatrix() const;
		void parseList();
		static AdjacencyList Graph::getAdjListFromFile(std::string file);

		std::vector<Vertex*> _verticies;
		std::vector<Edge*> _edges;
		std::auto_ptr<AdjacencyMatrix> _adjacencyMatrix;
		std::auto_ptr<AdjacencyList> _adjacencyList;
		std::auto_ptr<IncidenceMatrix> _incidenceMatrix;
	};
}