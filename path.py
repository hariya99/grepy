
class Path:
    '''
       get the path, grab all the files in that path  
    '''

    def __init__(self, in_path=''):
        self.in_path = in_path
        self.file_list = []
        if self.in_path:
            self.validate_path()
        else:
            self.get_cwd()
       
    
    def get_cwd(self):
        self.in_path = os.getcwd()

    
    def validate_path(self):
        pass

    def list_dir(self):
        print(os.listdir(path=self.in_path))

    def scan_dir(self):
        '''it performs better than list_dir '''
        with os.scandir(self.in_path) as f:
            for entry in f:
                if not entry.name.startswith('.') and entry.is_file():
                    self.file_list.append(entry.name)


    def __str__(self):
        return self.in_path
        


if __name__ == "__main__":
    import os 
    import sys 
    if len(sys.argv) == 2:
        get_path = str(sys.argv[1])
        test_path = Path(get_path)
        print(test_path)
        test_path.scan_dir()
        print(test_path.file_list)
    else:
        print("please provide the path name or '.' if CWD")
        print(sys.argv)