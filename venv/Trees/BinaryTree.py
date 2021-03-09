class Node():
    def __init__(self, val):
        self.left = None
        self.val = val
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None            #this is going to hold the tree's root Node

    def addUsingListHelper(self, root, level):
        """
        supportive function of addUsingList function
        :param root: current Node
        :param level: level of current Node
        :return: Nothing
        """
        head = root
        if head.left and head.right:
            self.addUsingListHelper(root.left, level + 1)
            self.addUsingListHelper(root.right, level + 1)
            return

        elif head.left == None and head.right == None:
            self.dic[self.ctr] = [head, level + 1, "Left"]
            self.ctr += 1
            self.dic[self.ctr] = [head, level + 1, "Right"]
            self.ctr += 1
        elif head.right == None:
            # n = Node(val)
            # head.right = n
            self.dic[self.ctr] = [head, level + 1, "Right"]
            self.ctr += 1
            self.addUsingListHelper(root.left, level + 1)

            return
        elif head.left == None:
            # n = Node(val)
            # head.left = n
            self.dic[self.ctr] = [head, level + 1, "Left"]
            self.ctr += 1
            self.addUsingListHelper(root.right, level + 1)

            return

        # self.addUsingListHelper(head.left,val)
        # self.addUsingListHelper(head.right, val)

    def addUsingList(self, data):
        """
        This function accepts a list and makes a tree from given list
        :param data: denotes passed list
        :return: Nothing
        """
        if self.root == None:
            n = Node(data[0])
            self.root = n
            del data[0]

            self.dic = {}
        for j in data:
            if len(self.dic) == 0:
                self.ctr = 0
                self.addUsingListHelper(self.root, 0)

            minimum_order = None
            for i in self.dic.keys():
                lis = self.dic[i]
                if minimum_order == None:
                    minimum_order = lis[1]
                else:
                    if minimum_order > lis[1]:
                        minimum_order = lis[1]
            item_to_be_removed = None
            for i in self.dic.keys():
                lis = self.dic[i]
                if lis[1] == minimum_order:
                    if lis[2] == "Left":
                        n = Node(j)
                        lis[0].left = n
                        item_to_be_removed = i
                    else:
                        n = Node(j)
                        lis[0].right = n
                        item_to_be_removed = i
                    break
            del self.dic[item_to_be_removed]

        # self.addUsingListHelper(self.root, data[0], 0)

    def showHelper(self, root):
        """
        supportive function of show function
        :param root: current Node
        :return: Nothing
        """
        if root.left and root.right:
            print(root.left.val)
            print(root.right.val)
            self.showHelper(root.left)

            self.showHelper(root.right)
        elif root.left == None and root.right == None:
            return
        elif root.left != None:

            print(root.left.val)
            print("None")  # for right
            self.showHelper(root.left)
        elif root.right != None:
            print("None")  # for left
            print(root.right.val)
            self.showHelper(root.right)

    def show(self):
        """
        Displays a tree
        :return: Nothing
        """
        if self.root == None:
            print("Tree is empty")
        else:
            print(self.root.val)
            self.showHelper(self.root)

    def levelFinderHelper(self, root, val, level):
        """
        it is a supportive function os levelFinder function
        :param root: denotes a Node
        :param val: value whose order is to be find
        :param level: level of current Node
        :return:
        """
        if root == None:
            return
        if root.val == val:
            print("its level is : " + str(level))

            return
        else:

            self.levelFinderHelper(root.left, val, level + 1)
            self.levelFinderHelper(root.right, val, level + 1)

    def levelFinder(self, val):
        """
        finds a level of passed value in tree
        :param val: accepts the val whole level is to be find
        :return: returns the level of value
        """
        if self.root == None:
            print("Create a tree first!!")
        else:
            level = 0
            self.levelFinderHelper(self.root, val, level)


lis = [1, 2, 3, 4, 5, 6, 7, 8, 9, None, 10, None, None, 11, None]
obj = BinaryTree()
obj.addUsingList(lis)
obj.show()
obj.levelFinder(6)
