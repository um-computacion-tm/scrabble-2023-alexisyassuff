class Player:
    def __init__(self):
        self.tiles = []
        
    def make_play(self, word): 
        if self.verify_tiles_in_hand(word): 
            #Si la funcion verificar devuelve True: 
                self.subtract_tiles(word) #Se va a restar de las fichas del player
                return word #Y retornara la palabra ingresada satisfactoriamente
            #Si devuelve False significa que hubo al menos una ficha que no tenia en su haber
        else: 
                print("No posee fichas en su mano")
                return
            
    
    def verify_tiles_in_hand(self, word):  #Verificacion fichas en mano devolvera:
            letter = list(word) 
            tiles_duplicado = self.tiles.copy() 
            for l in letter:
                if l in tiles_duplicado:
                    tiles_duplicado.remove(l)
                else:
                    print("Falta ficha ", l)
                    return False         #False si alguna ficha no esta en la palabra deseada
            return True                 #True si todas sus fichas estan en la palabra deseada
    
    def subtract_tiles(self, word): #Funcion especificamente de restar fichas para dividir en pequeñas tareas
            letter = list(word)     #Y tener posibilidad de reutilizar el codigo luego con esta funcion
            for l in letter:
                self.tiles.remove(l)
            return

