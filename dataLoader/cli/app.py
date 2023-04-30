from plumbum import cli
from loguru import logger

from dataLoader import __version__
import sys

class App(cli.Application):
    PROGNAME = "dataLoader"
    VERSION = __version__

    @cli.autoswitch(help='Adds logging, the data is output to the console')
    def log(self):
        logger.add(sys.stdout, colorize=True, format="<green>{time:HH:mm:ss}</green> <level>{message}</level>")

    def main(self):
        logger.remove(0)
        logger.info('Start process')
        print('Does something')
        logger.info('End process')


if __name__ == "__main__":
    App.run()