from tabulate import tabulate

class TableView:
    @staticmethod
    def render(data, headers="keys"):
        if not data:
            print("\n[!] No data to display.")
            return
        print("\n" + tabulate(data, headers=headers, tablefmt="fancy_grid"))