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
    def green(text, bold=False, system_log: bool = False, enable_staring: bool = False):
        Console.print_log(Console.get_message_format(text, enable_staring=enable_staring), color="green", bold=bold, system_log=system_log)

    @staticmethod
    def blue(text, bold=False, system_log: bool = False, enable_staring: bool = False):
        Console.print_log(Console.get_message_format(text, enable_staring=enable_staring), color="blue", bold=bold, system_log=system_log)

    @staticmethod
    def red(text, bold=False, system_log: bool = False, enable_staring: bool = False):
        Console.print_log(Console.get_message_format(text, enable_staring=enable_staring), color="red", bold=bold, system_log=system_log)

    @staticmethod
    def yellow(text, bold=False, system_log: bool = False, enable_staring: bool = False):
        Console.print_log(Console.get_message_format(text, enable_staring=enable_staring), color="yellow", bold=bold, system_log=system_log)

    @staticmethod
    def magenta(text, bold=False, system_log: bool = False, enable_staring: bool = False):
        Console.print_log(Console.get_message_format(text, enable_staring=enable_staring), color="magenta", bold=bold, system_log=system_log)

    @staticmethod
    def cyan(text, bold=False, system_log: bool = False, enable_staring: bool = False):
        Console.print_log(Console.get_message_format(text, enable_staring=enable_staring), color="cyan", bold=bold, system_log=system_log)

    @staticmethod
    def get_message_format(text, enable_staring: bool = False):
        if not enable_staring:
            return text
        return f"{Console.log_starting} {str(text)}"

    @staticmethod
    def error(message, system_log: bool = False, enable_staring: bool = True):
        return Console.red(message, True, system_log=system_log, enable_staring=enable_staring)

    @staticmethod
    def success(message, system_log: bool = False, enable_staring: bool = True):
        return Console.green(message, True, system_log=system_log, enable_staring=enable_staring)

    @staticmethod
    def info(message, system_log: bool = False, enable_staring: bool = True):
        return Console.yellow(message, True, system_log=system_log, enable_staring=enable_staring)

    @staticmethod
    def log(message, system_log: bool = False, enable_staring: bool = True):
        return Console.blue(message, True, system_log=system_log, enable_staring=enable_staring)

    @staticmethod
    def run(command, home, env=None):
        response = subprocess.run(command, shell=True, cwd=home, env=env)
        return response
