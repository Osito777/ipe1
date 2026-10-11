# -*- coding: utf-8 -*-
"""
Banco de preguntas IPE1 (DAW1) - UD1 La prevención de riesgos: conceptos básicos.
Formato: (tema, pregunta, respuesta_correcta, [incorrecta_1, incorrecta_2], explicación)
Las opciones se barajan al mostrarlas, así que el orden aquí no importa.
"""

PREGUNTAS = [
    # ------------------------------------------------------------------
    # CONCEPTO DE SALUD
    # ------------------------------------------------------------------
    ("Concepto de salud",
     "Según la OMS, la salud es...",
     "El estado de bienestar físico, mental y social completo, y no solo la ausencia de enfermedad",
     ["La ausencia de daño o enfermedad", "La capacidad de trabajar sin sufrir accidentes"],
     "La definición de la OMS incluye tres aspectos: bienestar físico, psíquico y social."),

    ("Concepto de salud",
     "Un riesgo laboral es...",
     "La posibilidad de que un trabajador sufra algún daño en su salud derivado de las condiciones de trabajo",
     ["Cualquier característica del trabajo que puede influir en que aparezcan riesgos",
      "El daño que el trabajador ya ha sufrido a causa de su trabajo"],
     "Riesgo = posibilidad de daño. La segunda opción describe la 'condición de trabajo'."),

    ("Concepto de salud",
     "¿Qué es una condición de trabajo?",
     "Cualquier característica del trabajo que pueda influir en la aparición de riesgos para la seguridad y la salud",
     ["La posibilidad de que el trabajador sufra un daño",
      "El conjunto de medidas para evitar los riesgos en la empresa"],
     "Incluye locales, instalaciones, equipos, agentes físicos/químicos/biológicos, procedimientos y organización del trabajo."),

    ("Concepto de salud",
     "Un trabajador sufre una crisis de ansiedad tras una discusión con un superior. Pierde el bienestar...",
     "Psíquico",
     ["Físico", "Social"],
     "El bienestar psíquico es el equilibrio emocional y la identificación del trabajador con su tarea."),

    ("Concepto de salud",
     "Un trabajador sufre burlas de sus compañeros en la empresa. Pierde el bienestar...",
     "Social",
     ["Físico", "Psíquico"],
     "El bienestar social son las relaciones con los demás, el reconocimiento y las expectativas de futuro."),

    ("Concepto de salud",
     "Cortarse un dedo con una herramienta supone la pérdida del bienestar...",
     "Físico",
     ["Psíquico", "Social"],
     "El bienestar físico es la ausencia de daño físico o enfermedad."),

    ("Concepto de salud",
     "La prevención de riesgos laborales es...",
     "El conjunto de medidas que se toman para evitar o disminuir los riesgos laborales en la empresa",
     ["El conjunto de sanciones que se aplican a la empresa tras un accidente",
      "El conjunto de indemnizaciones que cobra el trabajador tras un daño"],
     "Para ello se precisa una legislación en materia de prevención."),

    ("Concepto de salud",
     "Un trabajo realizado en condiciones inadecuadas produce...",
     "Riesgos laborales, que pueden provocar daños en la salud",
     ["Medidas de prevención y protección", "Legislación en prevención"],
     "Esquema: condiciones inadecuadas → riesgos → daños → medidas de prevención y protección → legislación."),

    # ------------------------------------------------------------------
    # FACTORES DE RIESGO
    # ------------------------------------------------------------------
    ("Factores de riesgo",
     "Los factores de riesgo laboral se clasifican en 4 grupos:",
     "Condiciones de seguridad, medioambientales, ergonómicas y psicosociales",
     ["Condiciones físicas, químicas, biológicas y mentales",
      "Condiciones de seguridad, de higiene, de medicina y de psicología"],
     "Los 4 grupos: seguridad, medioambientales, ergonómicas y psicosociales."),

    ("Factores de riesgo",
     "La falta de barandilla en una escalera es un factor de riesgo de las condiciones de...",
     "Seguridad (lugares de trabajo)",
     ["Medioambientales (agente físico)", "Ergonómicas (carga física)"],
     "Lugares de trabajo, espacios, instalaciones y escaleras pertenecen a las condiciones de seguridad."),

    ("Factores de riesgo",
     "Un volumen muy elevado de ruido de una máquina es un factor de riesgo de las condiciones...",
     "Medioambientales (agente físico)",
     ["De seguridad (equipos de trabajo)", "Psicosociales"],
     "El ruido, las radiaciones, las vibraciones, la temperatura y la iluminación son agentes físicos."),

    ("Factores de riesgo",
     "Levantar bobinas de cobre de 40 kg supone un factor de riesgo de las condiciones...",
     "Ergonómicas (carga física)",
     ["De seguridad (lugares de trabajo)", "Medioambientales (agente químico)"],
     "La carga física incluye esfuerzos, posturas y manipulación de cargas."),

    ("Factores de riesgo",
     "Las máquinas, las herramientas y los equipos de transporte son factores de las condiciones de...",
     "Seguridad (equipos de trabajo)",
     ["Medioambientales (agentes físicos)", "Ergonómicas (carga física)"],
     "Lugares y equipos de trabajo = condiciones de seguridad. Por eso el accidente se relaciona con ellas."),

    ("Factores de riesgo",
     "Los virus, las bacterias, los hongos y los protozoos son...",
     "Agentes biológicos (condiciones medioambientales)",
     ["Agentes químicos (condiciones medioambientales)", "Agentes físicos (condiciones de seguridad)"],
     "Los agentes físicos, químicos y biológicos forman las condiciones medioambientales."),

    ("Factores de riesgo",
     "Manejar mucha información de pedidos y cajas supone un riesgo de...",
     "Carga mental (condiciones ergonómicas)",
     ["Carga física (condiciones ergonómicas)", "Agente químico (condiciones medioambientales)"],
     "La carga mental es la cantidad de información, la rapidez en la toma de decisiones y el grado de atención."),

    ("Factores de riesgo",
     "La monotonía, la variedad en la tarea, la supervisión jerárquica y el horario son aspectos de...",
     "La organización del trabajo (condiciones psicosociales)",
     ["La carga mental (condiciones ergonómicas)", "Los equipos de trabajo (condiciones de seguridad)"],
     "La organización del trabajo y las características personales forman las condiciones psicosociales."),

    ("Factores de riesgo",
     "La perfección en la realización de la tarea, la motivación laboral y la percepción del riesgo son...",
     "Características personales (condiciones psicosociales)",
     ["Carga física (condiciones ergonómicas)", "Agentes físicos (condiciones medioambientales)"],
     "Las características personales pertenecen a las condiciones psicosociales."),

    ("Factores de riesgo",
     "En un almacén de cartonaje hay un ruido de fondo de 85 decibelios. Es un factor de...",
     "Condiciones medioambientales (agente físico)",
     ["Condiciones de seguridad (equipos de trabajo)", "Condiciones ergonómicas (carga mental)"],
     "El ruido es un agente físico."),

    # ------------------------------------------------------------------
    # ACCIDENTE DE TRABAJO (LEGAL)
    # ------------------------------------------------------------------
    ("Accidente de trabajo",
     "Según la Ley General de la Seguridad Social, accidente de trabajo es...",
     "Toda lesión corporal que el trabajador sufra con ocasión o por consecuencia del trabajo que ejecute por cuenta ajena",
     ["Cualquier suceso anormal en la empresa aunque no haya lesiones",
      "Todo daño material producido en el centro de trabajo"],
     "Para que exista accidente de trabajo legal debe haber lesión."),

    ("Accidente de trabajo",
     "Los 3 requisitos legales del accidente de trabajo son...",
     "Que exista lesión, relación laboral (cuenta ajena y también propia) y relación causa-efecto",
     ["Que exista lesión, daño material y baja médica",
      "Que exista lesión, testigos y denuncia a la Inspección"],
     "Lesión + relación laboral + causalidad entre el trabajo y la lesión."),

    ("Accidente de trabajo",
     "Respecto a los trabajadores autónomos y el accidente de trabajo:",
     "Están obligados a cotizar por accidente de trabajo, por lo que están protegidos",
     ["No están protegidos porque solo se reconoce a los trabajadores por cuenta ajena",
      "Solo están protegidos si contratan un seguro privado"],
     "Antes solo se reconocía a los trabajadores por cuenta ajena, pero hoy los autónomos también cotizan."),

    ("Accidente de trabajo",
     "El accidente in itinere es el que sufre el trabajador...",
     "Al ir o al volver del lugar de trabajo",
     ["Durante la jornada laboral dentro del centro de trabajo",
      "Al realizar tareas de categoría distinta a la suya"],
     "Es un supuesto asimilado por la ley a accidente de trabajo."),

    ("Accidente de trabajo",
     "Desde 2014, el accidente in itinere también incluye...",
     "El viaje entre el domicilio habitual y el laboral, por ejemplo en domingo",
     ["Cualquier desplazamiento de ocio durante el fin de semana",
      "Solo el trayecto en transporte público"],
     "Un trabajador atropellado un domingo por la noche yendo a su domicilio laboral para empezar el lunes sufre un accidente in itinere."),

    ("Accidente de trabajo",
     "En el accidente in itinere, las interrupciones entre el fin del trabajo y el accidente...",
     "Se admiten si son cortas y habituales (como ir a comprar unos yogures, TS 17-1-18)",
     ["No se admiten nunca, ninguna interrupción es válida",
      "Se admiten siempre, sin límite de tiempo"],
     "Las sentencias han matizado los requisitos, aunque son bastante flexibles."),

    ("Accidente de trabajo",
     "Según el TSJ de Cataluña, un patinete para ir al trabajo hoy en día...",
     "Se puede considerar un medio adecuado de transporte",
     ["No es un medio adecuado nunca", "Solo es adecuado si es eléctrico y con matrícula"],
     "En el accidente in itinere el medio utilizado debe ser adecuado y el recorrido el habitual."),

    ("Accidente de trabajo",
     "Un trabajador se cae en las escaleras de su finca cuando se dirige al trabajo. ¿Es accidente de trabajo?",
     "Sí, es accidente in itinere: se incluyen los accidentes fuera y dentro del domicilio al dirigirse al trabajo",
     ["No, porque no ocurrió en el centro de trabajo",
      "No, porque ocurrió en un lugar que no es de la empresa"],
     "Es un accidente in itinere."),

    ("Accidente de trabajo",
     "Un carnicero se corta accidentalmente con el cuchillo al cortar un filete. ¿Es accidente de trabajo?",
     "Sí, por una imprudencia profesional no temeraria derivada de la confianza que inspira conocer el trabajo",
     ["No, porque se debe a una imprudencia", "No, porque no hubo causa externa"],
     "La imprudencia profesional sí es accidente de trabajo."),

    ("Accidente de trabajo",
     "Un trabajador sufre un infarto en el trabajo y acusa el estrés al que está sometido. ¿Es accidente de trabajo?",
     "Sí, existe presunción de que todo accidente en el centro de trabajo en horario laboral es accidente laboral",
     ["No, porque un infarto siempre es una enfermedad común",
      "No, porque el estrés nunca puede relacionarse con el trabajo"],
     "Cabe prueba en contrario, que demuestre que no estaba relacionado con el trabajo."),

    ("Accidente de trabajo",
     "Un delegado de prevención es atropellado cuando acude al sindicato en el tiempo reservado para ello. Es...",
     "Accidente de trabajo (supuesto de cargo sindical)",
     ["Accidente no laboral", "Enfermedad profesional"],
     "Se incluyen los accidentes por el desempeño de funciones sindicales, así como al ir o volver de ejercerlas."),

    ("Accidente de trabajo",
     "Un administrativo se lesiona al mover cajas del almacén porque estaba ayudando. Es...",
     "Accidente de trabajo (tareas distintas a las de su categoría profesional)",
     ["Accidente no laboral porque no era su tarea", "Enfermedad del trabajo"],
     "Las tareas distintas ejecutadas por orden del empresario o por iniciativa propia para la buena marcha de la empresa son accidente de trabajo."),

    ("Accidente de trabajo",
     "Un trabajador se lesiona al salvar a un compañero de un incendio en la oficina. Es...",
     "Accidente de trabajo (acto de salvamento)",
     ["Accidente no laboral porque no es su función", "Incidente"],
     "Los actos de salvamento con conexión con el trabajo son accidente de trabajo."),

    ("Accidente de trabajo",
     "Las enfermedades del trabajo son...",
     "Enfermedades no profesionales contraídas con motivo del trabajo, si se prueba por sentencia que fue por causa exclusiva del trabajo (ej. estrés laboral)",
     ["Las enfermedades que figuran en la lista cerrada de enfermedades profesionales",
      "Cualquier enfermedad que el trabajador tenga mientras está contratado"],
     "Se consideran accidente de trabajo si se prueba por sentencia judicial."),

    ("Accidente de trabajo",
     "Un trabajador operado tras un accidente contrae un virus en el quirófano. Es...",
     "Consecuencia del accidente: se considera accidente de trabajo",
     ["Accidente no laboral nuevo", "Enfermedad profesional"],
     "Las consecuencias y complicaciones derivadas del accidente se incluyen como accidente de trabajo."),

    ("Accidente de trabajo",
     "Un trabajador con una lesión anterior sufre un esguince que se agrava a raíz de un accidente laboral. ¿Qué ocurre?",
     "Las enfermedades o defectos previos que se agravan como consecuencia del accidente se incluyen",
     ["No se incluyen porque ya existían antes", "Solo se incluyen si el trabajador es autónomo"],
     "Es otro supuesto de consecuencias del accidente."),

    ("Accidente de trabajo",
     "La directora financiera es atropellada por una moto camino del banco a firmar unos pagarés. ¿Es accidente de trabajo?",
     "Sí, es una tarea laboral fuera del centro en horario de trabajo (tarea 'in mission')",
     ["No, porque no ocurrió en el centro de trabajo", "No, porque fue culpa de un tercero"],
     "Salir del centro para realizar tareas laborales en horario de trabajo es accidente de trabajo."),

    ("Accidente de trabajo",
     "Una trabajadora sufre una depresión por acoso laboral y se demuestra en juicio que está vinculada al trabajo. Es...",
     "Accidente de trabajo (enfermedad del trabajo probada por sentencia)",
     ["Enfermedad común sin protección", "Incidente"],
     "Las enfermedades del trabajo probadas judicialmente se asimilan al accidente de trabajo."),

    ("Accidente de trabajo",
     "Mientras manipula el curvado de acero, un trabajador se distrae hablando con un compañero y se amputa un dedo. Es...",
     "Accidente de trabajo (imprudencia profesional)",
     ["No es accidente de trabajo por imprudencia temeraria", "No es accidente de trabajo por dolo"],
     "Un descuido no intencional por la confianza que inspira el trabajo habitual es imprudencia profesional."),

    ("Accidente de trabajo",
     "En una empresa de Alzira hay una inundación por lluvias torrenciales y un trabajador resbala golpeándose la cadera. Es...",
     "Accidente de trabajo, como ocurre con la insolación, el rayo y otros fenómenos parecidos de la naturaleza",
     ["No es accidente de trabajo porque fue fuerza mayor extraña",
      "No es accidente de trabajo porque lo causó la lluvia"],
     "Los fenómenos de la naturaleza como el rayo o la insolación sí se consideran accidente de trabajo."),

    ("Accidente de trabajo",
     "Respecto a las lesiones sufridas en el centro de trabajo en horario laboral:",
     "Se presume que son accidente de trabajo, salvo prueba en contrario",
     ["No son accidente de trabajo salvo que lo demuestre el trabajador",
      "Solo son accidente de trabajo si hay testigos"],
     "Es una presunción que admite prueba en contrario."),

    # ------------------------------------------------------------------
    # CASOS ESPECIALES Y EXCEPCIONES (vistos en clase)
    # ------------------------------------------------------------------
    ("Casos especiales (clase)",
     "Juris tantum significa que una presunción...",
     "Admite prueba en contrario",
     ["No admite ninguna prueba en contrario", "Solo la puede aplicar el Tribunal Supremo"],
     "La presunción de accidente de trabajo en el centro y horario laboral es juris tantum."),

    ("Casos especiales (clase)",
     "La jurisprudencia es...",
     "El criterio que fija el Tribunal Supremo al resolver casos mediante sentencias de casación",
     ["El conjunto de leyes aprobadas por el Parlamento", "Una norma elaborada por la empresa"],
     "Tribunal Supremo → juicios/casos → sentencia (casación) → jurisprudencia."),

    ("Casos especiales (clase)",
     "La imprudencia profesional del trabajador...",
     "Sí puede ser accidente de trabajo",
     ["Nunca es accidente de trabajo", "Es accidente solo si el empresario la ordena por escrito"],
     "Es el descuido no intencional derivado de la confianza que inspira el ejercicio habitual del trabajo."),

    ("Casos especiales (clase)",
     "La imprudencia temeraria del trabajador...",
     "No se considera accidente de trabajo",
     ["Sí se considera accidente de trabajo", "Se considera siempre enfermedad profesional"],
     "Imprudencia temeraria o dolo (intencional) del trabajador excluyen el accidente de trabajo."),

    ("Casos especiales (clase)",
     "Si el trabajador provoca el accidente con dolo (intencionadamente)...",
     "No es accidente de trabajo",
     ["Sí es accidente de trabajo", "Es accidente de trabajo si la empresa no puso medidas"],
     "El dolo es una de las excepciones que no se consideran accidente de trabajo."),

    ("Casos especiales (clase)",
     "Los accidentes debidos a fuerza mayor extraña al trabajo...",
     "No son accidente de trabajo, pero sí lo son la insolación, el rayo y fenómenos parecidos de la naturaleza",
     ["Son siempre accidente de trabajo, incluidos los de causa ajena al trabajo",
      "No son accidente de trabajo, ni siquiera el rayo o la insolación"],
     "Excepción: rayo e insolación sí cuentan como accidente de trabajo."),

    ("Casos especiales (clase)",
     "Un trabajador sufre lesiones por un rayo durante su jornada y la empresa no había colocado un pararrayos. ¿Es accidente de trabajo?",
     "Sí, el rayo es una excepción: sí es accidente de trabajo (más aún si la empresa no colocó pararrayos)",
     ["No, porque un rayo es siempre fuerza mayor extraña", "No, porque ocurrió por azar o mala suerte"],
     "Caso visto en clase: insolación o rayo → sí es accidente de trabajo."),

    ("Casos especiales (clase)",
     "Un trabajador sufre una insolación durante su jornada. ¿Es accidente de trabajo?",
     "Sí, es una excepción a la fuerza mayor extraña",
     ["No, porque es un fenómeno de la naturaleza", "No, porque fue mala suerte"],
     "Insolación y rayo sí son accidente de trabajo."),

    ("Casos especiales (clase)",
     "Un trabajador sufre un accidente cuya causa es la culpabilidad de un tercero. ¿Es accidente de trabajo?",
     "Sí, es accidente de trabajo",
     ["No, porque la culpa es de otra persona", "Solo si el tercero es otro trabajador de la empresa"],
     "La culpabilidad de un tercero no excluye el accidente de trabajo."),

    ("Casos especiales (clase)",
     "Un trabajador intenta robar algo en la empresa y se lesiona en el intento. ¿Es accidente de trabajo?",
     "No, porque su actuación fue dolosa y ajena al trabajo",
     ["Sí, porque ocurrió dentro del centro de trabajo", "Sí, porque ocurrió en horario laboral"],
     "Aunque haya presunción por lugar y horario, es una excepción: el dolo excluye el accidente de trabajo."),

    ("Casos especiales (clase)",
     "Un trabajador percibe restos de plástico en una máquina y mete el brazo sin pararla (hay un cartel rojo que lo prohíbe). Es...",
     "Imprudencia profesional",
     ["Imprudencia temeraria", "Dolo"],
     "Según el ejemplo del libro, el primer caso es imprudencia profesional."),

    ("Casos especiales (clase)",
     "Un trabajador de la construcción desoye las advertencias del encargado, baja por el hueco del andamio sin escalera ni arnés y cae. Es...",
     "Imprudencia temeraria",
     ["Imprudencia profesional", "Fuerza mayor extraña al trabajo"],
     "Según el ejemplo del libro, el segundo caso es imprudencia temeraria."),

    # ------------------------------------------------------------------
    # TIPOS DE ACCIDENTE Y CAUSAS
    # ------------------------------------------------------------------
    ("Tipos de accidente y causas",
     "Desde el punto de vista de la prevención, los 4 tipos de accidente son...",
     "Accidente típico, accidente caso, accidente blanco e incidente",
     ["Accidente grave, leve, mortal e incidente", "Accidente típico, atípico, blanco y negro"],
     "Se obtienen combinando lesiones en personas y daños materiales."),

    ("Tipos de accidente y causas",
     "El accidente típico es aquel en el que hay...",
     "Lesiones en las personas y daños materiales",
     ["Lesiones en las personas pero no daños materiales", "Daños materiales pero no lesiones"],
     "Ejemplo: golpe entre dos coches con daños en los coches y lesiones en las personas."),

    ("Tipos de accidente y causas",
     "El accidente caso es aquel en el que hay...",
     "Lesiones en las personas pero no daños materiales",
     ["Lesiones y daños materiales", "Daños materiales pero no lesiones"],
     "Ejemplo: lesiones en las personas pero al coche no le pasa nada."),

    ("Tipos de accidente y causas",
     "El accidente blanco es aquel en el que hay...",
     "Daños materiales pero no lesiones en las personas",
     ["Lesiones en las personas pero no daños materiales", "Ni lesiones ni daños materiales"],
     "Ejemplo: la carrocería sufre un golpe pero el conductor sale ileso."),

    ("Tipos de accidente y causas",
     "El incidente es aquella situación donde...",
     "No hay lesiones ni daños materiales, pero existe una situación de riesgo que podría haberlos provocado",
     ["Hay lesiones leves y daños materiales pequeños", "Solo hay lesiones psíquicas"],
     "Ejemplo: un adelantamiento negligente donde a última hora se evita el golpe."),

    ("Tipos de accidente y causas",
     "A efectos de baja para la Seguridad Social, son accidente de trabajo solo...",
     "El accidente típico y el accidente caso",
     ["El accidente blanco y el incidente", "Los cuatro tipos de accidente"],
     "Para la Seguridad Social se necesita lesión."),

    ("Tipos de accidente y causas",
     "¿Por qué desde el punto de vista preventivo se amplía el concepto a accidentes blancos e incidentes?",
     "Porque alertan de que existen fallos en el sistema de prevención y puede haber lesiones otra vez",
     ["Porque dan derecho a una baja médica", "Porque la empresa debe indemnizar los daños materiales"],
     "'No ha pasado nada' pero 'podría haber pasado'."),

    ("Tipos de accidente y causas",
     "La teoría de la causalidad dice que los accidentes...",
     "Tienen siempre una causa que se podría haber evitado; no se deben al azar ni a la superstición",
     ["Se deben al azar o a la mala suerte", "Solo se producen por el error del trabajador"],
     "Las causas se dividen en técnicas y humanas."),

    ("Tipos de accidente y causas",
     "En el almacén de un centro de salud se caen las estanterías con todo el material al suelo, pero el celador no estaba allí. Es un...",
     "Accidente blanco",
     ["Accidente típico", "Incidente"],
     "Hay daños materiales pero no lesiones."),

    ("Tipos de accidente y causas",
     "A un trabajador se le engancha la manga con una máquina que le arrastra el antebrazo y se lo amputa. Es un...",
     "Accidente típico",
     ["Accidente caso", "Accidente blanco"],
     "Hay lesiones en la persona y daños materiales en la ropa/máquina."),

    ("Tipos de accidente y causas",
     "Un electricista manipula la instalación sin verificar la ausencia de tensión, pero ese día no le pasa nada. Es un...",
     "Incidente",
     ["Accidente blanco", "Accidente caso"],
     "No hay lesiones ni daños, pero sí una situación de riesgo."),

    ("Tipos de accidente y causas",
     "Un trabajador se cae al romperse la rama del árbol en la que estaba apoyado, se fractura la tibia y la motosierra se destroza. Es un...",
     "Accidente típico",
     ["Accidente caso", "Accidente blanco"],
     "Hay lesiones y daños materiales."),

    ("Tipos de accidente y causas",
     "Pepe entró hace poco a trabajar y no le han informado de los riesgos de su puesto. La causa humana es que...",
     "El trabajador desconoce que existe un riesgo (falta de información y formación de la empresa)",
     ["El trabajador sabe cómo actuar pero decide no hacerlo", "El trabajador sabe que hay riesgo pero no sabe cómo actuar"],
     "Falta de formación e información por parte de la empresa."),

    ("Tipos de accidente y causas",
     "Pablo hizo un curso de prevención (charla y test) y sabe los riesgos, pero no sabría cómo actuar. La causa humana es...",
     "Sabe que existe un riesgo pero no sabe cómo actuar",
     ["Desconoce que existe un riesgo", "Conoce el riesgo y decide no actuar de forma preventiva"],
     "El curso no fue más allá de una charla y un test."),

    ("Tipos de accidente y causas",
     "Laura conoce los riesgos y sabe cómo evitarlos, pero piensa eliminar las medidas que ralentizan su trabajo. La causa humana es...",
     "Conoce el riesgo y sabe cómo actuar, pero decide no querer actuar de forma preventiva",
     ["Desconoce que existe un riesgo", "Sabe que existe un riesgo pero no sabe cómo actuar"],
     "Es una causa humana por decisión del trabajador."),

    # ------------------------------------------------------------------
    # ENFERMEDAD PROFESIONAL
    # ------------------------------------------------------------------
    ("Enfermedad profesional",
     "En el antiguo sistema de lista cerrada, una enfermedad era profesional si...",
     "Figuraba en la lista elaborada por el Ministerio de Trabajo",
     ["La decidía libremente el médico de cada empresa", "Era grave y duraba más de un año"],
     "Si la enfermedad estaba en la lista, se daba por hecho que era debida al trabajo."),

    ("Enfermedad profesional",
     "El RD 1.299/2006 establece un sistema mixto porque incluye...",
     "Un Anexo I (lista cerrada de enfermedades probadas) y un Anexo II (lista complementaria abierta)",
     ["Dos listas cerradas, una para empresas y otra para autónomos", "Una lista de enfermedades y otra de accidentes"],
     "El Anexo II recoge enfermedades que podrían considerarse profesionales en un futuro."),

    ("Enfermedad profesional",
     "Si una enfermedad se contrae por el trabajo pero no está en ninguna lista...",
     "Hay que demostrar ante el Juzgado la relación, y si se demuestra se considera accidente de trabajo",
     ["No se puede reclamar nada", "Se considera enfermedad profesional automáticamente"],
     "Se trata de una enfermedad del trabajo."),

    ("Enfermedad profesional",
     "Una diferencia entre la enfermedad profesional y el accidente de trabajo es que la enfermedad profesional...",
     "Es lenta y sus efectos aparecen al cabo de los años; el accidente es instantáneo",
     ["Es instantánea; el accidente aparece lentamente", "Tiene efectos idénticos en todos los trabajadores"],
     "La enfermedad profesional aumenta conforme se está más tiempo expuesto."),

    ("Enfermedad profesional",
     "Los efectos de la enfermedad profesional son...",
     "Individuales: en unas personas leves y en otras muy graves",
     ["Idénticos para todos los que la sufren", "Siempre leves"],
     "En el accidente, en cambio, los efectos son idénticos para todos."),

    ("Enfermedad profesional",
     "La enfermedad profesional se relaciona sobre todo con las condiciones...",
     "Medioambientales (físicas, químicas y biológicas)",
     ["De seguridad (lugares, instalaciones, equipos)", "Psicosociales"],
     "El accidente de trabajo se relaciona más con las condiciones de seguridad."),

    ("Enfermedad profesional",
     "Hasta 2006 el responsable de cumplimentar el parte de enfermedades profesionales era el empresario. Hoy es...",
     "La Mutua, que notifica y registra estas enfermedades",
     ["El propio trabajador", "El Ayuntamiento"],
     "El cambio busca evitar el subregistro (se declaraban muchas menos de las reales)."),

    ("Enfermedad profesional",
     "En las estadísticas, el mayor número de enfermedades profesionales corresponde a...",
     "Trastornos músculo-esqueléticos y dermatosis (enfermedades de la piel)",
     ["Cánceres y enfermedades respiratorias", "Enfermedades infecciosas y estrés"],
     "Son las más numerosas en el registro."),

    ("Enfermedad profesional",
     "La asbestosis por inhalación de partículas de amianto pertenece al grupo de enfermedades causadas por...",
     "Inhalación de sustancias y agentes no comprendidos en otros apartados",
     ["Agentes biológicos", "Agentes físicos"],
     "El amianto (uralita, tela aislante) también está incluido en el grupo de cancerígenos (mesotelioma)."),

    ("Enfermedad profesional",
     "El saturnismo provocado por intoxicación con plomo es una enfermedad causada por agentes...",
     "Químicos",
     ["Físicos", "Biológicos"],
     "El plomo es una sustancia química."),

    ("Enfermedad profesional",
     "El síndrome del dedo blanco por uso de herramientas vibratorias es una enfermedad causada por agentes...",
     "Físicos",
     ["Químicos", "Biológicos"],
     "Las vibraciones son un agente físico."),

    ("Enfermedad profesional",
     "El tétanos por heridas con clavos es una enfermedad causada por agentes...",
     "Biológicos",
     ["Físicos", "Químicos"],
     "Es una bacteria."),

    ("Enfermedad profesional",
     "El cáncer de pulmón en trabajos expuestos al polvo de sílice es una enfermedad causada por agentes...",
     "Cancerígenos",
     ["Biológicos", "Físicos"],
     "Es una enfermedad profesional causada por agentes cancerígenos."),

    ("Enfermedad profesional",
     "La sordera o hipoacusia profesional por ruido pertenece al grupo de enfermedades causadas por agentes...",
     "Físicos",
     ["Químicos", "Biológicos"],
     "El ruido es un agente físico."),

    ("Enfermedad profesional",
     "Un trabajador que manejó amianto hace muchos años y ahora tiene asbestosis...",
     "Puede reclamar una enfermedad profesional actual causada por un trabajo realizado hace muchos años",
     ["No puede reclamar porque ya pasó mucho tiempo", "Solo puede reclamar si sigue en la misma empresa"],
     "La presunción de que se ha adquirido por el contacto con los productos de la lista se mantiene a lo largo del tiempo."),

    # ------------------------------------------------------------------
    # FATIGA E INSATISFACCIÓN
    # ------------------------------------------------------------------
    ("Fatiga e insatisfacción",
     "La fatiga laboral es...",
     "La disminución de la capacidad física y mental para realizar el trabajo debido al cansancio",
     ["Una actitud negativa hacia el trabajo", "Un daño que solo produce la carga mental"],
     "Puede producirla la carga física o la carga mental."),

    ("Fatiga e insatisfacción",
     "La insatisfacción laboral es...",
     "Una actitud negativa hacia el trabajo por la diferencia entre las expectativas generadas y la realidad, y la importancia que se le da a esa diferencia",
     ["La disminución de la capacidad física y mental por el cansancio", "Una enfermedad profesional de lista cerrada"],
     "Influyen tres factores a la vez: expectativas, realidad e importancia."),

    ("Fatiga e insatisfacción",
     "La insatisfacción laboral puede llegar a producir...",
     "Estrés, depresión y burnout (síndrome de estar quemado)",
     ["Asbestosis y saturnismo", "Accidentes blancos"],
     "Es una patología inespecífica, igual que la fatiga."),

    # ------------------------------------------------------------------
    # PREVENCIÓN Y PROTECCIÓN
    # ------------------------------------------------------------------
    ("Prevención y protección",
     "La diferencia entre medidas de prevención y de protección es que las de prevención...",
     "Actúan antes de que se produzca el daño, eliminando o reduciendo las causas en su raíz (el foco)",
     ["Reducen las consecuencias del accidente una vez producido", "Solo protegen a un trabajador directamente"],
     "Ejemplo del coche: frenos ABS (prevención) frente a airbag (protección)."),

    ("Prevención y protección",
     "En el ejemplo del automóvil, el airbag es una medida de...",
     "Protección, porque no evita el accidente sino que minimiza las consecuencias",
     ["Prevención, porque evita el accidente", "Ninguna de las dos"],
     "Las de protección reducen o eliminan las consecuencias sobre el trabajador."),

    ("Prevención y protección",
     "Una red de seguridad o un extractor de humos son medidas de...",
     "Protección colectiva (actúan sobre el medio de transmisión)",
     ["Protección individual (actúan sobre el trabajador)", "Prevención (actúan sobre el foco)"],
     "Protegen a varios trabajadores a la vez."),

    ("Prevención y protección",
     "Sustituir una máquina ruidosa por otra más silenciosa es una medida de...",
     "Prevención (actúa sobre el foco)",
     ["Protección colectiva (actúa sobre el medio de transmisión)", "Protección individual (actúa sobre el trabajador)"],
     "Sustitución de máquinas y productos, reparación y diseño inicial son medidas sobre el foco."),

    ("Prevención y protección",
     "El orden de prioridad de las medidas es...",
     "Prevención, luego protección colectiva y por último protección individual",
     ["Protección individual, protección colectiva y prevención", "Protección colectiva, prevención y protección individual"],
     "Primero se evitan los riesgos en su origen; los EPIs son la última medida."),

    ("Prevención y protección",
     "Elementos sobre los que actúan: prevención, protección colectiva y protección individual, respectivamente:",
     "El foco, el medio de transmisión y el trabajador",
     ["El trabajador, el foco y el medio de transmisión", "El medio de transmisión, el trabajador y el foco"],
     "Ejemplos: sustituir máquinas / barandillas y pantallas / mascarillas y tapones."),

    ("Prevención y protección",
     "Instalar pantallas acústicas frente al ruido es una técnica de...",
     "Protección colectiva",
     ["Prevención sobre el foco", "Protección individual"],
     "Las pantallas, barandillas, redes, resguardos y la ventilación son protección colectiva."),

    ("Prevención y protección",
     "Medir el aire de una fábrica para detectar contaminantes químicos corresponde a la técnica de...",
     "Higiene industrial",
     ["Seguridad", "Medicina del trabajo"],
     "La higiene industrial previene las enfermedades profesionales por contaminantes físicos, químicos y biológicos."),

    ("Prevención y protección",
     "Hacer pausas cada 2 horas para disminuir la fatiga frente al ordenador corresponde a la técnica de...",
     "Ergonomía",
     ["Higiene industrial", "Psicosociología"],
     "La ergonomía adapta el trabajo al trabajador para evitar la fatiga."),

    ("Prevención y protección",
     "Realizar reconocimientos médicos anuales corresponde a la técnica de...",
     "Medicina del trabajo",
     ["Seguridad", "Ergonomía"],
     "Incluye vacunación y reconocimientos periódicos."),

    ("Prevención y protección",
     "Organizar el trabajo con rotación de tareas para evitar la monotonía corresponde a la técnica de...",
     "Psicosociología",
     ["Ergonomía", "Higiene industrial"],
     "La psicosociología lucha contra la insatisfacción laboral."),

    ("Prevención y protección",
     "Diseñar herramientas seguras que impidan el contacto eléctrico corresponde a la técnica de...",
     "Seguridad",
     ["Higiene industrial", "Medicina del trabajo"],
     "La seguridad actúa sobre las condiciones de seguridad para evitar accidentes."),

    ("Prevención y protección",
     "Los equipos de protección individual (EPIs) son...",
     "La última medida en la prevención de riesgos laborales",
     ["La primera medida que debe aplicar la empresa", "Las únicas medidas necesarias si el trabajador es experimentado"],
     "Antes deben tomarse las medidas de prevención y de protección colectiva."),

    ("Prevención y protección",
     "¿Cuál de las siguientes NO se considera un EPI?",
     "La ropa de trabajo corriente y los uniformes no destinados a proteger la salud (batas de vendedores)",
     ["Un casco", "Unos tapones para los oídos"],
     "Tampoco son EPI el material deportivo o los equipos de militares y policías."),

    ("Prevención y protección",
     "Un soldador necesita proteger los ojos y la cara. Su EPI será...",
     "Pantalla para soldadura",
     ["Calzado de seguridad", "Orejeras"],
     "Ojos y cara: gafas de montura, pantalla facial y pantalla para soldadura."),

    ("Prevención y protección",
     "Luis repara instalaciones eléctricas de baja tensión. Sus EPIs deben ser...",
     "Guantes dieléctricos, calzado de seguridad aislante y cascos eléctricamente aislantes",
     ["Mascarilla filtrante de partículas y orejeras", "Arnés antivibraciones y pantalla facial"],
     "Además, los EPIs no son el único elemento de protección: antes van las medidas preventivas y colectivas."),
]
