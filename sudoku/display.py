def sudoku_printer(sudoku):
    lines = []

    for i, row in enumerate(sudoku):
        line = (
            " | ".join(f"{str(cell):^15}" for cell in row[:3])
            + "  ||  "
            + " | ".join(f"{str(cell):^15}" for cell in row[3:6])
            + "  ||  "
            + " | ".join(f"{str(cell):^15}" for cell in row[6:])
        )

        lines.append(line)

        if i in [2, 5]:
            lines.append("=" * 153)
        else:
            lines.append("-" * 153)

    return "\n".join(lines)