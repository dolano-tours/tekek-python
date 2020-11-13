class CONFIG:
    FILE_RETRIES = 3
    REMOTE_RETRIES = 3

    class REMOTE:
        HOST = "http://localhost:5005"
        class DEBUG:
            ENDPOINT = "/debug"
            METHOD = "post"
        class INFO:
            INFO = "/info"
            METHOD = "post"
        class WARNING:
            WARNING = "/warning"
            METHOD = "post"
        class ERROR:
            ERROR = "/error"
            METHOD = "post"
        class CRITICAL:
            CRITICAL = "/critical"
            METHOD = "post"

setattr(CONFIG, "REMOTE", CONFIG.REMOTE)
setattr(CONFIG.REMOTE, "DEBUG", CONFIG.REMOTE.DEBUG)
setattr(CONFIG.REMOTE, "INFO", CONFIG.REMOTE.INFO)
setattr(CONFIG.REMOTE, "WARNING", CONFIG.REMOTE.WARNING)
setattr(CONFIG.REMOTE, "ERROR", CONFIG.REMOTE.ERROR)
setattr(CONFIG.REMOTE, "CRITICAL", CONFIG.REMOTE.CRITICAL)
