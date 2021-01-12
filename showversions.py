import subprocess


def get_version(args):
    res = subprocess.run(args, capture_output = True)
    lines = res.stdout.decode().splitlines()
    if len(lines) > 0:
        return lines[0]
    else:
        return ''


def get_git_version():
    return get_version(['git', '--version'])


def get_rust_version():
    return get_version(['rustc', '--version'])


def get_go_version():
    return get_version(['go', 'version'])


def get_python_version():
    return get_version(['python', '--version'])


def get_cmake_version():
    return get_version(['cmake', '--version'])


def get_gcc_version():
    return get_version(['gcc', '--version'])


def get_perl_version():
    res = subprocess.run(['perl', '--version'], capture_output = True)
    lines = res.stdout.decode().splitlines()
    if len(lines) > 1:
        return lines[1]
    else:
        return ''


def get_vscode_version():
    res = subprocess.run(['code.cmd', '--version'], capture_output = True)
    lines = res.stdout.decode().splitlines()
    if len(lines) > 0:
        return f'vscode {lines[0]}'
    else:
        return ''


def get_node_version():
    return 'node ' + get_version(['node', '--version'])


def get_miktex_version():
    return get_version(['mpm', '--version'])

def main():
    git_version = get_git_version()
    rust_version = get_rust_version()
    go_version = get_go_version()
    python_version = get_python_version()
    cmake_version = get_cmake_version()
    gcc_version = get_gcc_version()
    perl_version = get_perl_version()
    vscode_version = get_vscode_version()
    node_version = get_node_version()
    miktex_version = get_miktex_version()
    print(f'''
    {git_version}
    {rust_version}
    {go_version}
    {python_version}
    {cmake_version}
    {gcc_version}
    {perl_version}
    {vscode_version}
    {node_version}
    {miktex_version}
    ''')



if __name__ == '__main__':
    main()


