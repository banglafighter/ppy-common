import subprocess
import click


class Console:
    enable_log: bool = True
    log_starting: str = ">>"

    @staticmethod
    def print_log(text, color=None, bold=None, system_log: bool = False):
        if Console.enable_log or system_log:
            click.echo(click.style(text, fg=color, bold=bold))

    @staticmethod
    def green(text, bold=False, system_log: bool = False):
        Console.print_log(text, color="green", bold=bold, system_log=system_log)

    @staticmethod
    def blue(text, bold=False, system_log: bool = False):
        Console.print_log(text, color="blue", bold=bold, system_log=system_log)

    @staticmethod
    def red(text, bold=False, system_log: bool = False):
        Console.print_log(text, color="red", bold=bold, system_log=system_log)

    @staticmethod
    def yellow(text, bold=False, system_log: bool = False):
        Console.print_log(text, color="yellow", bold=bold, system_log=system_log)

    @staticmethod
    def magenta(text, bold=False, system_log: bool = False):
        Console.print_log(text, color="magenta", bold=bold, system_log=system_log)

    @staticmethod
    def cyan(text, bold=False, system_log: bool = False):
        Console.print_log(text, color="cyan", bold=bold, system_log=system_log)

    @staticmethod
    def get_message_format(text):
        return f"{Console.log_starting} {str(text)}"

    @staticmethod
    def error(message, system_log: bool = False):
        return Console.red(Console.get_message_format(message), True, system_log=system_log)

    @staticmethod
    def success(message, system_log: bool = False):
        return Console.green(Console.get_message_format(message), True, system_log=system_log)

    @staticmethod
    def info(message, system_log: bool = False):
        return Console.yellow(Console.get_message_format(message), True, system_log=system_log)

    @staticmethod
    def log(message, system_log: bool = False):
        return Console.blue(Console.get_message_format(message), True, system_log=system_log)

    @staticmethod
    def run(command, home, env=None):
        response = subprocess.run(command, shell=True, cwd=home, env=env)
        return response
