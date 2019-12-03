/*
	55. 기차운행
	Idea. Stack

Input.
3
2 1 3

PPOOPO

	@ Ref.
	@ Start day:  19. 12. 02.
	@ End day:   19. 12. 02.
*/

#include <cstdio>
#include <iostream>
#include <algorithm>
#include <queue>
#include <stack>
#include <vector>

using namespace std;

int main() {

	int n, num, j=1;
	stack<int> s;
	vector<char> str;
	scanf("%d", &n);
	vector<int> a(n + 1);

	for (int i = 1; i <= n; i++) {
		a[i] = i;
	}

	for (int i = 1; i <= n; i++) {
		scanf("%d", &num);
		s.push(num);
		str.push_back('P');

		while (1) {
			if (s.empty()) break;
			if (a[j] == s.top()) { // 스택의 맨 위와 같은 경우
				s.pop();
				j++;
				str.push_back('O');
			}
			else break;		// 값이 다른 경우 반복할 이유가 없다.
		}
	}

	if (!s.empty()) printf("impossible\n");
	else {
		for (int i = 0; i < str.size(); i++) {
			printf("%c", str[i]);
		}
	}

	return 0;
}


