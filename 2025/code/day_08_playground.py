from pathlib import Path

INPUT_FILE_PATH = f"{Path(__file__).parent}/../input_files/day_08_input.txt"


class UnionFind:
    """Union-Find (Disjoint Set Union) data structure with path compression and union by rank."""
    
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.size = [1] * n
    
    def find(self, x):
        """Find the root of the set containing x with path compression."""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        """Union the sets containing x and y. Returns True if they were in different sets."""
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x == root_y:
            return False  # Already in the same set
        
        # Union by rank: attach smaller tree under larger tree
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
            self.size[root_y] += self.size[root_x]
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]
        else:
            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]
            self.rank[root_x] += 1
        
        return True
    
    def get_circuit_sizes(self):
        """Get the sizes of all circuits."""
        root_to_size = {}
        for i in range(len(self.parent)):
            root = self.find(i)
            if root not in root_to_size:
                root_to_size[root] = self.size[root]
        return list(root_to_size.values())


def part_1():
    distance_to_pairs_dict: dict[int, list[tuple[int, int]]] = dict()
    boxes_list: list[tuple[int, int, int]] = []

    # Read all boxes and compute pairwise distances
    with open(INPUT_FILE_PATH) as f:
        for line in f:
            current_box = line.strip().split(',')
            current_box_tuple = (int(current_box[0]), int(current_box[1]), int(current_box[2]))
            
            for idx, box in enumerate(boxes_list):
                distance_squared = (
                    pow(current_box_tuple[0] - box[0], 2) +
                    pow(current_box_tuple[1] - box[1], 2) +
                    pow(current_box_tuple[2] - box[2], 2)
                )
                if distance_squared in distance_to_pairs_dict:
                    distance_to_pairs_dict[distance_squared].append((idx, len(boxes_list)))
                else:
                    distance_to_pairs_dict[distance_squared] = [(idx, len(boxes_list))]
            
            boxes_list.append(current_box_tuple)

    # Sort distances in ascending order
    distance_to_pairs_dict = dict(sorted(distance_to_pairs_dict.items()))
    
    # Initialize Union-Find with one set per junction box
    uf = UnionFind(len(boxes_list))
    
    # Connect the 1000 closest pairs
    handled_pairs = 0
    for _, list_of_pairs in distance_to_pairs_dict.items():
        for idx1, idx2 in list_of_pairs:
            uf.union(idx1, idx2)
            handled_pairs += 1
            
            if handled_pairs == 1000:
                break
        
        if handled_pairs == 1000:
            break

    # Get circuit sizes and multiply the three largest
    circuit_sizes = sorted(uf.get_circuit_sizes(), reverse=True)
    result = circuit_sizes[0] * circuit_sizes[1] * circuit_sizes[2]
    
    print(result)
    

if __name__ == "__main__":
    part_1()