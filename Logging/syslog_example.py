import syslog
import os
import logging.handlers

print(os.path.abspath(syslog.__file__))
syslog.syslog(f'Sending a log message through {__file__}!')
syslog.syslog(syslog.LOG_CRIT, "Test message at INFO priority")




class SyslogBOMFormatter(logging.Formatter):
    def format(self, record):
        result = super().format(record)
        return "ufeff" + result


handler = logging.handlers.SysLogHandler('/dev/log')
formatter = SyslogBOMFormatter(logging.BASIC_FORMAT)
handler.setFormatter(formatter)
root = logging.getLogger()
root.setLevel(os.environ.get("LOGLEVEL", "INFO"))
root.addHandler(handler)

try:
    root.debug("nahi nahi nahi")
except Exception:
    logging.exception("Exception in main()")
    exit(1)