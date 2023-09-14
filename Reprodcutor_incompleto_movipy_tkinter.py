import tkinter as tk 
from tkvideo import tkvideo
from moviepy.editor import VideoFileClip, clips_array

class pagina_principal( tk.Tk ): 

    def __init__(self): 

        super().__init__()

        self.title("Reproductor y editor de video")
        self.geometry("1500x1500")

        #Instancia de frames dentro de la raiz

        f1=FrameA_contenedor_de_video(self)

        f2=FrameB_controles_de_video(self)


class FrameA_contenedor_de_video(tk.Frame): 

    def __init__(self,raiz): 

        super().__init__(raiz)
        
        self.config(bg = "red" , width = "1000", height = "1000")
        self.pack(side="left")

        #Reproduccion del video 

        self.etiqueta=tk.Label(self,text="Etiqueta")
        self.etiquetaB=tk.Label(self, text= "Etiqueta B")
        #self.etiqueta.size((200,200))

        self.etiqueta.place(x = 0, y = 0)
        self.etiquetaB.place(x = 0, y = 20)
       
        #player = tkvideo( 'PAPELEO INICIO DE EMPRESA.mp4',self.etiquetaB, loop=1 , size = ( 200, 200 ) )

        clip1 = VideoFileClip('huracan.mp4').subclip(15,30) 

        clip1.write_videofile('huracan2.mp4')

        player = tkvideo( 'huracan2.mp4',self.etiquetaB, loop=1 , size = ( 200, 200 ) )

        #player.

        #print(player)

        player.play()


class FrameB_controles_de_video(tk.Frame):

    def __init__ (self, raiz): 

        super().__init__(raiz)

        self.config(bg="blue",width="500",height="1500")

        self.pack(side="left")
        
        #Creacion de botones e indicadores del corte/minuto

        tk.Button(self,text = "PAUSE").place(x=93,y=30)

        tk.Button(self,text ="Marca A").place(x=87,y=80)
        
        tk.Entry(self).place(x=50,y=110)

        tk.Button(self, text="Marca B").place(x=87,y=140)

        tk.Entry(self).place(x=50,y=170)

        tk.Button(self, text= "CORTAR").place(x=90,y=200)

#Instancia de la clase 

App = pagina_principal()

App.mainloop()
