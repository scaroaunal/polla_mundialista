import re

def validar_email(email):
    """Valida formato de email"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validar_cedula(cedula):
    """Valida que la cédula contenga solo números"""
    return cedula.isdigit() and len(cedula) >= 6

def validar_telefono(telefono):
    """Valida formato de teléfono"""
    telefono_limpio = telefono.replace(' ', '').replace('-', '')
    return telefono_limpio.isdigit() and len(telefono_limpio) >= 7

def validar_password(password):
    """Valida que la password tenga al menos 6 caracteres"""
    return len(password) >= 6