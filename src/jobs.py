from functools import lru_cache


# nome,cidade,telefone
# Ana,Curitiba,1111111
# Bernardo,Santos,999999

#   [
#     {"nome": "Ana", "cidade": "Curitiba", "telefone": "1111111"},
#     {"nome": "Bernardo", "cidade": "Santos", "telefone": "999999"}
#   ]


@lru_cache
def read(path):
    """Reads a file from a given path and returns its contents

    Parameters
    ----------
    path : str
        Full path to file

    Returns
    -------
    list
        List of rows as dicts
    """
    return []
