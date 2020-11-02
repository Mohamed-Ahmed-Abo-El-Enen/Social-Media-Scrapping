import sys
import traceback


def print_exception(ex):
    traceback.print_exc(file=sys.stdout)
    print("Uncontrolled error: " + str(ex))
    input("Press any key to continue...")
