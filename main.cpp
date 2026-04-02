#include <iostream>
using namespace std;

int main()
{
	int n1, n2;
	int N, next;

	cout << "Enter two numbers: ";
	cin >> n1 >> n2;
	cout << "Enter the number of sequences: ";
	cin >> N;
	cout << n1 << "\t" << n2 << "\t";

	for (int i =0; i < N-2; i++){
		next = n1 + n2;
		cout << next << "\t";
		n1 = n2;
		n2 = next;
	}
	cout <<endl;
}
