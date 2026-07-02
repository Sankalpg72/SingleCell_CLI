from pathlib import Path 
import scanpy as sc 

# Checks if the input path exists , if Exists matches the subfolder with defined pattern, if matched , return the subfolder 
def load_data(input_path : Path ) -> sc.AnnData : 
   
    """
    Search for files or Directory inside input_path.
    
   | ------------|
   | Parameters: |
   | ------------|
   
    input_path : Path object
        Parent directory to search in.

    input_path : is file : suffix == .h5ad or .h5 -> Load, else return error
            : is dir : check the files inside it , if they matches .mtx and .tsv then load it , else return error 
    """

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
        try: 
            return sc.read_10x_mtx(input_path)
        except ValueError : 
            pass

        
    # if input_path.is_dir():
        
    #     matrix = None 
    #     barcodes = None 
    #     features = None

    #     for i in input_path.iterdir():
    #         if i.is_file():
    #             if i.name.endswith('.mtx'):
    #                 matrix = i
    #             elif i.name.endswith('barcodes.tsv'):
    #                 barcodes = i 
    #             elif i.name.endswith('features.tsv'):
    #                 features = i
    #     if matrix and barcodes and features : 
    #         return sc.read_10x_mtx(input_path)
        
    #     raise ValueError("Cannot find the .mtx/.mtx.gz and .tsv files.")
        
    

