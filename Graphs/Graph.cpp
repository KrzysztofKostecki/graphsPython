#include "Graph.h"
#include <Python.h>
#include <string>
#include <fstream>
#include <algorithm>


namespace graphs {
	Graph::Graph(const AdjacencyList& adj) : _adjacencyList(new AdjacencyList(adj))
	{
		adjacencyListToIncidenceMatrix();
		incidenceMatrixToAdjacencyMatrix();
		parseList();
	}

	Graph::Graph(const AdjacencyMatrix& adj) : _adjacencyMatrix(new AdjacencyMatrix(adj))
	{
		adjacencyMatrixToAdjacencyList();
		adjacencyListToIncidenceMatrix();
		parseList();
	}


	Graph::Graph(const IncidenceMatrix& inc) : _incidenceMatrix(new IncidenceMatrix(inc))
	{
		incidenceMatrixToAdjacencyMatrix();
		adjacencyMatrixToAdjacencyList();
		parseList();
	}


	Graph::Graph(const Graph& graph) :
		_adjacencyList(new AdjacencyList(*graph._adjacencyList)),
		_adjacencyMatrix(new AdjacencyMatrix(*graph._adjacencyMatrix)),
		_incidenceMatrix(new IncidenceMatrix(*graph._incidenceMatrix))
	{
	}

	void Graph::adjacencyListToIncidenceMatrix() const
	{
		
	}

	void Graph::adjacencyMatrixToAdjacencyList() const
	{

	}

	void Graph::incidenceMatrixToAdjacencyMatrix() const
	{

	}

	void Graph::parseList()
	{
		for (unsigned i = 0; i < (*_adjacencyList).size(); i++)
		{
			_verticies.push_back(new Vertex(i));
		}

		
		for (unsigned i = 0; i < (*_adjacencyList).size(); i++)
		{
			for (std::list<int>::iterator j = (*_adjacencyList)[i].begin(); j != (*_adjacencyList)[i].end(); j++)
			{
				if (*j > (int)i)
				{
					_edges.push_back(new Edge(Vertex(i), Vertex(*j)));
				}
			}
		}
	}


	AdjacencyList Graph::getAdjListFromFile(std::string file)
	{
		std::ifstream istr(file);
		std::string str;
		unsigned i = 0;
		AdjacencyList t;

		while (std::getline(istr, str))
		{
			std::list<int> a;
			t.push_back(a);

			if (str[1] == ']')
			{
				i++;
				continue;
			}

			if (str[2] == ']')
			{
				std::string tmp = str.substr(1, 1);
				t[i++].push_back(std::atoi(tmp.c_str()));
				continue;
			}

			if (str[3] == ']')
			{
				std::string tmp = str.substr(1, 2);
				t[i++].push_back(std::atoi(tmp.c_str()));
				continue;
			}

			while (str.find(',') < str.length()-1 && str.find(',') != 0)
			{	
				
				int npos = str.find(',');
				std::string liczba = str.substr(1, npos-1);
				t[i].push_back(std::atoi(liczba.c_str()));
				str.erase(0, npos+1);
			}

			std::string s = str.substr(1, str.find(']'));
			t[i++].push_back(std::atoi(s.c_str()));
		}
		return t;
	}


	void Graph::printAdjacencyList() const
	{
		int z = 0;
		for (auto i : *_adjacencyList)
		{
			std::cout << z++ << ": ";
			for (auto j : i)
			{
				std::cout << j << " ";
			}
			std::cout << std::endl;
		}
	}

	void Graph::printAdjacencyMatrix() const
	{
		_adjacencyMatrix->print();
	}

	void Graph::printIncidenceMatrix() const
	{
		_incidenceMatrix->print();
	}
}