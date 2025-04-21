#clears all csv files
files=["create","findminmax","print","rebalance"]
types=["increasing","decreasing","random"]
for tree_type in ["AVL","BST"]:
    for file in files:
        for type in types:
            with open(f'benchmark_results/{tree_type}/{file}_{type}.csv', 'w') as file_csv:
                file_csv.write("file,input_size,time\n")
