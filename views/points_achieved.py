import streamlit as st
import pandas as pd
from datetime import date

class PointsAchievedPage:
    def __init__(self):
        # Datos simulados de puntos obtenidos por el usuario actual
        self.match_history = [
            {"fecha": date(2026, 3, 15), "partido": "Colombia vs Argentina", "tu_prediccion": "2 - 1", "resultado_real": "2 - 1", "puntos": 10, "tipo": "Marcador Exacto"},
            {"fecha": date(2026, 3, 15), "partido": "Chile vs Perú", "tu_prediccion": "1 - 0", "resultado_real": "1 - 1", "puntos": 0, "tipo": "Sin Puntos"},
            {"fecha": date(2026, 3, 16), "partido": "Brasil vs Uruguay", "tu_prediccion": "2 - 0", "resultado_real": "1 - 0", "puntos": 5, "tipo": "Ganador Acertado"},
            {"fecha": date(2026, 3, 17), "partido": "Francia vs España", "tu_prediccion": "1 - 1", "resultado_real": "2 - 2", "puntos": 5, "tipo": "Empate Acertado"},
            {"fecha": date(2026, 3, 18), "partido": "Alemania vs Inglaterra", "tu_prediccion": "3 - 2", "resultado_real": "3 - 2", "puntos": 10, "tipo": "Marcador Exacto"},
        ]

    def render(self):
        # Obtener nombre del usuario de la sesión
        user_name = st.session_state.user_data.get('nombre_completo', 'Usuario')
        
        st.title("🎯 Mis Puntos Logrados")
        st.write(f"Hola **{user_name}**, aquí tienes el detalle de tu rendimiento en la polla.")

        # --- RESUMEN DE MÉTRICAS ---
        total_puntos = sum(d['puntos'] for d in self.match_history)
        exactos = sum(1 for d in self.match_history if d['tipo'] == "Marcador Exacto")
        aciertos = sum(1 for d in self.match_history if d['puntos'] > 0)
        total_partidos = len(self.match_history)

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Puntos Totales", f"{total_puntos} pts")
        with col2:
            st.metric("Marcadores Exactos", exactos)
        with col3:
            st.metric("Aciertos Totales", aciertos)
        with col4:
            eficiencia = (aciertos / total_partidos * 100) if total_partidos > 0 else 0
            st.metric("Eficiencia", f"{eficiencia:.1f}%")

        st.markdown("---")

        # --- HISTORIAL DETALLADO ---
        st.subheader("📜 Historial de Partidos")
        
        if not self.match_history:
            st.info("Aún no tienes partidos calculados. ¡Tus puntos aparecerán aquí cuando los partidos finalicen!")
        else:
            df = pd.DataFrame(self.match_history)
            
            # Formatear fecha
            df['fecha'] = df['fecha'].apply(lambda x: x.strftime('%d %b'))
            
            # Renombrar columnas para la tabla
            df.columns = ["Fecha", "Partido", "Tu Predicción", "Resultado Real", "Puntos", "Detalle"]
            
            st.dataframe(
                df,
                use_container_width=True,
                hide_index=True,
                column_config={
                    "Puntos": st.column_config.NumberColumn("Pts", format="%d ⚽"),
                    "Detalle": st.column_config.TextColumn("Tipo de Acierto"),
                    "Partido": st.column_config.TextColumn("Enfrentamiento", width="large")
                }
            )

        st.markdown("---")

        # --- REGLAMENTO DE PUNTOS ---
        with st.expander("ℹ️ ¿Cómo se calculan mis puntos?"):
            st.markdown("""
            El sistema de puntos de la **Polla Mundialista** premia tu conocimiento futbolístico de la siguiente manera:
            
            *   **10 Puntos**: Por acertar el **marcador exacto** del partido. 🎯
            *   **5 Puntos**: Por acertar el **ganador** (pero no el marcador) o acertar el **empate**. ✅
            *   **0 Puntos**: Si no aciertas ni el ganador ni el marcador. ❌
            
            *Los puntos se actualizan automáticamente al finalizar cada encuentro.*
            """)
