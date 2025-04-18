# 🚀 Xyndril

Xyndril on kokeellinen full-stack-ohjelmointikieli, joka yhdistää modernin backendin, frontend-komponentit ja tekoälyn yhdeksi kieliytimeksi.

---

## 🔧 Mitä tämä versio sisältää (v0.0.1)

- `print()`-komento
- Luokkien (`class`) määrittely
- REST-rajapintojen (`route GET`) määrittely
- Esimerkkitiedosto: `examples/hello.nx`
- Yksinkertainen tokenizer, parseri ja runtime (Pythonilla)

---

## 🛠️ Suoritus

Varmista, että sinulla on Python 3.9 tai uudempi asennettuna.

Aja ohjelma komentoriviltä:

```bash
python cli/xyndril.py examples/hello.nx

🧭 Tiekartta (v0.0.2+)
🔜 ai.prompt(), ai.generate() – AI-komennot
🔜 import – Tiedostojen tuonti
🔜 Modulaarinen rakenne
🔜 Valinnainen staattinen tyypitys
🔜 REPL-tuki

📁 Projektirakenne
xyndril-kit/
├── cli/                 # CLI-käynnistysohjelma
│   └── xyndril.py
├── examples/            # Esimerkkiohjelmat (.nx)
│   └── hello.nx
├── parser/              # Tokenizer ja parser
│   ├── tokenizer.py
│   └── parser.py
├── interpreter/         # Tulkki AST:n evaluointiin
│   └── runtime.py
├── design/              # Clauden suunnittelutiedostot
│   ├── ast.cld.py
│   ├── interpreter.cld.py
│   └── parser_spec.md
└── README.md

💡 Miksi Xyndril?
Nykyinen ohjelmointikehitys on hajautunutta eri kieliin:

👨‍💻 Backend (Python, Go...)
🌐 Frontend-komponentit (JS, React...)
🤖 Tekoäly (OpenAI, langchain...)

Xyndril yhdistää kaiken yhteen kieleen.

Yksi kieli. Yksi projekti. Kaikki kerrokset.

🧠 Filosofia
"One language to rule every layer"

Syntaksi: helppolukuinen, laajennettava

Tyyppijärjestelmä: kevyt, valinnainen

Tekoäly: sisäänrakennettu ominaisuus, ei kirjasto

🧪 Esimerkkikoodi
print("Hello world!")

class User(name: string) {
  fn greet() {
    return "Hi, " + self.name
  }
}

route GET /hello => {
  return User("Tony").greet()
}

🧩 Lisätietoja
Design-tiedostot sijaitsevat design/-kansiossa ja sisältävät:

AST-määrittely: ast.cld.py

Interpreter-rakenne: interpreter.cld.py

Parser-kuvaus: parser_spec.md

Nämä tiedostot GPT refaktoroi tuotantokoodiksi:

src/ast.py

src/interpreter.py

parser/xyndril.g4

src/repl.py (REPL-tuki)

