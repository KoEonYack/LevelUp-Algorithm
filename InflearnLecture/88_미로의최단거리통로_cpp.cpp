/*
	88. 미로의 최단거리 통로
	Idea. BFS(pair 사용)

Input.
0 0 0 0 0 0 0
0 1 1 1 1 1 0
0 0 0 1 0 0 0
1 1 0 1 0 1 1
1 1 0 1 0 0 0
1 0 0 0 1 0 0
1 0 1 0 0 0 0

>12

@ 유사문제: 백준 2178 미로탐색
	@ Ref. https://blockdmask.tistory.com/182
	@ Start day:  19. 12. 01.
	@ End day:   19. 12. 01.
*/

#include <cstdio>
#include <iostream>
#include <algorithm>
#include <queue>
#include <vector>

using namespace std;

int map[30][30];
int check[30][30];
int dx[4] = { 1, -1, 0, 0 };
int dy[4] = { 0, 0, 1, -1};

bool isInside(int x, int y) {
	return (x < 7 && x >= 0) && (y < 7 && y >= 0);
}

int main() {

	for (int i = 0; i < 7; i++) for (int j = 0; j <7; j++)
				scanf("%1d", &map[i][j]);


	for (int i = 0; i < 7; i++) {
		for (int j = 0; j < 7; j++) {
			cout << map[i][j];
		}
		cout << endl;
	}

	int cur_y = 0;
	int cur_x = 0;

	queue<pair<int, int>> q;
	q.push(pair<int, int>(cur_y, cur_x));
	check[cur_y][cur_x] = 1; // BFS가 몇 번째에 해당 지점을 방문했는지

	while (!q.empty()) {
		cur_y = q.front().first;
		cur_x = q.front().second;
		q.pop();

		if ((cur_y == 6) && (cur_x == 6)) break; // 도착지점

		for (int i = 0; i < 4; i++) { // 4방향 탐색
			int next_y = cur_y + dy[i];
			int next_x = cur_x + dx[i];

			// 다음 좌표가 지도 안에 있고 && check 배열에 기록된 적 없고(한 번도 방문하지 않은 지점)
			// && map에 0으로 기록되어 있으면
			if (isInside(next_y, next_x) && check[next_y][next_x] == 0 && map[next_y][next_x] == 0) {
				check[next_y][next_x] = check[cur_y][cur_x] + 1; // 이전 방문 + 1
				q.push(pair<int, int>(next_y, next_x)); // 큐에 넣는다.
			}
		}
	}

	for (int i = 0; i < 7; i++) {
		for (int j = 0; j < 7; j++) {
			cout << check[i][j];
		}
		cout << endl;
	}


	printf("%d\n", check[6][6]-1); // 마지막 출발 지점을 제거한다.
	return 0;
}


