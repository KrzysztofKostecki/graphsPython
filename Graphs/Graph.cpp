#include "Graph.h"
#include <Python.h>
#include <string>
#include <fstream>
#include <algorithm>


namespace graphs {
	Graph::Graph(const AdjacencyList& adj) : _adjacencyList(new AdjacencyList(adj))
	{
		parseList();
		adjacencyListToIncidenceMatrix();
		incidenceMatrixToAdjacencyMatrix();
	}

	Graph::Graph(const AdjacencyMatrix& adj) : _adjacencyMatrix(new AdjacencyMatrix(adj))
	{
		adjacencyMatrixToAdjacencyList();
		parseList();
		adjacencyListToIncidenceMatrix();
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


	void Graph::adjacencyListToIncidenceMatrix()
	{
		int * b = new int[_edges.size()];
		for (unsigned j = 0; j < _edges.size(); j++)
		{
			b[j] = 0;
		}
		int** a = new int*[_edges.size()];
		for (unsigned j = 0; j < _edges.size(); j++)
		{
			a[j] = new int[_verticies.size()];
			for (unsigned k = 0; k < _verticies.size(); k++)
			{
				a[j][k] = 0;
			}
		}
		int j = 0;
		for (auto i : _edges)
		{
			a[j][((i->getVertexA()).getLabel())] = 1;
			b[j] = ((i->getVertexA()).getLabel());
			a[j][(i->getVertexB()).getLabel()] = 1;
			j++;
		}
		_incidenceMatrix = std::auto_ptr<IncidenceMatrix>(new IncidenceMatrix((unsigned)_edges.size(), (unsigned)_verticies.size(), a));
	}



	void Graph::incidenceMatrixToAdjacencyMatrix()
	{
		unsigned size = (*_adjacencyList).size();
		int** tab = new int*[size];
		for (unsigned i = 0; i < size; i++) {
			tab[i] = new int[size];

			for (unsigned j = 0; j < size; j++) {
				tab[i][j] = 0;
			}
			
		}
		for (unsigned i = 0; i < size; i++) {
			for (auto j = ((*_adjacencyList)[i]).begin(); j != ((*_adjacencyList)[i]).end(); j++) {
				try {
					tab[i][*j] = 1;
				}
				catch (...) {
					std::cout << "exc" << std::endl;
				}
			}
		}
		
		_adjacencyMatrix = std::auto_ptr<AdjacencyMatrix>(new AdjacencyMatrix((unsigned)_verticies.size(), (unsigned)_verticies.size(), tab));
	}

	void Graph::adjacencyMatrixToAdjacencyList()
	{
		AdjacencyList tmp;

		for (unsigned j = 0; j < _verticies.size(); j++)
		{
			std::list<int> a;
			tmp.push_back(a);
			for (unsigned k = 0; k < _verticies.size(); k++)
			{
				if (getAdjacencyMatrix().getMatrix()[j][k] == 1)
					tmp[j].push_back(k);
			}
		}
		_adjacencyList = std::auto_ptr<AdjacencyList>(new AdjacencyList(tmp));
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
		if (istr.fail()){
			std::cout << "Nie udalo sie otworzyc pliku" << std::endl;
			std::exit(-1);
		}
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

			while (str.find(',') < str.length() - 1 && str.find(',') != 0)
			{
				int npos = (int)str.find(',');
				std::string liczba = str.substr(1, npos - 1);
				t[i].push_back(std::atoi(liczba.c_str()));
				str.erase(0, npos + 1);
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