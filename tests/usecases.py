import os
import sys
from lecloud.client import Client

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# we read access key from system environment in this case.
# so make sure you have properly set them before run.
c = Client(os.environ['ACCESS_KEY'],
           os.environ['ACCESS_SECRET'],
           os.environ['ENDPOINT'])


def describe_instances():
    ret = c.call('DescribeInstances')
    print ret


def describe_volumes():
    ret = c.call('DescribeVolumes')
    print ret


def describe_networks():
    ret = c.call('DescribeNetworks')
    print ret


if __name__ == '__main__':
    describe_instances()
    describe_volumes()
    describe_networks()
