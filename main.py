"""
The catabase is composed of one data file per user defined type
and one or more index files for each one of those data files.
(append only preferred)
"""

from enum import Enum

user_types = dict()
data_files = dict()

class DType(Enum):
    BOOL = 1
    UINT8 = 2
    UINT32 = 3
    UINT64 = 4

def is_dtype(val: int, dtype: DType) -> bool:
    match dtype:
        case DType.BOOL:
            return 0 <= val < 2
        case DType.UINT8:
            return 0 <= val < 2**3
        case DType.UINT32:
            return 0 <= val < 2**5
        case DType.UINT64:
            return 0 <= val < 2**6

def create_type(name: str, tdef: dict[str, DType]) -> int:
    if user_types.get(name):
        return -1
    user_types[name] = tdef
    create_data_file(name, tdef)
    return 0

def create_data_file(name: str, tdef: dict[str, DType]) -> int:
    with open(f"{name}_data.bdg", "wb"):
        # margaret toucher
        pass


def save_obj(tname: str, obj: dict) -> int:
    utype = user_types.get(tname)
    if not utype:
        return -1
    for k, v in obj.items():
        if not is_dtype(v, utype[k]):
            return -1
    return 0

def create_index_file():
    # TODO
    pass
