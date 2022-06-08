import requests, appdirs, shutil, os, sys

APPNAME = "mindustry_launcher"

class Downloader:
    @staticmethod
    def _download(build: str, filename: str, bleeding_edge: bool) -> bool:
        if bleeding_edge:
            url = f"https://github.com/Anuken/MindustryBuilds/releases/download/{build}/Mindustry-BE-Desktop-{build}.jar"
        else:
            url = f"https://github.com/Anuken/Mindustry/releases/download/v{build}/Mindustry.jar"
        
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        
        with requests.get(url, stream=True) as r:
            if r.status_code == 200:
                with open(filename, "wb") as f:
                    shutil.copyfileobj(r.raw, f)
                    return True

        return False
    
    @staticmethod
    def resolve_build(build: str):
        if build == "LATEST_STABLE":
            return Downloader.get_latest_stable()
        elif build == "LATEST_ALPHA":
            return Downloader.get_latest_alpha()
        elif build == "LATEST_BE":
            return Downloader.get_latest_be()
        
        try:
            return str(int(build))
        except ValueError:
            try:
                return str(float(build))
            except ValueError:
                print(f"Invalid build number (\"{build}\")")
                sys.exit(1)
    
    @staticmethod
    def is_be(build: str):
        return float(build) > 20000
    
    @staticmethod
    def get_latest_stable() -> str:
        return requests.get("https://api.github.com/repos/Anuken/Mindustry/releases/latest").json()["tag_name"][1:]
    
    @staticmethod
    def get_latest_alpha() -> str:
        return requests.get("https://api.github.com/repos/Anuken/Mindustry/releases").json()[0]["tag_name"][1:]
    
    @staticmethod
    def get_latest_be() -> str:
        return requests.get("https://api.github.com/repos/Anuken/MindustryBuilds/releases/latest").json()["tag_name"]
    
    @staticmethod
    def get_filename(build: str) -> str:
        return os.path.join(appdirs.user_data_dir(APPNAME), f"Mindustry-{build}.jar")
    
    @staticmethod
    def download(build: str) -> str:
        build = Downloader.resolve_build(build)
        filename = Downloader.get_filename(build)

        if not Downloader._download(build, filename, Downloader.is_be(build)):
            print(f"Failed to download mindustry (build \"{build}\")")
            sys.exit(1)
        
        return filename
