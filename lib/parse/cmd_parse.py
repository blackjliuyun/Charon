import argparse
import sys


def cmd_line_parser():
    parser = argparse.ArgumentParser(description='powered by cdxy <mail:i@cdxy.me> ',
                                     usage='python3 Charon.py -u/-f url/file --script scripts',
                                     add_help=False)

    engine = parser.add_argument_group('ENGINE')
    engine.add_argument('-eT', dest="engine_thread", default=False, action='store_true',
                        help='Multi-Threaded engine (default choice)')

    engine.add_argument('-eG', dest="engine_gevent", default=False, action='store_true',
                        help='Gevent engine (single-threaded with asynchronous)')

    engine.add_argument('-t', metavar='NUM', dest="thread_num", type=int, default=10,
                        help='num of threads/concurrent, 10 by default')

    script = parser.add_mutually_exclusive_group()

    script.add_argument('-s', metavar='SCRIPT', dest="script_name", type=str, nargs='+', default=[],
                        help="select the scripts to check")
    script.add_argument('-s-all', metavar='SCRIPT_all', dest="script_all", type=str, default='',
                        help="select the script_all to check")
    script.add_argument('--batch', dest="batch", default=False, action='store_true',
                        help='batch fuzz using fuzz script')

    target = parser.add_mutually_exclusive_group()

    target.add_argument('-u', metavar='TARGET', dest="target_url", type=str, default='',
                        help="scan a single target (e.g. www.wooyun.org)")
    target.add_argument('-f', metavar='FILE', dest="target_file", type=str, default='',
                        help='load targets from targetFile (e.g. ./1.txt)')

    output = parser.add_argument_group('OUTPUT')

    output.add_argument('-o', metavar='FILE', dest="output_path", type=str, default='',
                        help='output file path&name. default in ./output/')

    system = parser.add_argument_group('SYSTEM')

    system.add_argument('-v', '--version', action='version', version='1.0',
                        help="show program's version number and exit")
    system.add_argument('-h', '--help', action='help',
                        help='show this help message and exit')

    proxy = parser.add_argument_group('PROXY')

    proxy.add_argument('-p', metavar='PROXY', dest="proxy_ip", type=str, default='',
                       help="scan a single target (e.g. www.wooyun.org)")
    proxy.add_argument('-pl', metavar='PROXY_POOL', dest="proxy_pool_ip", type=str, default='',
                       help='load targets from targetFile (e.g. ./data/wooyun_domain)')
    misc = parser.add_argument_group('MISC')
    misc.add_argument('--timeout', type=int, default=5, help="set the Timeout")
    if len(sys.argv) == 1:
        sys.argv.append('-h')
    args = parser.parse_args()
    return vars(args)
    # return args


