from functools import partial
import sys

redirect = lambda functions, stream: partial(functions, file=stream)
prefix = lambda function, prefix: partial(function, prefix)
error = prefix(redirect(print, sys.stderr), '[ERROR}')
error('Something went wrong')
