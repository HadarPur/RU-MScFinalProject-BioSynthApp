import sys

from executions.controllers.cli_controller import CLIController
from executions.controllers.gui_controller import GUIController
from utils.file_utils import delete_dir
from utils.input_utils import ArgumentParser
from utils.output_utils import Logger
from utils.text_utils import OutputFormat, set_output_format


class BioSynthApp:
    @staticmethod
    def execute(args):
        try:
            delete_dir('output')

            parser = ArgumentParser()
            gui, _, _, _, _, _, _, _ = parser.parse_args(args)

            if gui:
                set_output_format(OutputFormat.GUI)
                GUIController().execute()
            else:
                set_output_format(OutputFormat.TERMINAL)
                CLIController(args).execute()

        except KeyboardInterrupt:
            Logger.error("\nProgram stopped by the user.")


if __name__ == "__main__":
    BioSynthApp.execute(sys.argv[1:])
