
# SignAndVerify
Simple python script for signing and verifying signed documents with RSA

[Main.py](Main.py) is the executable file, it is a GUI for user to choose between *Sender* and *Receiver* interface. <br>
[Alice.py](Alice.py) is a program for: generating random bitsm, generating private and public RSA key, signing document with key.<br>
[Bob.py](Bob.py) is a program for veryfing signed document.<br>
Two sample files are provided: [new_york](new_york.jpg) which is the document to sign and [nba_sequence](nba_sequence.mp4) which is video sequence used to generate random bits. (Provided in Issues Tab) <br>
Program generates: 'pubkey.pem' which is a public key used in [Bob.py](Bob.py) and [signed](signed.txt) which is signed input file in [Alice.py](Alice.py)
