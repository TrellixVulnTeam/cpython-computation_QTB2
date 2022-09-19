#include <iostream>
#include <bitset>
int main( ) 
{ 
	using namespace std;

	const int max = 8;
	
	short val = 4;
	unsigned char left = val & 0xff;          // leftmost (least significant) byte
	cout << bitset<max>(left) << endl;

	unsigned char right = (val >> 8) & 0xff;  // rightmost (most significant) byte
	cout << bitset<max>(right) << endl;

	val = 256;
	right = (val >> 8) & 0xff;
	cout << bitset<max>(right) << endl;

	val = 2*val;
	right = (val >> 8) & 0xff;
	cout << bitset<max>(right) << endl;

	val = -8;
	bool sign_bit = val & 0x8000;             // sign bit
	cout << sign_bit << endl;
}