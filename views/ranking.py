import streamlit as st
import pandas as pd

class RankingPage:
    def __init__(self):
        # Datos simulados con tendencia (cambio de posición)
        # tendencia: positivo (subió), negativo (bajó), 0 (se mantuvo)
        self.ranking_data = [
            {"puesto": 1, "usuario": "Juan Pérez", "puntos": 158, "tendencia": 0, "avatar": "🥇"},
            {"puesto": 2, "usuario": "Maria Lopez", "puntos": 145, "tendencia": 1, "avatar": "🥈"},
            {"puesto": 3, "usuario": "Carlos Ruiz", "puntos": 132, "tendencia": -1, "avatar": "🥉"},
            {"puesto": 4, "usuario": "Ana Beltrán", "puntos": 128, "tendencia": 2, "avatar": "👤"},
            {"puesto": 5, "usuario": "Diego Sosa", "puntos": 115, "tendencia": -1, "avatar": "👤"},
            {"puesto": 6, "usuario": "Elena Sanz", "puntos": 110, "tendencia": 0, "avatar": "👤"},
            {"puesto": 7, "usuario": "Felipe Mesa", "puntos": 98, "tendencia": -2, "avatar": "👤"},
        ]

    def _inject_css(self):
        st.markdown("""
            <style>
            .podium-container {
                display: flex;
                justify-content: center;
                align-items: flex-end;
                gap: 20px;
                padding: 20px 0;
                margin-bottom: 30px;
            }
            .podium-card {
                background: white;
                border-radius: 15px;
                padding: 20px;
                text-align: center;
                box-shadow: 0 4px 15px rgba(0,0,0,0.1);
                transition: transform 0.3s ease;
                border: 2px solid transparent;
            }
            .podium-card:hover {
                transform: translateY(-10px);
            }
            .rank-1 { border-color: #ffd700; height: 220px; width: 220px; }
            .rank-2 { border-color: #c0c0c0; height: 180px; width: 180px; }
            .rank-3 { border-color: #cd7f32; height: 180px; width: 180px; }
            
            .rank-number {
                font-size: 2em;
                font-weight: bold;
                margin-bottom: 10px;
            }
            .user-name {
                font-weight: 600;
                font-size: 1.1em;
                color: #333;
            }
            .user-points {
                font-size: 1.3em;
                color: #2e7d32;
                font-weight: bold;
            }
            </style>
        """, unsafe_allow_html=True)

    def render(self):
        self._inject_css()
        st.title("🏆 Ranking de Participantes")
        st.write("Consulta quién lidera la polla y cómo han cambiado las posiciones.")

        # --- SECCIÓN PODIO ---
        st.markdown("### 🔝 Los Líderes")
        
        # Reordenar para que el 1 esté en el centro (2, 1, 3)
        top_3 = self.ranking_data[:3]
        col_side1, col_center, col_side2 = st.columns([1, 1.2, 1])

        with col_side1: # Puesto 2
            p2 = top_3[1]
            st.markdown(f"""
                <div class="podium-card rank-2">
                    <div style="font-size: 3em;">🥈</div>
                    <div class="user-name">{p2['usuario']}</div>
                    <div class="user-points">{p2['puntos']} pts</div>
                    <div style="color: green; font-weight: bold;">▲ {p2['tendencia']}</div>
                </div>
            """, unsafe_allow_html=True)

        with col_center: # Puesto 1
            p1 = top_3[0]
            st.markdown(f"""
                <div class="podium-card rank-1">
                    <div style="font-size: 4em;">🥇</div>
                    <div class="user-name" style="font-size: 1.4em;">{p1['usuario']}</div>
                    <div class="user-points" style="font-size: 1.6em;">{p1['puntos']} pts</div>
                    <div style="color: gray; font-size: 0.9em;">(Sin cambios)</div>
                </div>
            """, unsafe_allow_html=True)

        with col_side2: # Puesto 3
            p3 = top_3[2]
            st.markdown(f"""
                <div class="podium-card rank-3">
                    <div style="font-size: 3em;">🥉</div>
                    <div class="user-name">{p3['usuario']}</div>
                    <div class="user-points">{p3['puntos']} pts</div>
                    <div style="color: red; font-weight: bold;">▼ {abs(p3['tendencia'])}</div>
                </div>
            """, unsafe_allow_html=True)

        st.markdown("---")

        # --- TABLA COMPLETA CON BUSCADOR ---
        st.subheader("📊 Tabla de Posiciones")
        
        # Buscador de participantes
        search_query = st.text_input("🔍 Buscar participante por nombre...", placeholder="Ej: Elena Sanz").strip().lower()

        # Preparar datos para DataFrame
        df_list = []
        for d in self.ranking_data:
            # Aplicar filtro de búsqueda
            if search_query and search_query not in d['usuario'].lower():
                continue

            # Lógica de icono de tendencia
            if d['tendencia'] > 0:
                trend_icon = f"▲ {d['tendencia']}"
                trend_color = "Subió"
            elif d['tendencia'] < 0:
                trend_icon = f"▼ {abs(d['tendencia'])}"
                trend_color = "Bajó"
            else:
                trend_icon = "➖"
                trend_color = "Igual"
            
            df_list.append({
                "Pos": d['puesto'],
                "Icon": d['avatar'],
                "Participante": d['usuario'],
                "Puntos": d['puntos'],
                "Tendencia": trend_icon,
                "Estado": trend_color
            })

        if not df_list:
            st.warning(f"No se encontró ningún participante que coincida con '{search_query}'.")
        else:
            df = pd.DataFrame(df_list)

            # Configuración de columnas
            st.dataframe(
                df,
                use_container_width=True,
                hide_index=True,
                column_config={
                    "Pos": st.column_config.NumberColumn("Puesto", width="small"),
                    "Icon": st.column_config.TextColumn("", width="small"),
                    "Participante": st.column_config.TextColumn("Nombre", width="medium"),
                    "Puntos": st.column_config.ProgressColumn("Puntos", min_value=0, max_value=200, format="%d"),
                    "Tendencia": st.column_config.TextColumn("Cambio", width="small"),
                    "Estado": st.column_config.TextColumn("Estado", width="small"),
                }
            )

            if search_query:
                st.caption(f"Mostrando {len(df_list)} resultados para '{search_query}'")
            else:
                st.info("💡 El ranking se actualiza en tiempo real después de cada partido finalizado.")
