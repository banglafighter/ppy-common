from ppy_common import click


class Console:
    enable_log: bool = True
    log_starting: str = ">>"

    @staticmethod
    def print_log(text, color=None, bold=None):
        if Console.enable_log:
            click.echo(click.style(text, fg=color, bold=bold))

    @staticmethod
    def green(text, bold=False):
        Console.print_log(text, color="green", bold=bold)

    @staticmethod
    def blue(text, bold=False):
        Console.print_log(text, color="blue", bold=bold)

    @staticmethod
    def red(text, bold=False):
        Console.print_log(text, color="red", bold=bold)

    @staticmethod
    def yellow(text, bold=False):
        Console.print_log(text, color="yellow", bold=bold)

    @staticmethod
    def magenta(text, bold=False):
        Console.print_log(text, color="magenta", bold=bold)

    @staticmethod
    def cyan(text, bold=False):
        Console.print_log(text, color="cyan", bold=bold)

    @staticmethod
    def get_message_format(text):
        return f"{Console.log_starting} {str(text)}"

    @staticmethod
    def error(message):
        return Console.red(Console.get_message_format(message), True)

    @staticmethod
    def success(message):
        return Console.green(Console.get_message_format(message), True)

    @staticmethod
    def info(message):
        return Console.yellow(Console.get_message_format(message), True)

    @staticmethod
    def log(message):
        return Console.blue(Console.get_message_format(message), True)
