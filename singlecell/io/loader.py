from pathlib import Path 

# Checks if the input path exists , if Exists matches the subfolder with defined pattern, if matched , return the subfolder 
"""
Search for the first matching subfolder inside input_path.

Parameters: 
----------
input_path : str
    Parent directory to search in.
patterns : list[str]
    Folder names to look for.

Returns:
--------
Path | None
Path to the matching subfolder, or None if not found.

"""
def check_path(input_dir : str, patterns: list[str] ) -> Path | None :    
    dir_path = Path(input_dir)

    if dir_path.exists():
        for subfolder in dir_path.iterdir():
            if not subfolder.is_dir():
                continue

            for pattern in patterns : 
                if subfolder.match(pattern):
                    return subfolder
                
            
    return None

