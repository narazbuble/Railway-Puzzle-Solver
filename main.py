
# ==================================================
# RAILWAY PUZZLE SOLVER
# Backtracking + Constraint Satisfaction Problem
# ==================================================

TRACK_TYPES = {
    "1": ("┌", {"R", "D"}, "Belokan kiri atas"),
    "2": ("┐", {"L", "D"}, "Belokan kanan atas"),
    "3": ("└", {"R", "U"}, "Belokan kiri bawah"),
    "4": ("┘", {"L", "U"}, "Belokan kanan bawah"),
    "5": ("─", {"L", "R"}, "Rel horizontal"),
    "6": ("│", {"U", "D"}, "Rel vertikal")
}

DIRECTIONS = {
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
    "R": (0, 1)
}

OPPOSITE = {
    "U": "D",
    "D": "U",
    "L": "R",
    "R": "L"
}


def inside(r, c, rows, cols):
    return 0 <= r < rows and 0 <= c < cols


def solve_puzzle(rows, cols, horizontal, vertical, hints):

    grid = [[None] * cols for _ in range(rows)]

    ports = {}
    visited = set()

    row_count = [0] * rows
    col_count = [0] * cols

    states = 0
    answer = None

    symbols = {
        symbol: connections
        for symbol, connections, name in TRACK_TYPES.values()
    }

    # Memeriksa apakah jumlah rel masih memungkinkan
    def counts_possible():
        for r in range(rows):
            remaining = sum(
                grid[r][c] is None for c in range(cols)
            )

            if row_count[r] > horizontal[r]:
                return False

            if row_count[r] + remaining < horizontal[r]:
                return False

        for c in range(cols):
            remaining = sum(
                grid[r][c] is None for r in range(rows)
            )

            if col_count[c] > vertical[c]:
                return False

            if col_count[c] + remaining < vertical[c]:
                return False

        return True

    # Memeriksa kesesuaian hint
    def hint_matches(r, c, connections):
        if (r, c) not in hints:
            return True

        return symbols[hints[(r, c)]] == connections

    # Memeriksa sambungan dengan sel yang sudah dikunjungi
    def adjacency_valid(r, c, connections, previous):

        for direction in DIRECTIONS:
            dr, dc = DIRECTIONS[direction]
            nr, nc = r + dr, c + dc

            if (nr, nc) not in visited:
                continue

            neighbor_ports = ports[(nr, nc)]

            # Sel sebelumnya harus tersambung
            if (nr, nc) == previous:
                if direction not in connections:
                    return False

                if OPPOSITE[direction] not in neighbor_ports:
                    return False

            # Tidak boleh ada sambungan tambahan
            else:
                if direction in connections:
                    return False

                if OPPOSITE[direction] in neighbor_ports:
                    return False

        return True

    def all_hints_visited():
        return all(
            position in visited
            for position in hints
        )

    # Backtracking untuk membangun jalur
    def dfs(r, c, incoming, previous):

        nonlocal states, answer
        states += 1

        # Mencoba setiap kemungkinan arah keluar
        for outgoing in DIRECTIONS:

            if outgoing == incoming:
                continue

            dr, dc = DIRECTIONS[outgoing]
            nr, nc = r + dr, c + dc

            # Titik awal harus bergerak masuk ke grid
            if previous is None and not inside(
                nr, nc, rows, cols
            ):
                continue

            connections = {incoming, outgoing}

            # Memeriksa hint
            if not hint_matches(r, c, connections):
                continue

            # Menentukan simbol rel
            symbol = next(
                (
                    s for s, p, name in TRACK_TYPES.values()
                    if p == connections
                ),
                None
            )

            if symbol is None:
                continue

            # Memasang rel sementara
            grid[r][c] = symbol
            ports[(r, c)] = connections
            visited.add((r, c))

            row_count[r] += 1
            col_count[c] += 1

            valid = (
                adjacency_valid(
                    r, c, connections, previous
                )
                and counts_possible()
            )

            if valid:

                # Jalur mencapai tepi grid
                if not inside(nr, nc, rows, cols):

                    if (
                        previous is not None
                        and all_hints_visited()
                        and row_count == horizontal
                        and col_count == vertical
                    ):
                        answer = [row[:] for row in grid]

                        return True

                # Melanjutkan jalur
                elif (nr, nc) not in visited:

                    if dfs(
                        nr,
                        nc,
                        OPPOSITE[outgoing],
                        (r, c)
                    ):
                        return True

            # Membatalkan pilihan
            row_count[r] -= 1
            col_count[c] -= 1

            visited.remove((r, c))
            del ports[(r, c)]
            grid[r][c] = None

        return False

    # Mencoba seluruh posisi awal di tepi grid
    for r in range(rows):
        for c in range(cols):

            boundary_directions = []

            if r == 0:
                boundary_directions.append("U")

            if r == rows - 1:
                boundary_directions.append("D")

            if c == 0:
                boundary_directions.append("L")

            if c == cols - 1:
                boundary_directions.append("R")

            for start_direction in boundary_directions:

                # Arah masuk dari luar grid
                if dfs(
                    r,
                    c,
                    start_direction,
                    None
                ):
                    return answer, states

    return None, states


# ==================================================
# INPUT PROGRAM
# ==================================================

print("================================")
print("      RAILWAY PUZZLE SOLVER")
print("================================")

try:

    rows = int(input("Jumlah baris: "))
    cols = int(input("Jumlah kolom: "))

    if rows <= 0 or cols <= 0:
        raise ValueError("Ukuran grid harus positif.")

    horizontal = list(map(int, input(
        "Angka horizontal: "
    ).split()))

    vertical = list(map(int, input(
        "Angka vertikal: "
    ).split()))

    if len(horizontal) != rows:
        raise ValueError("Jumlah angka horizontal tidak sesuai.")

    if len(vertical) != cols:
        raise ValueError("Jumlah angka vertikal tidak sesuai.")

    if any(x < 0 or x > cols for x in horizontal):
        raise ValueError("Angka horizontal tidak valid.")

    if any(x < 0 or x > rows for x in vertical):
        raise ValueError("Angka vertikal tidak valid.")

    if sum(horizontal) != sum(vertical):
        raise ValueError("Total horizontal dan vertikal berbeda.")

    hint_count = int(input("Jumlah hint (0 jika tidak ada): "))

    if not 0 <= hint_count <= rows * cols:
        raise ValueError("Jumlah hint tidak valid.")

    hints = {}

    for i in range(hint_count):

        print(f"\n=== HINT {i + 1} ===")

        r = int(input("Baris: ")) - 1
        c = int(input("Kolom: ")) - 1

        if not inside(r, c, rows, cols):
            raise ValueError("Posisi hint di luar grid.")

        if (r, c) in hints:
            raise ValueError("Posisi hint duplikat.")

        print("\nPilih jenis rel:")

        for key, (symbol, connections, name) in TRACK_TYPES.items():
            print(f"{key}. {symbol} - {name}")

        choice = input(
            "Jenis rel (1-6 atau simbol): "
        ).strip()

        if choice in TRACK_TYPES:
            symbol = TRACK_TYPES[choice][0]

        else:
            matching = [
                symbol
                for symbol, connections, name
                in TRACK_TYPES.values()
                if symbol == choice
            ]

            if not matching:
                raise ValueError("Jenis rel tidak valid.")

            symbol = matching[0]

        hints[(r, c)] = symbol

    # Menjalankan algoritma
    print("\nSedang mencari solusi...")

    result, states = solve_puzzle(
        rows,
        cols,
        horizontal,
        vertical,
        hints
    )

    # Menampilkan hasil
    print("\n========== HASIL PUZZLE ==========")

    if result is not None:

        for row in result:
            print(" ".join(
                cell if cell is not None else "·"
                for cell in row
            ))

        print("\nSolusi ditemukan!")

    else:
        print("Tidak ditemukan solusi yang memenuhi aturan.")

    print("Jumlah state dieksplorasi:", states)

except ValueError as error:
    print("\nInput error:", error)

except KeyboardInterrupt:
    print("\nPencarian dibatalkan.")
