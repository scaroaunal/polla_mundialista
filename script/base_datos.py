from supabase import create_client, Client

class ConexionSupabase:

    def __init__(self,url,key):
        self.cliente = create_client(url, key)

    def ingresar_registro(self,tabla: str ,data:dict):
        '''
            Metodo para insertar registros a una tabla en especfico
        '''
        try:
            self.cliente.table(tabla).insert(data).execute()
            return True, 'Creacion usuario correcta'
        except Exception:
            return False, 'Algo salio mal verifica los datos ingresados'



