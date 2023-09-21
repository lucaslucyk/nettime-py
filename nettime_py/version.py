from pathlib import Path


UNKNOW_VERSION = "unknown (git checkout)"


def string() -> str:
    try:
        fp = Path(__file__).parent / "VERSION"
        if not fp.is_file(): return UNKNOW_VERSION
        with open(fp, "r", encoding="utf-8") as fh:
            version = fh.read().strip()
            if version:
                return version
    except:
        pass
    return UNKNOW_VERSION