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
#include <fstream>


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

		//write to adjList.txt
		void write();

		//random graph generator
		static std::auto_ptr<Graph> getRandomGraph()
		{
			Py_Initialize();
			std::string t = "import sys\nsys.path.append('..')\nimport generating as gen\ngen.run()";
			PyRun_SimpleString(t.c_str());

			AdjacencyList tt = Graph::getAdjListFromFile("files/adjList.txt");
			
			return std::auto_ptr<Graph>(new Graph(tt));
		}

		static void TransformToDiGraph(const std::auto_ptr<graphs::Graph>& tmp)
		{

			std::string t = "import sys\nsys.path.append('..')\nimport generating1 as gen\ngen.run()";
			PyRun_SimpleString(t.c_str());
			Py_Finalize();
		}

		static std::auto_ptr<Graph> getRandomGraph1()
		{
			/*Py_Initialize();
			std::string t = "import sys\nsys.path.append('.')\nimport generating as gen\ngen.run()";
			PyRun_SimpleString(t.c_str());
			Py_Finalize();*/
			AdjacencyList tt = Graph::getAdjListFromFile("files/adjList.txt");

			return std::auto_ptr<Graph>(new Graph(tt));
		}

		//getters
		const AdjacencyList& getAdjacencyList() const{ return *_adjacencyList; }
		const AdjacencyMatrix& getAdjacencyMatrix() const{ return *_adjacencyMatrix; }
		const IncidenceMatrix& getIncidenceMatrix() const{ return *_incidenceMatrix; }
		
		static IncidenceMatrix getIncidenceMatrixFromFile(){
			
			std::ifstream istr("files/incMat.txt");
			if (istr.fail()){
				std::cout << "Nie udalo sie otworzyc pliku" << std::endl;
				std::exit(-1);
			}

			std::string str;
			std::vector <std::string> strvec;
			while (std::getline(istr, str))
			{
				strvec.push_back(str);
			}
			int x = strvec.size();
			int y = strvec[0].length() / 2 + 1;

			int ** tab = new int*[x];
			for (int i = 0; i < x; i++) {
				tab[i] = new int[y];
				for (int j = 0; j < y; j++) {
					tab[i][j] = 0;
				}

			}
			int xx = 0;
			int yy = 0;
			for (auto i : strvec) {
				for (auto j : i) {
					if (j == '0') {
						tab[xx][yy++] = 0;
					}
					if (j == '1') {
						tab[xx][yy++] = 1;
					}
				}
				xx++;
				yy = 0;
			}
			return IncidenceMatrix(x, y, tab);
		}

		static AdjacencyList Graph::getAdjListFromFile(std::string file = "files/adjList.txt");
		
		static AdjacencyMatrix getAdjacencyMatrixFromFile(){

			std::ifstream istr("files/adjMat.txt");
			if (istr.fail()){
				std::cout << "Nie udalo sie otworzyc pliku" << std::endl;
				std::exit(-1);
			}

			std::string str;
			std::vector <std::string> strvec;
			while (std::getline(istr, str))
			{
				strvec.push_back(str);
			}
			int x = strvec.size();
			int y = x;

			int ** tab = new int*[x];
			for (int i = 0; i < x; i++) {
				tab[i] = new int[y];
				for (int j = 0; j < y; j++) {
					tab[i][j] = 0;
				}

			}
			int xx = 0;
			int yy = 0;
			for (auto i : strvec) {
				for (auto j : i) {
					if (j == '0') {
						tab[xx][yy++] = 0;
					}
					if (j == '1') {
						tab[xx][yy++] = 1;
					}
				}
				xx++;
				yy = 0;
			}
			return AdjacencyMatrix(x, y, tab);
		}

		//printers
		void printAdjacencyList() const;
		void printAdjacencyMatrix() const;
		void printIncidenceMatrix() const;
	private:
		
		void adjacencyListToIncidenceMatrix();
		void adjacencyMatrixToAdjacencyList();
		void incidenceMatrixToAdjacencyMatrix();
		void parseList();
		

		std::vector<Vertex*> _verticies;
		std::vector<Edge*> _edges;
		std::auto_ptr<AdjacencyMatrix> _adjacencyMatrix;
		std::auto_ptr<AdjacencyList> _adjacencyList;
		std::auto_ptr<IncidenceMatrix> _incidenceMatrix;
	};
}