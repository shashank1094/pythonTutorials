from datetime import datetime
# Import the library
import argparse
# Create the parser
import pytz

parser = argparse.ArgumentParser()
# Add an argument
parser.add_argument('--earlier', type=str, required=True)
# Add another argument
parser.add_argument('--later', type=str, required=False, default=None)
# Parse the argument
args = parser.parse_args()
# # Print "Hello" + the user input argument
# print('Hello,', args.name)
datetime_earlier = datetime.strptime(args.earlier, '%Y-%m-%dT%H:%M:%S.%f%z')
if args.later:
    datetime_later = datetime.strptime(args.later, '%Y-%m-%dT%H:%M:%S.%f%z')
else:
    datetime_later = datetime.utcnow().replace(tzinfo=pytz.utc)
diff = (datetime_later - datetime_earlier)
print(str(diff))
