#include <iostream>

class foo {
public:
	const double x;
	const double y;
	const double z;

	foo() : x(1.5), y(2.6), z(3.7) {

	}
};

int main(int argc, char* argv[]) {
	foo* f = new foo();
	std::cout << f->x << std::endl;

	return 0;
}