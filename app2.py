import gtts
#import winsound
from pydub import AudioSegment
from pydub.playback import play

import PyPDF2

from PIL import Image

import os, sys

import time


def abre_imagem(im, imdir):

    # open method used to open different extension image file 
    im = Image.open(imdir+'/'+im+'.png')  
    
    # This method will show image in any image viewer  
    im.show()  

def falar(texto, lang='pt'):

    textos = texto.split("(pausa)")

    for t in textos:
        
        t = t.replace('(pausa)', '')

        tts = gtts.gTTS(text=t, lang=lang)
        tts.save("rec.mp3")
        print ("Playing sound ...")
        #winsound.PlaySound("rec.wav", winsound.SND_FILENAME)
        song = AudioSegment.from_mp3("rec.mp3")
        play(song)

        time.sleep(1)

def main():
    imdir = '/home/netpartners/Downloads/py_leitor/imagens'
    imagens = os.listdir(imdir)
    
    with open('/home/netpartners/Downloads/py_leitor/rnns.txt', 'r') as file:
        data = file.read().replace('\n', '')

        paginas = data.split('(fim)')
        N = len(paginas)
        
        for k in range(N):
            
            texto = paginas[k]
            im = imagens[k]
            
            abre_imagem(im=str(k+1), imdir=imdir)

            falar(texto=texto)
            time.sleep(1)
        

if __name__ == '__main__':
    main()