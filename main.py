import json

LINE_LENGTH = 60


def produce_latex(input_file, output_file):
    # Open crew file
    with open(input_file) as json_file:
        crew = json.load(json_file)

    # Begin latex string
    final_str = '\\begin{equation}\\color{RedOrange}\\begin{align}\\begin{split}'

    for role in crew:
        # Prepare role
        role_str = '\\ '.join(role.split())
        # Create dots string
        case_len = len(max((crew[role]), key=len)) if isinstance(crew[role], list) else len(crew[role])
        dots_num = LINE_LENGTH - len(role) - case_len
        assert dots_num > 0, 'Length not supported!'
        dots = '.' * dots_num
        # Create cases string
        if isinstance(crew[role], list):
            cases = '\\begin{cases}'
            for entry in crew[role]:
                cases += '\\ '.join(entry.split()).upper() + '\\\\'
            cases += '\\end{cases}\\\\'
        else:
            cases = '\\ '.join(crew[role].split()).upper() + '\\\\'
        # Create final string
        final_str += '&' + role_str + '&' + dots + '&' + cases

    # Finalize latex string
    final_str += '\\end{split}\\end{align}\\end{equation}'

    # Save result in file
    with open(output_file, 'w') as file:
        file.write(final_str)


if __name__ == "__main__":
    produce_latex('files/crew.json', 'files/ouatih.txt')