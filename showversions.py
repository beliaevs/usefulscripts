import subprocess
import sys

def get_version(args):
    try:
        res = subprocess.run(args, capture_output = True)
        lines = res.stdout.decode().splitlines()
        if len(lines) > 0:
            return lines[0]
        else:
            return ''
    except FileNotFoundError:
        return f'{args[0]}: not found'


def get_git_version():
    return get_version(['git', '--version'])


def get_rust_version():
    return get_version(['rustc', '--version'])


def get_go_version():
    return get_version(['go', 'version'])


def get_python_version():
    res = sys.version.splitlines()[0]
    return f'python: {res}'


def get_cmake_version():
    return get_version(['cmake', '--version'])


def get_gcc_version():
    return get_version(['gcc', '--version'])


def get_perl_version():
    try:
        res = subprocess.run(['perl', '--version'], capture_output = True)
        lines = res.stdout.decode().splitlines()
        if len(lines) > 1:
            return lines[1]
        else:
            return ''
    except FileNotFoundError:
        return 'perl: not found'

def get_vscode_version():
    if sys.platform == 'win32':
        vscode = 'code.cmd'
    else:
        vscode = 'code'

    try:
        res = subprocess.run([vscode, '--version'], capture_output = True)
        lines = res.stdout.decode().splitlines()
        if len(lines) > 0:
            return f'vscode {lines[0]}'
        else:
            return ''
    except FileNotFoundError:
        return 'vs code: not found'
    except OSError:
        return 'vs code: cannot launch from script'


def get_node_version():
    return 'node ' + get_version(['node', '--version'])


def get_miktex_version():
    return get_version(['mpm', '--version'])


def get_julia_version():
    return get_version(['julia', '--version'])

def main():
    print(get_git_version())
    print(get_rust_version())
    print(get_go_version())
    print(get_python_version())
    print(get_cmake_version())
    print(get_gcc_version())
    print(get_perl_version())
    print(get_vscode_version())
    print(get_node_version())
    print(get_miktex_version())
    print(get_julia_version())


if __name__ == '__main__':
    main()


