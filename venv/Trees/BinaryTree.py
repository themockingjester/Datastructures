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
    def replaceHelper(self,root,val,newval):
        """
        This function will actually replace all the values matched with given values in a Tree on the basis of flag argument if flag will be true then all matching values will get replaced other wise single value get updated
        :param root: current Node
        :param val: value to be updated
        :param newval: new value which is to be assigned
        :return:
        """
        if root==None:
            return
        else:
            if root.val==val:
                if self.forreplacingall== False and self.shouldstop==False:
                    root.val = newval

                    self.matches_found += 1
                    self.shouldstop = True
                elif self.forreplacingall==True:
                    root.val = newval

                    self.matches_found+=1


                    self.replaceHelper(root.left,val,newval)
                    self.replaceHelper(root.right,val,newval)

            else:
                if self.shouldstop == False:
                    self.replaceHelper(root.left, val, newval)
                    self.replaceHelper(root.right, val, newval)

    def replaceAll(self,val,newval):
        """
        This function will replace all the values matched with given values in a Tree
        :param val: value to be replaced
        :param newval: new value which is going to be assigned to old valu
        :return: nothing
        """
        self.shouldstop = False
        self.forreplacingall = True
        if self.root == None:
            print("Tree is empty")
        else:
            self.matches_found = 0
            self.replaceHelper(self.root, val, newval)
            print(str(self.matches_found)+" matches found")

    def replace(self,val,newval):
        """
        This function will replace only one tree node which matches with given value
        :param val: value to be changed
        :param newval: new value to be assigned to old value
        :return: Nothing
        """
        self.shouldstop = False
        self.forreplacingall = False
        if self.root == None:
            print("Tree is empty")
        else:
            self.matches_found = 0
            self.replaceHelper(self.root,val,newval)
            print(str(self.matches_found)+" matches found")
    def inOrderTraversalHelper(self,root):
        """
        This is the actual inorder traversal performer
        inorder  ----> (Left, Root, Right)
        :param root: current Node
        :return: Nothing
        """
        if root:
            self.inOrderTraversalHelper(root.left)
            print(root.val)
            self.inOrderTraversalHelper(root.right)

    def inOrderTraversal(self):
        """
        this method initiates the inorder traversal
        :return: Nothing
        """
        self.inOrderTraversalHelper(self.root)
    def preOrderTraversalHelper(self,root):
        """
        Preorder -----> (Root, Left, Right)
        This is the actual preorder traversal performer
        :param root: current Node
        :return: Nothing
        """
        if root:
            print(root.val)
            self.preOrderTraversalHelper(root.left)
            self.preOrderTraversalHelper(root.right)
    def preOrderTraversal(self):
        """
        This method initiates the preorder traversal
        :return: Nothing
        """
        self.preOrderTraversalHelper(self.root)
    def postOrderTraversalHelper(self,root):
        """
        Postorder ----> (Left, Right, Root)
        This method is the actual postorder traversal performer
        :param root: current Node
        :return: Nothing
        """
        if root:
            self.postOrderTraversalHelper(root.left)
            self.postOrderTraversalHelper(root.right)
            print(root.val)

    def postOrderTraversal(self):
        """
        This function initiates the postorder traversal
        :return: Nothing
        """
        self.postOrderTraversalHelper(self.root)
    def removeHelper(self,root,val):
        """
        This method is responsible for actual removing
        :param root: current Node
        :param val: value to be removed
        :return: Nothing
        """
        if root:
            if self.shouldstop==False:
                if root.left:

                    if root.left.val==val:
                        root.left = None
                        if self.shouldremoveall == False:
                            self.shouldstop = True
                            return
                    else:
                        self.removeHelper(root.left, val)
                if root.right:
                    if root.right.val == val:
                        root.right = None
                        if self.shouldremoveall == False:
                            self.shouldstop = True
                            return
                    else:
                        self.removeHelper(root.right, val)

    def remove(self,val):
        """
        This methods is responsible for removing one matched value
        :param val: value to be removed
        :return: Nothing
        """
        self.shouldstop = False
        self.shouldremoveall = False
        if self.root.val==val:
            self.root = None
        else:
            self.removeHelper(self.root,val)
    def removeAll(self,val):
        """
        This method is responsible for removing all matching values
        :param val: value to be removed
        :return: Nothing
        """
        self.shouldstop = False
        self.shouldremoveall = True
        if self.root.val==val:
            self.root = None
        else:
            self.removeHelper(self.root,val)
lis = [1, 2, 3, 4, 5, 6, 7, 8, 9, None, 10, None, None, 11, None]

obj = BinaryTree()
obj.addUsingList(lis)

obj.postOrderTraversal()

