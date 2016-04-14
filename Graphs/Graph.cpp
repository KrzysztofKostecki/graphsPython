#include "Graph.h"
#include <Python.h>
#include <string>
#include <fstream>
#include <algorithm>
#include <vector>


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
		int** tab = new int*[(*_incidenceMatrix).getYSize()];
		for (unsigned i = 0; i < (*_incidenceMatrix).getYSize(); i++) {
			tab[i] = new int[(*_incidenceMatrix).getYSize()];
			for (unsigned j = 0; j < (*_incidenceMatrix).getYSize(); j++) {
				tab[i][j] = 0;
			}
		}
		std::cout << std::endl;
		std::vector<int> vec;
		for (unsigned i = 0; i < (*_incidenceMatrix).getXSize(); i++) {
			for (unsigned j = 0; j < (*_incidenceMatrix).getYSize(); j++) {
				if ((*_incidenceMatrix).getMatrix()[i][j] == 1) {
					vec.push_back(j);
				}
			}
			for (auto k = vec.begin(); k < vec.end(); k++) {
				for (auto z = k + 1; z < vec.end(); z++) {
					tab[*k][*z] = 1;
					tab[*z][*k] = 1;
				}
			}
			vec.clear();
		}

		_adjacencyMatrix = std::auto_ptr<AdjacencyMatrix>(new AdjacencyMatrix((unsigned)(*_incidenceMatrix).getYSize(), (unsigned)(*_incidenceMatrix).getYSize(), tab));
		
	}

	void Graph::adjacencyMatrixToAdjacencyList()
	{
		AdjacencyList tmp;

		for (unsigned j = 0; j < (*_adjacencyMatrix).getXSize(); j++)
		{
			std::list<int> a;
			tmp.push_back(a);
			for (unsigned k = 0; k < (*_adjacencyMatrix).getXSize(); k++)
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

	void Graph::write()
	{
		std::ofstream ostr("files/adjList.txt");
		for (auto i : *_adjacencyList)
		{
			ostr << "[";
			unsigned j = 0;
			for (auto k = i.begin(); j != i.size() - 1; k++, j++)
			{
				ostr << *k << ", ";
			}
			ostr << i.back();
			ostr << "]\n";
		}
	}

	void Graph::draw()
	{
		write();
		Py_Initialize();
		std::string t = "import sys\nsys.path.append('..')\nimport draw as d\nd.draw()";
		PyRun_SimpleString(t.c_str());
		Py_Finalize();

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