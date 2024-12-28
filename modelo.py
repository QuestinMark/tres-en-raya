# Lógica del juego

tablero = [
    ['', '', ''],
    ['', '', ''],
    ['', '', '']
]

turno = 'X'

def hacer_movimiento(fila, columna):
    if tablero[fila][columna] == '':
        tablero[fila][columna] = turno  
    
        # Verificar filas
        for fila in tablero:
            if fila[0] == fila[1] == fila[2] != '':
                return True
        
        # Verificar columnas
        for col in range(3):
            if tablero[0][col] == tablero[1][col] == tablero[2][col] != '':
                return True
        
        # Verificar diagonales
        if tablero[0][0] == tablero[1][1] == tablero[2][2] != '':
            return True
        if tablero[0][2] == tablero[1][1] == tablero[2][0] != '':
            return True
        
        # Cambiar turno
        global turno
        turno = 'O' if turno == 'X' else 'X'
    
    return False