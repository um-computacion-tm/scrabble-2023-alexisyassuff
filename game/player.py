class Player:
    def __init__(self):
        self.tiles = []
        points_player = 0

    def make_play(self, word):
        if self.verify_tiles_in_hand(word):
            # Si la funcion verificar devuelve True:
            # Se va a restar de las fichas del player
            self.subtract_tiles(word)
            return word  # Y retornara la palabra ingresada satisfactoriamente
            # Si devuelve False significa que hubo al menos una ficha que no tenia en su haber
        else:
            print("No posee fichas en su mano")
            return

    # Verificacion fichas en mano devolvera:
    def verify_tiles_in_hand(self, word):
        letter = list(word)
        tiles_duplicado = self.tiles.copy()
        for l in letter:
            if l in tiles_duplicado:
                tiles_duplicado.remove(l)
            else:
                print("Falta ficha ", l)
                return False  # False si alguna ficha no esta en la palabra deseada
        return True  # True si todas sus fichas estan en la palabra deseada

    # Funcion especificamente de restar fichas para dividir en pequeñas tareas
    def subtract_tiles(self, word):
        # Y tener posibilidad de reutilizar el codigo luego con esta funcion
        letter = list(word)
        for l in letter:
            self.tiles.remove(l)
        return

    def put_tiles_to_bagtiles(self, tiles): #Funcion especifica sobre cuando el jugador quiera 
        self.subtract_tiles(tiles)          #retirar fichas de la bolsa

    def take_tiles_from_bagtiles(self, tiles): #Funcion que se habilita cuando el jugador tome fichas de la bolsa
        self.tiles.extend(tiles)

    