// tidy_numbers.cpp : definisce il punto di ingresso dell'applicazione console.
//

#include <iostream>
#include <string>
using namespace std;

int main() {
	int t;
	string n;
	bool change;
	cin >> t;
	for (int i = 1; i <= t; ++i) {
		cin >> n;

		do {
			change = false;

			for (int j = 0; j < n.length()-1 && !change; ++j)
				if (n[j] > n[j + 1]) {

					n[j]--;
					for (int k = 1; k < n.length()-j; ++k)
						n[j+k] = '9';

					change = true;
				}

			if (n[0] == '0' && change) {
				// remove initial zero
				n.erase(n.begin());
			}
		} while (change);


		cout << "Case #" << i << ": " << n << endl;
	}

	return EXIT_SUCCESS;
}
