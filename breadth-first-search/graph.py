# Breadth-First Search (BFS) allows you to find the shortest distance between two things

"""
BFS solves the shortest-path problem — finding the shortest route between two nodes in a graph.

Graphs:
 A graph is a set of connections e.g. "alex owes money to rama" → alex -> rama
 Graphs are made up of nodes and edges:
 alex and rama are nodes
the arrow (->) between them is the edge
Graphs model how different things are connected to one another

Queues (FIFO - First In, First Out):
 Like a bus stop: if you arrive before your friend, you board the bus first
In BFS, nodes are added to the back of the queue (enqueue) 
and processed from the front (dequeue)
the order is not a matter
"""
# implemention of algorithms python uses append and popleft instead of enqueue and dequeue
from collections import deque

graph = {}
graph['you'] = ['alice', 'bob', 'claire']
graph['alice'] = ['peggy']
graph['bob'] = ['anuj', 'peggy']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []

def person_is_seller(name):
  return name[-1] == 'm'

from collections import deque

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = set()

    while search_queue:
        person = search_queue.popleft()

        if person not in searched:
            if person_is_seller(person):
                print(person + " is a mango seller")
                return True
            else:
                search_queue += graph[person]
                searched.add(person)

    return False

search('you')


