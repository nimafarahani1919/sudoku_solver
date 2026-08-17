def sudoku_printer(sudoku):
    for i, row in enumerate(sudoku):
        print(
            " | ".join(
                f"{str(cell):^15}"
                for cell in row[:3]
            ),
            "||",
            " | ".join(
                f"{str(cell):^15}"
                for cell in row[3:6]
            ),
            "||",
            " | ".join(
                f"{str(cell):^15}"
                for cell in row[6:]
            )
        )

        if i in [2, 5]:
            print("=" * 153)
        else:
            print("-" * 153)