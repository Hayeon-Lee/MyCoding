#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;

vector<vector<int>> graph;
vector<int> point;
queue<int> q;

int N, M;
int index = 0;

void init();
void bfs(int R);

int main() {
	int R;
	scanf("%d %d %d", &N, &M, &R);

	init();
	bfs(R);

	for (int i = 1; i <= N; i++) printf("%d\n", point[i]);
}

void init() {
	graph.resize(N+1);//1차원크기 N+1로 확대
	point.resize(N + 1);

	int tmp1, tmp2;
	for (int i = 0; i < M; i++)
	{
		scanf("%d %d", &tmp1, &tmp2);

		graph[tmp1].push_back(tmp2); 
		graph[tmp2].push_back(tmp1);
	}

	for (int i = 0; i <= N; i++) sort(graph[i].begin(), graph[i].end()); //오름차순 정렬 시작정점으로부터.
}

void bfs(int R) {
	point[R] = ++index;
	q.push(R);

	while (q.empty() != true) {
		int u = q.front();
		q.pop();
		int graphsize = graph[u].size();
		for (int i = 0; i < graphsize; i++) {
			if (point[graph[u][i]] == false) {
				point[graph[u][i]] = ++index;
				q.push(graph[u][i]);
			}
		}
	}
}