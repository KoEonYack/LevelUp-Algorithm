
#include<cstdio>
#include<iostream>
#include <algorithm>

using namespace std;
int MAP[250][250];
bool check[250][250];
int X, Y;
int ans;

const int dx[] = { -1, -1, -1, 0, 0, 1, 1, 1 };
const int dy[] = { -1, 0, 1, -1, 1, -1, 0, 1 };

void dfs(int x, int y) {
	check[x][y] = true;

	for (int i = 0; i < 8; i++) {
		int nx = x + dx[i], ny = y + dy[i];

		if (nx < 0 || nx >= X || ny < 0 || ny >= Y) {
			continue;
		}

		if (!check[nx][ny] && MAP[nx][ny]) dfs(nx, ny);

	}
}

int main() {

	scanf("%d %d", &X, &Y);

	for (int i = 0; i < X; i++){
		for (int j = 0; j < Y; j++) {
			scanf("%d", &MAP[i][j]);
		}
	}

	for (int i = 0; i < Y; i++) {
		for (int j = 0; j < X; j++) {
			if (!check[i][j] && MAP[i][j] == 1) {
				dfs(i, j);
				ans += 1;
			}
		}
	}

	printf("%d", ans);
	return 0;
}


