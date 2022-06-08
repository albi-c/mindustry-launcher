from .download import Downloader

import os

class Launcher:
    @staticmethod
    def launch(build: str):
        build = Downloader.resolve_build(build)
        filename = Downloader.get_filename(build)

        if not os.path.isfile(filename):
            Downloader.download(build)
        
        os.system(f"java -jar {filename}")
