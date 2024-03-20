# Certificates
All you need to know about certificates (CA).


## Files
```sh
.
├── ca-private.pem          # Private key for ROOT CA
├── ca.crt                  # ROOT CA
├── server.pem              # Private key for server
├── server.csr              # Certificate Signing Request (server -> ROOT)          
├── server.crt              # Generated Certificate (user cert)
└── server.srl              # Contains certificate serial number
```


## OPENSSL

<details>
<summary>

```sh
# Check openssl information
openssl version -a
```
</summary>

```sh
# Result
OpenSSL 1.1.1l  24 Aug 2021
built on: Tue Aug 24 14:48:55 2021 UTC
platform: Msys-x86_64
options:  bn(64,64) rc4(16x,int) des(int) blowfish(ptr)
compiler: gcc  -march=x86-64 -mtune=generic -O2 -pipe -DTERMIOS -DL_ENDIAN -DOPENSSL_PIC -DOPENSSL_CPUID_OBJ -DOPENSSL_IA32_SSE2 -DOPENSSL_BN_ASM_MONT -DOPENSSL_BN_ASM_MONT5 -DOPENSSL_BN_ASM_GF2m -DSHA1_ASM -DSHA256_ASM -DSHA512_ASM -DKECCAK1600_ASM -DRC4_ASM -DMD5_ASM -DAESNI_ASM -DVPAES_ASM -DGHASH_ASM -DECP_NISTZ256_ASM -DX25519_ASM -DPOLY1305_ASM -DZLIB -DNDEBUG
OPENSSLDIR: "/usr/ssl"
ENGINESDIR: "/usr/lib/openssl/engines-1.1"
Seeding source: os-specific
```
</details>


## Root Certification authority (CA)

<details>
<summary>

```sh
# Create Private key for Root CA - ca.key
openssl genrsa -out ca-private.pem 2048
```
</summary>

```sh
# Result - cat ca-private.pem
-----BEGIN RSA PRIVATE KEY-----
<private key>
-----END RSA PRIVATE KEY-----
```
</details>

<details>
<summary>

```sh
# Generate CA cert - ca.key
openssl req -new -x509 -sha256 -key ca-private.pem -out ca.crt
```
</summary>

```sh
# Information
Country Name (2 letter code) [AU]:.
State or Province Name (full name) [Some-State]:.
Locality Name (eg, city) []:.
Organization Name (eg, company) [Internet Widgits Pty Ltd]:.
Organizational Unit Name (eg, section) []:.
Common Name (e.g. server FQDN or YOUR name) []:TEST-CA
Email Address []:.
```

```sh
# Result - openssl x509 -in ca.crt -text
Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number:
            4b:70:a6:38:bb:06:be:fd:41:76:54:ce:08:7c:16:49:d7:c9:58:66
        Signature Algorithm: sha256WithRSAEncryption
        Issuer: CN = TEST-CA
        Validity
            Not Before: Mar 20 15:55:46 2024 GMT
            Not After : Apr 19 15:55:46 2024 GMT
        Subject: CN = TEST-CA
        Subject Public Key Info:
            Public Key Algorithm: rsaEncryption
                RSA Public-Key: (2048 bit)
                Modulus:
                    00:dd:6d:4c:80:e1:9b:56:1f:58:e4:35:05:cd:2b:
                    53:3f:8f:19:54:01:e9:1a:26:fc:67:6e:b5:a7:b4:
                    68:fa:38:f3:ed:b0:c4:af:81:af:fe:f0:d2:0b:b0:
                    47:77:48:f4:65:7f:41:56:59:aa:fe:50:60:3c:2f:
                    c6:3c:b5:b3:ee:93:29:a5:ae:49:80:a3:31:21:0a:
                    38:a9:09:5e:71:91:c4:4a:94:16:07:47:cc:2b:45:
                    fd:ac:6e:9d:12:53:ca:7a:41:99:08:14:cc:67:f4:
                    14:89:42:29:4b:5b:a6:87:50:47:fb:a9:f6:66:90:
                    d5:1e:b8:20:0f:18:0c:f5:f7:0e:cc:b5:f0:ed:25:
                    86:b7:3a:3b:92:60:d4:06:00:19:7b:c1:5e:33:ee:
                    d8:bf:06:2c:f2:26:0e:d0:99:87:0b:5d:e2:02:ef:
                    d4:a0:f6:f2:80:f7:ae:47:7c:e1:aa:62:04:0a:04:
                    33:54:47:96:08:5b:f1:4e:92:b8:46:91:8f:48:49:
                    61:01:d0:32:9c:07:45:85:dd:9e:3e:ef:c7:73:d5:
                    30:ca:bd:62:96:60:75:31:e4:27:86:20:6b:bd:92:
                    cc:f6:ea:06:20:0e:82:69:1e:ac:8b:9c:cb:e3:f3:
                    49:83:33:d5:4b:6b:e2:87:0f:a0:cd:56:c7:59:2d:
                    bc:71
                Exponent: 65537 (0x10001)
        X509v3 extensions:
            X509v3 Subject Key Identifier:
                CF:79:D8:E0:4C:FD:24:05:A8:11:78:A4:48:AD:84:33:94:87:6A:D1
            X509v3 Authority Key Identifier:
                keyid:CF:79:D8:E0:4C:FD:24:05:A8:11:78:A4:48:AD:84:33:94:87:6A:D1

            X509v3 Basic Constraints: critical
                CA:TRUE
    Signature Algorithm: sha256WithRSAEncryption
         cb:14:36:97:0a:f2:c7:d6:0d:f1:02:87:9d:7a:e7:91:e0:fb:
         1e:c1:1d:6e:ad:83:ac:5d:9a:c2:3d:3d:48:99:20:2b:00:d9:
         fe:01:bd:87:e4:39:3e:96:ff:81:d4:a9:85:a9:9b:5c:c0:06:
         62:29:e5:1e:5b:60:42:66:76:2f:92:9f:28:96:a7:c5:21:e8:
         26:31:7c:df:f4:c3:9d:2a:1e:14:8f:0c:cf:22:0c:2e:c7:a7:
         74:19:c3:d6:57:91:f0:f8:37:48:7b:b8:eb:26:4f:93:e2:82:
         b9:14:c1:b5:8e:19:bf:26:72:55:64:27:21:59:4e:0a:81:1f:
         35:4d:aa:6c:b0:95:c2:62:81:91:7d:e9:fa:95:30:4c:6a:c0:
         3b:d6:d5:0a:a8:35:62:1f:f2:41:49:f4:4b:89:5d:c6:6c:1d:
         43:90:85:13:95:b9:a2:ac:4d:1f:92:74:4e:0c:f2:1f:78:2f:
         77:4c:c5:3f:0c:1a:7b:4c:4d:85:ab:dc:a5:78:c7:f0:e9:54:
         62:f6:a1:e2:6f:b0:21:b2:46:24:28:b7:01:47:7b:53:78:17:
         80:e8:54:a7:ff:c9:11:53:eb:d3:92:e0:63:99:f6:9b:16:9d:
         c4:fc:7d:e3:e4:4d:d4:d5:70:09:0f:c0:31:88:25:b7:e9:bd:
         c9:00:df:f9
-----BEGIN CERTIFICATE-----
MIIDBTCCAe2gAwIBAgIUS3CmOLsGvv1BdlTOCHwWSdfJWGYwDQYJKoZIhvcNAQEL
BQAwEjEQMA4GA1UEAwwHVEVTVC1DQTAeFw0yNDAzMjAxNTU1NDZaFw0yNDA0MTkx
NTU1NDZaMBIxEDAOBgNVBAMMB1RFU1QtQ0EwggEiMA0GCSqGSIb3DQEBAQUAA4IB
DwAwggEKAoIBAQDdbUyA4ZtWH1jkNQXNK1M/jxlUAekaJvxnbrWntGj6OPPtsMSv
ga/+8NILsEd3SPRlf0FWWar+UGA8L8Y8tbPukymlrkmAozEhCjipCV5xkcRKlBYH
R8wrRf2sbp0SU8p6QZkIFMxn9BSJQilLW6aHUEf7qfZmkNUeuCAPGAz19w7MtfDt
JYa3OjuSYNQGABl7wV4z7ti/BizyJg7QmYcLXeIC79Sg9vKA965HfOGqYgQKBDNU
R5YIW/FOkrhGkY9ISWEB0DKcB0WF3Z4+78dz1TDKvWKWYHUx5CeGIGu9ksz26gYg
DoJpHqyLnMvj80mDM9VLa+KHD6DNVsdZLbxxAgMBAAGjUzBRMB0GA1UdDgQWBBTP
edjgTP0kBagReKRIrYQzlIdq0TAfBgNVHSMEGDAWgBTPedjgTP0kBagReKRIrYQz
lIdq0TAPBgNVHRMBAf8EBTADAQH/MA0GCSqGSIb3DQEBCwUAA4IBAQDLFDaXCvLH
1g3xAoedeueR4PsewR1urYOsXZrCPT1ImSArANn+Ab2H5Dk+lv+B1KmFqZtcwAZi
KeUeW2BCZnYvkp8olqfFIegmMXzf9MOdKh4UjwzPIgwux6d0GcPWV5Hw+DdIe7jr
Jk+T4oK5FMG1jhm/JnJVZCchWU4KgR81TapssJXCYoGRfen6lTBMasA71tUKqDVi
H/JBSfRLiV3GbB1DkIUTlbmirE0fknRODPIfeC93TMU/DBp7TE2Fq9yleMfw6VRi
9qHib7AhskYkKLcBR3tTeBeA6FSn/8kRU+vTkuBjmfabFp3E/H3j5E3U1XAJD8Ax
iCW36b3JAN/5
-----END CERTIFICATE-----
```

```sh
-----BEGIN CERTIFICATE-----
<CERTIFICATE>
-----END CERTIFICATE-----
```

</details>

## Certificate Signing Request 
```sh
# Create Private key for Server cert - ca.key
openssl genrsa -out server.pem 2048
```

<details>
<summary>

```sh
# Create Certificate Signing Request
openssl req -new -sha256 -key server.pem -out server.csr -subj "/CN=TEST-SERVER"
```
</summary>

```sh
# Result - cat server.csr
-----BEGIN CERTIFICATE REQUEST-----
<Certificate Signing Request>
-----END CERTIFICATE REQUEST-----
```

```sh
# Verify CSR
openssl req -text -in server.csr -noout -verify
```
</details>

## Process a Certificate Signing Request (CSR) on the Root Certificate Authority (CA)

<details>
<summary>

```sh
# Signed certificate
openssl x509 -req -in server.csr -CA ca.crt -CAkey ca-private.pem -CAcreateserial -out server.crt -days 1000 -sha256
```
</summary>

```sh
# Result - cat ca.srl - serial number for certs
1991C2A2206BA968A6C091F03B1406DCF462EF55
```
```sh
# Result - openssl x509 -in server.crt -text
Certificate:
    Data:
        Version: 1 (0x0)
        Serial Number:
            19:91:c2:a2:20:6b:a9:68:a6:c0:91:f0:3b:14:06:dc:f4:62:ef:55
        Signature Algorithm: sha256WithRSAEncryption
        Issuer: CN = TEST-CA
        Validity
            Not Before: Mar 20 16:15:48 2024 GMT
            Not After : Dec 15 16:15:48 2026 GMT
        Subject: CN = TEST-SERVER
        Subject Public Key Info:
            Public Key Algorithm: rsaEncryption
                RSA Public-Key: (2048 bit)
                Modulus:
                    00:e7:4a:dc:cd:ef:da:04:13:6e:5f:9d:19:f2:57:
                    ac:2d:6f:9d:7d:db:56:f4:79:41:a9:fb:c0:2b:b4:
                    a6:e8:c0:b7:c0:16:dc:ba:a5:10:ac:41:15:26:ec:
                    11:82:15:ab:33:58:31:ed:8b:e4:59:f3:fa:ce:32:
                    43:2e:36:cf:14:66:e6:0a:be:c8:ec:aa:46:2e:d6:
                    f1:54:c3:27:e5:7f:15:b0:be:e2:27:b2:bc:4d:1b:
                    c7:0a:f7:87:ab:0b:ac:54:cf:61:d5:58:30:a2:6b:
                    30:54:38:94:de:d5:5e:01:82:ed:c7:d7:a9:54:96:
                    b1:1b:50:a9:f3:53:38:81:49:cc:df:a9:3f:80:32:
                    0a:3c:63:5d:64:2b:08:68:89:24:05:97:98:07:0d:
                    08:db:77:9e:7f:34:6a:bb:e4:12:dc:b3:e9:2c:05:
                    42:10:bd:67:57:a0:b3:5e:3c:db:ef:3f:17:e0:68:
                    09:57:d7:fd:6a:b8:ad:d4:64:b1:56:73:11:34:60:
                    6a:59:4e:f1:f6:dc:6d:a4:b0:d5:2a:95:f2:22:f4:
                    a1:a3:33:2f:da:51:07:99:9d:38:df:73:82:4f:b4:
                    ae:21:ab:de:09:90:c0:d8:c9:8a:cf:0a:fd:94:b5:
                    8a:91:1e:0f:26:e6:81:13:80:e3:65:64:ab:a7:2d:
                    1d:43
                Exponent: 65537 (0x10001)
    Signature Algorithm: sha256WithRSAEncryption
         0b:8b:1f:22:b2:d8:a2:dd:e3:71:c0:be:0e:ad:96:f9:d8:4f:
         e4:e2:7e:7b:a7:bd:30:d1:0f:fb:06:38:d1:cb:b8:ef:bd:e6:
         22:42:ce:ed:2c:8c:de:6a:1d:7d:f1:b2:80:df:6e:61:c5:6b:
         cb:58:69:88:0f:e5:38:9f:cb:13:d6:87:70:3b:1c:b0:7d:fd:
         bf:ac:8f:22:46:28:29:f2:27:39:27:18:14:6d:0d:ff:0e:98:
         3e:89:8b:8e:10:50:8e:7c:6f:43:98:20:92:78:48:fd:97:41:
         cf:3b:8a:df:97:02:27:4e:39:5c:65:da:31:76:aa:c4:92:18:
         55:8d:67:aa:65:e5:de:13:f5:78:6d:45:4a:9f:f5:f8:19:30:
         1d:71:2b:3a:82:3c:e6:ee:3f:e0:5d:30:7c:8b:35:4d:67:ce:
         46:85:c2:5a:be:ce:f2:d2:f6:83:11:90:ad:48:c4:36:8f:ef:
         82:18:37:38:ba:3c:a6:b1:e9:a8:0d:bf:90:1d:ff:1e:d6:11:
         ba:65:78:33:fc:3f:ce:af:68:80:8b:d0:8c:4d:6e:8a:88:89:
         02:98:ce:3d:31:04:b3:1a:06:c4:40:d0:43:10:c3:f0:40:ac:
         3c:0e:d8:c2:c3:e7:f5:d3:a3:9d:5e:6d:21:5f:90:ce:76:b4:
         51:d6:a7:02
-----BEGIN CERTIFICATE-----
MIICrzCCAZcCFBmRwqIga6lopsCR8DsUBtz0Yu9VMA0GCSqGSIb3DQEBCwUAMBIx
EDAOBgNVBAMMB1RFU1QtQ0EwHhcNMjQwMzIwMTYxNTQ4WhcNMjYxMjE1MTYxNTQ4
WjAWMRQwEgYDVQQDDAtURVNULVNFUlZFUjCCASIwDQYJKoZIhvcNAQEBBQADggEP
ADCCAQoCggEBAOdK3M3v2gQTbl+dGfJXrC1vnX3bVvR5Qan7wCu0pujAt8AW3Lql
EKxBFSbsEYIVqzNYMe2L5Fnz+s4yQy42zxRm5gq+yOyqRi7W8VTDJ+V/FbC+4iey
vE0bxwr3h6sLrFTPYdVYMKJrMFQ4lN7VXgGC7cfXqVSWsRtQqfNTOIFJzN+pP4Ay
CjxjXWQrCGiJJAWXmAcNCNt3nn80arvkEtyz6SwFQhC9Z1egs1482+8/F+BoCVfX
/Wq4rdRksVZzETRgallO8fbcbaSw1SqV8iL0oaMzL9pRB5mdON9zgk+0riGr3gmQ
wNjJis8K/ZS1ipEeDybmgROA42Vkq6ctHUMCAwEAATANBgkqhkiG9w0BAQsFAAOC
AQEAC4sfIrLYot3jccC+Dq2W+dhP5OJ+e6e9MNEP+wY40cu4773mIkLO7SyM3mod
ffGygN9uYcVry1hpiA/lOJ/LE9aHcDscsH39v6yPIkYoKfInOScYFG0N/w6YPomL
jhBQjnxvQ5ggknhI/ZdBzzuK35cCJ045XGXaMXaqxJIYVY1nqmXl3hP1eG1FSp/1
+BkwHXErOoI85u4/4F0wfIs1TWfORoXCWr7O8tL2gxGQrUjENo/vghg3OLo8prHp
qA2/kB3/HtYRumV4M/w/zq9ogIvQjE1uioiJApjOPTEEsxoGxEDQQxDD8ECsPA7Y
wsPn9dOjnV5tIV+Qzna0UdanAg==
-----END CERTIFICATE-----
```

```sh
# cat server.crt
-----BEGIN CERTIFICATE-----
<SERVER CRT>
-----END CERTIFICATE-----
```
</details>


```sh
# Verify User Certificate with CA
openssl verify -check_ss_sig -CAfile ca.crt server.crt 
# Result: server.crt: OK
```

Resource
 - [Add certificate to keystore](https://stackoverflow.com/questions/16062072/how-to-add-certificate-chain-to-keystore)
 - [Certificate order in truststore](https://stackoverflow.com/questions/52400491/do-i-need-to-import-ssl-chain-in-order)
 - [Check openssl version](https://phoenixnap.com/kb/how-to-check-openssl-version)
 - [Install root certificates](https://docs.devolutions.net/kb/general-knowledge-base/install-root-certificates/)
 - [Generate CA](https://docs.devolutions.net/kb/general-knowledge-base/secure-self-signed-certificates/)
 - [Check public key certificate 1](https://security.stackexchange.com/questions/261430/check-public-key-certificate)
 - [Check public key certificate 2](https://developers.yubico.com/PIV/Guides/Generating_keys_using_OpenSSL.html)
 - [OpenSSL guide](https://www.digicert.com/kb/ssl-support/openssl-quick-reference-guide.htm)
 - [Openssl Documentation](https://manpages.ubuntu.com/manpages/noble/en/man1/openssl.1ssl.html)
 - [Verify Certificate Chain](https://stackoverflow.com/questions/25482199/verify-a-certificate-chain-using-openssl-verify)