import streamlit as st

class MatchWidget:
    """Widget reutilizable para mostrar un partido con banderas y entrada de marcadores"""
    
    @staticmethod
    def get_flag_emoji(country_code):
        """Convierte un código de país de 2 letras en un emoji de bandera"""
        if not country_code or len(country_code) != 2:
            return "🏳️"
        return chr(ord(country_code[0].upper()) + 127397) + chr(ord(country_code[1].upper()) + 127397)

    @staticmethod
    def inject_custom_css():
        """Inyecta el CSS necesario para el widget de partidos una sola vez"""
        st.markdown("""
            <style>
            /* Fondo verde claro para los contenedores de partidos */
            div[data-testid="stVerticalBlockBordered"] {
                background-color: #f0fff4 !important;
                border: 2px solid #c6f6d5 !important;
                border-radius: 12px !important;
                padding: 8px !important; /* Reducido */
                margin-bottom: 5px !important;
            }
            /* Centrado de columnas y sus contenidos */
            [data-testid="column"] {
                display: flex !important;
                flex-direction: column !important;
                align-items: center !important;
                justify-content: center !important;
                text-align: center !important;
            }
            /* Centrado de banderas */
            [data-testid="stImage"] > img {
                display: block;
                margin: 0 auto !important;
            }
            /* Centrado de métricas y ajuste de fuentes */
            [data-testid="stMetricValue"] {
                text-align: center !important;
                width: 100% !important;
                font-size: 1.1rem !important; /* Más pequeño para 3 cols */
            }
            [data-testid="stMetricLabel"] {
                text-align: center !important;
                width: 100% !important;
                font-size: 0.8rem !important; /* Más pequeño */
            }
            /* Ajuste del VS */
            .vs-text {
                text-align: center;
                padding-top: 0px; 
                font-weight: bold;
                color: #2f855a;
                font-size: 1.2em; /* Reducido */
            }
            /* Estilo para la fecha y hora */
            .match-schedule {
                text-align: center;
                font-size: 0.8rem;
                color: #666;
                margin-top: -5px;
                margin-bottom: 10px;
                font-weight: 500;
            }
            /* Centrado y tamaño de inputs */
            .stNumberInput {
                width: 100% !important;
                display: flex !important;
                justify-content: center !important;
            }
            .stNumberInput div[data-baseweb="input"] {
                width: 65px !important; /* Más estrecho */
                margin: 0 auto !important;
            }
            </style>
        """, unsafe_allow_html=True)



    @staticmethod
    def render(team_a_name, team_a_code, team_b_name, team_b_code, match_id, match_date="--", match_time="--"):
        """
        Renderiza una fila de partido.
        Diseño optimizado para evitar errores de formulario en Streamlit.
        """
        flag_a_url = f"https://flagcdn.com/w80/{team_a_code.lower()}.png"
        flag_b_url = f"https://flagcdn.com/w80/{team_b_code.lower()}.png"
        
        with st.container(border=True):
            # Fecha y Hora arriba
            st.markdown(f'<div class="match-schedule">📅 {match_date} &nbsp; 🕒 {match_time}</div>', unsafe_allow_html=True)
            
            col_a, col_vs, col_b = st.columns([1, 0.4, 1])
            
            with col_a:
                st.image(flag_a_url, width=40)
                st.metric(label="Local", value=team_a_name)
                score_a = st.number_input("Goles A", min_value=0, max_value=20, step=1, key=f"score_a_{match_id}", label_visibility="collapsed")
                
            with col_vs:
                st.markdown('<div class="vs-text">VS</div>', unsafe_allow_html=True)
                
            with col_b:
                st.image(flag_b_url, width=40)
                st.metric(label="Visitante", value=team_b_name)
                score_b = st.number_input("Goles B", min_value=0, max_value=20, step=1, key=f"score_b_{match_id}", label_visibility="collapsed")
        
        return score_a, score_b

        
        return score_a, score_b






