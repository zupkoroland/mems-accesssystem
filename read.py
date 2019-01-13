import RPi.GPIO as GPIO
import MFRC522
import sys
import os
import time
import led2 as LED2
import sql as SQL

#208 147 83 37 53 (Fehér)
#137 12 86 211 0 (Kék)

GPIO.setwarnings(False)

## Itt ellenőrzöm a kártyát
def checkCardID(cardID):
    #Eltárolom stringbe az azonostót.
    cardInputString = str(cardID[0]) + str(cardID[1]) + str(cardID[2]) + str(cardID[3]) + str(cardID[4])
    stringDateTime = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
    
    #Itt majd adatbázis kell!!
    if SQL.queryCards(cardInputString) == 1:
        print ("Belepes engedélyezve!", stringDateTime, end="")
        LED2.ledOut2(35)
        SQL.uploadLogs(cardInputString, stringDateTime)
    else:
        print ("Belepes elutasitva!",  stringDateTime, end="")
        LED2.ledOut2(32)
        SQL.uploadLogs(cardInputString, stringDateTime)
    #Két sec altatás, hogy ne tudjon gyorsan ovlasni.
    time.sleep(1)

#mfrc = MFRC522.MFRC522()

def loop():
	global mfrc
	while(True):
		inCmd = "olvass"
		#print (inCmd)
		if (inCmd == "olvass"):
			#print ("Scanning ... ")
			mfrc = MFRC522.MFRC522()
			isScan = True
			while isScan:
				# Scan for cards    
                                (status,TagType) = mfrc.MFRC522_Request(mfrc.PICC_REQIDL)
				# If a card is found
				#if status == mfrc.MI_OK:
					#print ("Card detected")
				# Get the UID of the card
                                (status,uid) = mfrc.MFRC522_Anticoll()				
				# If we have the UID, continue
                                if status == mfrc.MI_OK:
					#print ("Card UID: "+ str(map(hex,uid)))
                                    print ("olvastam!")
                                    map(hex,uid)
                                    checkCardID(uid)
                                    
loop()
GPIO.cleanup()