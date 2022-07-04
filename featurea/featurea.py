from argparse import _SubParsersAction, ArgumentParser
from ast import arg, parse


class FeatureA:
    verboseOutput = False

    def __init__(self, parentargparser: ArgumentParser):
        # print("FeatureA init")
        parser = parentargparser.add_parser("featurea")
        parser.add_argument(
            "command", type=str, help="command to run", choices=["list", "get"]
        )
        parser.add_argument(
            "--id",
            type=str,
            help="id",
        )

    def checkargs(self, args):
        if args.verbose:
            self.verboseOutput = True

        if args.feature != "featurea":
            self.verbose("not featurea")
            return

        if args.command == "list":
            self.list()
        elif args.command == "get":
            self.get(args.id)
        elif args.command == "set":
            self.set(args.id, args.key, args.value)
        elif args.command == "delete":
            self.delete(args.id)

    def verbose(self, message):
        if self.verboseOutput:
            print(message)

    def list(self):
        self.verbose("FeatureA-List")

    def get(self, id):
        self.verbose(f"FeatureA-Get {id}")

    def set(self, id, key, value):
        self.verbose("FeatureA-Set")

    def delete(self, id):
        self.verbose("FeatureA-Set")
