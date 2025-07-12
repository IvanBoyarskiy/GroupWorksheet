import shutil
from pathlib import Path
import os

documentType = [
    'txt', 'md', 'markdown', 'doc', 'docx', 'odt', 'rtf', 'wpd', 'pages',
    'tex', 'ltx', 'wri', 'pwi', 'mcw', 'sdw', 'stw', 'uot', 'vor', 'dot',
    'dotx', 'dotm', 'sxw', 'pdb', 'pml', 'pub', 'abw', '1st', 'key', 'text',

    'xls', 'xlsx', 'xlsm', 'ods', 'csv', 'tsv', 'numbers', 'dif', 'slk',
    'xlr', 'gnumeric', 'sxc', 'stc', 'ots', 'dbf', 'prn', 'wbk', 'xltx',
    'xltm', 'xlam', 'xlsb',

    'accdb', 'mdb', 'sqlite', 'sqlitedb', 'db', 'db3', 'sdf', 'firebird',
    'ib', 'myd', 'frm', 'ibd', 'mdf', 'ldf', 'bson', 'paradox', 'edb',
    'accdr', 'accdc', 'sqlite3',

    'ppt', 'pptx', 'pps', 'ppsx', 'odp', 'keynote', 'pot', 'potx', 'potm',
    'ppam', 'sxi', 'sti', 'otp', 'sldx', 'thmx', 'show', 'emf',

    'epub', 'mobi', 'azw', 'azw3', 'fb2', 'lit', 'pdb', 'prc', 'djvu', 'cbz',
    'cbr', 'opf', 'ncx', 'chm', 'oxps', 'xps', 'org', 'rst', 'jnote', 'note',
    'nb', 'snote', 'zim', 'enex', 'jrn', 'diary', 'logbook',

    'pdf', 'ps', 'eps', 'dvi', 'afm', 'pfm', 'ttf', 'otf', 'woff', 'woff2', 'eot', 'fon', 'font',
]
archiveType = [
    'zip', 'rar', '7z', 'tar', 'gz', 'bz2', 'xz', 'lzma', 'z', 'tgz', 'tbz2',
    'zipx', 'jar', 'war', 'ear', 'apk', 'xpi', 'iso', 'img', 'vhd', 'vhdx', 'dmg',
    'sit', 'sitx', 'pkg', 'deb', 'rpm', 'cab', 'msi', '7z.001', 'part', '001', 'split', 'z01'
]
imageType = [
    'jpg', 'jpeg', 'png', 'gif', 'bmp', 'webp', 'tiff', 'tif', 'ico', 'heic', 'heif',
    'jp2', 'j2k', 'jpf', 'jpx', 'jpm', 'mj2', 'xcf', 'psd', 'raw', 'cr2', 'nef',
    'orf', 'sr2', 'dng', 'arw', 'raf', 'pef', 'x3f', 'rw2', 'erf', '3fr', 'mdc', 'mef',
    'mos', 'nrw', 'ptx', 'kdc', 'rwl', 'dcr', 'drf', 'k25', 'rol', 'ciff', 'iiq', 'dsc',
    'pcx', 'tga', 'exr', 'hdr', 'pic', 'fits', 'fit', 'pbm', 'pgm', 'ppm', 'pnm',
    'bpg', 'avif', 'flif', 'sgi', 'ras', 'wbmp', 'cur', 'xbm', 'dds', 'pdd', 'pat',

    'ai', 'cdr', 'sketch', 'fig', 'xd', 'vdx', 'vsdx', 'wmf', 'emf', 'fla', 'swc',
    'cpt', 'pln', 'dwg', 'dxf', 'plt', 'step', 'stp', 'iges', 'igs', 'stl', 'obj',
    '3mf', 'ply', 'off', 'collada', 'dae', 'u3d', 'ma', 'blend', 'sldprt',
]
videoType = [
    'mp4', 'mkv', 'webm', 'avi', 'mov', 'wmv', 'flv', 'ogg', 'ogv', 'mts',
    'm2ts', 'ts', 'mxf', 'asf', 'rm', 'rmvb', 'vob', 'ifo', 'bup', 'divx', 'xvid',
    '3gp', '3g2', 'amv', 'dav', 'dvr-ms', 'm1v', 'm2v', 'm4v', 'mpg', 'mpeg',
    'mpe', 'mpv', 'm2p', 'ps', 'pes', 'rec', 'tp', 'trp', 'tpr', 'nsv', 'nsa',

    'f4v', 'f4p', 'f4a', 'f4b', 'm3u8', 'ism', 'ismv', 'isma', 'mss', 'mpls',
    'bdmv', 'clpi', 'bdjo', 'hls', 'dash', 'mpd', 'smil', 'fli', 'flc',

    '3gpp', '3gp2', 'k3g', '3gpp2', '3ga', '3gpw', 'mob', 'mod', 'tod', 'pva',
    'r3d', 'ari', 'crx', 'm21', 'mjp', 'mjpg', 'cam', 'dv', 'dif', 'dvc', 'dvx',

    'lrv', 'thm', 'gifv', 'apng', 'vro', 'tdt', 'sub', 'idx', 'sup', 'pgs', 'evo', 'eac3',

    'yuv', 'avs', 'nut', 'smv', 'rv', 'vfw', 'dl', 'cel', 'cmv', 'anx', 'axa',
    'vpy', 'vpl', 'vmlf', 'vtf', 'wtv',
]
audioType = [
    'mp3', 'wav', 'flac', 'aac', 'm4a', 'wma', 'alac', 'aiff', 'aif',
    'ape', 'wv', 'tta', 'mp2', 'mp1', 'opus', 'amr', 'dts', 'ac3', 'eac3',
    'pcm', 'al', 'adpcm', 'dsd', 'dff', 'dsf', 'sacd', 'shn', 'la', 'tak',

    'm4b', 'm4r', 'aa', 'aax', 'ra', 'ram', 'oga', 'spx', 'caf', 'gsm', 'awb',
    'ulaw', 'alaw', 'dvf', 'gpx', 'mogg',

    'mid', 'midi', 'rmi', 'kar', 'xen', 'sf2', 'sfz', 'gig', 'its',
    'xm', 'umx', 'mo3', 'nst', 'ptm', '669', 'mtm', 'far', 'mdl',
    'okt', 'dmf', 'pt36', 'amf', 'ult', 'uni', 'stm', '6cm', 'sfx', 'psm',

    'au', 'snd', 'ircam', 'svx', 'nist', 'voc', 'w64', 'mat',
    'pvf', 'xi', 'hcom', '8svx', 'sds', 'smp', 'sd2', 'paud', 'nsf', 'hes',
    'kss', 'scc', 'dlt', 'mc', 'tfmx', 'vox', 'dss', 'msv',
    'oma', 'aa3', 'm4p', 'mmf', 'sdx', 'vqf', 'aud',
]
appType = [
    'exe', 'dll', 'bat', 'cmd', 'msi', 'com', 'scr', 'chm', 'cpl', 'ink',

    'run', 'bin', 'elf', 'so', 'ko', 'mod',

    'app', 'command', 'workflow', 'scpt', 'pkg', 'mpkg', 'osascript',

    'pyc', 'pyo', 'jar', 'war', 'class', 'dex', 'apk', 'ipa', 'msix',
]
shortcutType = [
    'lnk', 'url', 'desktop', 'webloc', 'shb', 'ink', 'website', 'library-ms',
]
codeType = [
    'py', 'java', 'cpp', 'cxx', 'cc', 'c', 'h', 'hpp', 'cs', 'php', 'rb', 'pl',
    'go', 'rs', 'swift', 'kt', 'kts', 'scala', 'm', 'mm', 'vb', 'fs', 'groovy',
    'dart', 'ts', 'tsx', 'js', 'jsx', 'vue', 'svelte', 'sol', 'clj', 'cljs', 'erl',

    'asm', 's', 'S', 'rc', 'def', 'exp', 'inl', 'inc', 'glsl', 'hlsl', 'cl', 'metal',

    'bash', 'zsh', 'fish', 'vbs', 'ahk', 'au3', 'scpt', 'applescript',

    'html', 'htm', 'xhtml', 'xml', 'rss', 'xslt', 'xsd', 'dtd', 'json', 'yaml',
    'yml', 'toml', 'plist', 'log', 'bak',
]

def get_info_file(file_path):
    print(f"Полный путь: {file_path.resolve()}")
    print(f"Папка: {file_path.parent}")
    print(f"Имя файла с расширением: {file_path.name}")
    print('-' * 40)
def if_directory_exist(directory_path):
    if os.path.exists(directory_path):
        return True
    else:
        return False
def directory_name_by_ext(file_type: str):
    if file_type in documentType:
        return "\DocumentFiles"
    elif file_type in archiveType:
        return "\ArchiveFiles"
    elif file_type in imageType:
        return "\ImageFiles"
    elif file_type in videoType:
        return "\VideoFiles"
    elif file_type in audioType:
        return "\AudioFiles"
    elif file_type in appType:
        return "\AppFiles"
    elif file_type in shortcutType:
        return "\ShortcutFiles"
    elif file_type in codeType:
        return "\CodeFiles"
    else:
        return "\AnotherFiles"
def get_worksheet_path(file_path: str):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            path = file.readline().strip()
            if path:
                return path
            else:
                print("Файл существует, но он пуст.")
                return None
    except FileNotFoundError:
        print(f"Файл '{file_path}' не найден.")
        return None
def get_files(file_type):
    dict = []
    for type in file_type:
        for file_path in Path(get_worksheet_path("worksheetpath.txt")).glob(f'*.{type}'):
            get_info_file(file_path)
            full_path = file_path.resolve()
            directory = file_path.parent
            filename = file_path.name
            new_directory = f'{directory}{directory_name_by_ext(type)}'
            # newpath = f'{directory}{directory_name_by_ext(type)}\\{filename}'
            dict.append([full_path, Path(new_directory)])
    return dict
def send_files(files):
    for file in files:
        file_path = file[0]
        directory = file[1]
        directory.mkdir(parents=True, exist_ok=True)
        shutil.move(str(file_path), str(directory))
def get_all_files(mas):
    dict = []
    for theme in mas:
        for file in theme:
            dict.append(file)
    return dict

all_text_files = get_files(documentType)
all_archive_files = get_files(archiveType)
all_image_files = get_files(imageType)
all_video_files = get_files(videoType)
all_audio_files = get_files(audioType)
all_app_files = get_files(appType)
all_shortcut_files = get_files(shortcutType)
all_code_files = get_files(codeType)

send_files(get_all_files([all_text_files, all_archive_files, all_image_files, all_video_files, all_audio_files,
                    all_app_files, all_shortcut_files, all_code_files]))








