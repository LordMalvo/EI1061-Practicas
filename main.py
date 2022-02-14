import sys

# Definicion de vectores
MEM_D = []  # Memoria de datos
REG = []    # Banco de registros
MEM_I = []  # Memorida de isntrucciones
RS_IF_ID = []   # Registro de segmentacion etapa de IF a ID
RS_ID_EX = []   # Registro de segmentacion etapa de ID a EX
RS_EX_MEM = []  # Registro de segmentacion etapa de EX a MEM
RS_MEM_WD = []  # Registro de segmentacion etapa de MEM a WD

# Esta funcion devuelve una lista de instrucciones tal que
# [[instruccion1, [registros]], [instruccion2, [registros]], ...]
def read_data(f):
    lines = f.readlines()
    instrucciones = []
    for i in range(len(lines)):
        instrucciones.append(lines[i].split())
        instrucciones[i][1] = instrucciones[i][1].split(',')
    return instrucciones

def main(instrucciones):
    print(instrucciones)
    MEM_I = instrucciones

def etapa_if(MEM_I, RS_IF_ID):
    pass

def etapa_id(RS_IF_ID, RS_ID_EX, REG):
    pass

def etapa_ex(RS_ID_EX, RS_EX_MEM):
    pass

def etapa_mem(RS_EX_MEM, RS_MEM_WB, MEM_D):
    pass

def etapa_wb(RS_MEM_WB, REG):
    pass

if __name__ == '__main__':
    data = read_data(sys.stdin)
    main(data)

