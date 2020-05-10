from cmd import Cmd
import subprocess
from renderer import Renderer
from interpreter import Interpreter

class DockerImages(Cmd, Interpreter):

    renderer = Renderer()

    def __init__(self, completekey='tab', stdin=None, stdout=None):
        super().__init__(completekey, stdin, stdout)
        self.prompt = '<images>'

    def do_list(self, args):
        result = subprocess.run('docker images', shell = True, capture_output=True)
        if result.returncode == 1:
            exit(1)
        self.renderer.render_ok_command(result)
