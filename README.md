
# SignAndVerify
Simple python script for signing and verifying signed documents with RSA

[Main.py](Main.py) is the executable file, it is a GUI for user to choose between *Sender* and *Receiver* interface. <br>
[Alice.py](Alice.py) is a program for: generating random bitsm, generating private and public RSA key, signing document with key.<br>
[Bob.py](Bob.py) is a program for veryfing signed document.<br>
Two sample files are provided: [new_york](new_york.jpg) which is the document to sign and nba_sequence which is video sequence used to generate random bits. (Provided in latest Issue). But any file can be signed and any video file can be used to genearte RSA keys (videos must be longer than 1/2 minutes) <br>
Program generates: 'pubkey.pem' which is a public key used in [Bob.py](Bob.py) and [signed](signed.txt) which is signed input file in [Alice.py](Alice.py)

/Hubson321/SignAndVerify/releases/latest/download/nba_sequence.mp4
