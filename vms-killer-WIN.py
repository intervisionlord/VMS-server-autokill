import psutil

VMS = r'TS VMS 2.0.exe'
VMSSERV = r'TS VMS Server.exe'

def killServer(VMS, VMSSERV):
    for proc in psutil.process_iter():
        if proc.name() == VMS:
            print('TS VMS is still running!')
            exit(1)
        elif proc.name() == VMSSERV or proc.name() == 'vms_crash_handler_x64.exe' or proc.name() == 'Watcher.exe':
            proc.terminate()
            print(proc.name(), 'was killed')
    print('Done!')

killServer(VMS, VMSSERV)
