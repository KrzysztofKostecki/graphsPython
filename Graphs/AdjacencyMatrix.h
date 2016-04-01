#pragma once
#include "Matrix.h"

namespace graphs {
	class AdjacencyMatrix : public Matrix
	{
	public:
		AdjacencyMatrix(const AdjacencyMatrix& mat);
		AdjacencyMatrix(unsigned x, unsigned y, int** tab, int *tab1);
		~AdjacencyMatrix();
	};

}