from pathlib import Path 
import scanpy as sc 

def load_data(input_path : str ) -> sc.AnnData : 

    input_path = Path(str)

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
        return sc.read_10x_mtx(input_path)
    
    raise ValueError(f"Input path is neither a file nor a directory: {input_path}")
    



# # Checks if the input path exists , if Exists matches the subfolder with defined pattern, if matched , return the subfolder 
# """
# Search for the first matching subfolder inside input_path.

# Parameters: 
# ----------
# input_path : str
#     Parent directory to search in.
# patterns : list[str]
#     Folder names to look for.

# Returns:
# --------
# Path | None
# Path to the matching subfolder, or None if not found.

# """
# def check_path(input_dir : str, patterns: list[str] ) -> Path | None :    
#     dir_path = Path(input_dir)

#     if dir_path.exists():
#         for subfolder in dir_path.iterdir():
#             if not subfolder.is_dir():
#                 continue

#             for pattern in patterns : 
#                 if subfolder.match(pattern):
#                     return subfolder
                
            
#     return None

