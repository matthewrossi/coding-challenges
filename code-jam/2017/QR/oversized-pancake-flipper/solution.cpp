// oversized_pancake_flipper.cpp : definisce il punto di ingresso dell'applicazione console.
//

#include <iostream>
#include <string>
using namespace std;

string flipK(string s, int pos, int k) {
	string flipped = "";

	for (int i = 0; i < pos; i++) {
		if (s[i] == '+') {
			flipped.append("+");
		}
		else {
			flipped.append("-");
		}
	}
	for (int i = 0; i < k; i++) {
		if (s[pos + i] == '+') {
			flipped.append("-");
		}
		else {
			flipped.append("+");
		}
	}
	for (int i = pos + k; i < s.length(); i++) {
		if (s[i] == '+') {
			flipped.append("+");
		}
		else {
			flipped.append("-");
		}
	}

	return flipped;
}

int main() {
	int t, k, moves;
	string s;
	bool impossible;
	cin >> t;
	for (int i = 1; i <= t; ++i) {
		cin >> s >> k;
		impossible = false;
		moves = 0;

		for (int j = 0; j < s.length() && !impossible; j++)
			if (s[j] == '-') {
				int neg_seq = 0;
				while (s[j + neg_seq] == '-')
					neg_seq++;
				if (neg_seq >= k) {
					s = flipK(s, j, k);
					moves++;
				}
				else {
					// try to get a sequence of k '-' with further flip
					if (j + neg_seq + k - 1 < s.length()) {
						s = flipK(s, j + neg_seq, k);
						moves++;
						j--;
					}
					else {
						cout << "Case #" << i << ": IMPOSSIBLE" << endl;
						impossible = true;
					}
				}
			}

		if (!impossible) {
			cout << "Case #" << i << ": " << moves << endl;
		}
		
	}
	return EXIT_SUCCESS;
}
