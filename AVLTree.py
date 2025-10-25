"""A class representing a node in an AVL tree"""

class AVLNode(object):
	"""Constructor for class AVLNode
	
	@type key: int
	@param key: key of your node
	@type value: string
	@param value: data of your node
	"""
	#time complexity: O(1)

	def __init__(self, key, value):
		self.key = key
		self.value = value
		self.left = None
		self.right = None
		self.parent = None
		self.height = -1

	"""returns whether self is not a virtual node 

	@rtype: bool
	@returns: False if self is a virtual node, True otherwise.
	"""
	#time complexity: O(1)

	def is_real_node(self):
		if self.key is None: return False
		return True

	"""returns the left child

	@rtype: AVLNode
	@returns: the left child of self, None if there is no left child (if self is virtual)
	"""
	#time complexity: O(1)

	def get_left(self):
		return self.left

	"""returns the right child

	@rtype: AVLNode
	@returns: the right child of self, None if there is no right child (if self is virtual)
	"""
	#time complexity: O(1)

	def get_right(self):
		return self.right

	"""returns the parent

	@rtype: AVLNode
	@returns: the parent of self, None if there is no parent
	"""
	#time complexity: O(1)

	def get_parent(self):
		return self.parent

	"""returns the key

	@rtype: int or None
	@returns: the key of self, None if the node is virtual
	"""
	#time complexity: O(1)

	def get_key(self):
		return self.key

	"""returns the value

	@rtype: any
	@returns: the value of self, None if the node is virtual
	"""
	#time complexity: O(1)

	def get_value(self):
		return self.value

	"""returns the height

	@rtype: int
	@returns: the height of self, -1 if the node is virtual
	"""
	#time complexity: O(1)

	def get_height(self):
		return self.height

	"""sets left child

	@type node: AVLNode
	@param node: a node
	"""
	#time complexity: O(1)

	def set_left(self, node):
		self.left = node

	"""sets right child

	@type node: AVLNode
	@param node: a node
	"""
	#time complexity: O(1)

	def set_right(self, node):
		self.right = node

	"""sets parent

	@type node: AVLNode
	@param node: a node
	"""
	#time complexity: O(1)

	def set_parent(self, node):
		self.parent = node

	"""sets key

	@type key: int or None
	@param key: key
	"""
	#time complexity: O(1)

	def set_key(self, key):
		self.key = key

	"""sets value

	@type value: any
	@param value: data
	"""
	#time complexity: O(1)

	def set_value(self, value):
		self.value = value

	"""sets the height of the node

	@type h: int
	@param h: the height
	"""
	#time complexity: O(1)

	def set_height(self, h):
		self.height = h

	""""calculates the height of node according to children

	@rtype: int
	@returns: the calculated height of self, -1 if the node is virtual
	"""
	#time complexity: O(1)

	def calc_height(self):
		if not self.is_real_node(): return -1
		else: return max(self.left.height , self.right.height) + 1

	""""fixes the height of node according to children, if node is not virtual
	"""
	#time complexity: O(1)

	def fix_height(self):
		if self.is_real_node(): self.set_height(max(self.left.height , self.right.height) + 1)

	"""returns the balance factor of a node - height difference between left child
	to right child, if node is not virtual

	@rtype: int
	@returns: the balance factor of self
	"""
	#time complexity: O(1)

	def get_balance_factor(self):
		return self.left.height - self.right.height

	"""sets node as the right child of self and sets node's parent as self

	@type node: AVLNode
	@param node: a node
	"""
	#time complexity: O(1)

	def set_right_with_parent(self, node):
		self.right = node
		node.set_parent(self)

	"""sets node as the left child of self and sets node's parent as self

	@type node: AVLNode
	@param node: a node
	"""
	#time complexity: O(1)

	def set_left_with_parent(self, node):
		self.left = node
		node.set_parent(self)

"""
A class representing an AVL tree
"""

class AVLTree(object):

	"""
	Constructor for class AVLTree 
	"""
	#time complexity: O(1)

	def __init__(self, selfRoot = None, selfMax = None , selfTreeSize = 0):
		self.root = selfRoot
		self.max = selfMax
		self.tree_size = selfTreeSize

	"""searches for a node in the dictionary corresponding to the key (starting at the root)
        
	@type key: int
	@param key: a key to be searched
	@rtype: (AVLNode,int)
	@returns: a tuple (x,e) where x is the node corresponding to key (or None if not found),
	and e is the number of edges on the path between the starting node and ending node+1.
	"""
	# time complexity: O(log(n))

	def search(self, key):
		node = self.root
		edges = 1
		while (node is not None) and (node.is_real_node()):
			currKey = node.get_key()
			if currKey == key: return node, edges
			if currKey < key:
				node = node.get_right()
				edges += 1
			else: 
				node = node.get_left()
				edges += 1
		if node is not None and not node.is_real_node(): #did not find key, remove 1 edge travelled to virtual node
			edges = edges - 1
		return None, edges

	"""searches for a node in the dictionary corresponding to the key, starting at the max
        
	@type key: int
	@param key: a key to be searched
	@rtype: (AVLNode,int)
	@returns: a tuple (x,e) where x is the node corresponding to key (or None if not found),
	and e is the number of edges on the path between the starting node and ending node+1.
	"""
	# time complexity: O(log(n))

	def finger_search(self, key):
		node = self.max
		edges = 1
		#going up from pointer to max until we reach the node key could be in the subtree of
		while (node.is_real_node()) and (key < node.key) and (node != self.root):
			node = node.get_parent()
			edges += 1

		#searching the subtree starting from the node we found with regular search
		while (node is not None) and (node.is_real_node()):
			currKey = node.get_key()
			if currKey == key: return node, edges
			if currKey < key:
				node = node.get_right()
				edges += 1
			else:
				node = node.get_left()
				edges += 1
		if node is not None and not node.is_real_node():  # did not find key, remove 1 edge travelled to virtual node
			edges = edges - 1
		return None, edges

	"""inserts a new node into the dictionary with the corresponding key and value (starting at the root)

	@type key: int
	@pre: key currently does not appear in the dictionary
	@param key: key of item that is to be inserted to self
	@type val: string
	@param val: the value of the item
	@rtype: (AVLNode,int,int)
	@returns: a 3-tuple (x,e,h) where x is the new node,
	e is the number of edges on the path between the starting node and new node before rebalancing,
	and h is the number of PROMOTE cases during the AVL rebalancing
	"""
	# time complexity: O(log(n))

	def insert(self, key, val):
		node = self.root
		edges = 0
		cntPromotes = 0

		if node is None: #empty tree - insert new node as root and done
			self.root = AVLNode(key,val)
			self.root.set_height(0)
			self.max = self.root
			self.root.set_left_with_parent(AVLNode(None,None))
			self.root.set_right_with_parent(AVLNode(None,None))
			self.tree_size += 1  # update tree size
			return self.root, edges, cntPromotes
		
		else: #not an empty tree
			#look for insertion point in a virtual node through searching the key
			while node.is_real_node():
				if node.get_key() < key:
					node = node.get_right()
					edges += 1
				else: 
					node = node.get_left()
					edges += 1

			#now, node is the virtual node we insert in. insertion:
			node.set_key(key)
			node.set_value(val)
			node.set_height(0)
			node.set_left_with_parent(AVLNode(None,None))
			node.set_right_with_parent(AVLNode(None,None))
			# rebalance starting from parent of node we found
			cntPromotes = self.rebalance(node.get_parent())

		if key > self.max.get_key(): self.max = node #update max key of tree
		self.tree_size += 1 #update tree size
		self.fix_root() # fixing root if needed

		return node, edges, cntPromotes 

	"""rebalances AVL tree after insertion

	@type node: AVLNode
	@pre: node is the parent of an inserted node
	@rtype: int
	@returns: the number of PROMOTE cases during rebalancing
	"""
	# time complexity: O(log(n))

	def rebalance (self, node):
		cntPromotes = 0
		while node is not None: #going up the tree, rebalancing where needed
				bf = node.get_balance_factor()
				if -1 <= bf <= 1: #valid balance factor for node
					if node.get_height() < node.calc_height(): #height needs to be promoted
						cntPromotes += 1
					node.fix_height()
					node = node.get_parent() #moving up
				else: #invalid balance factor - rotations needed
					self.rotate(node) #rotating tree around node 
		return  cntPromotes

	"""rotates tree around node with an invalid balance factor

	@type node: AVLNode
	@pre: node points to a node in self
	"""
	# time complexity: O(1)

	def rotate (self, node):
		if node.get_balance_factor() == 2: #left subtree is longer
			if node.get_left().get_balance_factor() == 1: #right rotation 
				self.right_rotate(node)
			else: #bf = -1, left rotation (on left child) then right rotation (on node) 
				self.left_rotate(node.get_left())
				self.right_rotate(node)
		else: #bf = -2, right subtree is longer	
			if node.get_right().get_balance_factor() == -1: #left rotation 
				self.left_rotate(node)
			else: #bf = 1, right rotation (on right child) then left rotation (on node) 
				self.right_rotate(node.get_right())
				self.left_rotate(node)
		
	"""rotates edge between node and left child to right

	@type node: AVLNode
	@pre: node points to a node in self
	"""
	# time complexity: O(1)

	def right_rotate (self, node):
		temp = node.get_left() #the new root of the subtree of node 
		#fixing parent of node to be parent of new root
		parent = node.get_parent()
		if parent is None: #node is the root of whole tree
			self.root = temp
			temp.set_parent(None)
		else: #parent exists
			if node.get_key() > parent.get_key(): #node is right child of parent
				parent.set_right_with_parent(temp)
			else: #node is left child of parent
				parent.set_left_with_parent(temp)
		node.set_left_with_parent(temp.get_right()) #moving right child of temp
		temp.set_right_with_parent(node) #temp is the new root
		temp.fix_height()
		node.fix_height()

	"""rotates edge between node and right child to left

	@type node: AVLNode
	@pre: node points to a node in self
	"""
	# time complexity: O(1)

	def left_rotate (self, node):
		temp = node.get_right() #the new root of the subtree of node 
		#fixing parent of node to be parent of new root
		parent = node.get_parent()
		if parent is None: #node is the root of whole tree
			self.root = temp
			temp.set_parent(None)
		else: #parent exists
			if node.get_key() > parent.get_key(): #node is right child of parent
				parent.set_right_with_parent(temp)
			else: #node is left child of parent
				parent.set_left_with_parent(temp)
		node.set_right_with_parent(temp.get_left()) #moving left child of temp
		temp.set_left_with_parent(node) #temp is the new root
		temp.fix_height()
		node.fix_height()

	"""inserts a new node into the dictionary with corresponding key and value, starting at the max

	@type key: int
	@pre: key currently does not appear in the dictionary
	@param key: key of item that is to be inserted to self
	@type val: string
	@param val: the value of the item
	@rtype: (AVLNode,int,int)
	@returns: a 3-tuple (x,e,h) where x is the new node,
	e is the number of edges on the path between the starting node and new node before rebalancing,
	and h is the number of PROMOTE cases during the AVL rebalancing
	"""
	# time complexity: O(log(n))

	def finger_insert(self, key, val):
		node = self.max
		if node is None: return self.insert(key, val) #tree is empty, perform regular insert

		edges = 0
		#finger search - going up from pointer to max until we reach the node key should have been in the subtree of
		while (node.is_real_node()) and (key < node.key) and (node != self.root) and (key < node.get_parent().get_key()):
			node = node.get_parent()
			edges += 1

		#look for insertion point in a virtual node through searching the key, starting from node
		cntPromotes = 0
		while node.is_real_node():
			if node.get_key() < key:
				node = node.get_right()
				edges += 1
			else:
				node = node.get_left()
				edges += 1

		# now, node is the virtual node we insert in
		# #inserting node at the subtree starting from the node we found, same as in method insert
		node.set_key(key)
		node.set_value(val)
		node.set_height(0)
		node.set_left_with_parent(AVLNode(None, None))
		node.set_right_with_parent(AVLNode(None, None))
		cntPromotes += self.rebalance(node.get_parent())  # rebalance starting from parent of node we found

		if key > self.max.get_key(): self.max = node  # update max key of tree
		self.tree_size += 1  # update tree size
		self.fix_root() # fixing root if needed

		return node, edges, cntPromotes

	"""fixes the root of the tree if the root has a new father

	@pre: root is a node in self
	"""
	# time complexity: O(1)

	def fix_root(self):
		while self.root.get_parent() is not None:
			self.root = self.root.get_parent()

	"""deletes node from the dictionary

	@type node: AVLNode
	@pre: node is a real pointer to a node in self
	"""
	# time complexity: O(log(n))

	def delete(self, node):
		if not node or not node.is_real_node(): #node is a virtual node
			return None

		#Case 1: node is a leaf (has only virtual children)
		if not node.get_left().is_real_node() and not node.get_right().is_real_node():
			parent = node.get_parent()
			virtual_node = AVLNode(None,None)
			if parent is None: #node is the root
				self.root =  None
			elif parent.get_left() == node: #replace with virtual node
				parent.set_left_with_parent(virtual_node) #node is left child
			else:
				parent.set_right_with_parent(virtual_node) #node is right child
			self.rebalance_delete(parent) #rebalancing

		#Case 2: node has one real child, one virtual child
		elif not node.get_left().is_real_node(): #the virtual child is the left child
			self.replace_node_delete(node, node.get_right())
			self.rebalance_delete(node.get_right()) #rebalancing after delete
		elif not node.get_right().is_real_node(): #the virtual child is the right child
			self.replace_node_delete(node, node.get_left())
			self.rebalance_delete(node.get_left()) #rebalancing after delete

		#Case 3: node has 2 real children
		else:
			successor = self.successor(node)  # finding the successor of node
			successor_parent = successor.get_parent()

			if successor_parent is not node: #successor's is not the direct right child of node
				self.replace_node_delete(successor, successor.get_right())
				successor.set_right_with_parent(node.get_right())

			self.replace_node_delete(node, successor)
			successor.set_left_with_parent(node.get_left())

			#rebalance after all the changes
			if successor_parent is not node:
				self.rebalance_delete(successor_parent)
			else:
				self.rebalance_delete(successor)

		#update the max pointer and the tree size 
		self.tree_size -= 1
		if self.tree_size == 0: ##if the tree is empty after deletion
			self.max = None
		elif node == self.max: #tree is not empty
			self.update_max()

	"""rebalances the tree after deleting a node
	
	@type node: AVLNode
	@pre: node is a parent of a deleted node
	"""
	#time complexity: O(log(n))
	
	def rebalance_delete(self,node): 
		while node is not None:
			node.fix_height()
			bf = node.get_balance_factor()
			if abs(bf) > 1:
				self.rotate(node)
			node = node.get_parent()

	"""replaces a node with his one son
	
	@type old_node: AVLNode
	@type new_node: AVLNode
	"""
	#time complexity: O(1)

	def replace_node_delete(self, old_node, new_node):
		parent = old_node.get_parent()
		if parent is None: #old node is the root
			self.root = new_node
			if new_node.is_real_node():
				new_node.set_parent(None)
		else: #old node is not the root
			if parent.get_left() == old_node:
				parent.set_left_with_parent(new_node)
			else:
				parent.set_right_with_parent(new_node)

	"""updates the max pointer by searching the tree
	
	@post: the max pointer points to the node with the highest key in the tree, or None if the tree is empty
	"""
	# time complexity: O(log(n))

	def update_max(self): 
		if self.root is None: #the tree is empty, has no max
			self.max = None
			return None
		currentNode = self.root #tree is not empty, going the last right child
		while currentNode.get_right().is_real_node():
			currentNode = currentNode.get_right()
		self.max = currentNode

	"""return the successor of node in case it has a right subtree

		@type node: AVLNode
		@pre: node is a real pointer to a node in self
		@rtype: AVLNode
		@returns: the successor of node, None if node has the max key
		"""

	# time complexity O(log(n))

	def successor(self,node): #method for case 3 of delete, so we know there is a right child
		temp = node.get_right()
		while temp.get_left().is_real_node():
			temp = temp.get_left()
		return temp
	
	"""joins self with item and another AVLTree

	@type tree2: AVLTree 
	@param tree2: a dictionary to be joined with self
	@type key: int 
	@param key: the key separting self and tree2
	@type val: string
	@param val: the value corresponding to key
	@pre: all keys in self are smaller than key and all keys in tree2 are larger than key,
	or the opposite way
	"""
	# time complexity: O(|h1-h2|)

	def join(self, tree2, key, val):
		#edge cases
		if self.root is None or self.root.get_key() is None: #self is an empty tree
			#insert x to tree2 and update self to be tree2
			tree2.insert(key,val)
			self.root = tree2.get_root()
			self.tree_size = tree2.size()
			self.max = tree2.max_node()
			return None

		if tree2.get_root() is None or tree2.get_root().get_key() is None: #tree2 is an empty tree
			#insert x to self
			self.insert(key,val)
			return None

		size1 = self.tree_size
		size2 = tree2.size()  # tree sizes before mutating trees
		x = AVLNode(key, val)  # node "separating" trees

		if self.root.get_key() < key: #all the keys in self are smaller than in tree2
			h1 = self.root.get_height()
			h2 = tree2.get_root().get_height()

			if h1 <= h2: #tree2 is taller or the same height as self
				#travel down left of tree2 to find connection point
				b = tree2.get_root()
				while b.get_height() > h1: 
					b = b.get_left()
				c = b.get_parent()
				#now, b is of height h1 or h1 - 1, c is of height h1 + 1 or h1 + 2
				#join trees through x
				x.set_left_with_parent(self.root)
				x.set_right_with_parent(b)
				x.fix_height()
				if c is not None: #if b is not the root of tree2
					c.set_left_with_parent(x)

			else: #self is taller than tree2
				#travel down right of tree2 to find connection point
				b = self.get_root()
				while b.get_height() > h2: 
					b = b.get_right()
				c = b.get_parent()
				#now, b is of height h1 or h1 - 1, c is of height h1 + 1 or h1 + 2
				#join trees through x
				x.set_right_with_parent(tree2.get_root())
				x.set_left_with_parent(b)
				x.fix_height()
				#b cannot be the root of tree2, it's height is lower
				c.set_right_with_parent(x)

			self.root = tree2.get_root()
			self.tree_size = size1 + size2 + 1
			self.max = tree2.max_node()
			self.fix_root() #fixing root if needed
			self.rebalance_delete(x) #rebalancing upwards of connecting node in the same way as in delete
		
		else: #all the keys in self are larger than in tree2
			tree2.join(self, key, val) #calling the function on tree2 with self as a parameter instead
			#updating self to be tree2
			self.root = tree2.get_root()
			self.max = tree2.max_node()
			self.tree_size = tree2.get_size()

	"""splits the dictionary at a given node - wrapper function

		@type node: AVLNode
		@pre: node is in self
		@param node: the node in the dictionary to be used for the split
		@rtype: (AVLTree, AVLTree)
		@returns: a tuple (left, right), where left is an AVLTree representing the keys in the 
		dictionary smaller than node.key, and right is an AVLTree representing the keys in the 
		dictionary larger than node.key.
		"""

	# time complexity O(log(n))

	def split(self, node):
		t1, t2 = self.rec_split(node)
		t1.update_max()
		t2.update_max()
		return t1, t2

	"""splits the dictionary at a given node - recursive function

	@type node: AVLNode
	@pre: node is in self
	@param node: the node in the dictionary to be used for the split
	@rtype: (AVLTree, AVLTree)
	@returns: a tuple (left, right), where left is an AVLTree representing the keys in the 
	dictionary smaller than node.key, and right is an AVLTree representing the keys in the 
	dictionary larger than node.key.
	"""
	# time complexity O(log(n))
	
	def rec_split(self, node):
		if node.get_key() == self.root.get_key(): #split on root
			return (AVLTree(self.root.get_left(), self.root.get_left(), 0),
					AVLTree(self.root.get_right(), self.root.get_right(), 0))

		#subtrees of root
		currLeft = AVLTree(self.root.get_left(), self.root.get_left(), 0)
		currRight = AVLTree(self.root.get_right(), self.root.get_right(), 0)

		if node.get_key() < self.root.get_key(): #split on left subtree
			lLeft, lRight = currLeft.split(node) #recursivly splitting left subtree
			#joining larger keys subtrees with root inbetween
			lRight.join(currRight, self.root.get_key(), self.root.get_value()) 
			return lLeft, lRight

		else: #split on right subtree
			rLeft, rRight = currRight.split(node) #recursivly splitting right subtree
			#joining smaller keys subtrees with root inbetween
			rLeft.join(currLeft, self.root.get_key(), self.root.get_value()) 
			return rLeft, rRight

	"""returns an array representing the dictionary 

	@rtype: list
	@returns: a sorted list according to key of tuples (key, value) representing the dictionary
	"""
	# time complexity: O(n)

	def avl_to_array(self):
		arr = []
		self.avl_to_array_rec(self.root, arr)
		return arr

	"""returns an array representing the dictionary, recursive
	
	@type node: AVLNode
	@:param node: the current node being traversed
	type result: list
	@:param result: list to store the in-order traversal
	"""
	# time complexity O(n)

	def avl_to_array_rec(self, node, arr):
		if node and node.is_real_node(): #node is a real node
			self.avl_to_array_rec(node.get_left(), arr)
			arr.append((node.get_key(), node.get_value()))
			self.avl_to_array_rec(node.get_right(), arr)
	
	"""returns the node with the maximal key in the dictionary

	@rtype: AVLNode
	@returns: the maximal node, None if the dictionary is empty
	"""
	#complexity: O(1)

	def max_node(self):
		return self.max 

	"""returns the number of items in dictionary 

	@rtype: int
	@returns: the number of items in dictionary 
	"""
	#complexity: O(1)

	def size(self):
		return self.tree_size

	"""returns the root of the tree representing the dictionary

	@rtype: AVLNode
	@returns: the root, None if the dictionary is empty
	"""
	#complexity: O(1)

	def get_root(self):
		return self.root