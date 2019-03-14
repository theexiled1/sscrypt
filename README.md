# SSCrypt
SSCrypt is my custom encryption algorithm in which uses mathematical equations to securely encrypt your data precluding it from being scrutinized without your custom key.

### Encrypt Data:
```
>>> import sscrypt
>>> sscrypt.encrypt(data,key)
>>> sscrypt.decrypt(encrypted data,key)
```
### Encrypt Files:
```
>>> import sscrypt
>>> sscrypt.encrypt_file(file,key)
>>> sscrypt.decrypt_file(file,key)
```
