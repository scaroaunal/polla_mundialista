import streamlit as st

class RankingPage:
    def render(self):
        st.title("🏆 Ranking de Participantes")
        st.write("Consulta la tabla de posiciones de todos los polleros.")
        
        # Simulated ranking data
        ranking_data = [
            {"Puesto": 1, "Usuario": "Juan Pérez", "Puntos": 150},
            {"Puesto": 2, "Usuario": "Maria Lopez", "Puntos": 145},
            {"Puesto": 3, "Usuario": "Carlos Ruiz", "Puntos": 130},
        ]
        
        st.table(ranking_data)
        st.info("El ranking se actualiza automáticamente después de cada partido.")
