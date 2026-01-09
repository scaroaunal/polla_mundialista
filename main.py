import streamlit as st
from database import DatabaseManager
from views.login import LoginPage
from views.match_scores import MatchScoresPage
from views.ranking import RankingPage
from views.proposed_scores import ProposedScoresPage
from views.points_achieved import PointsAchievedPage

# Configuración de la página
st.set_page_config(
    page_title="Polla Mundialista",
    page_icon="⚽",
    layout="wide"
)

# Inicializar componentes
if 'db' not in st.session_state:
    st.session_state.db = DatabaseManager()

# Inicializar estado de sesión
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'user_data' not in st.session_state:
    st.session_state.user_data = None
if 'page' not in st.session_state:
    st.session_state.page = 'dashboard'
if 'mis_pollas' not in st.session_state:
    st.session_state.mis_pollas = []

def dashboard_page():
    """Dashboard principal después del login"""
    st.title("⚽ Panel Principal")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Pollas Activas", len(st.session_state.mis_pollas))
    
    with col2:
        st.metric("Puntos Totales", "0")
    
    with col3:
        st.metric("Posición", "-")
    
    st.markdown("---")
    
    st.subheader("📊 Próximos Partidos")
    st.info("Funcionalidad en desarrollo...")
    
    st.subheader("🏆 Mis Pollas")
    if len(st.session_state.mis_pollas) == 0:
        st.warning("No tienes pollas activas. ¡Crea tu primera polla!")
    else:
        for polla in st.session_state.mis_pollas:
            st.write(f"- {polla}")

def sidebar_navigation():
    """Maneja la navegación en el sidebar"""
    with st.sidebar:
        st.title("⚽ Polla Mundialista")
        st.markdown("---")
        
        # Información del usuario
        st.markdown(f"**👤 Usuario:** {st.session_state.user_data['nombre_completo']}")
        st.markdown(f"**📧 Email:** {st.session_state.user_data['correo_electronico']}")
        st.markdown("---")
        
        # Menú de navegación
        st.subheader("📋 Menú")
        
        if st.button("🏠 Dashboard", use_container_width=True):
            st.session_state.page = 'dashboard'
            st.rerun()
        
        if st.button("⚽ Ingresar Marcadores", use_container_width=True):
            st.session_state.page = 'match_scores'
            st.rerun()
        
        if st.button("🏆 Ranking", use_container_width=True):
            st.session_state.page = 'ranking'
            st.rerun()
            
        if st.button("📋 Marcadores Propuestos", use_container_width=True):
            st.session_state.page = 'proposed_scores'
            st.rerun()
            
        if st.button("🎯 Puntos Logrados", use_container_width=True):
            st.session_state.page = 'points_achieved'
            st.rerun()
        
        st.markdown("---")
        
        # Botón de cerrar sesión
        if st.button("🚪 Cerrar Sesión", use_container_width=True, type="secondary"):
            st.session_state.logged_in = False
            st.session_state.user_data = None
            st.session_state.page = 'dashboard'
            st.session_state.mis_pollas = []
            st.rerun()

def main():
    """Función principal (Controlador de la UI)"""
    if not st.session_state.logged_in:
        login_view = LoginPage(st.session_state.db)
        login_view.render()
    else:
        sidebar_navigation()
        
        # Router de páginas
        if st.session_state.page == 'dashboard':
            dashboard_page()
        elif st.session_state.page == 'match_scores':
            MatchScoresPage().render()
        elif st.session_state.page == 'ranking':
            RankingPage().render()
        elif st.session_state.page == 'proposed_scores':
            ProposedScoresPage().render()
        elif st.session_state.page == 'points_achieved':
            PointsAchievedPage().render()

if __name__ == "__main__":
    main()