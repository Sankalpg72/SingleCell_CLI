import typer 
from singlecell.core.logger import logger
from pathlib import Path
from typing import Annotated
import sys
import time 
from singlecell.io.loader import load_data

app = typer.Typer()

# RUN Command 
@app.command()
def run(input_path : Annotated[ Path , typer.Option(...,'-i','--input',exists =  True , help='Path to input file (.h5ad or .h5) or directory (10x mtx dir)')],
        config : Annotated[str, typer.Option('-c','--config',help = 'Input your custom configs in YAML format.' )] = ''):
    '''Run the whole pipeline at once. '''
    
    if input_path:
        logger.info(f"Loading data from {input}")
        adata = load_data(input_path)
        logger.info(f"Loaded AnnData: {adata.shape[0]} cells x {adata.shape[1]} genes")



    return 

@app.command()
def qc():
    logger.info('QC in Progress ')
    time.sleep(2)


if __name__ == '__main__':
        app()