def draw_christmas_tree(height):
    # Star
    print(" " * height + "⭐")

    # Tree body
    for i in range(height):
        spaces = height - i
        stars = 2 * i + 1
        print(" " * spaces + "*" * stars)

    # Trunk
    trunk_width = 3
    trunk_height = 2
    for _ in range(trunk_height):
        print(" " * (height - 1) + "|" * trunk_width)


# Call the function
draw_christmas_tree(6)
