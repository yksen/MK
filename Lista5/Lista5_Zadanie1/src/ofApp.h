#pragma once

#include "ofMain.h"

#define W 800
#define H 600

class ofApp : public ofBaseApp
{

public:
	void setup();
	void update();
	void draw();

	ofBufferObject A1, A2;

	ofTexture texture;
	ofShader shader;

	int tick = 0;

	float A1cpu[W * H];
	float A2cpu[W * H];
};
