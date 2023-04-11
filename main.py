import json

LINE_LENGTH = 85


def produce_dots(crew_dict, role):
    case_len = len(max((crew_dict[role]), key=len)) if isinstance(
        crew_dict[role], list) else len(crew_dict[role])
    dots_num = LINE_LENGTH - len(role) - case_len
    assert dots_num >= 0, 'Error in dots calculation(less than zero)!'
    return '.' * dots_num


def produce_cases(crew_dict):
    cases_str = ''
    for role in crew_dict:
        # Prepare role
        role_str = '\\ '.join(role.split())
        # Create dots string
        dots = produce_dots(crew_dict, role)
        # Create cases string
        if isinstance(crew_dict[role], list):
            cases = '\\begin{cases}'
            for entry in crew_dict[role]:
                cases += '\\ '.join(entry.split()).upper() + '\\\\'
            cases += '\\end{cases}\\\\'
        else:
            cases = '\\ '.join(crew_dict[role].split()).upper() + '\\\\'
        # Create final string
        cases_str += '&' + role_str + dots + cases

    return cases_str


def produce_latex(crew_dict, document=False):
    latex_start = ('\\documentclass{report}\\usepackage{color}\\usepackage'
                   '{amsmath}\\begin{document}'if document else '') + '\\begin' \
                   '{equation}\\color{RedOrange}\\begin{align}\\begin{split}'
    latex_end = '\\end{split}\\end{align}\\end{equation}' + ('\\end{document}'
                                                             if document else '')

    return latex_start + produce_cases(crew_dict) + latex_end


if __name__ == "__main__":
    # Open default crew location
    with open('files/crew.json') as json_file:
        crew = json.load(json_file)

    # Transform
    final_str = produce_latex(crew)

    # Save result in default location
    with open('files/ouatih.tex', 'w') as file:
        file.write(final_str)