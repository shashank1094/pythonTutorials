# pythonTutorials
The best python tutorials I can make while I learn Python 3.

# Useful Links

Most important tutorials : [Link](https://www.python-course.eu/)

1. [MarkDown Tutorials](https://guides.github.com/features/mastering-markdown/)
2. [UnderScore In Python](https://hackernoon.com/understanding-the-underscore-of-python-309d1a029edc)
3. [An interesting collection of surprising snippets and lesser-known Python features.](https://github.com/satwikkansal/wtfpython)
4. [Packing and Unpacking](https://www.geeksforgeeks.org/packing-and-unpacking-arguments-in-python/) , [Another Link](https://stackoverflow.com/questions/6967632/unpacking-extended-unpacking-and-nested-extended-unpacking)
5. [Importing modules and packages](https://docs.python.org/3/tutorial/modules.html)
6. [Different printing styles...print()](https://docs.python.org/3/tutorial/inputoutput.html)
7. [Decorators](https://www.thecodeship.com/patterns/guide-to-python-function-decorators/) , [Another Link](https://www.python-course.eu/python3_decorators.php)
8. [SetupTools](http://setuptools.readthedocs.io/en/latest/setuptools.html#installing-setuptools)
9. [MRO](https://www.python-course.eu/python3_multiple_inheritance.php),[Ambigous MRO](https://stackoverflow.com/questions/29214888/typeerror-cannot-create-a-consistent-method-resolution-order-mro), [C3 linearization](https://en.wikipedia.org/wiki/C3_linearization)
10. [any() and all()](https://www.geeksforgeeks.org/any-all-in-python/)
11. [Sorting](https://docs.python.org/3.3/howto/sorting.html)
# Building Python From Source LINUX

```
  sudo apt-get install -y build-essential git libexpat1-dev libssl-dev zlib1g-dev \
  libncurses5-dev libbz2-dev liblzma-dev \
  libsqlite3-dev libffi-dev tcl-dev linux-headers-$(uname -r) libgdbm-dev \
  libreadline-dev tk tk-dev

  Download and Extract File 
  
  cd cpython && ./configure --prefix=/usr \
  --enable-loadable-sqlite-extensions \
  --enable-shared \
  --with-lto \
  --enable-optimizations \
  --with-system-expat \
  --with-system-ffi \
  --enable-ipv6 --with-threads --with-pydebug --disable-rpath \
  && make \
  && sudo make install
  ```