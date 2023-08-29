class Player:
    def __init__(self):
        self.tiles = []
        
    def hacer_jugada(self, palabra):
        letras = list(palabra) #Deletrea la palabra ingresada por usuario
        tiles_duplicado = self.tiles.copy() #Hago una duplicacion de las fichas del jugador para la verificacion
    #Y no borrar de la lista de fichas del jugador hasta que la coincidencia sea total
    
        for l in letras: #Recorro la palabra del usuario deletreada 
            if l in tiles_duplicado: 
                tiles_duplicado.remove(l) #La elimino de la lista si coinciden
            else:
                print("No posee fichas en su mano") 
                return #Si no coincide en alguna letra: salta
        return palabra # retorna la palabra ingresada corrrectamente si existio coincidencia siempre
            
        
        
    