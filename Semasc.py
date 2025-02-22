from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

# ─── Configuración de Selenium ───────────────────────────────────
options = Options()
options.add_argument("--headless")  # Ejecutar en segundo plano
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument('--start-maximized')
options.add_argument('--disable-notifications')

# Inicializar el driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

CATEGORIAS = {
    # ── CATEGORÍAS GENERALES ─────────────────────────────
    "club": "General",
    "deportivo": "General",
    "atletico": "General",
    "amateur": "General",
    "liga": "General",
    
    # ── DEPORTES PRINCIPALES ─────────────────────────────
    "futbol": "Fútbol",
    "baloncesto": "Baloncesto",
    "voleibol": "Voleibol",
    "rugby": "Rugby",
    "tenis": "Tenis",
    "natacion": "Natación",
    "atletismo": "Atletismo",
    "ciclismo": "Ciclismo",
    "gimnasia": "Gimnasia",
    "boxeo": "Boxeo",
    "karate": "Karate",
    "taekwondo": "Taekwondo",
    "judo": "Judo",
    "beisbol": "Béisbol",
    "softbol": "Softbol",
    "hockey-sobre-cesped": "Hockey",
    "hockey-sobre-hielo": "Hockey",
    "surf": "Surf",
    "escalada": "Escalada",
    "patinaje": "Patinaje",
    "motociclismo": "Motociclismo",
    "automovilismo": "Automovilismo",
    "esports": "eSports",
    "futsal": "Futsal",
    "squash": "Squash",
    "ping-pong": "Ping Pong",
    "badminton": "Bádminton",
    "waterpolo": "Waterpolo",
    "equitacion": "Equitación",
    "remo": "Remo",
    "esgrima": "Esgrima",
    "skateboard": "Skateboarding",
    "skate": "Skateboarding",
    "snowboard": "Snowboard",
    "crossfit": "CrossFit",
    "powerlifting": "Powerlifting",
    "levantamiento-de-pesas": "Levantamiento de Pesas",
    
    # ── DEPORTES ADICIONALES (TRADICIONALES, EXTREMOS, NO CONVENCIONALES Y DE AVENTURA) ─────────────────────────
    "actividades-subacuaticas": "Subacuaticas",
    "club-de-actividades-subacuaticas": "Subacuaticas",
    "asociacion-de-actividades-subacuaticas": "Subacuaticas",
    "clubes-de-actividades-subacuaticas": "Subacuaticas",
    
    "ajedrez": "Ajedrez",
    "club-de-ajedrez": "Ajedrez",
    "asociacion-de-ajedrez": "Ajedrez",
    "clubes-de-ajedrez": "Ajedrez",
    
    "arqueria": "Arqueria",
    "club-de-arqueria": "Arqueria",
    "asociacion-de-arqueria": "Arqueria",
    "clubes-de-arqueria": "Arqueria",
    
    "balonmano": "Balonmano",
    "club-de-balonmano": "Balonmano",
    "asociacion-de-balonmano": "Balonmano",
    "clubes-de-balonmano": "Balonmano",
    
    "billar": "Billar",
    "club-de-billar": "Billar",
    "asociacion-de-billar": "Billar",
    
    "bowling": "Bowling",
    "club-de-bowling": "Bowling",
    "asociacion-de-bowling": "Bowling",
    "clubes-de-bowling": "Bowling",
    
    "canotaje": "Canotaje",
    "club-de-canotaje": "Canotaje",
    "asociacion-de-canotaje": "Canotaje",
    "clubes-de-canotaje": "Canotaje",
    
    "ciclismo-bmx-racing": "Ciclismo BMX",
    "club-de-ciclismo-bmx-racing": "Ciclismo BMX",
    "asociacion-de-ciclismo-bmx-racing": "Ciclismo BMX",
    "clubes-de-ciclismo-bmx-racing": "Ciclismo BMX",
    
    "ciclismo-de-montana": "Ciclismo Montaña",
    "club-de-ciclismo-de-montana": "Ciclismo Montaña",
    "asociacion-de-ciclismo-de-montana": "Ciclismo Montaña",
    "clubes-de-ciclismo-de-montana": "Ciclismo Montaña",
    
    "ciclismo-en-pista": "Ciclismo Pista",
    "club-de-ciclismo-en-pista": "Ciclismo Pista",
    "asociacion-de-ciclismo-en-pista": "Ciclismo Pista",
    "clubes-de-ciclismo-en-pista": "Ciclismo Pista",
    
    "ciclismo-en-ruta": "Ciclismo Ruta",
    "club-de-ciclismo-en-ruta": "Ciclismo Ruta",
    "asociacion-de-ciclismo-en-ruta": "Ciclismo Ruta",
    "clubes-de-ciclismo-en-ruta": "Ciclismo Ruta",
    
    "clavados": "Clavados",
    "club-de-clavados": "Clavados",
    "asociacion-de-clavados": "Clavados",
    "clubes-de-clavados": "Clavados",
    
    "ecuestre": "Equitacion",
    "club-de-ecuestre": "Equitacion",
    "asociacion-de-ecuestre": "Equitacion",
    "clubes-de-ecuestre": "Equitacion",
    
    "esqui-nautico": "Esqui Nautico",
    "club-de-esqui-nautico": "Esqui Nautico",
    "asociacion-de-esqui-nautico": "Esqui Nautico",
    "clubes-de-esqui-nautico": "Esqui Nautico",
    
    "futbol-de-salon": "Futbol de Salon",
    "club-de-futbol-de-salon": "Futbol de Salon",
    "asociacion-de-futbol-de-salon": "Futbol de Salon",
    "clubes-de-futbol-de-salon": "Futbol de Salon",
    
    "gimnasia-artistica": "Gimnasia Artistica",
    "club-de-gimnasia-artistica": "Gimnasia Artistica",
    "asociacion-de-gimnasia-artistica": "Gimnasia Artistica",
    "clubes-de-gimnasia-artistica": "Gimnasia Artistica",
    
    "gimnasia-ritmica": "Gimnasia Ritmica",
    "club-de-gimnasia-ritmica": "Gimnasia Ritmica",
    "asociacion-de-gimnasia-ritmica": "Gimnasia Ritmica",
    "clubes-de-gimnasia-ritmica": "Gimnasia Ritmica",
    
    "gimnasia-trampolin": "Gimnasia Trampolin",
    "club-de-gimnasia-trampolin": "Gimnasia Trampolin",
    "asociacion-de-gimnasia-trampolin": "Gimnasia Trampolin",
    "clubes-de-gimnasia-trampolin": "Gimnasia Trampolin",
    
    "golf": "Golf",
    "club-de-golf": "Golf",
    "asociacion-de-golf": "Golf",
    
    "hapkido": "Hapkido",
    "club-de-hapkido": "Hapkido",
    "asociacion-de-hapkido": "Hapkido",
    "clubes-de-hapkido": "Hapkido",
    
    "lucha": "Lucha",
    "club-de-lucha": "Lucha",
    "asociacion-de-lucha": "Lucha",
    "clubes-de-lucha": "Lucha",
    
    "natacion-artistica": "Natacion Artistica",
    "club-de-natacion-artistica": "Natacion Artistica",
    "asociacion-de-natacion-artistica": "Natacion Artistica",
    "clubes-de-natacion-artistica": "Natacion Artistica",
    
    "patinaje-artistico": "Patinaje Artistico",
    "club-de-patinaje-artistico": "Patinaje Artistico",
    "asociacion-de-patinaje-artistico": "Patinaje Artistico",
    "clubes-de-patinaje-artistico": "Patinaje Artistico",
    
    "patinaje-velocidad": "Patinaje Velocidad",
    "club-de-patinaje-velocidad": "Patinaje Velocidad",
    "asociacion-de-patinaje-velocidad": "Patinaje Velocidad",
    "clubes-de-patinaje-velocidad": "Patinaje Velocidad",
    
    "polo-acuatico": "Polo Acuatico",
    "club-de-polo-acuatico": "Polo Acuatico",
    "asociacion-de-polo-acuatico": "Polo Acuatico",
    "clubes-de-polo-acuatico": "Polo Acuatico",
    
    "porrismo": "Porrismo",
    "club-de-porrismo": "Porrismo",
    "asociacion-de-porrismo": "Porrismo",
    "clubes-de-porrismo": "Porrismo",
    
    "rugby-7": "Rugby 7",
    "club-de-rugby-7": "Rugby 7",
    "asociacion-de-rugby-7": "Rugby 7",
    "clubes-de-rugby-7": "Rugby 7",
    
    "skateboarding": "Skateboarding",
    "club-de-skateboarding": "Skateboarding",
    "asociacion-de-skateboarding": "Skateboarding",
    "clubes-de-skateboarding": "Skateboarding",
    
    "tejo": "Tejo",
    "club-de-tejo": "Tejo",
    "asociacion-de-tejo": "Tejo",
    "clubes-de-tejo": "Tejo",
    
    "tenis-de-mesa": "Tenis de Mesa",
    "club-de-tenis-de-mesa": "Tenis de Mesa",
    "asociacion-de-tenis-de-mesa": "Tenis de Mesa",
    "clubes-de-tenis-de-mesa": "Tenis de Mesa",
    
    "tiro-deportivo": "Tiro Deportivo",
    "club-de-tiro-deportivo": "Tiro Deportivo",
    "asociacion-de-tiro-deportivo": "Tiro Deportivo",
    "clubes-de-tiro-deportivo": "Tiro Deportivo",
    
    "triatlon": "Triatlon",
    "club-de-triatlon": "Triatlon",
    "asociacion-de-triatlon": "Triatlon",
    "clubes-de-triatlon": "Triatlon",
    
    "vela": "Vela",
    "club-de-vela": "Vela",
    "asociacion-de-vela": "Vela",
    "clubes-de-vela": "Vela",
    
    "voleibol-playa": "Voleibol Playa",
    "club-de-voleibol-playa": "Voleibol Playa",
    "asociacion-de-voleibol-playa": "Voleibol Playa",
    "clubes-de-voleibol-playa": "Voleibol Playa",
    
    # ── ORGANIZACIONES Y ESTRUCTURAS ─────────────────────
    "academia": "Organizacion",
    "academias": "Organizacion",
    "asociacion": "Organizacion",
    "federacion": "Organizacion",
    "union": "Organizacion",
    "centro-deportivo": "Organizacion",
    "escuela-deportiva": "Organizacion",
    "fifa": "Organizacion",
    "uefa": "Organizacion",
    "conmebol": "Organizacion",
    "concacaf": "Organizacion",
    "caf": "Organizacion",
    
    # ── ADJETIVOS Y CALIFICATIVOS (GENERALES) ──────────────
    "dinamico": "General",
    "activo": "General",
    "bravo": "General",
    "vigoroso": "General",
    "invencible": "General",
    "poderoso": "General",
    "elite": "General",
    "regional": "General",
    "municipal": "General",
    "nacional": "General",
    "provincial": "General",
    "internacional": "General",
    "juvenil": "General",
    "senior": "General",
    "veterano": "General",
    "femenino": "General",
    "masculino": "General",
    "mixto": "General",
    "pasion": "General",
    "fuerza": "General",
    "corazon": "General",
    "alma": "General",
    "garra": "General",
    "coraje": "General",
    "valor": "General",
    "victoria": "General",
    "triunfo": "General",
    "esfuerzo": "General",
    "gloria": "General",
    "honor": "General",
    "leyenda": "General",
    "historia": "General",
    "desafio": "General",
    "reto": "General",
    "superacion": "General",
    "sede": "General",
    "cancha": "General",
    "estadio": "General",
    "arena": "General",
    "sol": "General",
    "luna": "General",
    "estrella": "General",
    "meteoro": "General",
    "rayo": "General",
    "trueno": "General",
    "dinamita": "General",
    "energia": "General",
    "campeon": "General",
    "campeones": "General",
    "vencedor": "General",
    "legendario": "General",
    "mitico": "General",
    "eterno": "General",
    "torneo": "General",
    "copa": "General",
    "campeonato": "General",
    
    # ── CALIFICADORES / DESCRIPTORES ──────────────────────
    "atletico-en-colombia": "General",
    "club-en-colombia": "General",
    "universitario": "General",
    "semi-profesional": "General",
    "entrenador": "General",
    "jugador": "General",
    "equipo": "General",
    "varonil": "General",
    "femenil": "General",
    "iniciativa": "General",
    "orgullo": "General",
    "pasion-por-el-deporte": "General",
    "competitivo": "General",
    "disciplina": "General",
    "tactico": "General",
    "estrategia": "General",
    "innovador": "General",
    "tradicional": "General",
    "comunidad": "General",
    "respeto": "General",
    "integridad": "General",
    "dedicacion": "General",
    "entusiasmo": "General",
    "compromiso": "General",
    "progreso": "General",
    "ambicion": "General",
    "superior": "General",
    
    # ── CLUBES FAMOSOS DEL MUNDO ─────────────────────────
    # FÚTBOL (Internacionales)
    "real": "Fútbol",            # Real Madrid
    "barca": "Fútbol",           # FC Barcelona
    "bayern": "Fútbol",          # Bayern Munich
    "united": "Fútbol",          # Manchester United
    "city": "Fútbol",            # Manchester City
    "psg": "Fútbol",             # Paris Saint-Germain
    "chelsea": "Fútbol",         # Chelsea
    "arsenal": "Fútbol",         # Arsenal
    "hotspur": "Fútbol",         # Tottenham Hotspur
    "juventus": "Fútbol",        # Juventus
    "inter": "Fútbol",           # Internazionale
    "ajax": "Fútbol",            # Ajax
    "psv": "Fútbol",             # PSV Eindhoven
    "feyenoord": "Fútbol",       # Feyenoord
    "benfica": "Fútbol",         # Benfica
    "porto": "Fútbol",           # FC Porto
    "galatasaray": "Fútbol",     # Galatasaray
    "fenerbahce": "Fútbol",      # Fenerbahce
    "besiktas": "Fútbol",        # Besiktas
    "celtic": "Fútbol",          # Celtic
    "rangers": "Fútbol",         # Rangers
    "borussia": "Fútbol",        # Borussia Dortmund
    "shalke": "Fútbol",          # Schalke 04
    "eintracht": "Fútbol",       # Eintracht Frankfurt
    "america": "Fútbol",         # Club América
    "chivas": "Fútbol",          # Chivas
    "tigres": "Fútbol",          # Tigres UANL
    
    # LATINOAMERICANOS (Fútbol)
    "independiente": "Fútbol",
    "racing": "Fútbol",
    "san-lorenzo": "Fútbol",
    "velez-sarsfield": "Fútbol",
    "nacional": "Fútbol",
    "fluminense": "Fútbol",
    "botafogo": "Fútbol",
    "vasco-da-gama": "Fútbol",
    "palmeiras": "Fútbol",
    "gremio": "Fútbol",
    "internacional": "Fútbol",
    "colo-colo": "Fútbol",
    "catolica": "Fútbol",
    "universidad": "Fútbol",
    "alianza": "Fútbol",
    "universitario-de-deportes": "Fútbol",
    "sporting-cristal": "Fútbol",
    
    # EXTENSION: FÚTBOL EUROPEO / RUSO, ETC.
    "dinamo": "Fútbol",
    "spartak": "Fútbol",
    "cska": "Fútbol",
    "zenit": "Fútbol",
    "shakhtar": "Fútbol",
    "fiorentina": "Fútbol",
    "lazio": "Fútbol",
    "roma": "Fútbol",
    
    # BALONCESTO
    "lakers": "Baloncesto",
    "warriors": "Baloncesto",
    "bulls": "Baloncesto",
    "celtics": "Baloncesto",
    "heat": "Baloncesto",
    "cavaliers": "Baloncesto",
    "rockets": "Baloncesto",
    "mavericks": "Baloncesto",
    "spurs": "Baloncesto",
    "76ers": "Baloncesto",
    "knicks": "Baloncesto",
    "clippers": "Baloncesto",
    "jazz": "Baloncesto",
    "magic": "Baloncesto",
    "bucks": "Baloncesto",
    "raptors": "Baloncesto",
    "nuggets": "Baloncesto",
    "suns": "Baloncesto",
    "trail-blazers": "Baloncesto",
    "kings": "Baloncesto",
    "grizzlies": "Baloncesto",
    "pistons": "Baloncesto",
    "thunder": "Baloncesto",
    "supersonics": "Baloncesto",
    "wizards": "Baloncesto",
    "hornets": "Baloncesto",
    "pelicans": "Baloncesto",
    "bobcats": "Baloncesto",
    
    # OTROS DEPORTES INTERNACIONALES
    # Béisbol
    "yankees": "Béisbol",
    "red-sox": "Béisbol",
    "dodgers": "Béisbol",
    "giants": "Béisbol",
    "astros": "Béisbol",
    "cubs": "Béisbol",
    "mets": "Béisbol",
    "orioles": "Béisbol",
    "cardinals": "Béisbol",
    "brewers": "Béisbol",
    "royals": "Béisbol",
    "tigers": "Béisbol",
    # Rugby
    "all-blacks": "Rugby",
    "springboks": "Rugby",
    "harlequins": "Rugby",
    "wasps": "Rugby",
    "blue-bulls": "Rugby",
    # Hockey (Ice Hockey)
    "maple-leafs": "Hockey",
    "canadiens": "Hockey",
    "blackhawks": "Hockey",
    "sharks": "Hockey",
    "flames": "Hockey",
    "avalanche": "Hockey",
    # Fútbol Americano
    "patriots": "Fútbol Americano",
    "packers": "Fútbol Americano",
    "eagles": "Fútbol Americano",
    "cowboys": "Fútbol Americano",
    "steelers": "Fútbol Americano",
    "49ers": "Fútbol Americano",
    "jets": "Fútbol Americano",
    "bills": "Fútbol Americano",
    
    # eSports
    "cloud9": "eSports",
    "team-liquid": "eSports",
    "fnatic": "eSports",
    "g2": "eSports",
    "tsm": "eSports",
    "skgaming": "eSports",
    "evil-geniuses": "eSports",
    
    # ── ARTES MARCIALES ADICIONALES ─────────────────────────
    "taekido": "Artes Marciales",
    "club-de-taekido": "Artes Marciales",
    "asociacion-de-taekido": "Artes Marciales",
    "clubes-de-taekido": "Artes Marciales",
    
    "muay-thai": "Artes Marciales",
    "club-de-muay-thai": "Artes Marciales",
    "asociacion-de-muay-thai": "Artes Marciales",
    "clubes-de-muay-thai": "Artes Marciales",
    
    "savate": "Artes Marciales",
    "club-de-savate": "Artes Marciales",
    "asociacion-de-savate": "Artes Marciales",
    "clubes-de-savate": "Artes Marciales",
    
    "sambo": "Artes Marciales",
    "club-de-sambo": "Artes Marciales",
    "asociacion-de-sambo": "Artes Marciales",
    "clubes-de-sambo": "Artes Marciales",
    
    "brazilian-jiu-jitsu": "Artes Marciales",
    "club-de-brazilian-jiu-jitsu": "Artes Marciales",
    "asociacion-de-brazilian-jiu-jitsu": "Artes Marciales",
    "clubes-de-brazilian-jiu-jitsu": "Artes Marciales",
    
    "kung-fu": "Artes Marciales",
    "wushu": "Artes Marciales",
    "tai-chi": "Artes Marciales",
    "krav-maga": "Artes Marciales",
    "capoeira": "Artes Marciales",
    "kickboxing": "Artes Marciales",
    
    # ── DEPORTES MOTORIZADOS, DE AVENTURA Y EXTREMOS ─────────
    "formula-1": "Automovilismo",
    "nascar": "Automovilismo",
    "indycars": "Automovilismo",
    
    "karting": "Automovilismo",
    "drifting": "Automovilismo",
    "trial": "Automovilismo",
    "enduro": "Motociclismo",
    
    # ── DEPORTES DE AVENTURA Y PARACAIDISMO ───────────────
    "parapente": "Parapente",
    "paracaidismo": "Paracaidismo",
    "salto-base": "Salto Base",
    
    # ── DEPORTES NO CONVENCIONALES ─────────────────────────
    "dodgeball": "Dodgeball",
    "sepaktakraw": "Sepaktakraw",
    "quidditch": "Quidditch",
    "orienteering": "Orienteering",
    
    # ── DEPORTES MOTORIZADOS/CICLISTICOS EXTRAS ─────────────
    "bmx": "Ciclismo",
    "mtb": "Ciclismo",
    
    # ── ORGANIZACIONES, CALIFICADORES Y OTROS TERMOS ─────
    "iniciativa": "General",
    "orgullo": "General",
    "pasion-por-el-deporte": "General",
    "competitivo": "General",
    "disciplina": "General",
    "tactico": "General",
    "estrategia": "General",
    "innovador": "General",
    "tradicional": "General",
    "comunidad": "General",
    "respeto": "General",
    "integridad": "General",
    "dedicacion": "General",
    "entusiasmo": "General",
    "compromiso": "General",
    "progreso": "General",
    "ambicion": "General",
    "superior": "General",
    
    # ── ORGANIZACIONES INTERNACIONALES ───────────────────
    "fifa": "Organizacion",
    "uefa": "Organizacion",
    "conmebol": "Organizacion",
    "concacaf": "Organizacion",
    "caf": "Organizacion",
    
    # ── CATEGORÍA ADICIONAL ─────────────────────────────────
    "liga": "General"
}

# ─── URL base ─────────────────────────────────────────
BASE_URL = "https://www.paginasamarillas.com.co/servicios/"

# ─── Lista para almacenar los datos extraídos ─────────────────────────────────
clubes = []

# ─── Función para hacer scroll y cargar más datos ─────────────────────────
def scroll_page():
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)

# ─── Función para extraer datos de una página ─────────────────────────
def extraer_datos_pagina(deporte):
    cantidad_extraidos = 0
    print("🔍 Extrayendo datos de la página actual...")

    try:
        # Hacer scroll para cargar todas las tarjetas
        scroll_page()

        # Esperar a que las tarjetas de negocio se carguen
        elementos = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.advertise.Advertise_advertise__gh2Qj"))
        )

        print(f"✅ Se encontraron {len(elementos)} clubes en la página.")

        for elemento in elementos:
            try:
                nombre = elemento.find_element(By.CSS_SELECTOR, "div.title.Advertise_title__hWhjt").text.strip()
                telefono = elemento.find_element(By.CSS_SELECTOR, "a.phone.Advertise_phone__WAlFe").text.strip() if elemento.find_elements(By.CSS_SELECTOR, "a.phone.Advertise_phone__WAlFe") else "No disponible"
                correo = elemento.find_element(By.CSS_SELECTOR, "a[href^='mailto:']").get_attribute("href").replace("mailto:", "").strip() if elemento.find_elements(By.CSS_SELECTOR, "a[href^='mailto:']") else "No disponible"

                clubes.append({
                    "Nombre": nombre,
                    "Teléfono": telefono,
                    "Correo": correo,
                    "Deporte": deporte
                })
                cantidad_extraidos += 1
            except Exception as e:
                print(f"⚠ Error extrayendo datos de un club: {e}")
                continue

        return cantidad_extraidos

    except TimeoutException:
        print("⏳ Tiempo de espera agotado para cargar clubes.")
        return 0

# ─── Recorrer todas las categorías ─────────────────────────────────────────
for categoria, deporte in CATEGORIAS.items():
    url_actual = f"{BASE_URL}{categoria}"
    print(f"🚀 Iniciando scraping en: {url_actual} - Categoría: {deporte}")
    driver.get(url_actual)
    time.sleep(5)

    pagina = 1
    total_extraidos = 0

    while True:
        print(f"📄 Procesando página {pagina} de la categoría {categoria.upper()} ({deporte})")
        cantidad_pagina = extraer_datos_pagina(deporte)
        total_extraidos += cantidad_pagina

        if cantidad_pagina == 0:
            print("🚫 No se encontraron más clubes. Pasando a la siguiente categoría.")
            break

        # Intentar hacer clic en el botón "Siguiente"
        try:
            siguiente_btn = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//li[contains(@class, 'page-item-next')]//a"))
            )

            print(f"➡️ Haciendo clic en página {pagina + 1} de la categoría {categoria.upper()} ({deporte})")
            driver.execute_script("arguments[0].scrollIntoView();", siguiente_btn)
            time.sleep(2)
            siguiente_btn.click()
            time.sleep(5)
            pagina += 1

        except:
            print("🚫 No hay más páginas disponibles en esta categoría.")
            break

    print(f"📊 Total de clubes extraídos en {categoria.upper()} ({deporte}): {total_extraidos}")

# ─── Cerrar Selenium ───────────────────────────────────
driver.quit()

# ─── Guardar en Excel ───────────────────────────────────
if len(clubes) == 0:
    print("❌ No se recolectaron datos!")
else:
    df = pd.DataFrame(clubes).drop_duplicates()
    print(f"✅ Se encontraron {len(df)} clubes únicos.")
    df.to_excel("clubes_deportivos_colombia.xlsx", index=False)
    print("📂 Datos guardados en 'clubes_deportivos_colombia.xlsx'.")


