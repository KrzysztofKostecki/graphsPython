#include "Vertex.h"

namespace graphs {
	std::ostream& operator<< (std::ostream& scr, const Vertex& obj)
	{
		scr << obj.label;
		return scr;
	}
}