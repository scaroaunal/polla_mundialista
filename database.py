import hashlib
import json
import os

class DatabaseManager:
    """Gestor de base de datos simulado usando archivos JSON"""
    
    def __init__(self):
        self.users_file = "users_data.json"
        self._init_db()
    
    def _init_db(self):
        """Inicializa la base de datos si no existe"""
        if not os.path.exists(self.users_file):
            with open(self.users_file, 'w', encoding='utf-8') as f:
                json.dump({}, f, ensure_ascii=False)
    
    def _hash_password(self, password):
        """Encripta la password usando SHA-256"""
        return hashlib.sha256(password.encode()).hexdigest()
    
    def _load_users(self):
        """Carga los usuarios del archivo"""
        try:
            with open(self.users_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return {}
    
    def _save_users(self, users):
        """Guarda los usuarios en el archivo"""
        with open(self.users_file, 'w', encoding='utf-8') as f:
            json.dump(users, f, indent=2, ensure_ascii=False)
    
    def verify_user(self, username, password):
        """Verifica las credenciales del usuario"""
        users = self._load_users()
        username_lower = username.lower()
        
        if username_lower in users:
            stored_hash = users[username_lower]['password']
            if stored_hash == self._hash_password(password):
                return users[username_lower]
        return None
    
    def create_user(self, user_data):
        """Crea un nuevo usuario"""
        users = self._load_users()
        username_lower = user_data['cedula'].lower()
        
        # Verificar si el usuario ya existe
        if username_lower in users:
            return False, "La cédula ya está registrada"
        
        # Verificar si el correo ya existe
        for user in users.values():
            if user['correo_electronico'].lower() == user_data['correo_electronico'].lower():
                return False, "El correo electrónico ya está registrado"
        
        # Encriptar password
        user_data['password'] = self._hash_password(user_data['password'])
        
        # Guardar usuario
        users[username_lower] = user_data
        self._save_users(users)
        
        return True, "¡Cuenta creada exitosamente!"
