/*
	89. 토마토
	Idea. BFS(pair 사용)

Input.
6 4
1 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1

>>8

@ 유사문제:
	@ Ref.
	@ Start day:  19. 12. 01.
	@ End day:   19. 12. 01.
*/

#include <cstdio>
#include <iostream>
#include <algorithm>
#include <queue>
#include <vector>

using namespace std;

int map[1000][1000];
int check[1000][1000];
int dx[4] = { 1, -1, 0, 0 };
int dy[4] = { 0, 0, 1, -1};
int X, Y;

bool isInside(int x, int y) {
	return (x >= 0 && x < X) && (y >= 0 && y < Y);
}

// 한 번 방문한 곳을 -1로 설명하면 된다.
int main() {

	int cur_y = -1;
	int cur_x = -1;

	scanf("%d %d", &X, &Y);

	for (int i = 0; i < Y; i++) {
		for (int j = 0; j < X; j++){
			scanf("%d", &map[i][j]);
			if (map[i][j] == 1) {
				cur_y = i;
				cur_x = j;
			}
		}
	}

	queue<pair<int, int>> q;
	q.push(pair<int, int>(cur_y, cur_x));
	if (cur_x == -1 && cur_y == -1) { // 익은 토마토가 존재하지 않는 상황
		printf("-1");
		return 0;
	}


	/*
	for (int i = 0; i < Y; i++) {
		for (int j = 0; j < X; j++) {
			if (map[cur_y][cur_x] == 1) {
				map[cur_y][cur_x] = -1; // 썩은 토마토는 가지 못하는 토마토로 바꾸어야한다.
				check[cur_y][cur_x] = 1;
			}
		}
	}
	*/

	map[3][5] = -1; // 썩은 토마토는 가지 못하는 토마토로 바꾸어야한다.
	check[3][5] = 1;
	cur_y = 3;
	cur_x = 5;
	while (!q.empty()) {

		cur_y = q.front().first;
		cur_x = q.front().second;
		q.pop();


		for (int i = 0; i < 4; i++) {
			int next_y = cur_y + dy[i];
			int next_x = cur_x + dx[i];

			// 다음 좌표가 지도 내부에 있으며, check가 기록된 적 없으며
			// map에서 -1(썩은거), 1(익은거)이 아니여야한다.
			if (isInside(next_x, next_y) && check[next_y][next_x] == 0 && map[next_y][next_x] != 1 && map[next_y][next_x] != -1) {
				check[next_y][next_x] = check[cur_y][cur_x] + 1;
				q.push(pair<int, int>(next_y, next_x));
			}
		}
	}

	for (int i = 0; i < 3; i++) {
		for (int j = 0; j < 5; j++) {
			cout << check[i][j];
		}
		cout << endl;
	}

	return 0;
}
