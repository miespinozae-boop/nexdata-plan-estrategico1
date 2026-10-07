import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="NEXDATA | Dashboard Estratégico IA", page_icon="🧠", layout="wide")

NAVY="#0B1F3A"; BLUE="#2563EB"; CYAN="#00B8D9"; GREEN="#20C997"; ORANGE="#FFB020"; RED="#EF476F"; BG="#F5F7FB"; TEXT="#172B4D"

st.markdown(f"""
<style>
.stApp {{background:{BG}; color:{TEXT};}}
.block-container {{padding-top:1.4rem; padding-bottom:3rem; max-width:1500px;}}
h1,h2,h3,h4,p,span,label {{color:{TEXT};}}
.hero {{background:white;border:1px solid #E4EAF2;border-radius:18px;padding:22px 26px;margin-bottom:16px;box-shadow:0 4px 18px rgba(11,31,58,.05)}}
.hero h1 {{margin:0;color:{NAVY};font-size:31px}}
.hero p {{margin:7px 0 0;color:#60758F}}
.card {{background:white;border:1px solid #E4EAF2;border-radius:16px;padding:18px;height:100%;box-shadow:0 3px 14px rgba(11,31,58,.04)}}
.small {{font-size:13px;color:#6B7F99}}
.kpi {{font-size:27px;font-weight:800;color:{NAVY}}}
.badge {{display:inline-block;background:#EAF2FF;color:{BLUE};padding:5px 10px;border-radius:20px;font-weight:700;font-size:12px}}
.flow {{background:white;border:1px solid #E4EAF2;border-radius:15px;padding:15px;text-align:center;font-weight:700;color:{NAVY};}}
.ai {{background:#EEF8FF;border-left:5px solid {BLUE};padding:18px 20px;border-radius:12px;color:{TEXT};}}
div[data-testid="stMetric"] {{background:white;border:1px solid #E4EAF2;padding:15px;border-radius:15px}}
</style>
""", unsafe_allow_html=True)

st.markdown("""<div class="hero">
<span class="badge">ACTIVIDAD DE SESIÓN · MANAGEMENT BY RESULTS</span>
<h1>🧠 NEXDATA — Dashboard IA del Plan Estratégico</h1>
<p>Plan estratégico como sistema de gestión: modelo de negocio, dirección estratégica, 4 funciones de gestión, objetivos, KPI, acciones, cronograma y presupuesto.</p>
</div>""", unsafe_allow_html=True)

tabs = st.tabs(["📊 Resumen", "🧩 Modelo de negocio", "🎯 Dirección estratégica", "⚙️ Gestión", "📈 Objetivos & KPI", "🗓️ Cronograma", "💰 Presupuesto", "🤖 Análisis IA"])

areas = pd.DataFrame({
    "Área":["Marketing","RR. HH.","Finanzas","Operaciones / Logística"],
    "Objetivo":[
        "Posicionar NEXDATA y captar MYPES interesadas en soluciones de analítica de datos.",
        "Fortalecer las competencias del equipo para asegurar una gestión eficiente del servicio.",
        "Alcanzar sostenibilidad financiera mediante el control de ingresos, costos y presupuesto.",
        "Garantizar el funcionamiento eficiente, continuo y mejorable de la plataforma."
    ],
    "Meta":[
        "30 prospectos y 10 clientes en 6 meses",
        "100% del equipo con 2 capacitaciones en 6 meses",
        "Cubrir ≥100% de los costos operativos al mes 6",
        "Disponibilidad ≥95% y atención crítica ≤24 h"
    ],
    "KPI":["Tasa de conversión","% de personal capacitado","Cobertura de costos","Disponibilidad de plataforma"],
    "Fórmula":[
        "Clientes / Prospectos × 100",
        "Personal capacitado / Total × 100",
        "Ingresos / Costos × 100",
        "Horas disponibles / Horas totales × 100"
    ],
    "Meta_KPI":[33.0,100.0,100.0,95.0],
})

if "actuales" not in st.session_state:
    st.session_state.actuales={"Marketing":28.0,"RR. HH.":75.0,"Finanzas":82.0,"Operaciones / Logística":97.0}
if "presupuesto_ejecutado" not in st.session_state:
    st.session_state.presupuesto_ejecutado=1420

with tabs[0]:
    st.subheader("Resumen ejecutivo del sistema de gestión")
    c1,c2,c3 = st.columns(3)
    with c1:
        st.markdown("""<div class="card"><b>VISIÓN</b><br><br>Ser una plataforma referente en analítica de datos para las MYPES peruanas, reconocida por facilitar la gestión empresarial mediante información clara, accesible y orientada a la toma de decisiones.</div>""",unsafe_allow_html=True)
    with c2:
        st.markdown("""<div class="card"><b>MISIÓN</b><br><br>Transformar los datos de las MYPES en información útil y comprensible mediante herramientas digitales que permitan analizar su desempeño, identificar oportunidades y tomar mejores decisiones empresariales.</div>""",unsafe_allow_html=True)
    with c3:
        st.markdown("""<div class="card"><b>CULTURA Y VALORES</b><br><br>Innovación · orientación al cliente · trabajo colaborativo · orientación a resultados · responsabilidad · mejora continua.</div>""",unsafe_allow_html=True)

    st.markdown("### Integración del Plan Estratégico")
    cols=st.columns(7)
    flow=["Modelo de negocio","Visión, misión y cultura","Dirección estratégica","Objetivos + metas","KPI + acciones","Cronograma + presupuesto","Control + decisiones"]
    for col,label in zip(cols,flow):
        with col: st.markdown(f'<div class="flow">{label}</div>',unsafe_allow_html=True)

    vals=[]
    for _,r in areas.iterrows():
        actual=st.session_state.actuales[r["Área"]]
        vals.append(min(actual/r["Meta_KPI"]*100,100))
    cumplimiento=sum(vals)/len(vals)
    k1,k2,k3,k4=st.columns(4)
    k1.metric("Cumplimiento estratégico",f"{cumplimiento:.0f}%")
    k2.metric("Objetivos en meta",f"{sum(st.session_state.actuales[r['Área']]>=r['Meta_KPI'] for _,r in areas.iterrows())}/4")
    k3.metric("Presupuesto total","S/ 2,100")
    k4.metric("Presupuesto ejecutado",f"S/ {st.session_state.presupuesto_ejecutado:,.0f}")

    fig=go.Figure(go.Indicator(mode="gauge+number",value=cumplimiento,title={"text":"Avance global del Plan Estratégico"},gauge={"axis":{"range":[0,100]},"bar":{"color":BLUE}}))
    fig.update_layout(height=290,paper_bgcolor="white",font={"color":TEXT})
    st.plotly_chart(fig,use_container_width=True,config={"displayModeBar":False})

with tabs[1]:
    st.subheader("Modelo de negocio NEXDATA — Business Model Canvas")
    canvas=[
        ("Socios clave","Proveedores tecnológicos, servicios cloud, aliados empresariales y organizaciones vinculadas con MYPES."),
        ("Actividades clave","Desarrollo y mantenimiento de la plataforma, análisis de datos, soporte, captación y mejora continua."),
        ("Recursos clave","Plataforma web, infraestructura tecnológica, conocimiento analítico, equipo y base de usuarios."),
        ("Propuesta de valor","Convertir datos empresariales en información visual, comprensible y útil para que las MYPES tomen mejores decisiones."),
        ("Relación con clientes","Acompañamiento digital, soporte, demostraciones, capacitación y atención continua."),
        ("Canales","Plataforma web, redes sociales, contacto digital, demostraciones y alianzas."),
        ("Segmentos de clientes","MYPES que necesitan analizar ventas, rentabilidad y desempeño sin contar con herramientas avanzadas de BI."),
        ("Estructura de costos","Desarrollo, hosting, herramientas digitales, marketing, soporte y capacitación."),
        ("Fuentes de ingresos","Planes de suscripción y servicios asociados a funcionalidades y análisis de la plataforma.")
    ]
    for i in range(0,len(canvas),3):
        cc=st.columns(3)
        for j,(title,body) in enumerate(canvas[i:i+3]):
            with cc[j]: st.markdown(f'<div class="card"><b>{title}</b><br><span class="small">{body}</span></div>',unsafe_allow_html=True)

with tabs[2]:
    st.subheader("Herramientas de dirección estratégica")
    st.info("Las herramientas no se presentan de forma aislada: el diagnóstico orienta los objetivos, los KPI miden su cumplimiento y el dashboard permite controlar y retroalimentar la estrategia.")
    a,b=st.columns(2)
    with a:
        st.markdown("#### Matriz FODA")
        st.markdown("""**Fortalezas:** propuesta accesible, visualización simple, análisis y simulación en una sola solución.  
**Oportunidades:** digitalización de MYPES y mayor interés por decisiones basadas en datos.  
**Debilidades:** etapa inicial, recursos limitados y necesidad de validación comercial.  
**Amenazas:** soluciones BI consolidadas, cambios tecnológicos y resistencia a adoptar nuevas herramientas.""")
    with b:
        st.markdown("#### Herramientas integradas")
        st.markdown("""**Business Model Canvas:** define cómo NEXDATA crea, entrega y captura valor.  
**FODA:** identifica condiciones internas y externas.  
**KPI:** convierten los objetivos en resultados medibles.  
**Dashboard IA:** integra seguimiento, alertas y recomendaciones para la toma de decisiones.""")
    st.markdown("### Relación estratégica")
    st.success("Canvas → FODA → Objetivos estratégicos → Metas → KPI → Acciones → Dashboard IA → Control y mejora continua")

with tabs[3]:
    st.subheader("Las 4 funciones claves de la gestión")
    funcs=[
        ("1. Planificación","Define visión, misión, cultura, objetivos, metas, indicadores, acciones, cronograma y presupuesto."),
        ("2. Organización","Asigna responsables, recursos y funciones entre Marketing, RR. HH., Finanzas y Operaciones/Logística."),
        ("3. Dirección","Coordina al equipo, ejecuta las acciones estratégicas y orienta los recursos hacia los resultados esperados."),
        ("4. Control","Compara los KPI reales con las metas, identifica desviaciones y permite aplicar acciones correctivas.")
    ]
    cc=st.columns(4)
    for c,(t,b) in zip(cc,funcs):
        with c: st.markdown(f'<div class="card"><b>{t}</b><br><br><span class="small">{b}</span></div>',unsafe_allow_html=True)
    st.markdown("### Sistema de gestión")
    st.write("La gestión es cíclica: los resultados del **Control** retroalimentan la **Planificación**, permitiendo actualizar decisiones, recursos y acciones.")

with tabs[4]:
    st.subheader("Objetivos estratégicos, metas e indicadores")
    st.dataframe(areas[["Área","Objetivo","Meta","KPI","Fórmula"]],use_container_width=True,hide_index=True)
    st.markdown("### Simulación de avance de KPI")
    cols=st.columns(4)
    ranges={"Marketing":100,"RR. HH.":100,"Finanzas":160,"Operaciones / Logística":100}
    for col,(_,r) in zip(cols,areas.iterrows()):
        with col:
            st.session_state.actuales[r["Área"]] = st.slider(
                r["Área"],0.0,float(ranges[r["Área"]]),float(st.session_state.actuales[r["Área"]]),1.0,
                help=f"{r['KPI']} | Meta: {r['Meta_KPI']}"
            )
            actual=st.session_state.actuales[r["Área"]]
            estado="🟢 Cumple" if actual>=r["Meta_KPI"] else ("🟡 En riesgo" if actual>=r["Meta_KPI"]*.75 else "🔴 Crítico")
            st.caption(f"{r['KPI']}: {actual:.1f}% · Meta {r['Meta_KPI']:.0f}%")
            st.write(estado)

    st.markdown("### Acciones y entregables")
    actions=pd.DataFrame([
        ["Marketing","Campañas digitales y contenido educativo","Plan de contenidos + piezas digitales","Marketing"],
        ["Marketing","Demostraciones y prueba piloto","Base de prospectos + reporte de captación","Marketing"],
        ["RR. HH.","Capacitación en datos y atención","Plan y registro de capacitación","RR. HH."],
        ["Finanzas","Control mensual de ingresos y costos","Reporte financiero y flujo de caja","Finanzas"],
        ["Operaciones / Logística","Pruebas y corrección de incidencias","Registro de incidencias","Tecnología"],
        ["Operaciones / Logística","Mejoras funcionales de la plataforma","Versión optimizada de NEXDATA","Tecnología"],
    ],columns=["Área","Acción","Entregable","Responsable"])
    st.dataframe(actions,use_container_width=True,hide_index=True)

with tabs[5]:
    st.subheader("Cronograma estratégico")
    cron=pd.DataFrame([
        ["Optimización de plataforma","Operaciones / Logística","2026-10-01","2026-11-30"],
        ["Pruebas de funcionamiento","Operaciones / Logística","2026-10-15","2026-12-15"],
        ["Capacitación del equipo","RR. HH.","2026-11-01","2027-02-28"],
        ["Contenido y campaña digital","Marketing","2026-10-15","2027-03-31"],
        ["Captación de MYPES","Marketing","2026-11-01","2027-03-31"],
        ["Seguimiento financiero","Finanzas","2026-10-01","2027-03-31"],
        ["Evaluación de indicadores","Dirección","2026-12-15","2027-03-31"],
    ],columns=["Actividad","Área","Inicio","Fin"])
    cron["Inicio"]=pd.to_datetime(cron["Inicio"]); cron["Fin"]=pd.to_datetime(cron["Fin"])
    fig=px.timeline(cron,x_start="Inicio",x_end="Fin",y="Actividad",color="Área",title="Cronograma de trabajo — Oct. 2026 a Mar. 2027")
    fig.update_yaxes(autorange="reversed")
    fig.update_layout(height=450,paper_bgcolor="white",plot_bgcolor="white",font={"color":TEXT})
    st.plotly_chart(fig,use_container_width=True,config={"displayModeBar":False})
    st.dataframe(cron,use_container_width=True,hide_index=True)

with tabs[6]:
    st.subheader("Presupuesto estratégico")
    budget=pd.DataFrame({
        "Concepto":["Desarrollo y mejoras","Hosting y herramientas","Marketing y publicidad","Capacitación","Pruebas y soporte","Contingencias"],
        "Presupuesto":[500,300,600,300,200,200]
    })
    st.session_state.presupuesto_ejecutado=st.slider("Presupuesto ejecutado (S/)",0,2100,int(st.session_state.presupuesto_ejecutado),50)
    b1,b2,b3=st.columns(3)
    b1.metric("Presupuesto planificado","S/ 2,100")
    b2.metric("Ejecutado",f"S/ {st.session_state.presupuesto_ejecutado:,}")
    b3.metric("Disponible",f"S/ {2100-st.session_state.presupuesto_ejecutado:,}")
    fig=px.bar(budget,x="Concepto",y="Presupuesto",text_auto=True,title="Distribución del presupuesto")
    fig.update_layout(height=370,paper_bgcolor="white",plot_bgcolor="white",font={"color":TEXT})
    st.plotly_chart(fig,use_container_width=True,config={"displayModeBar":False})
    st.dataframe(budget,use_container_width=True,hide_index=True)

with tabs[7]:
    st.subheader("🤖 Análisis Estratégico IA")
    gaps=[]
    for _,r in areas.iterrows():
        actual=st.session_state.actuales[r["Área"]]
        gap=(actual-r["Meta_KPI"])/r["Meta_KPI"]*100
        gaps.append((r["Área"],gap,actual,r["Meta_KPI"],r["KPI"]))
    worst=min(gaps,key=lambda x:x[1])
    best=max(gaps,key=lambda x:x[1])
    cumplimiento=sum(min(st.session_state.actuales[r["Área"]]/r["Meta_KPI"]*100,100) for _,r in areas.iterrows())/4
    recs={
        "Marketing":"reforzar las demostraciones, contenido educativo y seguimiento de prospectos para elevar la conversión.",
        "RR. HH.":"completar el plan de capacitación y verificar la aplicación de los conocimientos en las actividades del equipo.",
        "Finanzas":"revisar costos operativos y priorizar acciones que incrementen los ingresos recurrentes.",
        "Operaciones / Logística":"priorizar incidencias críticas, monitorear disponibilidad y mantener un ciclo de mejora continua."
    }
    st.markdown(f"""<div class="ai"><b>Diagnóstico automático</b><br><br>
El Plan Estratégico registra un cumplimiento aproximado de <b>{cumplimiento:.0f}%</b>. 
El área con mayor desviación relativa es <b>{worst[0]}</b>, con un resultado actual de <b>{worst[2]:.1f}%</b> frente a una meta de <b>{worst[3]:.0f}%</b>.
El mejor desempeño relativo corresponde a <b>{best[0]}</b>.<br><br>
<b>Recomendación IA:</b> Se recomienda {recs[worst[0]]}
El resultado debe revisarse periódicamente para retroalimentar la planificación y aplicar acciones correctivas.</div>""",unsafe_allow_html=True)

    st.markdown("### Semáforo estratégico")
    sem=[]
    for _,r in areas.iterrows():
        actual=st.session_state.actuales[r["Área"]]
        ratio=actual/r["Meta_KPI"]
        estado="🟢 Cumple" if ratio>=1 else ("🟡 En riesgo" if ratio>=.75 else "🔴 Crítico")
        sem.append([r["Área"],r["KPI"],f"{actual:.1f}%",f"{r['Meta_KPI']:.0f}%",estado])
    st.dataframe(pd.DataFrame(sem,columns=["Área","KPI","Actual","Meta","Estado"]),use_container_width=True,hide_index=True)

st.caption("NEXDATA · Dashboard IA del Plan Estratégico · Actividad académica")
