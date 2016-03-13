#pragma once
#include <iostream>
#include "Vertex.h"

namespace graphs {
	class Edge
	{
	public:
		Edge(const Vertex& v1, const Vertex& v2) : a(v1), b(v2){}
		~Edge(){}
		friend std::ostream& operator<< (std::ostream& scr, const graphs::Edge& obj);
	private:
		double _cost;
		Vertex a, b;
	};
}


