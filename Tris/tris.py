import numpy as np
import pygame
import time

class Mappa:

    def __init__(self):
        self._alt=1 #x o cerchio
        self.__FPS=30 #frame per secondo
        self.__width=700 #larghezza finestra
        self.__heigth=700  #altezza finestra
        self.__font = pygame.font.Font(None, 48) #varie scritte
        self.__circle_win = self.__font.render('O ha vinto', True, (254,0,0))
        pygame.transform.scale(self.__circle_win, (310, 0))
        self.__ics_win = self.__font.render('X ha vinto', True, (0,0,254))
        pygame.transform.scale(self.__ics_win, (310, 0))
        self.__patta = self.__font.render('Patta', True, (0,254,0))
        pygame.transform.scale(self.__patta, (310, 0))
        
        self.__circle = pygame.image.load(r'Image\O.png') #carico l'immagine del cerchio e della x
        self.__ics = pygame.image.load(r'Image\x.png')
        self.__cucciola_circle =  pygame.transform.scale(self.__circle, (60, 60)) #resize
        self.__cucciola_ics = pygame.transform.scale(self.__ics, (80, 60))
        self.__ics = pygame.transform.scale(self.__ics, (120, 100))
        self.__circle = pygame.transform.scale(self.__circle, (100, 100))
        self.__screen = pygame.display.set_mode((self.__width, self.__heigth))
        pygame.display.set_caption("Tic Tac Toe!") #titolo
        
        self._matrice=self._reset() #setto la mappa nello stato iniziale
        self.stampa() #refresh
        self._res=1 #mappa vuota
        
    def stampa(self):
       # blockSize=150 
        black=(0,0,0) #nero
        white=(254,254,254) #bianco, guerra razziale
        self.__screen.fill(white) #sfondo bianco
        
        
        pygame.draw.line(self.__screen, black, (250, 150), (250, 550),5)#linea verticale 1
        pygame.draw.line(self.__screen, black, (420, 150), (420, 550),5)#linea verticale 2
        pygame.draw.line(self.__screen, black, (80, 420), (590, 420),5)#linea orizzontale 2
        pygame.draw.line(self.__screen, black, (80, 280), (590, 280),5)#linea orizzontale 1

        if self._alt==1:#in base a chi tocca stampo l'immagine
            self.__screen.blit(self.__cucciola_ics, (590, 30)) 

        elif self._alt==2:
            self.__screen.blit(self.__cucciola_circle, (600, 30))  

        for i in range(3):#stampo tutta la matrice
            for j in range(3):
                if self._matrice[i][j]==1:
                    if i==0 and j==0:
                        self.__screen.blit(self.__ics, (110, 160)) #170 x

                    elif i==0 and j==1:
                        self.__screen.blit(self.__ics, (280, 160))
                        
                    elif i==0 and j==2:
                        self.__screen.blit(self.__ics, (450, 160))
                    #----------------------------------------------
                    elif i==1 and j==0:
                        self.__screen.blit(self.__ics, (110, 300)) #140 x

                    elif i==1 and j==1:
                        self.__screen.blit(self.__ics, (280, 300))
                        
                    elif i==1 and j==2:
                        self.__screen.blit(self.__ics, (450, 300))
                    #---------------------------------------------
                    elif i==2 and j==0:
                        self.__screen.blit(self.__ics, (110, 440)) #140 x

                    elif i==2 and j==1:
                        self.__screen.blit(self.__ics, (280, 440))
                        
                    elif i==2 and j==2:
                        self.__screen.blit(self.__ics, (450, 440))

                        
                elif self._matrice[i][j]==2:
                    if i==0 and j==0:
                        self.__screen.blit(self.__circle, (110, 160)) #170 x

                    elif i==0 and j==1:
                        self.__screen.blit(self.__circle, (280, 160))
                        
                    elif i==0 and j==2:
                        self.__screen.blit(self.__circle, (450, 160))

                    elif i==1 and j==0:
                        self.__screen.blit(self.__circle, (110, 300)) #140 x

                    elif i==1 and j==1:
                        self.__screen.blit(self.__circle, (280, 300))
                        
                    elif i==1 and j==2:
                        self.__screen.blit(self.__circle, (450, 300))

                    elif i==2 and j==0:
                        self.__screen.blit(self.__circle, (110, 440)) #140 x

                    elif i==2 and j==1:
                        self.__screen.blit(self.__circle, (280, 440))
                        
                    elif i==2 and j==2:
                        self.__screen.blit(self.__circle, (450, 440))


    
        self._aggiornaSchermo() #refresh
                
    def _reset(self): #reset mappa
        self._res=1
        return np.zeros((3,3))
    

    def _isOk(self,i,j): #verifico se l'indice è accettabile
        if i<0 or i>2 or j<0 or j>2 or self._matrice[i][j]!=0:
            return False

        return True


    def __disegna_vittoria(self,riga,verso): #0 orizzontale - 1 verticale - 2 diagonale
        color=(0,254,0)
        if riga==0 and verso==0: #disegna una linea orizzontale in base a dove ho vinto
            pygame.draw.line(self.__screen, color, (80, 210), (600, 210),7)

        elif riga==1 and verso==0:
            pygame.draw.line(self.__screen, color, (80, 350), (600, 350),7)

        elif riga==2 and verso==0:
            pygame.draw.line(self.__screen, color, (80, 490), (600, 490),7)
    #--------------------------------------------------------------------------
        elif riga==0 and verso==1: #disegna una linea verticale in base a dove ho vinto
            if self._alt==2:
                pygame.draw.line(self.__screen, color, (170, 130), (170, 580),7)
            else:
                pygame.draw.line(self.__screen, color, (160, 130), (160, 580),7)
                

        elif riga==1 and verso==1:
            if self._alt==2:
                pygame.draw.line(self.__screen, color, (340, 130), (340, 580),7)
            else:
                pygame.draw.line(self.__screen, color, (330, 130), (330, 580),7)

        elif riga==2 and verso==1:
            if self._alt==2:
                pygame.draw.line(self.__screen, color, (510, 130), (510, 580),7)
            else:
                pygame.draw.line(self.__screen, color, (500, 130), (500, 580),7)

        elif riga==4 and verso==0: #diagonale principale, l'altra è quella da (0,2) a (2,0)
            if self._alt==2:
                pygame.draw.line(self.__screen, color, (100, 150), (580, 550),7)
            else:
                pygame.draw.line(self.__screen, color, (100, 160), (580, 560),7)

        elif riga==4 and verso==1:
            if self._alt==2:
                pygame.draw.line(self.__screen, color, (580, 150), (100, 550),7)
            else:
                pygame.draw.line(self.__screen, color, (580, 150), (100, 540),7)

        if self._alt==2:  #stampo la scritta in base a chi ha vinto  
            self.__screen.blit(self.__ics_win,(280,50))
        else:
            self.__screen.blit(self.__circle_win,(280,50))
            
        self._aggiornaSchermo() #refersh
            
    
    def _victory(self):
        
        for i in range(3): #verifico se c'è una situazione di vittoria lungo le righe
            conta=1
            for j in range(2):
                if self._matrice[i][j]==self._matrice[i][j+1] and self._matrice[i][j]!=0:
                    conta+=1
            if conta==3:
                self.__disegna_vittoria(i,0)
                return True
            
        for i in range(3):#verifico se c'è una situazione di vittoria lungo le colonne
            conta=1
            for j in range(2):
                if self._matrice[j][i]==self._matrice[j+1][i] and self._matrice[j][i]!=0:
                    conta+=1
            
            if conta==3:
                self.__disegna_vittoria(i,1)
                return True
    
        if self._matrice[0][0]==self._matrice[1][1] and self._matrice[0][0]==self._matrice[2][2] and self._matrice[1][1]!=0:#verifico se c'è una situazione di vittoria lungo la diag principale
            self.__disegna_vittoria(4,0)
            return True

    
        if self._matrice[0][2]==self._matrice[1][1] and self._matrice[0][2]==self._matrice[2][0] and self._matrice[1][1]!=0:#verifico se c'è una situazione di vittoria lungo la diag secondaria
            self.__disegna_vittoria(4,1)
            return True

        return False

    def _stop(self):
        for lista in self._matrice: #se tutte le celle sono occupate allora patta
            for element in lista:
                if element==0:
                    return False
        self.__screen.blit(self.__patta,(290,50))
        self._aggiornaSchermo()
        return True

    def _aggiornaSchermo(self):
        pygame.display.update() #aggiorno il display
        pygame.time.Clock().tick(self.__FPS) #frame di aggiornamento

    

    
#-------------------------------------------------------------------------------------------------------------------------------


class Game(Mappa): #comandi base per giocare
    def __init__(self):
        super().__init__() #inizializzo la mappa (classe ereditata)
        


    def set(self,click): #click sarebbe la posizione del mouse
        posi=self.__trasforma(click) #funzione che mi ritorna la cella della matrice che si vuole settare
        i=posi[0]
        j=posi[1]
   
        if self._isOk(i,j): #verifico se è libera la cella o se gli indici hanno un valore accettabile
            self._res=0     #indica che la matrice non è vuota
            self._matrice[i][j]=self._alt #setto il valore nella matrice 1->x 2->O
            self.stampa() #refresh
            if self._alt==1: #se ero la x adesso sono il cerchio
                self._alt=2
            else:
                self._alt=1

            if self._victory()==True: #verifico se dopo aver settato la cella mi trovo in uno stato di vittoria
                self.__resetMe() #reset della mappa
                return False
            
            if self._stop()==True and self._res!=1: #verifico se dopo aver settato la cella mi trovo in uno stato di reset
                self.__resetMe() #reset della mappa
                return False
        return True





    def __trasforma(self,click): #prendo la posizione del mouse
        x=click[0]
        y=click[1]
        #----------------------------------------1 riga
        if x>80 and x<250 and y>150 and y<280: #in base alla poszione del cursore posso capire la cella
            return [0,0]

        elif x>250 and x<420 and y> 150 and y<280:
            return [0,1]
        
        elif x>420 and x<590 and y>150 and y<280:
            return [0,2]
        #----------------------------------------2 riga

        if x>80 and x<250 and y>280 and y<420:
            return [1,0]

        elif x>250 and x<420 and y>280 and y<420:
            return [1,1]
        
        elif x>420 and x<590 and y>280 and y<420:
            return [1,2]
        #----------------------------------------3 riga

        if x>80 and x<250 and y>420 and y<550:
            return [2,0]

        elif x>250 and x<420 and y>420 and y<550:
            return [2,1]
        
        elif x>420 and x<590 and y>420 and y<550:
            return [2,2]
        else:
            return [-1,-1] #posizione non accettabile
    
    def __resetMe(self):
        time.sleep(2)
        self._alt=1
        super().__init__() #costruttore superclasse

#-------------------------------------------------------------------------------------------------------------------------------


pygame.init() #inizializzo pygame e i suoi metodi
m=Game() #oggetto per giocare
ciclo=True #finchè non viene cliccata la X si gioca

while ciclo: 

    for event in pygame.event.get(): #scorro tutti gli eventi che accadono   
        if event.type == pygame.QUIT:#se viene premuta la x
            ciclo=False #interrompo il ciclo
            break
        if event.type == pygame.MOUSEBUTTONUP:#mouse click
            pos = pygame.mouse.get_pos() #salvo la posizione del click
            m.set(pos) #chiamo la funzione per settare la x o il cerchio
            break
    m.stampa() #refresh e stampa
    
pygame.quit() # chiudo tutto

