from argparse import ArgumentParser

parser = ArgumentParser(description='Process some integers.')

parser.add_argument("-d", "--directory", dest="directory",
                    help="directory containing nc files", metavar="")
# parser.add_argument("-q", "--quiet",
#                     action="store_false", dest="verbose", default=True,
#                     help="don't print status messages to stdout")

print(vars(parser.parse_args())['directory'])
