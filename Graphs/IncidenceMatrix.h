#pragma once
#include "Matrix.h"
namespace graphs {
	class IncidenceMatrix : public Matrix
	{
	public:
		IncidenceMatrix(unsigned x, unsigned y, int** tab, int *tab1);
		IncidenceMatrix(const IncidenceMatrix& mat);
		~IncidenceMatrix();
	};

}