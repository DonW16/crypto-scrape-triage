import re
import os
import shutil
import psutil
import hashlib
import datetime
import sys

blacklisted_extentions = {
    '.py',
    '.pyc',
    '.lnk',
    '.ini',
    '.json',
    '.css',
    '.htm',
    '.html',
    '.js',
    '.mcwebhelp',
    '.props',
    '.png',
    '.jpeg',
    '.xml',
    '.qml',
    '.qmlc',
    '.mui',
    '.exe',
    '.dll',
    '.xrm-ms',
    '.asp',
    '.aspx',
    '.tmSnippet',
    '.dotx',
    '.h',
    '.idl',
    '.snippet',
    '.cdp',
    '.browser',
    '.cache',
    '.bin',
    '.gif',
    '.cs',
    '.pm',
    '.spdata',
    '.webpart',
    '.ascx',
    '.ascx.cs',
    '.ascx.designer.cs',
    '.vb',
    '.cshtml',
    'ascx.pp',
}

blacklisted_filenames = {
    '',
}

default_wallet_names = [
    r'default_wallet\w+',
    r'wallet_\d+',
    r'wallet',
    r'cash',
    r'cash.+',
    r'seed+',
    r'money+'
    r'crypto+'
    #r'bitcoin\w+'
]


# MD5 function.
def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

# Create dir if not exists.
def check_case_dir_exists(examiner_name, case_ref, exhibit_ref, description):
    path = os.getcwd() + "\\cases\\%s %s %s %s" % (examiner_name, case_ref, exhibit_ref, description)
    os.makedirs(path)

# Full system scan for wallet names and crypto regex.
def fetch_wallets_win(examiner_name, case_ref, exhibit_ref, description):
    usb_path = os.getcwd() + "\\cases\\%s %s %s %s\\" % (examiner_name, case_ref, exhibit_ref, description)
    # Save report to text file location on Triage drive.
    current_time = datetime.datetime.now()
    sys.stdout = open('%s%s_%s_%s_%s_%s_%s %s %s %s %s Triage report.txt' % (usb_path, current_time.day, current_time.month, current_time.year, current_time.hour, current_time.minute, current_time.second, examiner_name, case_ref, exhibit_ref, description), 'w')
    # Fetch from default locations stored on windows.
    dir_users = os.listdir('C:\\Users\\')
    # Append all profile names to regex list.
    for user in dir_users:
        default_wallet_names.append(user)

    for user in dir_users:
        # Some crypto wallets have the computer name as the wallet file name.
        path = os.getcwd() + "\\cases\\%s %s %s %s\\" % (examiner_name, case_ref, exhibit_ref, description)
        default_wallets_win = {
            'electrum': 'C:\\Users\\' + user + '\\AppData\\Roaming\\Electrum\\wallets',
            'electrum_testnet': 'C:\\Users\\' + user + '\\AppData\\Roaming\\Electrum\\testnet\\wallets',
            'bitcoin_core': 'C:\\Users\\' + user + '\\AppData\\Roaming\\Bitcoin\\wallets',
            'bitcoin_core_testnet': 'C:\\Users\\' + user + '\\AppData\\Roaming\\Bitcoin\\testnet3\\wallets',
            'monero': 'C:\\Users\\' + user + '\\Documents\\Monero\\wallets\\',
            'litecoin': 'C:\\Users\\' + user +'\\AppData\\Roaming\\Litecoin\\wallets'
        }

        default_electrum_dir = os.path.isdir(default_wallets_win['electrum'])
        default_electrum_test_dir = os.path.isdir(default_wallets_win['electrum_testnet'])
        default_bitcoin_core_dir = os.path.isdir(default_wallets_win['bitcoin_core'])
        default_bitcoin_core_test_dir = os.path.isdir(default_wallets_win['bitcoin_core_testnet'])
        default_litecoin_dir = os.path.isdir(default_wallets_win['litecoin'])
        default_monero_dir = os.path.isdir(default_wallets_win['monero'])

        if (default_electrum_dir == True):
            current_time = datetime.datetime.now()
            print("%s : Electrum installed on system for user %s!" % (current_time, user))
            try:
                shutil.copytree(default_wallets_win['electrum'], path + 'wallets\\' + user + '\\electrum')
            except shutil.Error:
                print('Please run crypto scrape, as admin!')
        else:
            current_time = datetime.datetime.now()
            print("%s : Electrum not installed for user %s!" % (current_time, user))

        if (default_electrum_test_dir == True):
            current_time = datetime.datetime.now()
            print("%s : Electrum (Testnet) installed on system for user %s!" % (current_time, user))
            try:
                shutil.copytree(default_wallets_win['electrum_testnet'], path + 'wallets\\' + user + '\\electrum_testnet')
            except shutil.Error:
                print('Please run crypto scrape, as admin!')
        else:
            current_time = datetime.datetime.now()
            print("%s : Electrum not installed for user %s!" % (current_time, user))

        if (default_bitcoin_core_dir == True):
            current_time = datetime.datetime.now()
            print("%s : Bitcoin core installed on system for user %s! Copying wallets!" % (current_time, user))
            try:
                shutil.copytree(default_wallets_win['bitcoin_core'], path + 'wallets\\' + user + '\\bitcoin_core')
            except shutil.Error:
                print('Please run crypto scrape, as admin!')
        else:
            current_time = datetime.datetime.now()
            print("%s : Bitcoin core not installed for user %s!" % (current_time, user))

        if (default_bitcoin_core_test_dir == True):
            current_time = datetime.datetime.now()
            print("%s : Bitcoin core (Testnet) installed on system for user %s! Copying wallets!" % (current_time, user))
            try:
                shutil.copytree(default_wallets_win['bitcoin_core_testnet'], path + 'wallets\\' + user + '\\bitcoin_core_testnet')
            except shutil.Error:
                print('Please run crypto scrape, as admin!')
                break
        else:
            current_time = datetime.datetime.now()
            print("%s : Bitcoin (Testnet) core not installed for user %s!" % (current_time, user))

        if (default_monero_dir == True):
            current_time = datetime.datetime.now()
            print("%s : Monero installed on system for user %s! Copying wallets!" % (current_time, user))
            try:
                shutil.copytree(default_wallets_win['monero'], path + 'wallets\\' + user + '\\monero')
            except shutil.Error:
                print('Please run crypto scrape, as admin!')
                break
        else:
            current_time = datetime.datetime.now()
            print("%s : Monero core not installed for user %s!" % (current_time, user))

        if (default_litecoin_dir == True):
            current_time = datetime.datetime.now()
            print("%s : Litecoin installed on system for user %s! Copying wallets!" % (current_time, user))
            try:
                shutil.copytree(default_wallets_win['litecoin'], path + 'wallets\\' + user + '\\litecoin')
            except shutil.Error:
                print('Please run crypto scrape, as admin!')
                break
        else:
            current_time = datetime.datetime.now()
            print("%s : Litecoin is not installed for user %s!" % (current_time, user))

    # http://code.activestate.com/recipes/580737-get-disk-partition-information-with-psutil-cross-p/
    # Scans and searches common document files for addresses.
    # Get list of drives on computer.
    
    os.makedirs(usb_path + 'potential_wallets')
    #os.makedirs(usb_path + 'addresses')
    dps = psutil.disk_partitions()
    for i in range(len(dps)):
        dp = dps[i]
        for path, dirs, files in os.walk(dp.device):
            #print(path)
            for f in files:
                filename, file_extension = os.path.splitext(f)
                if file_extension in blacklisted_extentions:
                    break
                for r in default_wallet_names:
                    regex = re.compile(r)
                    #print(f)
                    if re.match(regex, f) is not None:
                        usb_drive = os.path.splitdrive(os.getcwd())
                        usb_drive = usb_drive[0].upper() + '\\'
                        if (dp.device == usb_drive):
                            pass
                        else:
                            file_path = path + '\\' + f
                            try:
                                md5_hash = md5(file_path)
                            except:
                                print('Please run Crypto Scrape as Administrator!')
                            
                            if os.path.isfile(usb_path + 'potential\\' + f):
                                print('Duplicate of %s ' % (f))
                            else:
                                current_time = datetime.datetime.now()
                                print('%s : %s\\%s found! Copying' % (current_time, path, f))
                                try:
                                    os.makedirs(usb_path + 'potential_wallets\\' + md5_hash)
                                    shutil.copy2(path + '\\' + f, usb_path + 'potential_wallets\\' + md5_hash + '\\' + f)
                                except FileExistsError:
                                    print('%s : %s\\%s duplicate found!' % (current_time, path, f))