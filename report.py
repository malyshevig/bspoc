import argparse
import logging
import sys
from lp.conf import Config
from lp.dp import generate

logging.basicConfig(stream=sys.stdout,encoding='utf-8', format='%(asctime)s %(levelname)s %(message)s',
                    level=logging.INFO)

#
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
                    prog='report',
                    description='Analyze data'
                    )

    parser.add_argument('filename')  # positional argument
    parser.add_argument('-t', '--tech', help="technology name", default="Apache Ignite")
    parser.add_argument('-d', '--dir', help="directory with data files, default=/data", default="/data")
    parser.add_argument('-p', '--period', type=int, help="period of aggregation in seconds")
    parser.add_argument('-s', '--session', type=str, help="optional filter to session")
    parser.add_argument('-w', '--warmup', type=int, help="warm uo time in mins", default="45")
    parser.add_argument('-r', '--rhead', type=int, help="remove heading mins", default="0")

    args = parser.parse_args()

    conf = Config()
    conf.period = args.period if args.period else 30
    conf.filename = args.filename
    conf.technology = args.tech
    conf.directory = args.dir
    conf.session = args.session
    conf.warmup = int(args.warmup)
    conf.remove_head = int(args.rhead)

    generate(conf)