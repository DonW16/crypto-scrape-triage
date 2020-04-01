# crypto-scrape-triage
A Windows cryptocurrency triage tool, to help find wallets and seeds on windows systems and copies them onto the removable media you're running ```crypto-scrape-triage.exe``` from.


## Downloads
For binaries

## How does it work?
There are two scan modes within this triage tool, ```quick``` and ```full```.

```quick``` goes to common locations where cryptocurrency wallets are setup by default for example.

```C:\\Users\\%USERPROFILE%\\AppData\\Roaming\\Bitcoin\\wallets```

Whereas the ```full``` scan mode itterates the filenames throughout the whole filesystem and using regular expressions compares a the filename to a list of common wallet names such as,

```
r'default_wallet\w+',
r'wallet_\d+',
r'wallet',
r'cash',
r'cash.+',
r'seed+',
r'money+'
r'crypto+'
```

## Supported wallets?
* Electrum
* Bitcoin core
* Monero
* Litecoin