#pragma once
#include <iostream>

namespace graphs{

	class Matrix abstract {
	public:
		Matrix(int x, int y) {
			_xSize = x;
			_ySize = y;
			_matrix = new int*[x];
			for (int i = 0; i < x; i++)
			{
				_matrix[i] = new int[y];
				for (int j = 0; j < y; j++)
				{
					_matrix[i][j] = 0;
				}
			}
		}

		virtual ~Matrix() = 0
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
					if (j == 0)
						std::cout << "| ";
					std::cout << _matrix[i][j] << " ";
				}
				std::cout << " |" << std::endl;
			}
		}

		unsigned getXSize() const { return _xSize; }
		unsigned getYSize() const { return _ySize; }

		int** getMatrix() const { return _matrix; }

	protected:
		unsigned _xSize;
		unsigned _ySize;
		int** _matrix;
	};

}