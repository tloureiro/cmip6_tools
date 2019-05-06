import glob
from argparse import ArgumentParser

parser = ArgumentParser(description='list all nc files')

parser.add_argument("-d", "--directory", dest="directory",
                    help="directory containing nc files", metavar="")


directory = vars(parser.parse_args())['directory']


print(glob.glob(directory + '*.nc'))

