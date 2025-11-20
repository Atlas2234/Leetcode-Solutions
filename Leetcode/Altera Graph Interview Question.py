# // Given a graph with N nodes and M weighted edges,
# // write a function which returns the shortest
# // path from a given source to a given destination.
# //
# // Sample Graph:
# //  {0, 1, 100},    0 -> 1 has a weight of 100
# //  {1, 2, 100},    1 -> 2 has a weight of 100
# //  {0, 2, 500},    0 -> 2 has a weight of 500
# //  {2, 3, 100},    2 -> 3 has a weight of 100
# //  {1, 3, 600},    1 -> 3 has a weight of 600

#include <iostream>
#include <vector>
#include <limits>
# using namespace std;

# const int INF = numeric_limits<int>::max();

# struct Edge {
#     int u, v, w;
# };

# int shortest_path(N, M, edges, start, end) {
#   vector<int> distances = (N, INF);
#   distances[start] = 0;
#   for node in range(0, N):
#     for edge in edges:
#       if distances[edge.u] != INF && dist[edge.u] + edge.w < dist[edge.v]:
#         dist[edge.v] = dist[edge.u] + edge.w;

#   return distances[end];
# }

# int main() {
#     int N = 4, M = 5;
#     vector<Edge> edges = {
#         {0, 1, 100},
#         {1, 2, 100},
#         {0, 2, 500},
#         {2, 3, 100},
#         {1, 3, 600},
#     };
#     int result = shortest_path(N, M, edges, 0, 3);
#     cout << result << endl;
#     return 0;
# }

