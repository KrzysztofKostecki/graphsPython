#pragma once
#include <iostream>

namespace graphs{

	class Matrix {
	public:
		Matrix(int x, int y, int *tab1) {
			_xSize = x;
			_ySize = y;
			_matrix = new int*[x];
			_tab = new int[x];
			for (int i = 0; i < x; i++)
			{
				_matrix[i] = new int[y];
				_tab[i] = 0;
				for (int j = 0; j < y; j++)
				{
					_matrix[i][j] = 0;
				}
			}
		}

		virtual ~Matrix()
		{
			for (unsigned i = 0; i < _xSize; i++)
			{
				delete _matrix[i];
			}
			delete _matrix;
		}

		virtual void print(){
			for (unsigned i = 0; i < _xSize; i++) {
				for (unsigned j = 0; j < _ySize; j++) {
					if (j == 0 && i <= 9)
					{
						std::cout << i << " | ";
					}
					else if (j == 0 && i >= 10)
					{
						std::cout << i << "| ";
					}
					std::cout << _matrix[i][j] << " ";
				}
				std::cout << " |" << std::endl;
			}
		}

		int** getMatrix() const { return _matrix; }
		unsigned getXSize() const { return _xSize; }
		unsigned getYSize() const { return _ySize; }
		int* getTab() const { return _tab; }

	protected:
		unsigned _xSize;
		unsigned _ySize;
		int *_tab;
		int** _matrix;
	};

}