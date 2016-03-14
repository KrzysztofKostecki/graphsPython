#include "AdjacencyMatrix.h"

namespace graphs {
	AdjacencyMatrix::AdjacencyMatrix(const AdjacencyMatrix& mat) : Matrix(mat._xSize, mat._ySize)
	{
		for (unsigned i = 0; i < mat._xSize; i++)
		{
			for (unsigned y = 0; i < mat._ySize; y++)
			{
				_matrix[i][y] = mat._matrix[i][y];
			}
		}
	}

	AdjacencyMatrix::AdjacencyMatrix(unsigned x, unsigned y, int** tab) : Matrix(x, y)
	{
		for (unsigned i = 0; i < x; i++)
		{
			for (unsigned j = 0; j < y; j++)
			{
				_matrix[i][j] = tab[i][j];
			}
		}
	}


	AdjacencyMatrix::~AdjacencyMatrix()
	{
	}
}