#include<cstdio>
#include<iostream>
#include <algorithm>
#include <queue>
#include <vector>

using namespace std;


int ch[30];
int dis[30];

int main() {

	int n, m, a, b, x;
	vector<int> map[30];
	queue<int> Q;
	scanf("%d %d", &n, &m);

	for (int i = 1; i <= m; i++) {
		scanf("%d %d", &a, &b);
		map[a].push_back(b);
	}

	Q.push(1);
	ch[1] = 1;

	while (!Q.empty()) {
		x = Q.front();
		Q.pop();

		for (int i = 1; i < map[x].size(); i++) {
			if (ch[map[x][i]] == 0) {
				ch[map[x][i]] = 1;
				Q.push(map[x][i]);				// 큐에 값을 집어 넣음
				dis[map[x][i]] = dis[x] + 1;  // 거리 증가
			}
		}
	}

	for (int i = 2; i <= n; i++) {
		printf("%d : %d\n", i, dis[i]);
	}

	return 0;
}
