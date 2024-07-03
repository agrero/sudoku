from configparser import ConfigParser
import os

class SudokuConfig(ConfigParser):
    def read_config(self, verbose=False):
        for section in self.sections():
            print(section)
        
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

# make a list of every configuration thing possible in the tests file
# make 2 versions
# one for testing one for non testing
# use __setattr__(self, att, val) to use it through #
    


