class SuffixTrie:
      class Node:
         def __init__(self) -> None:
            self.value = ""
            self.children = []
         
         def addChild(self, n):
            self.children.append(n)

         def hasChild(self, char):
            for node in self.children:
                if node.value == char:
                    return node
            
            return None

         
         
      def __init__(self) -> None:
        self.root = self.Node()

      def generateSuffixes(self, string):
         suffixes = []
         for i in range(len(string)):
            suffixes.append(string[i:])
         
         return suffixes

      def insertString(self, string):
         suffixes = self.generateSuffixes(string)

         for suffix in suffixes:
            stack = []
            stack.append(self.root)
            i = 0
            while stack and i < len(suffix):
               curNode = stack.pop()
               next = curNode.hasChild(suffix[i])

               if next is not None:
                  stack.append(next)
               else:
                  newNode = self.Node()
                  newNode.value = suffix[i]
                  curNode.addChild(newNode)
                  stack.append(newNode)
               
               i += 1
         
      def printAll(self):
         stack = []
         stack.append(self.root)
         f = open("output.txt", "w")
         output = ""
         while stack:
            curNode = stack.pop()
            print(curNode.value)
            output += curNode.value + "\n"
            for node in curNode.children:
                stack.append(node)
         f.write(output[1:])
         
         
      
      def check(self, string):
         stack = []
         stack.append(self.root)

         for char in string:
            curNode = stack.pop()
            if curNode.hasChild(char) is None:
               return False
            else:
               stack.append(curNode.hasChild(char))
            
         return True
      
      def condense(self):
         stack = []
         stack.append(self.root)

         while stack:
            curNode = stack.pop()
            newVal = ""
            if len(curNode.children) == 1:
               newVal = curNode.value
               tempStack = []
               tempStack.append(curNode.children[0])
               while len(tempStack[-1].children) == 1:
                  newVal += tempStack[-1].value
                  node = tempStack[-1].children[0]
                  tempStack.pop()
                  tempStack.append(node)
               
               
               node = tempStack.pop()
               curNode.value = newVal + node.value
               curNode.children.clear()

               if len(node.children) != 0:
                  for nodes in node.children:
                     curNode.children.append(nodes)
                     stack.append(nodes)
            else:
               for node in curNode.children:
                  stack.append(node)

            




             
                
            
                  

            

string = "GTAGT$"

tree = SuffixTrie()
tree.insertString(string)
tree.condense()
tree.printAll()