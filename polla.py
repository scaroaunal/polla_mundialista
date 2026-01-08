import os
from PIL import Image
import streamlit as st
from supabase import create_client, Client
from dotenv import load_dotenv
from config_path_routs import ConfigPathRoutes as cpr
from script import ConexionSupabase

## VARIABLES DEN ENTORNO
load_dotenv()
url = os.getenv('URL')
key = os.getenv('KEY')
ruta_script = cpr.resolver_rutas("script")
ruta_imagenes= cpr.resolver_rutas("imagenes")
print(url)
print(key)

def login_page():
    """Página de inicio de sesión y registro"""
    st.title(":green[Polla Mundialista Comercial Nutresa]",text_alignment='center')
    st.markdown("### Enterate de todo lo relacionado con el mundial de futbol 2026")
    st.markdown("---")
    imagen = Image.open(os.path.join(ruta_imagenes,'colombia_mundial.png'))
    st.image(imagen)
    objeto_base =  ConexionSupabase(url,key)
    col1, col2, = st.columns([1, 2])

    
        # Pestañas para Login y Registro
    tab1, tab2 = st.tabs(["🔐 Iniciar Sesión", "📝 Registrarse"])
        
    with tab1:
        st.subheader("Iniciar Sesión")
            
        with st.form("login_form"):
            username = st.text_input("correo electronico")
            password = st.text_input("Contraseña", type="password")
                
            if st.form_submit_button("Iniciar Sesión", use_container_width=True):
                if username and password:
                    user = ''
                    if user:
                        st.session_state.logged_in = True
                        st.session_state.user_data = user
                        st.success("¡Inicio de sesión exitoso!")
                        st.rerun()
                    else:
                        st.error("Usuario o contraseña incorrectos")
                else:
                    st.error("Por favor, completa todos los campos")
        
    with tab2:
            st.subheader("Registrarse")
            
            with st.form("register_form"):
                col1, col2 = st.columns(2)
                
                with col1:
                    nombre_completo = st.text_input("Nombre Completo *")
                    cedula = st.text_input("Cédula *")
                
                with col2:
                    correo_electronico = st.text_input("Correo Electrónico *")
                    telefono = st.text_input("Teléfono *")
                    contraseña = st.text_input("Contraseña *", type="password")
                confirmar_contraseña = st.text_input("Confirmar Contraseña *", type="password")
                
                if st.form_submit_button("Crear Cuenta", use_container_width=True):
                    # Validar campos obligatorios
                    if all([nombre_completo, cedula, 
                           correo_electronico, telefono, contraseña]):
                        
                        # Validar confirmación de contraseña
                        if contraseña != confirmar_contraseña:
                            st.error("Las contraseñas no coinciden")
                        else:
                            # Crear diccionario con los datos del usuario
                            user_data = {
                                "nombre_usuario": nombre_completo,
                                "cedula": cedula,
                                "correo_electronico": correo_electronico,
                                "telefono": telefono,
                                "contrasena": contraseña
                            }
                            
                            # Intentar crear el usuario
                            success, message =  objeto_base.ingresar_registro('users',user_data )
                            
                            if success:
                                st.success(message)
                                st.info(f"{nombre_completo} Ya puedes iniciar sesión con tu nueva cuenta")
                            else:
                                st.error(message)
                    else:
                        st.error("Por favor, completa todos los campos obligatorios")

def main():
    "Funcion principal de la aplicacion"
    login_page()


if __name__ == '__main__':
    
    main()