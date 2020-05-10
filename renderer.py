from rich.console import Console
from rich.panel import Panel
from rich import print

class Renderer():
    encoding = 'utf-8'
    console = Console()

    def render_ok_command(self, command_result):
        # TODO: Stocker les images ids pour faire de la completion dessus.
        output = command_result.stdout.decode(self.encoding)
        if self.is_output_one_line(output):
            output = 'No Docker images on your system.'
        print(Panel(output))

    def is_output_one_line(self, output):
        return (output.count('\n') == 1)