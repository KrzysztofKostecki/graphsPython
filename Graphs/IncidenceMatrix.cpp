#include "IncidenceMatrix.h"

namespace graphs {
	IncidenceMatrix::IncidenceMatrix(unsigned x, unsigned y, int** tab) : Matrix(x, y)
	{
		for (unsigned i = 0; i < x; i++)
		{
			for (unsigned j = 0; j < y; j++)
			{
				_matrix[i][j] = tab[i][j];
			}
			delete[] tab[i];
		}
		delete[] tab;
	}

	IncidenceMatrix::IncidenceMatrix(const IncidenceMatrix& mat) : Matrix(mat._xSize, mat._ySize)
	{

		for (unsigned i = 0; i < mat._xSize; i++)
		{
			for (unsigned y = 0; y < mat._ySize; y++)
			{
				_matrix[i][y] = mat._matrix[i][y];
			}
		}
	}


	IncidenceMatrix::~IncidenceMatrix()
	{
	}

}