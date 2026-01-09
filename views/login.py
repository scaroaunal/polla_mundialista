import streamlit as st
from datetime import datetime
from database import DatabaseManager
from utils import validar_email, validar_cedula, validar_telefono, validar_contraseña

class LoginPage:
    def __init__(self, db: DatabaseManager):
        self.db = db

    def render(self):
        # Estilo personalizado
        st.markdown("""
            <style>
            .main-title {
                text-align: center;
                color: #1e3a8a;
                font-size: 3em;
                font-weight: bold;
                margin-bottom: 10px;
            }
            .subtitle {
                text-align: center;
                color: #64748b;
                font-size: 1.2em;
                margin-bottom: 30px;
            }
            </style>
        """, unsafe_allow_html=True)
        
        st.markdown('<p class="main-title">⚽ Polla Mundialista 2026</p>', unsafe_allow_html=True)
        st.markdown('<p class="subtitle">Demuestra que sabes de fútbol y gana premios</p>', unsafe_allow_html=True)
        st.markdown("---")
        
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col2:
            # Pestañas para Login y Registro
            tab1, tab2 = st.tabs(["🔐 Iniciar Sesión", "📝 Registrarse"])
            
            with tab1:
                st.subheader("Iniciar Sesión")
                
                with st.form("login_form"):
                    cedula = st.text_input("Cédula", placeholder="Ingresa tu cédula")
                    password = st.text_input("Contraseña", type="password", placeholder="Ingresa tu contraseña")
                    
                    submitted = st.form_submit_button("🚀 Iniciar Sesión", use_container_width=True)
                    
                    if submitted:
                        if cedula and password:
                            user = self.db.verify_user(cedula, password)
                            if user:
                                st.session_state.logged_in = True
                                st.session_state.user_data = user
                                st.success("¡Bienvenido de vuelta! 🎉")
                                st.rerun()
                            else:
                                st.error("❌ Cédula o contraseña incorrectos")
                        else:
                            st.warning("⚠️ Por favor, completa todos los campos")
            
            with tab2:
                st.subheader("Crear Nueva Cuenta")
                st.markdown("Todos los campos son obligatorios")
                
                with st.form("register_form"):
                    col_a, col_b = st.columns(2)
                    
                    with col_a:
                        nombre_completo = st.text_input("Nombre Completo", placeholder="Juan Pérez")
                        cedula_reg = st.text_input("Cédula", placeholder="1234567890")
                        telefono = st.text_input("Teléfono", placeholder="3001234567")
                    
                    with col_b:
                        correo_electronico = st.text_input("Correo Electrónico", placeholder="ejemplo@email.com")
                        contraseña = st.text_input("Contraseña", type="password", placeholder="Mínimo 6 caracteres")
                        confirmar_contraseña = st.text_input("Confirmar Contraseña", type="password", placeholder="Repite tu contraseña")
                    
                    submitted = st.form_submit_button("✅ Crear Cuenta", use_container_width=True)
                    
                    if submitted:
                        # Validar campos vacíos
                        if not all([nombre_completo, cedula_reg, correo_electronico, telefono, contraseña, confirmar_contraseña]):
                            st.error("❌ Por favor, completa todos los campos")
                        
                        # Validar cédula
                        elif not validar_cedula(cedula_reg):
                            st.error("❌ La cédula debe contener solo números y tener al menos 6 dígitos")
                        
                        # Validar email
                        elif not validar_email(correo_electronico):
                            st.error("❌ El correo electrónico no tiene un formato válido")
                        
                        # Validar teléfono
                        elif not validar_telefono(telefono):
                            st.error("❌ El teléfono debe contener al menos 7 dígitos")
                        
                        # Validar contraseña
                        elif not validar_contraseña(contraseña):
                            st.error("❌ La contraseña debe tener al menos 6 caracteres")
                        
                        # Validar confirmación de contraseña
                        elif contraseña != confirmar_contraseña:
                            st.error("❌ Las contraseñas no coinciden")
                        
                        else:
                            # Crear diccionario con los datos del usuario
                            user_data = {
                                "nombre_completo": nombre_completo.strip(),
                                "cedula": cedula_reg.strip(),
                                "correo_electronico": correo_electronico.strip().lower(),
                                "telefono": telefono.strip(),
                                "contraseña": contraseña,
                                "fecha_registro": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                            }
                            
                            # Intentar crear el usuario
                            success, message = self.db.create_user(user_data)
                            
                            if success:
                                st.success(f"✅ {message}")
                                st.info("🎉 Ya puedes iniciar sesión con tu nueva cuenta")
                            else:
                                st.error(f"❌ {message}")
