/*
  Celem zadania jest zabawa z technika RAII (Resource Acquisition is Initialisation).

  Ponizsze narzedzia riming,scope,  kod zajmuja sie raportowaniem przebiegu dzialania programu.
  W celu ujednolicenia stosowane jest makro "report", ktorego moglo by nie byc. 

  Kompilowac z -Wall -g to pliku exc

  UWAGA: Prosze zauwazyc w kazdym raporcie trzeba zastosowac troche inne podejscie.  
  UWAGA: Czas nalezy odczytac funkcja gettimeofday (ssg taurus potem  man gettimeofday).
 */
#include <iostream>
#include "report.h"
using namespace std;

void call1() {
  report(timing);
  report(scope);
  std::cout << "Wolam call1 i costam robie" << std::endl;
}


void call2( int x, double y) {
  report(scope);
  report(args(x));
  report(args(y));
  std::cout << "Inna funkcja"   << std::endl;
  call1();
}

void call3() {
  report(scope);
  throw std::runtime_error("dla zabawy");
}


int main(int argc, char** argv) {
  report(timing);
  report(scope);
  call2(55, 8.19);
  call2(21, 1.23);
  {
    report(scope);
    call1();
  }
  try {
    call3();
  } catch(...){}
  
}
/* wynik dzialania
./exc  | tee results
Entering main
Entering call2
Passed int arg: 55
Passed double arg: 8.19
Inna funkcja
Entering call1
Wolam call1 i costam robie
Leaving call1
Execution time 8e-06
Leaving call2
Entering call2
Passed int arg: 21
Passed double arg: 1.23
Inna funkcja
Entering call1
Wolam call1 i costam robie
Leaving call1
Execution time 8e-06
Leaving call2
Entering main
Entering call1
Wolam call1 i costam robie
Leaving call1
Execution time 8e-06
Leaving main
Entering call3
Leaving call3
Leaving main
Execution time 0.00019

*/
