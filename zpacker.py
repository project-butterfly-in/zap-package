import lzma
import os
from sys import argv, platform
import pack

def usage():
    print("Usage: zpacker [option (optional *if available)] <command> <source> [destination (optional)]")

def availableCommands():
    commands_list = """List of available commands:
    1. pack - to create .zpackage & .zpakref for an application
    2. unpack - to unpack .zpackage file.
    """
    
    print(commands_list)

def main():
    # This part to obtain extra optional args like verbose, help, etc
    extra_args = 0
    option_args = ""
    if (len(argv) > 4):
        extra_args = len(argv) - 4
        i = 0
        while i < extra_args and i < len(argv):
            option_args = option_args + argv[i+1]
            i+=1
        option_args = ''.join(option_args.split('-')).lower()

    # To obtain command, source and destination arguments
    # TODO: Maybe this shouldn't be handled here. Move to pack.py.
    command = argv[1 + extra_args]
    source_dir = argv[2 + extra_args]
    try:
        destination = argv[3 + extra_args]
    except IndexError as e:
        destination = os.getcwd()
    if command == None or source_dir == None:
        usage()
        raise SystemExit
    else:
        ## Getting bools from option_args
        doVerbose = "v" in option_args 
        ## Executing options
        if command == 'pack':
            if os.path.isdir(source_dir) or os.path.isdir(destination):
                print('Creating package\n...')
                pack.Packer(command, source_dir, destination, verbose=doVerbose)
            else:
                raise NotADirectoryError("Source or destination directory doesn't exists")
        else:
            print("No such command exists.")
            availableCommands()
            exit()

if __name__ == '__main__':
    main()
