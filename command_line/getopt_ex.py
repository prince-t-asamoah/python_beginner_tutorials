import getopt, sys

argument_list = sys.argv[1:]
short_options = "hmo:"

long_options = ['Help', 'My_file', 'Output=']

try:
    arguments, values = getopt.getopt(args=argument_list, shortopts=short_options, longopts=long_options)
    
    for current_arg, current_value in arguments:
        if current_arg in ('-h', '--Help'):
            print("Displaying Help")
        elif current_arg in ('-m', '--My_file'):
            print('Displaying file_name:', sys.argv[0])
        elif current_arg in ('-o', '--Output'):
            print(("Enabling special output mode (% s)") % (current_value))
except getopt.error as error:
    print(str(error))
