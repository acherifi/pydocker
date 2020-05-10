from cmd import Cmd
from docker_images import DockerImages
from interpreter import Interpreter

class DockerCmd(Cmd, Interpreter):

    def __init__(self, completekey='tab', stdin=None, stdout=None):
        super().__init__(completekey, stdin, stdout)
        self.prompt = self.interpreter

    def do_images(self, input):
        DockerImages().cmdloop()
        pass
    
    def do_inspect(self):
        # TODO: Enter the inspect interpreter
        pass

    def do_container(self):
        #TODO: Enter the container interpreter
        pass



