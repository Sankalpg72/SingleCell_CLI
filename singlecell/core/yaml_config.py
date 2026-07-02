from pathlib import Path
import yaml 

# Load config file 
def load_config(config_path : str): 

    config_path = Path(config_path)

    if not config_path.exists():
        raise FileNotFoundError('Config file cannot be found , please enter correct path ! ')
    
    if config_path.is_file():
        if config_path.suffix == '.yaml':
            with open(config_path, 'r') as f:
                config = yaml.safe_load(f)
                '''
                yaml.load(f): Can trigger malicious code if an attacker modifies your config file.
                yaml.safe_load(f): Restricts parsing to basic, safe types (dicts, lists, strings, numbers). It blocks code execution completely.
                '''
                print("Config Loaded !")
                return config
        else: 
            raise ValueError(f"Wrong file Type , Expected .yaml file")