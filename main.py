import argparse

from featurea.featurea import FeatureA
from featureb.featureb import FeatureB

ARGS = None


def main():
    print("Sample CLI Tool")


def setup():
    # print("Setup")
    parser = argparse.ArgumentParser(description="Description of tool")
    parser.add_argument(
        "-x", "--xaver", action="store_true", help="Show xaver information"
    )
    parser.add_argument("-a", "--about", action="store_true", help="About this tool")
    parser.add_argument("-v", "--verbose", action="store_true", help="Output verbose")
    subparsers = parser.add_subparsers(title="actions")
    # subparsers.required = True
    subparsers.dest = "feature"

    featurea = FeatureA(subparsers)
    featureb = FeatureB(subparsers)

    # args = vars(parser.parse_args())
    ARGS = parser.parse_args()

    featurea.checkargs(ARGS)
    featureb.checkargs(ARGS)

    if ARGS.about:
        show_about()
    if ARGS.xaver:
        xaver()
    # verbose(ARGS)


def verbose(message: str):
    if ARGS:
        if ARGS.verbose:
            print(message)
    else:
        print("No ARGS")


def show_about():
    verbose("About")


def xaver():
    verbose("Xaver")


if __name__ == "__main__":
    main()
    setup()
