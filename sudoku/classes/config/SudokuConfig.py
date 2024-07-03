from configparser import ConfigParser
import os

class SudokuConfig(ConfigParser):
    def __init__(self, config_path) -> None:
        super().__init__()
        self.config_path = config_path

    # how config is going to work
    # # 1) read config will 
        # .read(filepath)
        # .sections()
        # iterate over previous 
        # config[i] = dictionary #
    # # 2) write config will just take in dictionary of dictionaries
        # where each outer dictionary will be what pertains to a class
        # and there should be a training and testing variant for each. 
        # these training and testing variants will be delineated by file

    def read_config(self, verbose=False): # we should make this recursive
        self.read(self.config_path)
        for section in self.sections():
            if verbose: print(f'{section}')
            for key in self[section]:
                value = self[section][key] 
                self[section][key] = value 
                # can flip this to write
                if verbose: print(f'{key} : {value}')
    
    def add_item(self, **kwargs):
        """
        Add an item to the config object for subsequent writing
        **kwargs format: section = {key_n : value_n}
        """
        for section, key in kwargs.items():
            self[section] = key
    
    def append_item(self, **kwargs):
        self.read_config()
        self.add_item(**kwargs)
        self.write_config(self.config_path)

            
    def write_config(self, write_path):
        """
        Write an entry from a kwargs
        """
        # write configuration object to .ini file in write_path
        with open(write_path, 'w') as configfile:
            self.write(configfile)

    


config_path = os.path.join('configs', 'config.ini')
test_dict = {
    'test_key1' : 'testvalue1',
    'test_key2' : 'testvalue2'
}
addi = {
    'additional_key' : 'additionalvalue'
}
config = SudokuConfig(config_path)

config = SudokuConfig('test.ini')
config.read_config(verbose=True)
config.append_item(additional = addi)
print('round2')
config.read_config(verbose=True)