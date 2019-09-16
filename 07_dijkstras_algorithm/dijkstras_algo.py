import unittest


class TestSearch(unittest.TestCase):
    @staticmethod
    def get_graph():
        graph = dict()
        graph['start'] = dict()
        graph['start']['a'] = 6
        graph['start']['b'] = 2

        graph['a'] = dict()
        graph['a']['fin'] = 1

        graph['b'] = dict()
        graph['b']['a'] = 3
        graph['b']['fin'] = 5

        graph['fin'] = dict()
        return graph

    @staticmethod
    def get_costs():
        costs = dict()
        costs['a'] = 6
        costs['b'] = 2
        costs['fin'] = float('inf')
        return costs

    @staticmethod
    def get_parents():
        parents = dict()
        parents['a'] = 'start'
        parents['b'] = 'start'
        parents['fin'] = None
        return parents

    def test_if_exists(self):
        answer = ['start', 'b', 'a', 'fin']
        graph = self.get_graph()
        costs = self.get_costs()
        parents = self.get_parents()

        self.assertEqual(dijkstra(graph, costs, parents), answer)


def find_lowest_cost_node(costs, processed):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        if costs[node] < lowest_cost and node not in processed:
            lowest_cost = costs[node]
            lowest_cost_node = node
    return lowest_cost_node


def get_min_path(parents):
    node = 'fin'
    path = list()
    while node != 'start':
        path.append(node)
        node = parents[node]
    path.append('start')
    return path[::-1]


def dijkstra(graph, costs, parents):
    """
    Dijkstra's algorithm
    :param graph:    Graph
    :param costs:    Edge's costs
    :param parents:  Node's parents with minimal cost
    :return:         Path with minimal cost
    """
    processed = list()

    node = find_lowest_cost_node(costs, processed)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]

        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs, processed)
    return get_min_path(parents)


if __name__ == '__main__':
    unittest.main()
