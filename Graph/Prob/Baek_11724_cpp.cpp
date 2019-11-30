/*

    백준 11724번. 
    Ref. https://jaimemin.tistory.com/637
    Start-End. 2019. 10. 30.

    Input.
    6 5
    1 2
    2 5
    5 1
    3 4
    4 6
    
    Out. 
    2

*/


#include <iostream>
#include <vector>
using namespace std;

const int MAX = 1000 + 1;

int M, N;
vector<int> graph[MAX];
bool visited[MAX];

void DFS(int node){
    visited[node] = true;

    for(int i=0; i<graph[node].size(); i++){
        int next = graph[node][i];
        if(!visited[next]){
            DFS(next);
        }
    }
}

int main(void)
{
    cin>> N >> M;
    for ( int i=0; i<M; i++){
        int node1, node2;
        cin >> node1 >> node2;

        graph[node1].push_back(node2);
        graph[node2].push_back(node1);
    }

    int cnt = 0;
    for( int i=1; i<=N; i++){
        if(!visited[i]){
            DFS(i);
            cnt++;
        }
    }
    cout << cnt << endl;
    return 0;
}