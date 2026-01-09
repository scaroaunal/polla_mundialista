import streamlit as st

class MatchWidget:
    """Widget reutilizable para mostrar un partido con banderas y entrada de marcadores"""
    
    @staticmethod
    def render(team_a_name, team_a_code, team_b_name, team_b_code, match_id):
        """
        Renderiza una fila de partido.
        team_a_code/team_b_code deben ser códigos de país de 2 letras (ej: 'co', 'ar')
        """
        # Flag CDN URL: https://flagcdn.com/w80/{code}.png
        flag_a_url = f"https://flagcdn.com/w80/{team_a_code.lower()}.png"
        flag_b_url = f"https://flagcdn.com/w80/{team_b_code.lower()}.png"
        
        # Estenedor personalizado para alinear verticalmente
        st.markdown("""
            <style>
            .match-row {
                display: flex;
                align-items: center;
                justify-content: space-between;
                padding: 10px;
                border-bottom: 1px solid #e2e8f0;
                background-color: #f8fafc;
                border-radius: 8px;
                margin-bottom: 10px;
            }
            .team-info {
                display: flex;
                align-items: center;
                gap: 15px;
                width: 35%;
            }
            .team-name {
                font-weight: 600;
                font-size: 1.1em;
            }
            .vs-divider {
                font-weight: bold;
                color: #64748b;
            }
            </style>
        """, unsafe_allow_html=True)
        
        col1, col2, col3, col4, col5 = st.columns([2, 1, 0.5, 1, 2])
        
        with col1:
            # Team A Info
            c1, c2 = st.columns([1, 3])
            with c1:
                st.image(flag_a_url, width=40)
            with c2:
                st.markdown(f"<p style='margin-top:10px; font-weight:600;'>{team_a_name}</p>", unsafe_allow_html=True)
                
        with col2:
            score_a = st.number_input("", min_value=0, max_value=20, step=1, key=f"score_a_{match_id}", label_visibility="collapsed")
            
        with col3:
            st.markdown("<p style='text-align:center; margin-top:10px; font-weight:bold;'>VS</p>", unsafe_allow_html=True)
            
        with col4:
            score_b = st.number_input("", min_value=0, max_value=20, step=1, key=f"score_b_{match_id}", label_visibility="collapsed")
            
        with col5:
            # Team B Info
            c1, c2 = st.columns([3, 1])
            with c1:
                st.markdown(f"<p style='text-align:right; margin-top:10px; font-weight:600;'>{team_b_name}</p>", unsafe_allow_html=True)
            with c2:
                st.image(flag_b_url, width=40)
        
        return score_a, score_b
