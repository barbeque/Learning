#include <sstream>
#include <iostream>

// Demos how to use stl stringstream to produce stl strings.
int main(int argc, char* argv[]) {
	std::stringstream s;
	s << "Hello world: " << 123 << " Blah blah blah " << 456.491;
	std::string result = s.str();
	std::cout << result << std::endl;
	return 0;
}