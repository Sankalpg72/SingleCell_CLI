from pathlib import Path 
import scanpy as sc 

def load_data(input_path : Path ) -> sc.AnnData : 

    input_path = Path(input_path)

    if not input_path.exists():
        raise FileNotFoundError("Input path not found ! ")

    if input_path.is_file():
        if input_path.suffix == '.h5ad':
            return sc.read_h5ad(input_path)
        elif input_path.suffix == '.h5':
            return sc.read_10x_h5(input_path)
        else: 
            raise FileExistsError("No File exists.")

    if input_path.is_dir():
        for i in input_path:
            if i.is_file() and i.suffix in ['.mtx','.tsv','.csv']: 
                return sc.read_10x_mtx(input_path)
    
    raise ValueError(f"Input path is neither a file nor a directory: {input_path}")
    

# Checks if the input path exists , if Exists matches the subfolder with defined pattern, if matched , return the subfolder 
"""
Search for the first matching subfolder inside input_path.

Parameters: 
----------
input_path : Path object
    Parent directory to search in.

input_path : is file : suffix == .h5ad or .h5 -> Load, else return error
           : is dir : load it 
Returns:
--------
Path | None
Path to the matching subfolder, or None if not found.

"""
