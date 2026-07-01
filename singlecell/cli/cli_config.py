import typer 
from singlecell.core.logger import logger
from pathlib import Path
from typing import Annotated
import sys
import time 
from singlecell.io.loader import 

app = typer.Typer()


# RUN Command 
@app.command()
def run(
        input : Annotated[str ,typer.Option('-i','--input',help='Input Your Data (mtx dir / .h5ad / .h5 )'), typer] 
):
    '''
    Load your data 
    '''
    return 

@app.command()
def qc():
    logger.info('QC in Progress ')
    time.sleep(2)


if __name__ == '__main__':
        app()