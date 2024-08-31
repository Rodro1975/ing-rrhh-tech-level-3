def f(sequence: str) -> str:
    n = len(sequence)
    collisions = [0] * n
    robots = list(sequence)

    # Simular movimientos y colisiones
    while True:
        changes = False
        new_robots = robots.copy()

        # Detectar colisiones y cambiar direcciones
        for i in range(n - 1):
            if robots[i] == 'R' and robots[i + 1] == 'L':
                collisions[i] += 1
                collisions[i + 1] += 1
                new_robots[i], new_robots[i + 1] = 'L', 'R'  # Cambiar direcciones
                changes = True

        robots = new_robots
        
        # Si no hay más cambios, romper el ciclo
        if not changes:
            break

    return ' '.join(map(str, collisions))

# Ejemplo de uso
print(f('LR'))  # Output: '0 0'
print(f('RL'))  # Output: '1 1'
print(f('RRR'))  # Output: '0 0 0'
print(f('RRL'))  # Output: '1 2 1'


