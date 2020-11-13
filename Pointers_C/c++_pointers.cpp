#include<iostream>
using namespace std;
int p = 1;
int main(){
	cout<<p;
	p = 4;
	cout<<p;
	int x=5;
	int *y = &x;
	cout<<x<<"\n";
	cout<<&x<<"\n";
	cout<<y<<"\n";
	cout<<*y<<"\n";
	cout<<&y<<"\n";
	return 1;
}
