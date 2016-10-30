# -*- coding: utf-8 -*- 
# tekKartPc.com
# twitter.com/tekKartPc
# facebook.com/tekKartPc
# -------------
# buzzer çalıştırma için önce
# gerekli bağlantıyı yapınız.
# detaylı bilgi için http://tekkartpc.com/raspberry-pi-ile-led-yakmak-ve-buzzer-calistirmak/ adresini ziyaret edip sorularınızı sorabilirsiniz.

import RPi.GPIO as GPIO
import time

hangiPin = 18

GPIO.setmode(GPIO.BOARD)
GPIO.setup(hangiPin,GPIO.OUT)

try:

	while True:

		GPIO.output(hangiPin,True)
 		time.sleep(1)
 		GPIO.output(hangiPin,False)
 		time.sleep(1)

except KeyboardInterrupt: 
#cikis yapildi
	GPIO.output(hangiPin,False)
	print("buzzer uygulamasindan cikis yapildi")
finally:
	GPIO.cleanup()
