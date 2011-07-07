#include <cmath>
#include <vector>
#include <cassert>

#define PI 3.141592654f

class Vector {
public:
	float x, y, z;
public:
	Vector() {
		this->x = this->y = this->z = 0.0f;
	}
	Vector(float x, float y, float z) {
		this->x = x;
		this->y = y;
		this->z = z;
	}
	void normalize() {
		float length = this->length();
		this->x /= length;
		this->y /= length;
		this->z /= length;
	}
	Vector getNormalized() const {
		Vector output = Vector(this->x, this->y, this->z);
		output.normalize();
		return output;
	}
	float length() const {
		return sqrtf((x * x) + (y * y) + (z * z));
	}
	Vector cross(const Vector& other) const {
		float cx = (y * other.z) - (z * other.y);
		float cy = (z * other.x) - (x * other.z);
		float cz = (x * other.y) - (y * other.x);
		return Vector(cx, cy, cz);
	}
	Vector operator*(float scalar) const {
		return Vector(x * scalar, y * scalar, z * scalar);
	}
	Vector operator+(Vector other) const {
		return Vector(x + other.x, y + other.y, z + other.z);
	}
	Vector operator-(Vector other) const {
		return Vector(x - other.x, y - other.y, z - other.z);
	}
};

class Ray {
public:
	Vector origin;
	Vector direction;
public:
	Ray(Vector origin, Vector direction) {
		this->origin = origin;
		this->direction = direction;
	}
};

class Camera {
public:
	Vector position;
	Vector lookAt;
	Vector up;
public:
	Camera(Vector position, Vector lookAt, Vector up) {
		this->position = position;
		this->lookAt = lookAt;
		this->up = up;
	}
};

std::vector< std::vector<Ray> > getRaysForScreen(unsigned int width, unsigned int height, const Camera& camera) {
	Vector n = (camera.position - camera.lookAt).getNormalized();
	Vector u = camera.up.cross(n).getNormalized();
	Vector v = n.cross(u).getNormalized();
	
	Vector viewPortCentre = camera.position - n;
	
	float hfov = PI / 3.5f;
	float vfov = (hfov * (float)height / (float)width);
	float pixelWidth = 2.0f * tanf(hfov * 0.5) / width;
	float pixelHeight = 2.0f * tanf(vfov * 0.5) / height;
	
	std::vector< std::vector<Ray> > output;
	
	for(unsigned int y = 0; y < height; y++) {
		std::vector<Ray> thisLine;
		
		for(unsigned int x = 0; x < width; x++) {
			Vector rayPoint = viewPortCentre + (u * (width * 0.5f) * pixelWidth) + (v * (y - (height * 0.5f) * pixelHeight));
			Vector rayDirection = (rayPoint - camera.position).getNormalized();
			
			thisLine.push_back(Ray(rayPoint, rayDirection));
		}
		
		output.push_back(thisLine);
	}
	
	return output;
}

int main(int argc, char* argv[]) {
	unsigned int width = 640;
	unsigned int height = 480;
	Camera c = Camera(Vector(0, 0, 0), Vector(1, 1, 1), Vector(0, 1, 0));
	
	std::vector< std::vector<Ray> > rays = getRaysForScreen(width, height, c);
	assert(rays.size() == height);
	for(unsigned int y = 0; y < rays.size(); y++) {
		assert(rays[y].size() == width);
	}
}