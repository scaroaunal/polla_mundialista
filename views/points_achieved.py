import streamlit as st

class PointsAchievedPage:
    def render(self):
        st.title("🎯 Puntos Logrados")
        st.write("Consulta el detalle de los puntos que has obtenido en cada partido.")
        
        # Simulated points data
        points_summary = {
            "Total Puntos": 45,
            "Partidos Acertados": 3,
            "Marcadores Exactos": 1
        }
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Puntos Totales", points_summary["Total Puntos"])
        with col2:
            st.metric("Partidos Acertados", points_summary["Partidos Acertados"])
        with col3:
            st.metric("Marcadores Exactos", points_summary["Marcadores Exactos"])
            
        st.info("El detalle por cada partido estará disponible próximamente.")
