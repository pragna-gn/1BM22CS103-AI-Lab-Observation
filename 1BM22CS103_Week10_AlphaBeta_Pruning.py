class AlphaBetaPruning:
    def __init__(self):
        self.pruned_branches = []  

    def alpha_beta(self, node, depth, alpha, beta, maximizing_player):
        """
        Perform Alpha-Beta Pruning on a given game tree.
        """
        if isinstance(node, int):
            return node

        if maximizing_player:
            max_eval = float('-inf')
            for child in node:
                eval = self.alpha_beta(child, depth - 1, alpha, beta, False)
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    self.pruned_branches.append(child)  
                    break
            return max_eval
        else:
            min_eval = float('inf')
            for child in node:
                eval = self.alpha_beta(child, depth - 1, alpha, beta, True)
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    self.pruned_branches.append(child)  
                    break
            return min_eval

    def run(self, game_tree):
        """
        Initiates Alpha-Beta pruning and records values.
        """
        alpha = float('-inf')
        beta = float('inf')
        max_value = self.alpha_beta(game_tree, float('inf'), alpha, beta, True)
        return max_value, self.pruned_branches


def construct_tree_from_leaves(leaves):
    """
    Constructs a full binary tree from the given leaf nodes.
    """
    current_level = leaves
    while len(current_level) > 1:
        next_level = []
        for i in range(0, len(current_level), 2):
            if i + 1 < len(current_level):
                next_level.append([current_level[i], current_level[i + 1]])
            else:
                next_level.append(current_level[i])  
        current_level = next_level
    return current_level[0]


def input_leaf_nodes():
    """
    Takes input for the leaf nodes of the game tree.
    """
    print("Enter the leaf nodes of the game tree separated by spaces (e.g., 3 5 6 9 1 4 7 10 11):")
    while True:
        try:
            leaves = list(map(int, input("Leaf nodes: ").split()))
            if len(leaves) >= 2:
                return leaves
            else:
                print("Please enter at least two leaf nodes.")
        except ValueError:
            print("Invalid input. Please enter integers only.")


if __name__ == "__main__":
    leaves = input_leaf_nodes()
    game_tree = construct_tree_from_leaves(leaves)

    abp = AlphaBetaPruning()
    final_max_value, pruned_branches = abp.run(game_tree)

    print(f"Final value of MAX node: {final_max_value}")
    print(f"Subtrees pruned: {pruned_branches}")
