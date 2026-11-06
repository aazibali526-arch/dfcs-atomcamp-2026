# Task B4: OpenSSL Encryption and the Salted__ Header

## What I did

I encrypted a text file with AES-256 using OpenSSL, then inspected the first bytes of the encrypted file with `xxd` to understand the header OpenSSL writes.

## Step 1: Encrypt the file

```bash
echo 'my secret message' > secret.txt
openssl enc -aes-256-cbc -salt -pbkdf2 -in secret.txt -out secret.enc
```

![Encrypt command](screenshots/b4-encrypt-command.png)

**What this proves:** The file `secret.txt` was encrypted with AES-256-CBC using a password. `-salt` adds a random salt, and `-pbkdf2` uses the modern method to turn the password into a key.

## Step 2: Look inside the encrypted file

```bash
ls -l secret.txt secret.enc
xxd -l 16 secret.enc
file secret.enc
```

Output:

```
┌──(aazib㉿aazib)-[~/DFCS/s01-Foundation/b4-work]
└─$ xxd -l 16 secret.enc
00000000: 5361 6c74 6564 5f5f e722 b7dd 92d2 278d  Salted__."....'.
```

![xxd output](screenshots/b4-xxd-output.png)

**What this proves:** The first 8 bytes of the file are the text `Salted__`, and `file` recognises the file as OpenSSL encrypted data with a salted password.

## What Salted__ means

The 8 characters "Salted__" serve as the OpenSSL magic header (label).

The subsequent 8 bytes represent the random salt visible in the remaining bytes of xxd -l 16.

This is not a secret; its sole purpose is to inform the decryption process which salt to use.

In digital forensics, "Salted__" and the file command are used to identify unknown binary blobs.
