#pragma once
#include <iostream>
namespace graphs {
	class Vertex
	{
	public:
		Vertex(int s) : label(s) {}
		~Vertex(){}
		friend std::ostream& operator<< (std::ostream& scr, const Vertex& obj);
		const int getLabel(){ return label; }
	private:
		const int label;
	};

}