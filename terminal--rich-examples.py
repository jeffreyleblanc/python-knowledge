#! /usr/bin/env python3

if __name__ == '__main__':
    from rich.console import Console

    console = Console()

    #-- Table -------------------------------------------------------------------#

    from rich.table import Table

    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Date", style="dim", width=12)
    table.add_column("Title")
    table.add_column("Description", justify="right")
    table.add_column("unit", justify="right")
    table.add_row(
        "2021-12-05", "Stuff", "Various things", "34.8"
    )
    table.add_row(
        "2021-12-07", "Long Stuff", "very very very very very long text that just keeps going on and on", "14"
    )
    table.add_row(
        "2021-12-18", "Groceries", "Apples\nOranges\nPears", "1034.45"
    )
    table.add_row(
        "2021-12-19", "Stuff", "Various things", "34.8"
    )
    console.print(table)

    #-- Markdown -------------------------------------------------------------------#

    from rich.markdown import Markdown
    import textwrap


    console = Console()

    readme = textwrap.dedent('''
        # Header 1

        * a list of **things**
        * including `code`
            * lots of code
        * etc...

        ## Sub header 1

        An aside:

        > A great and long quote
        >
        > from someone who is
        >
        > very, very cool

        And a block

            A block
            quote
            of things

        and some code

        ```sh
        $ ls /tmp/var

        # And then do a ping
        $ ping google.com -c 6
        ```

    ''')

    markdown = Markdown(readme)
    console.print(markdown)

