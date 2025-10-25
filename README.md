# AVL Balanced Tree - Data Structures Project
This project contains a practical implementation of an AVL tree according to the definitions taught in class, using Python 3.13.  
I focused on developing the necessary rotation mechanisms and height maintenance to guarantee the critical $O(\log n)$ W.C time complexity for all dictionary operations.  
Beyond the standard dictionary operations insert/search/delete, I implemented complex structural operations like finger search, join and split.   

### Key Requirements

* Each item has a **value** and an integer **key**. All keys are distinct, and the order of nodes is based solely on the keys.
* The implementation uses **virtual nodes** (nodes without a key) as children for all real leaves.
* no library implementation of a data structure is used.
* All operations are implemented with **optimal asymptotic complexity.**

#### Class `AVLNode`:

| Field | Description |
| :--- | :--- |
| `key` | int, The integer key of the node. |
| `value` | string, The value of the node. |
| `left` | AVLNode, Pointer to the left child. |
| `right` | AVLNode, Pointer to the right child. |
| `parent` | AVLNode, Pointer to the parent of the node. |
| `height` | int, The height of the node. |
| `is_real_node()` | Returns `TRUE` if the node represents a real node in the tree (not virtual). |   


| Method | Description | Time Complexity |
| :--- | :--- | :--- |
| **`__init__(key, value)`** | Constructor | $O(1)$ |
| **`is_real_node()`** | returns whether self is not a virtual node  | $O(1)$ |
| **`get_left()`** |returns the left child | $O(1)$ |
| **`get_right()`** | returns the right child | $O(1)$ |
| **`get_parent()`** | returns the parent | $O(1)$ |
| **`get_key()`** | returns the key | $O(1)$ |
| **`get_value()`** | returns the value | $O(1)$ |
| **`get_height()`** | returns the height | $O(1)$ |
| **`set_left(node)`** |sets the left child | $O(1)$ |
| **`set_right(node)`** | sets the right child | $O(1)$ |
| **`set_parent(node)`** | sets the parent | $O(1)$ |
| **`set_key(key)`** | sets the key | $O(1)$ |
| **`set_value(value)`** | sets the value | $O(1)$ |
| **`set_height(h)`** | sets the height | $O(1)$ |
| **`calc_height()`** | calculates the height of node according to children | $O(1)$ |
| **`fix_height()`** | fixes the height of node according to children, if node is not virtual | $O(1)$ |
| **`get_balance_factor()`** | returns the balance factor of a node if it is not virtual | $O(1)$ |
| **`set_right_with_parent(node)`** | sets node as the right child of self and sets node's parent as self | $O(1)$ |
| **`set_left_with_parent(node)`** | sets node as the left child of self and sets node's parent as self | $O(1)$ |


#### Class `AVLTree`:

| Field | Description |
| :--- | :--- |
| `root` | AVLNode, The root of the tree. |
| `max` | AVLNode, pointer to the node with the maximum value in the tree. |
| `tree_size` | int, the number of nodes in the tree. |


| Method | Description | Time Complexity |
| :--- | :--- | :--- |
| **`search(key)`** | searches for a node in the dictionary corresponding to the key (starting at the root) | $O(\log n)$ |
| **`finger_search(key)`** | searches for a node in the dictionary corresponding to the key, starting at the max | $O(\log n)$ |
| **`insert(key, val)`** | inserts a new node into the dictionary with the corresponding key and value (starting at the root) | $O(\log n)$ |
| **`rebalance(node)`** | rebalances AVL tree after insertion | $O(\log n)$ |
| **`rotate(node)`** | rotates tree around node with an invalid balance factor | $O(1)$ |
| **`right_rotate(node)`** | rotates edge between node and left child to right | $O(1)$ |
| **`left_rotate(node)`** | rotates edge between node and right child to left | $O(1)$ |
| **`finger_insert(key, val)`** | inserts a new node into the dictionary with corresponding key and value, starting at the max | $O(\log n)$ |
| **`fix_root()`** | fixes the root of the tree if the root has a new father | $O(\log n)$ |
| **`delete(node)`** | rebalances the tree after deleting a node | $O(\log n)$ |
| **`rebalance_delete(node)`** | deletes node from the dictionary | $O(\log n)$ |
| **`replace_node_delete(node)`** | replaces a node with his one son | $O(1)$ |
| **`update_max()`** | updates the max pointer by searching the tree | $O(1)$ |
| **`successor(node)`** | return the successor of node in case it has a right subtree | $O(\log n)$ |
| **`join(tree2, key, val)`** | joins self with item and another AVLTree | $O(h1 - h2)$ |
| **`split(node)`** | splits the dictionary at a given node - wrapper | $O(\log n)$ |
| **`rec_split(node)`** | splits the dictionary at a given node - recursive | $O(\log n)$ |
| **`avl_to_array()`** | returns an array representing the dictionary - wrapper | $O(n)$ |
| **`avl_to_array_rec()`** | returns an array representing the dictionary - recursive | $O(n)$ |
| **`max_node()`** | returns the node with the maximal key in the dictionary | $O(1)$ |
| **`size()`** | returns the number of items in the dictionary  | $O(1)$ |
| **`get_root()`** | returns the root of the tree representing the dictionary | $O(1)$ |
