/*
    71. 송아지 찾기

    Input 5 14
    Output 3

    @ Start day: 19. 11. 30
    @ End day: 19. 11. 30
*/


////////////////////////////////////////////////////////////
#pragma warning(disable : 4996)
#pragma warning(disable : 4700)
#pragma warning(disable : 6031)
////////////////////////////////////////////////////////////

#include <cstdio>
#include <iostream>
#include <algorithm>
#include <queue>
#include <vector>

using namespace std;

int check[10001];
int d[3] = { 1, -1, 5 };

int main() {
	int start, end, x, pos;
	queue<int> Q;

	scanf("%d %d", &start, &end);
	check[start] = 1;
	Q.push(start);

	while (!Q.empty()) {
		x = Q.front();
		Q.pop();

		for (int i = 0; i < 3; i++) {
			pos = x + d[i];
			if (pos < 1 && pos>10000) continue; // 음수 인덱스 접근이 발생할 수 있기 때문
			if (pos == end) {
				printf("%d\n", check[x]);
				exit(0);
			}
			if (check[pos] == 0) {
				check[pos] = check[x] + 1;
				Q.push(pos);
			}
		}

	}

	// 몇 번 만에 가는지

	return 0;
}


