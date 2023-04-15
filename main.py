import json


LINE_LENGTH = 85


def _produce_dots(crew_dict, role):
    """
    Produces a string, with the analogous amount of dots filling the space
    between the role and its longest crew member name.
    """
    case_len = len(max((crew_dict[role]), key=len)) if isinstance(
        crew_dict[role], list) else len(crew_dict[role])
    dots_num = LINE_LENGTH - len(role) - case_len
    assert dots_num >= 0, 'Error in dots calculation(less than zero)!'
    return '.' * dots_num


def _produce_cases(crew_dict):
    """
    Produces the main body Latex string, containing cases. Cases are the
    groupings of roles with their corresponding crew members.
    """
    cases_str = ''
    for role in crew_dict:
        # Prepare role
        role_str = '\\ '.join(role.split())
        # Create dots string
        dots = _produce_dots(crew_dict, role)
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


def produce_latex(crew_dict, full_doc=False):
    """
    Produces the final document or equation, by wrapping the cases with
    appropriate Latex start/end.
    """

    assert isinstance(crew_dict, dict), 'Error, unsupported argument type!'

    latex_start = ('\\documentclass{report}\\usepackage{color}\\pagecolor{black}'
                   '\\usepackage{amsmath}\\begin{full_doc}' if full_doc else '') \
                  + '\\begin{equation}\\color{yellow}\\begin{align}\\begin{split}'
    latex_end = '\\end{split}\\end{align}\\end{equation}' + \
                ('\\end{full_doc}' if full_doc else '')

    return latex_start + _produce_cases(crew_dict) + latex_end


if __name__ == "__main__":
    # Open default crew location
    with open('files/crew.json') as json_file:
        crew = json.load(json_file)

    # Transform
    final_str = produce_latex(crew, full_doc=True)

    # Save result in default location
    with open('files/output.tex', 'w') as file:
        file.write(final_str)