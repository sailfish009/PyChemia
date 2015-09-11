import os
from ._incar import InputVariables
from ._poscar import write_poscar
from pychemia import Structure


def write_from_queue(queue, entry_id, destination=None):

    if destination is None:
        dest = '.'
    elif os.path.isfile(destination):
        dest = os.path.dirname(os.path.abspath(destination))
    elif not os.path.exists(destination):
        os.mkdir(destination)
        dest = destination
    elif os.path.isdir(destination):
        dest = destination
    else:
        raise ValueError('Destination not valid')

    st = queue.get_input_structure(entry_id)
    inpvars = queue.get_input_variables(entry_id)

    vi = InputVariables()
    vi.variables = inpvars

    write_poscar(st, dest + os.sep + 'POSCAR')
    vi.write(dest + os.sep + 'INCAR')

    queue.write_input_files(entry_id, dest)