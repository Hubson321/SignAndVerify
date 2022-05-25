from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
import easygui

#Get SHA3 hashValue
def SHA3(filename):
  file = open(filename,'rb').read()
  return SHA256.new(file)

#Verify certificate
def verifyCertificate(originalFile,certificateFile,publicKeyFile):
    '''
    Verify signed file. \n
    Args: \n
        originalFile    - original file that was signed by sender \n
        certificateFile - signed file by sender \n
        publicKeyFile   - public key file in pem format
    
    '''
    
    certificate = open(certificateFile,'rb').read()
    publicKeyFile = open(publicKeyFile,'rb')
    publicKey = RSA.import_key(publicKeyFile.read())
    
    verification = PKCS1_v1_5.new(publicKey)
    
    if verification.verify(SHA3(originalFile),certificate):
        easygui.msgbox("Signature is valid")
    else:
        easygui.msgbox("Signature is invalid")
        
        
def GUI():

    easygui.msgbox("Choose original file")#,"Choose original file",["Ok","Exit"])
    original_file = easygui.fileopenbox(title="Choose original file")
    easygui.msgbox("Choose signature file")#,"Choose signature file",["Ok","Exit"])
    certificate_file = easygui.fileopenbox(title="Choose signature file")
    easygui.msgbox("Choose public key file")#,"Choose public key file",["Ok","Exit"])
    publicKey_file = easygui.fileopenbox(title="Choose public key file")
    
    verifyCertificate(original_file,certificate_file,publicKey_file)     
       





