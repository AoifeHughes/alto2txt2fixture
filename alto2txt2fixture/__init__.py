from argparse import ArgumentParser


def parse_args(argv=None):
    parser = ArgumentParser()
    parser.add_argument(
        "-c",
        "--collections",
        nargs="+",
        help="<Optional> Set collections",
        required=False,
    )
    parser.add_argument(
        "-m",
        "--mountpoint",
        type=str,
        help="<Optional> Mountpoint",
        required=False,
    )
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        help="<Optional> Set an output directory",
        required=False,
    )
    return parser.parse_args(argv)
