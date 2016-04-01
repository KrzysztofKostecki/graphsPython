#include "IncidenceMatrix.h"

namespace graphs {
	IncidenceMatrix::IncidenceMatrix(unsigned x, unsigned y, int** tab, int *tab1) : Matrix(x, y, tab1)
	{
		for (unsigned i = 0; i < x; i++)
		{
			_tab[i] = tab1[i];
			for (unsigned j = 0; j < y; j++)
			{
				_matrix[i][j] = tab[i][j];
			}
		}
	}

	IncidenceMatrix::IncidenceMatrix(const IncidenceMatrix& mat) : Matrix(mat._xSize, mat._ySize, mat._tab)
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