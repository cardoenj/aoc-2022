tree_matrix = []
import numpy as np

with open("day_eight/input.dat") as fp:
    tree_matrix = fp.read().splitlines()

tree_matrix = [list(map(int, x)) for x in tree_matrix]
tree_np = np.array(tree_matrix)
visibility_grid = np.zeros_like(tree_np)
scenic_scores = np.ones_like(tree_np)
# rotate the matrix 4 times
for rot in range(4):
    for (x, y), _ in np.ndenumerate(tree_np):
        tree_is_lower = [t < tree_np[x, y] for t in tree_np[x, y + 1 :]]
        has_boundaries = [i + 1 for i, n in enumerate(tree_is_lower) if ~n]
        if not has_boundaries:
            scenic_scores[x, y] *= len(tree_is_lower)
        else:
            scenic_scores[x, y] *= has_boundaries[0]

        if all(tree_is_lower):
            visibility_grid[x, y] = 1

    tree_np, visibility_grid, scenic_scores = map(
        np.rot90, [tree_np, visibility_grid, scenic_scores]
    )

print(visibility_grid.sum())
print(scenic_scores.max())
