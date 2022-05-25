
# SignAndVerify
Simple python script for signing and verifying signed documents with RSA

'Main.py' is the executable file, it is a GUI for user to choose between *Sender* and *Receiver* interface. <br>
'Alice.py' is a program for: generating random bitsm, generating private and public RSA key, signing document with key.<br>
'Bob.py' is a program for veryfing signed document.<br>
Two sample files are provided: 'new_york.png' which is the document to sign and 'nba.mp4' which is video sequence used to generate random bits. <br>
Program generates: 'pubkey.pem' which is a public key used in 'Bob.py' and 'signed.txt' which is signed input file in 'Alice.py'.
