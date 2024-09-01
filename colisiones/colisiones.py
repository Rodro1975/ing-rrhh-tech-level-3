def f(sequence: str) -> str:
    n = len(sequence)
    collisions = [0] * n
    robots = list(sequence)

    # Simulate movements and collisions
    while True:
        changes = False
        new_robots = robots.copy()

        # Detect collisions and change directions
        for i in range(n - 1):
            if robots[i] == 'R' and robots[i + 1] == 'L':
                collisions[i] += 1
                collisions[i + 1] += 1
                new_robots[i], new_robots[i + 1] = 'L', 'R'  # Cambiar direcciones
                changes = True

        robots = new_robots
        
        # If there are no more changes, break the cycle
        if not changes:
            break

    return ' '.join(map(str, collisions))

# Example of use
print(f('LR'))  # Output: '0 0'
print(f('RL'))  # Output: '1 1'
print(f('RRR'))  # Output: '0 0 0'
print(f('RRL'))  # Output: '1 2 1'


