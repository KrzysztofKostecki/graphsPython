#include "Edge.h"

namespace graphs {
	std::ostream& operator << (std::ostream& scr, const graphs::Edge& obj)
	{
		scr << obj.a << "<->" << obj.b << std::endl;
		return scr;
	}
}