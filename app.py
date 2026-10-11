# -*- coding: utf-8 -*-
import random

import streamlit as st

from preguntas import PREGUNTAS

st.set_page_config(page_title="IPE1 · Test PRL", page_icon="🦺", layout="centered")

TEMAS = list(dict.fromkeys(p[0] for p in PREGUNTAS))  # orden de aparición


def iniciar(temas, n, modo):
    pool = [p for p in PREGUNTAS if p[0] in temas]
    random.shuffle(pool)
    quiz = []
    for tema, q, ok, malas, exp in pool[:n]:
        opts = [ok] + list(malas)
        random.shuffle(opts)
        quiz.append({"tema": tema, "q": q, "opts": opts, "ok": ok, "exp": exp})
    # limpiar respuestas de rondas anteriores
    for k in [k for k in st.session_state if str(k).startswith("r")]:
        del st.session_state[k]
    st.session_state.update(quiz=quiz, i=0, resp={}, modo=modo, fin=False)


def pantalla_inicio():
    st.title("🦺 Test IPE1 · UD1")
    st.caption("La prevención de riesgos: conceptos básicos")
    temas = st.multiselect("Temas", TEMAS, default=TEMAS)
    disponibles = len([p for p in PREGUNTAS if p[0] in temas])
    if disponibles == 0:
        st.warning("Elige al menos un tema.")
        return
    n = st.slider("Número de preguntas", 1, disponibles, min(20, disponibles)) if disponibles > 1 else 1
    modo = st.radio(
        "Modo",
        ["Práctica", "Examen"],
        captions=["Corrección al momento", "Corrección al final"],
    )
    if st.button("Empezar", type="primary", use_container_width=True):
        iniciar(temas, n, modo)
        st.rerun()


def siguiente():
    s = st.session_state
    if s.i + 1 < len(s.quiz):
        s.i += 1
    else:
        s.fin = True
    st.rerun()


def pregunta():
    s = st.session_state
    i, quiz = s.i, s.quiz
    item = quiz[i]
    practica = s.modo == "Práctica"
    respondida = practica and i in s.resp

    st.progress(i / len(quiz))
    st.caption(f"Pregunta {i + 1} de {len(quiz)} · {item['tema']}")
    st.subheader(item["q"])

    eleccion = st.radio(
        "Elige una opción",
        item["opts"],
        index=None,
        key=f"r{i}",
        disabled=respondida,
        label_visibility="collapsed",
    )

    if practica:
        if not respondida:
            if st.button("Comprobar", type="primary", disabled=eleccion is None, use_container_width=True):
                s.resp[i] = eleccion
                st.rerun()
        else:
            if s.resp[i] == item["ok"]:
                st.success("✅ ¡Correcto!")
            else:
                st.error(f"❌ Incorrecto. La respuesta correcta es: **{item['ok']}**")
            st.info(f"💡 {item['exp']}")
            etiqueta = "Siguiente" if i + 1 < len(quiz) else "Ver resultados"
            if st.button(etiqueta, type="primary", use_container_width=True):
                siguiente()
    else:
        etiqueta = "Siguiente" if i + 1 < len(quiz) else "Finalizar"
        if st.button(etiqueta, type="primary", use_container_width=True):
            s.resp[i] = eleccion
            siguiente()

    if st.button("Abandonar test"):
        del st.session_state["quiz"]
        st.rerun()


def resultados():
    s = st.session_state
    quiz = s.quiz
    aciertos = sum(1 for i, it in enumerate(quiz) if s.resp.get(i) == it["ok"])
    nota = 10 * aciertos / len(quiz)
    st.title("Resultados")
    st.metric("Aciertos", f"{aciertos} / {len(quiz)}", f"Nota: {nota:.1f} / 10")
    if nota >= 5:
        st.success("¡Aprobado!")
    else:
        st.warning("Toca repasar un poco más.")

    fallos = [(i, it) for i, it in enumerate(quiz) if s.resp.get(i) != it["ok"]]
    if fallos:
        st.subheader(f"Repaso de fallos ({len(fallos)})")
        for i, it in fallos:
            with st.expander(f"{i + 1}. {it['q']}"):
                tu = s.resp.get(i)
                st.markdown(f"**Tu respuesta:** {tu if tu else '_Sin responder_'}")
                st.markdown(f"**Correcta:** {it['ok']}")
                st.caption(it["exp"])

    c1, c2 = st.columns(2)
    if c1.button("Repetir test", use_container_width=True):
        temas = sorted({it["tema"] for it in quiz})
        iniciar(temas, len(quiz), s.modo)
        st.rerun()
    if c2.button("Volver al inicio", use_container_width=True):
        del st.session_state["quiz"]
        st.rerun()


if "quiz" not in st.session_state:
    pantalla_inicio()
elif st.session_state.fin:
    resultados()
else:
    pregunta()
