import unittest
from collections import deque


class TestSearch(unittest.TestCase):
    graph = dict()
    graph["you"] = ["alice", "bob", "claire"]
    graph["bob"] = ["anuj", "peggy"]
    graph["alice"] = ["peggy"]
    graph["claire"] = ["thom", "johnny"]
    graph["anuj"] = []
    graph["peggy"] = []
    graph["thom"] = []
    graph["johnny"] = []

    def test_if_exists(self):
        self.assertEqual(bf_search("you", self.graph), True)
        self.assertEqual(bf_search("claire", self.graph), True)

    def test_if_not_exists(self):
        self.assertEqual(bf_search("peggy", self.graph), False)
        self.assertEqual(bf_search("alice", self.graph), False)
        self.assertEqual(bf_search("bob", self.graph), False)


def is_the_shining(name):
    return name == 'johnny'


def bf_search(name, graph):
    """
    Breadth first search
    :param name:  name of starting vertice
    :param graph: graph, where to do search
    :return:      True if we can get from name to 'johnny' else False
    """
    search_queue = deque()
    search_queue += graph[name]
    searched = list()

    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if is_the_shining(person):
                print(f"Here's {person}!")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False


if __name__ == '__main__':
    unittest.main()
