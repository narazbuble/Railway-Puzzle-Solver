
from itertools import combinations

# Enam jenis potongan rel
TRACK_TYPES = {
    "1": ("┌", "Belokan kiri atas"),
    "2": ("┐", "Belokan kanan atas"),
    "3": ("└", "Belokan kiri bawah"),
    "4": ("┘", "Belokan kanan bawah"),
    "5": ("─", "Rel horizontal"),
    "6": ("│", "Rel vertikal")
}


def solve_puzzle(rows, cols, horizontal, vertical, hints):
    grid = [[0 for _ in range(cols)] for _ in range(rows)]
    explored_states = 0

    fixed_hints = {}

    # Memasukkan hint ke grid
    for (r, c), symbol in hints.items():
        grid[r][c] = symbol
        fixed_hints[(r, c)] = symbol

    col_count = [0] * cols

    for r, c in hints:
        col_count[c] += 1

    # Memeriksa jumlah hint
    for r in range(rows):
        if sum(1 for c in range(cols) if grid[r][c] != 0) > horizontal[r]:
            return None, explored_states

    if any(col_count[c] > vertical[c] for c in range(cols)):
        return None, explored_states

    def backtrack(row):
        nonlocal explored_states
        explored_states += 1

        if row == rows:
            return col_count == vertical

        fixed = [
            c for c in range(cols)
            if grid[row][c] != 0
        ]

        available = [
            c for c in range(cols)
            if grid[row][c] == 0
        ]

        needed = horizontal[row] - len(fixed)

        if needed < 0 or needed > len(available):
            return False

        for selected in combinations(available, needed):

            for c in selected:
                grid[row][c] = "■"
                col_count[c] += 1

            remaining_rows = rows - row - 1

            valid = all(
                col_count[c] <= vertical[c]
                and col_count[c] + remaining_rows >= vertical[c]
                for c in range(cols)
            )

            if valid and backtrack(row + 1):
                return True

            # Membatalkan pilihan jika tidak valid
            for c in selected:
                grid[row][c] = 0
                col_count[c] -= 1

        return False

    if backtrack(0):
        return grid, explored_states

    return None, explored_states


# ==================================
# INPUT PROGRAM
# ==================================

print("=== RAILWAY PUZZLE SOLVER ===")

rows = int(input("Jumlah baris: "))
cols = int(input("Jumlah kolom: "))

horizontal = list(map(int, input(
    "Angka horizontal: "
).split()))

vertical = list(map(int, input(
    "Angka vertikal: "
).split()))

if rows <= 0 or cols <= 0:
    print("Ukuran grid harus positif.")

elif len(horizontal) != rows or len(vertical) != cols:
    print("Jumlah angka tidak sesuai ukuran grid.")

elif (
    any(x < 0 or x > cols for x in horizontal)
    or any(x < 0 or x > rows for x in vertical)
):
    print("Target jumlah rel tidak valid.")

elif sum(horizontal) != sum(vertical):
    print("Tidak ada solusi: total horizontal dan vertikal berbeda.")

else:
    hint_count = int(input("Jumlah hint (0 jika tidak ada): "))

    hints = {}
    valid_input = True

    if hint_count < 0 or hint_count > rows * cols:
        print("Jumlah hint tidak valid.")
        valid_input = False

    for i in range(hint_count):
        if not valid_input:
            break

        print(f"\n=== HINT {i + 1} ===")

        r = int(input("Baris: ")) - 1
        c = int(input("Kolom: ")) - 1

        if not (0 <= r < rows and 0 <= c < cols):
            print("Posisi hint tidak valid.")
            valid_input = False
            break

        if (r, c) in hints:
            print("Posisi hint sudah digunakan.")
            valid_input = False
            break

        print("\nPilih jenis rel:")

        for key, (symbol, name) in TRACK_TYPES.items():
            print(f"{key}. {symbol} - {name}")

        choice = input("Jenis rel (1-6): ")

        if choice not in TRACK_TYPES:
            print("Pilihan jenis rel tidak valid.")
            valid_input = False
            break

        symbol, name = TRACK_TYPES[choice]
        hints[(r, c)] = symbol

        print(f"Hint disimpan: {symbol} ({name})")

    if valid_input:
        result, states = solve_puzzle(
            rows, cols, horizontal, vertical, hints
        )

        print("\n=== HASIL PUZZLE ===")

        if result is not None:
            for row in result:
                print(" ".join(
                    str(cell) if cell != 0 else "·"
                    for cell in row
                ))

            print("\nSolusi ditemukan!")
        else:
            print("Tidak ditemukan solusi.")

        print("Jumlah state dieksplorasi:", states)
