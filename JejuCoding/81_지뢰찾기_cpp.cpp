

/*
	81. 지뢰찾기
Idea. 상하좌우

Input.
0 1 0 0 0
0 0 0 0 0
0 0 0 1 0
0 0 1 0 0
0 0 0 0 0

* f * 0 0
0 * 0 * 0
0 0 * f *
0 * f * 0
0 0 * 0 0

	@ Ref.
	@ Start day:  19. 12. 03.
	@ End day:   19. 12. 03.
*/


#include <cstdio>
#include <iostream>
#include <algorithm>
#include <queue>
#include <stack>
#include <vector>

using namespace std;

#define X 5
#define Y 5

int main() {

	int xx, yy;
	int flag[5][5];
	char minewepper[5][5];
	memset(minewepper, '0', sizeof(minewepper));
	int dx[4] = { -1, 1, 0, 0 };
	int dy[4] = { 0, 0, -1, 1 };

	printf("입력 값\n");
	for (int i = 0; i < Y; i++) {
		for (int j = 0; j < X; j++) {
			scanf("%d", &flag[i][j]);
		}
	}


	for (int i = 0; i < Y; i++) {
		for (int j = 0; j < X; j++) {
			if (flag[i][j] == 1) {
				minewepper[i][j] = 'f';
				for (int k = 0; k < 4; k++) {
					yy = i + dy[k];
					xx = j + dx[k];
					if (xx < 5 && xx >= 0 && yy < 5 && yy >= 0) {
						minewepper[yy][xx] = '*';
					}
				}
			}
		}
	}


	printf("결과");
	printf("\n");
	for (int i = 0; i < Y; i++) {
		for (int j = 0; j < X; j++) {
			printf("%c ", minewepper[i][j]);
		}
		printf("\n");
	}


	return 0;
}

