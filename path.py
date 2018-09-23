
class Path:
    '''
       get the path, grab all the files in that path  
    '''

    def __init__(self, in_path='.'):
        self.in_path = in_path
        self.file_list = []
        self.validate_path()
       
    
    def validate_path(self):
        if os.path.exists(self.in_path):    #returns True or False
            if self.in_path == '.' :
                print ('Searching in current working directory')
            else:
                print('searching for files in path %s' %self.in_path)
        else:
            print('Invalid path provided, please check the path')
            sys.exit()
        

    def scan_dir(self):
        '''scans all the files in a directory'''
        with os.scandir(self.in_path) as f:
            for entry in f:
                if not entry.name.startswith('.') and entry.is_file():
                    self.file_list.append(entry.name)


    def __str__(self):
        return self.in_path
        


if __name__ == "__main__":
    import os 
    import sys 

    #Check whether user has provided the path or not, if not then search in CWD
    if len(sys.argv) == 2:
        get_path = str(sys.argv[1])
        test_path = Path(get_path)          
    else:
        test_path = Path() 

    test_path.scan_dir()
    print(test_path.file_list)

