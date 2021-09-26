from collections import deque


def topological_sort(vertices, edges):
  sortedOrder = []
  if vertices <= 0:
    return sortedOrder

  # a. Initialize the graph
  inDegree = {i: 0 for i in range(vertices)}  # count of incoming edges
  graph = {i: [] for i in range(vertices)}  # adjacency list graph

  # b. Build the graph
  for edge in edges:
    parent, child = edge[0], edge[1]
    graph[parent].append(child)  # put the child into it's parent's list
    inDegree[child] += 1  # increment child's inDegree

  # c. Find all sources i.e., all vertices with 0 in-degrees
  sources = deque()
  for key in inDegree:
    if inDegree[key] == 0:
      sources.append(key)

  # d. For each source, add it to the sortedOrder and subtract one from all of its children's in-degrees
  # if a child's in-degree becomes zero, add it to the sources queue
  while sources:
    vertex = sources.popleft()
    sortedOrder.append(vertex)
    for child in graph[vertex]:  # get the node's children to decrement their in-degrees
      inDegree[child] -= 1
      if inDegree[child] == 0:
        sources.append(child)

  # topological sort is not possible as the graph has a cycle
  if len(sortedOrder) != vertices:
    return []

  return sortedOrder


def main():
  print("Topological sort: " +
        str(topological_sort(4, [[3, 2], [3, 0], [2, 0], [2, 1]])))
  print("Topological sort: " +
        str(topological_sort(5, [[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]])))
  print("Topological sort: " +
        str(topological_sort(7, [[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1]])))


main()




from collections import deque


def is_scheduling_possible(tasks, prerequisites):
  sortedOrder = []
  if tasks <= 0:
    return False

  # a. Initialize the graph
  inDegree = {i: 0 for i in range(tasks)}  # count of incoming edges
  graph = {i: [] for i in range(tasks)}  # adjacency list graph

  # b. Build the graph
  for prerequisite in prerequisites:
    parent, child = prerequisite[0], prerequisite[1]
    graph[parent].append(child)  # put the child into it's parent's list
    inDegree[child] += 1  # increment child's inDegree

  # c. Find all sources i.e., all vertices with 0 in-degrees
  sources = deque()
  for key in inDegree:
    if inDegree[key] == 0:
      sources.append(key)

  # d. For each source, add it to the sortedOrder and subtract one from all of its children's in-degrees
  # if a child's in-degree becomes zero, add it to the sources queue
  while sources:
    vertex = sources.popleft()
    sortedOrder.append(vertex)
    for child in graph[vertex]:  # get the node's children to decrement their in-degrees
      inDegree[child] -= 1
      if inDegree[child] == 0:
        sources.append(child)

  # if sortedOrder doesn't contain all tasks, there is a cyclic dependency between tasks, therefore, we
  # will not be able to schedule all tasks
  return len(sortedOrder) == tasks


def main():
  print("Is scheduling possible: " +
        str(is_scheduling_possible(3, [[0, 1], [1, 2]])))
  print("Is scheduling possible: " +
        str(is_scheduling_possible(3, [[0, 1], [1, 2], [2, 0]])))
  print("Is scheduling possible: " +
        str(is_scheduling_possible(6, [[0, 4], [1, 4], [3, 2], [1, 3]])))

main()




from collections import deque


def find_order(tasks, prerequisites):
  sortedOrder = []
  if tasks <= 0:
    return sortedOrder

  # a. Initialize the graph
  inDegree = {i: 0 for i in range(tasks)}  # count of incoming edges
  graph = {i: [] for i in range(tasks)}  # adjacency list graph

  # b. Build the graph
  for prerequisite in prerequisites:
    parent, child = prerequisite[0], prerequisite[1]
    graph[parent].append(child)  # put the child into it's parent's list
    inDegree[child] += 1  # increment child's inDegree

  # c. Find all sources i.e., all vertices with 0 in-degrees
  sources = deque()
  for key in inDegree:
    if inDegree[key] == 0:
      sources.append(key)

  # d. For each source, add it to the sortedOrder and subtract one from all of its children's in-degrees
  # if a child's in-degree becomes zero, add it to the sources queue
  while sources:
    vertex = sources.popleft()
    sortedOrder.append(vertex)
    for child in graph[vertex]:  # get the node's children to decrement their in-degrees
      inDegree[child] -= 1
      if inDegree[child] == 0:
        sources.append(child)

  # if sortedOrder doesn't contain all tasks, there is a cyclic dependency between tasks, therefore, we
  # will not be able to schedule all tasks
  if len(sortedOrder) != tasks:
    return []

  return sortedOrder


def main():
  print("Is scheduling possible: " + str(find_order(3, [[0, 1], [1, 2]])))
  print("Is scheduling possible: " +
        str(find_order(3, [[0, 1], [1, 2], [2, 0]])))
  print("Is scheduling possible: " +
        str(find_order(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])))


main()




from collections import deque


def print_orders(tasks, prerequisites):
  sortedOrder = []
  if tasks <= 0:
    return False

  # a. Initialize the graph
  inDegree = {i: 0 for i in range(tasks)}  # count of incoming edges
  graph = {i: [] for i in range(tasks)}  # adjacency list graph

  # b. Build the graph
  for prerequisite in prerequisites:
    parent, child = prerequisite[0], prerequisite[1]
    graph[parent].append(child)  # put the child into it's parent's list
    inDegree[child] += 1  # increment child's inDegree

  # c. Find all sources i.e., all vertices with 0 in-degrees
  sources = deque()
  for key in inDegree:
    if inDegree[key] == 0:
      sources.append(key)

  print_all_topological_sorts(graph, inDegree, sources, sortedOrder)


def print_all_topological_sorts(graph, inDegree, sources, sortedOrder):
  if sources:
    for vertex in sources:
      sortedOrder.append(vertex)
      sourcesForNextCall = deque(sources)  # make a copy of sources
      # only remove the current source, all other sources should remain in the queue for the next call
      sourcesForNextCall.remove(vertex)
      # get the node's children to decrement their in-degrees
      for child in graph[vertex]:
        inDegree[child] -= 1
        if inDegree[child] == 0:
          sourcesForNextCall.append(child)

      # recursive call to print other orderings from the remaining (and new) sources
      print_all_topological_sorts(
        graph, inDegree, sourcesForNextCall, sortedOrder)

      # backtrack, remove the vertex from the sorted order and put all of its children back to consider
      # the next source instead of the current vertex
      sortedOrder.remove(vertex)
      for child in graph[vertex]:
        inDegree[child] += 1

  # if sortedOrder doesn't contain all tasks, either we've a cyclic dependency between tasks, or
  # we have not processed all the tasks in this recursive call
  if len(sortedOrder) == len(inDegree):
    print(sortedOrder)


def main():
  print("Task Orders: ")
  print_orders(3, [[0, 1], [1, 2]])

  print("Task Orders: ")
  print_orders(4, [[3, 2], [3, 0], [2, 0], [2, 1]])

  print("Task Orders: ")
  print_orders(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])


main()




from collections import deque


def find_order(words):
  if len(words) == 0:
    return ""

  # a. Initialize the graph
  inDegree = {}  # count of incoming edges
  graph = {}  # adjacency list graph
  for word in words:
    for character in word:
      inDegree[character] = 0
      graph[character] = []

  # b. Build the graph
  for i in range(0, len(words)-1):
    # find ordering of characters from adjacent words
    w1, w2 = words[i], words[i + 1]
    for j in range(0, min(len(w1), len(w2))):
      parent, child = w1[j], w2[j]
      if parent != child:  # if the two characters are different
        # put the child into it's parent's list
        graph[parent].append(child)
        inDegree[child] += 1  # increment child's inDegree
        break  # only the first different character between the two words will help us find the order

  # c. Find all sources i.e., all vertices with 0 in-degrees
  sources = deque()
  for key in inDegree:
    if inDegree[key] == 0:
      sources.append(key)

  # d. For each source, add it to the sortedOrder and subtract one from all of its children's in-degrees
  # if a child's in-degree becomes zero, add it to the sources queue
  sortedOrder = []
  while sources:
    vertex = sources.popleft()
    sortedOrder.append(vertex)
    for child in graph[vertex]:  # get the node's children to decrement their in-degrees
      inDegree[child] -= 1
      if inDegree[child] == 0:
        sources.append(child)

  # if sortedOrder doesn't contain all characters, there is a cyclic dependency between characters, therefore, we
  # will not be able to find the correct ordering of the characters
  if len(sortedOrder) != len(inDegree):
    return ""

  return ''.join(sortedOrder)


def main():
  print("Character order: " + find_order(["ba", "bc", "ac", "cab"]))
  print("Character order: " + find_order(["cab", "aaa", "aab"]))
  print("Character order: " + find_order(["ywx", "wz", "xww", "xz", "zyy", "zwz"]))


main()




from collections import deque


def can_construct(originalSeq, sequences):
  sortedOrder = []
  if len(originalSeq) <= 0:
    return False

  # a. Initialize the graph
  inDegree = {}  # count of incoming edges
  graph = {}  # adjacency list graph
  for sequence in sequences:
    for num in sequence:
      inDegree[num] = 0
      graph[num] = []

  # b. Build the graph
  for sequence in sequences:
    for i in range(1, len(sequence)):
      parent, child = sequence[i - 1], sequence[i]
      graph[parent].append(child)
      inDegree[child] += 1

  # if we don't have ordering rules for all the numbers we'll not able to uniquely construct the sequence
  if len(inDegree) != len(originalSeq):
    return False

  # c. Find all sources i.e., all vertices with 0 in-degrees
  sources = deque()
  for key in inDegree:
    if inDegree[key] == 0:
      sources.append(key)

  # d. For each source, add it to the sortedOrder and subtract one from all of its children's in-degrees
  # if a child's in-degree becomes zero, add it to the sources queue
  while sources:
    if len(sources) > 1:
      return False  # more than one sources mean, there is more than one way to reconstruct the sequence
    if originalSeq[len(sortedOrder)] != sources[0]:
      # the next source(or number) is different from the original sequence
      return False

    vertex = sources.popleft()
    sortedOrder.append(vertex)
    for child in graph[vertex]:  # get the node's children to decrement their in-degrees
      inDegree[child] -= 1
      if inDegree[child] == 0:
        sources.append(child)

  # if sortedOrder's size is not equal to original sequence's size, there is no unique way to construct
  return len(sortedOrder) == len(originalSeq)


def main():
  print("Can construct: " +
        str(can_construct([1, 2, 3, 4], [[1, 2], [2, 3], [3, 4]])))
  print("Can construct: " +
        str(can_construct([1, 2, 3, 4], [[1, 2], [2, 3], [2, 4]])))
  print("Can construct: " +
        str(can_construct([3, 1, 4, 2, 5], [[3, 1, 5], [1, 4, 2, 5]])))


main()




from collections import deque


def find_trees(nodes, edges):
  if nodes <= 0:
    return []

  # with only one node, since its in-degrees will be 0, therefore, we need to handle it separately
  if nodes == 1:
    return [0]

  # a. Initialize the graph
  inDegree = {i: 0 for i in range(nodes)}  # count of incoming edges
  graph = {i: [] for i in range(nodes)}  # adjacency list graph

  # b. Build the graph
  for edge in edges:
    n1, n2 = edge[0], edge[1]
    # since this is an undirected graph, therefore, add a link for both the nodes
    graph[n1].append(n2)
    graph[n2].append(n1)
    # increment the in-degrees of both the nodes
    inDegree[n1] += 1
    inDegree[n2] += 1

  # c. Find all leaves i.e., all nodes with 1 in-degrees
  leaves = deque()
  for key in inDegree:
    if inDegree[key] == 1:
      leaves.append(key)

  # d. Remove leaves level by level and subtract each leave's children's in-degrees.
  # Repeat this until we are left with 1 or 2 nodes, which will be our answer.
  # Any node that has already been a leaf cannot be the root of a minimum height tree, because
  # its adjacent non-leaf node will always be a better candidate.
  totalNodes = nodes
  while totalNodes > 2:
    leavesSize = len(leaves)
    totalNodes -= leavesSize
    for i in range(0, leavesSize):
      vertex = leaves.popleft()
      # get the node's children to decrement their in-degrees
      for child in graph[vertex]:
        inDegree[child] -= 1
        if inDegree[child] == 1:
          leaves.append(child)

  return list(leaves)


def main():
  print("Roots of MHTs: " +
        str(find_trees(5, [[0, 1], [1, 2], [1, 3], [2, 4]])))
  print("Roots of MHTs: " +
        str(find_trees(4, [[0, 1], [0, 2], [2, 3]])))
  print("Roots of MHTs: " +
        str(find_trees(4, [[1, 2], [1, 3]])))


main()