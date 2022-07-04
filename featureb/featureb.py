from argparse import ArgumentParser


class FeatureB:
    verboseOutput = False

    def __init__(self, parentargparser: ArgumentParser):
        # print("FeatureB init")
        parser = parentargparser.add_parser("featureb")
        parser.add_argument(
            "command", type=str, help="command to run", choices=["list", "get"]
        )

    def checkargs(self, args):
        if args.verbose:
            self.verboseOutput = True

        if args.feature != "featureb":
            self.verbose("not featureb")
            return

        if args.command == "list":
            self.list()
        elif args.command == "get":
            self.get(args.id)

    def verbose(self, message):
        if self.verboseOutput:
            print(message)

    def list(self):
        self.verbose("FeatureB-List")

    def get(self, id):
        self.verbose("FeatureB-Get")

    def set(self, id, key, value):
        self.verbose("FeatureB-Set")

    def delete(self, id):
        self.verbose("FeatureB-Delete")
