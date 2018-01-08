

class Color:
    RED = 0
    GREEN = 1
    BLUE = 3
    BOLD = 4


def format_table(table_data, state_index=None):
    """Print a table with nice formatting.

    :table_data: the data of the table including headers (2D list)
    :state_index: index of the column that contains the format information
    """
    col_widths = get_max_widths(table_data)

    print separation(col_widths)
    print format_line(table_data[0], col_widths, state_index)
    print separation(col_widths)
    for line in table_data[1:]:
        print format_line(line, col_widths, state_index)
    print separation(col_widths)


def format_line(line, widths, state_index=None):
    """Format a line as in a table.

    Optionnally add a color effect to lines of the table if a column contains
    the dedicated information, and its index is passed as the second argument
    of this function.

    :line: List of cell's data
    :widths: Largest size per column
    :state_index: Indicate the cell in the line that contains the state info
    """
    result = []
    for i, cell in enumerate(line):
        result.append(' {:<{size}} '.format(cell, size=widths[i]))
    if state_index is not None:
        effect = get_effect(line[state_index])
        result = [effect(x) for x in result]
    return '|' + '|'.join(result) + '|'


def separation(width):
    return '+' + ('=' * (sum(width) + (3 * len(width) - 1))) + '+'


def get_max_widths(table):
    transposed = [list(col) for col in zip(*table)]
    return [max([len(str(cell)) for cell in col]) for col in transposed]


def get_effect(color_code):
    return {0: danger, 1: success, 3: info, 4: bold}.get(color_code, default)


def bold(txt):
    return '\033[1m' + str(txt) + '\033[0m'


def info(txt):
    return '\033[94m' + str(txt) + '\033[0m'


def success(txt):
    return '\033[92m' + str(txt) + '\033[0m'


def danger(txt):
    return '\033[91m' + str(txt) + '\033[0m'


def default(txt):
    return txt


def table_line(*columns):
    line = ""
    for col in columns:
        line += " | {:<20} | {:<20} | {}".format(columns[0], columns[1], columns[2])
