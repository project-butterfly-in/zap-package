import os


class Packer():
    """
    # Class: Package

    This should be used to create, extract package, metadata & reference files for Zpak

    ## Available methods:
    - createPackage
        - To create .zpack file
    - getFileList
        - To get file list
    - extractPackage
        - To extract .zpack file
    - makeZpackref
        - To make .zpackref
    """
    def __init__(self, command, source, destination, verbose=False):
        self.command, self.source, self.destination, self.verbose = command, source, destination, verbose
        if command == 'pack':
            self.createPackage()
        elif command == 'unpack':
            pass

    def createPackage(self):
        """
        Method: createPackage()
        
        Creates an archive software package with .zpack extension
        """
        self.getFileList()


    def getFileList(self):
        listOfFiles = list()
        for (dirpath, dirnames, filenames) in os.walk(self.source):
            last_len = len(listOfFiles)

            listOfFiles += [os.path.join(dirpath, file) for file in filenames]

            # for verbose mode
            if self.verbose == True and len(listOfFiles) != last_len:
                added = len(listOfFiles) - last_len
                if added > 0:
                    for i in range(0, added):
                        print(listOfFiles[-1 * i])
        self.listOfFiles = listOfFiles
