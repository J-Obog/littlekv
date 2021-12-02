import signal

def handle_sig(s,f): pass

signal.signal(signal.SIGINT, handle_sig)