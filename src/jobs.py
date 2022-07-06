from functools import lru_cache
import csv


# nome,cidade,telefone
# Ana,Curitiba,1111111
# Bernardo,Santos,999999

#   [
#     {"nome": "Ana", "cidade": "Curitiba", "telefone": "1111111"},
#     {"nome": "Bernardo", "cidade": "Santos", "telefone": "999999"}
#   ]

# https://app.betrybe.com/course/computer-science/introducao-a-python/entrada-e-saida-de-dados/105dc022-72fa-425f-a452-29b3595bb64d/conteudos/0463c6a9-e3c8-4fe0-aa61-34b41dd0fc33/manipulando-arquivos-csv/89e369f1-a938-4cbb-a84e-d398e253174c?use_case=side_bar
# https://stackoverflow.com/questions/46416570/how-to-format-a-list-of-dictionaries-from-csv-python
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
    with open(path, encoding="utf8") as file:
        file_reader = csv.reader(file, delimiter=",", quotechar='"')
        # Usando o conceito de desempacotamento
        header, *data = file_reader

    return [dict(zip(header, index)) for index in data]
