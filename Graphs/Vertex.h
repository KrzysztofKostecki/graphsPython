#pragma once
#include <iostream>
namespace graphs {
	class Vertex
	{
	public:
		Vertex(int s) : label(s) {}
		~Vertex(){}
		friend std::ostream& operator<< (std::ostream& scr, const Vertex& obj);
	private:
		const int label;
	};

}