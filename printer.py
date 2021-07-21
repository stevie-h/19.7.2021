# ex20

class Printer:
    def __init__(self, model):
        self.model = model
        print(f'A new printer has arrived')

    def print_pages(self, *args):
        [print(s) for s in args]


# ex21
class PocketPrinter(Printer):
    pass

