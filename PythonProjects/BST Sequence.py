class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None


def addToSequence(nextSteps, arraySoFar, solutions):
  for node in nextSteps:
    newNextSteps = nextSteps[:]
    newNextSteps.remove(node)
    if (node.left):
      newNextSteps.append(node.left)
    if (node.right):
      newNextSteps.append(node.right)

    newArraySoFar = arraySoFar[:]
    newArraySoFar.append(node.val)

    addToSequence(newNextSteps, newArraySoFar, solutions)

  if len(nextSteps) == 0:
    solutions.append(arraySoFar)
  return

def genSequences(root):
  # Return list of lists
  solutions = []
  addToSequence([root], [], solutions)
  return solutions

root = Node('d')
root.left = Node('b')
root.right = Node('f')
root.left.left = Node('a')
root.left.right = Node('c')
root.right.left = Node('f')
root.right.right = Node('g')

solution = genSequences(root)
for line in (solution):
  print(line)

print("The number of possible arrays:", len(solution))