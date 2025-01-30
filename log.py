from logging import basicConfig, captureWarnings
from warnings import warn as log

basicConfig(
    filename="STMS.log",
    filemode="a",
    format="%(asctime)s | %(message)s",
)
captureWarnings(True)
if __name__ == "__main__":
    log("Github Copilot!")
    log("Hello, world!")
    log("Test log msg(s).")
