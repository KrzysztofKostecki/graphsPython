#pragma once

extern "C" {
class MyClass
{
public:
  MyClass();

  /* use virtual otherwise linker will try to perform static linkage */
  virtual void DoSomething();

private:
  int x;
};
}
