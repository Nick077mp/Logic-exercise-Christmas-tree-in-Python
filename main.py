def christmas_tree(input_value):
    # Determine the central position for the trunk
    up = input_value // 2

    # Loop through each level of the tree
    for i in range(1, input_value + 2):
        # Initialize the line with spaces
        line = [" " for _ in range(input_value)]
        
        # Place the trunk in the center
        line[up] = "*"  

        # Add branches to the tree
        if i <= up + 1:    
            # Loop to place the branches on both sides of the trunk
            for j in range(1, i):
                # Ensure we don't go out of bounds on the left
                if up - j >= 0:
                    line[up - j] = "*"
                # Ensure we don't go out of bounds on the right
                if up + j < input_value:
                    line[up + j] = "*"

        # Print the current line of the tree
        print("".join(line))

# Test the function with an odd number
christmas_tree(15)
