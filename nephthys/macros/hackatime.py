from nephthys.macros.types import ReplyMacro
from nephthys.utils.env import env


class Hackatime(ReplyMacro):
    """
    A simple macro telling people to use #hackatime-help.
    """

    name = "hackatime"
    message = env.transcript.hackatime_macro
    post_as_helper = True
