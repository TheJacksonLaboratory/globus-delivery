import keyring
import argparse
import subprocess

def main(local, remote, svc, localdir, remotedir):
    passw = keyring.get_password("globus", svc)
    activate = ['globus', 'endpoint', 'activate', '--myproxy', '--myproxy-lifetime', '168', 
                '--force', '-U', svc, '-P', passw, remote]
    process = subprocess.Popen(activate,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    stdoutval, stderrval = process.communicate()
    stdoutval, stderrval = stdoutval.decode('UTF-8'), stderrval.decode('UTF-8')
    print("stdout:",stdoutval)
    print("stderr:",stderrval)

    transfer = ['globus', 'transfer', '--delete', '--sync-level', 'checksum', '--recursive', 
                local+":"+localdir, remote+":"+remotedir]
    process = subprocess.Popen(transfer,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    stdoutval, stderrval = process.communicate()
    stdoutval, stderrval = stdoutval.decode('UTF-8'), stderrval.decode('UTF-8')
    print("stdout:",stdoutval)
    print("stderr:",stderrval)

    return


if __name__ == '__main__':
    description = "One-command globus activate-and-sync"
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('endpoint',
                        type=str,
                        help='Local endpoint to be sync-ed')
    parser.add_argument('--remoteendpoint',
                        type=str,
                        help='Remote endpoint to be sync-ed',
                        default='b8377de1-47c2-11e7-bd5c-22000b9a448b')
    parser.add_argument('--svcuser',
                        type=str,
                        help='Service username that is running this',
                        default='svc-delivery')
    parser.add_argument('--localdir',
                        type=str,
                        help='Directory in the local endpoint that will be sync-ed',
                        default='')
    parser.add_argument('--remotedir',
                        type=str,
                        help='Remote directory where data will be sync-ed to',
                        default='/projects/researchit/ratame/globus-python')
    args = parser.parse_args()
    main(args.endpoint, args.remoteendpoint, args.svcuser, args.localdir, args.remotedir)