/*
    @ Baek 1182
    @ Prob. https://www.acmicpc.net/problem/1182
      Ref.
    @ Algo: Backtracking
    @ Start day: 19. 12. 17
    @ End day:

*/


#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;

int answer = 0;
int N;
int result;

void go(vector<int> numVec, int index, int sum) {

	if (N == index) {
		if (sum == result) {
			answer += 1;
		}
		return;
	}

	go(numVec, index + 1, sum + numVec[index]);
	go(numVec, index + 1, sum);
}

int main() {
	cin >> N>> result;
	vector<int> numVec(N);

	for (int i = 0; i < N; i++) {
		cin >> numVec[i];
	}

	go(numVec, 0, 0);
	if (result == 0) answer -= 1;
	cout << answer << endl;

	return 0;
}