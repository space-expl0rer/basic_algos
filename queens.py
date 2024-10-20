#prints all possible positionings of N queens on N*N chess board
def print_it(table):
    for i in range(len(table[0])):
        for j in range(len(table[0])):
            if table[i][j] == -1:
                print('#', end=' ')
            else:
                print('o', end=' ')
        print()
    print()

def draw_lava_cells(table, cur, i, n):
    lvl = 1
    for j in range(cur + 1, n):
        table[j][i] += 1
        if i - lvl > -1:
            table[j][i - lvl] += 1
        if i + lvl < n:
            table[j][i + lvl] += 1
        lvl += 1

def erase_lava_cells(table, cur, i, n):
    lvl = 1
    table[cur][i] = 0
    for j in range(cur + 1, n):
        table[j][i] -= 1
        if i - lvl > -1:
            table[j][i - lvl] -= 1
        if i + lvl < n:
            table[j][i + lvl] -= 1
        lvl += 1

def walker(cur, n, table):
    if cur == n:
        print_it(table)
        return
    for i in range(n):
        if table[cur][i] == 0:
            draw_lava_cells(table, cur, i, n)
            table[cur][i] = -1
            walker(cur + 1, n, table)
            erase_lava_cells(table, cur, i, n)
def main():
    n = int(input())
    table = [[0 for _ in range(n)] for _ in range(n)]
    walker(0, n, table)
main()


