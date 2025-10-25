import os
import datetime

def smart_log(*args, **kwargs) -> None:
    message = " ".join(str(s) for s in args)
    ts = kwargs.get('timestamp', True)
    d = kwargs.get('date', False)
    c = kwargs.get('color', True)
    st = kwargs.get('save_to', '')
    level = kwargs.get('level', 'info')

    colors = {'info': '\033[34m', 'debug': '\033[90m', 'warning': '\033[33m', 'error': '\033[31m'}
    types = {'info': '[INFO]', 'debug': '[DEBUG]', 'warning': '[WARNING]', 'error': '[ERROR]'}
    col = colors.get(level, '\033[37m')
    type_msg = types.get(level, '[INFO]')

    time_str = datetime.datetime.now().strftime('%H:%M:%S') if ts else ''
    date_str = datetime.datetime.now().date().isoformat() if d else ''

    log_msg = f"{col}{date_str} {time_str} {type_msg} {message}\033[0m" if c else f"{date_str} {time_str} {type_msg} {message}"
    print(log_msg)

    if st:
        plain_msg = f"{date_str} {time_str} {type_msg} {message}"
        with open(st, 'a') as f:
            f.write(plain_msg + '\n')

smart_log("System started successfully.", level="info", timestamp=True)
smart_log("User", "username", "logged in", level="debug", timestamp=True)
smart_log("Low disk space detected!", level="warning", save_to="logs/errors.log")
smart_log("Model training failed", level="error", color=True, save_to="logs/errors.log")
smart_log("Process end", level="info", color=False, save_to="logs/errors.log")