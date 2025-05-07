# CHANGELOG

2025-04-24
 Toteutettu REPL (run_editor_agent.py), joka tukee aritmeettisia lausekkeita, muuttujia ja määrittelyjä.

 Päivitetty dokumentaatio REPL:n osalta (language-spec.md).

2025-04-23
Laajennettu testejä kattamaan muuttujat ja määrittelyt.

Päivitetty dokumentaatio (parser_spec.md, language-spec.md).

Otettu käyttöön GitHub Actions -workflow testien ja lint-analyysin automatisointiin.

2025-04-23
Päivitetty AST-solmut (NumberNode, BinOpNode → Literal, BinaryOperation) ja attribuutit (op → operator).

Laajennettu testejä kattamaan virhetilanteet (jakolasku nollalla, määrittelemätön muuttuja).


2025-04-22
- Lisätty parser/xyndril.g4-kielioppi ja generoitu parseri/lexer.
- Suoritettu yksikkötestit onnistuneesti aritmeettisille lausekkeille.


## 2025-04-22
- Suoritettu task-006: Synkronoitu docs/parser_spec.md parserin logiikan (parser/parser.py) kanssa, dokumentoitu tuki aritmeettisille lausekkeille ja suluille.

## 2025-04-22
- Suoritettu task-005: Laajennettu parseri (parser/parser.py) tukemaan AST-rakennetta, mukaan lukien kertolasku, jakolasku ja sulut.


## 2025-04-21
- Added argparse-based CLI with 'run' subcommand to cli/xyndril.py. Now supports running .nx files with `xyndril run <file.nx>`. Added error handling and English-only messages. (Task: Improve CLI launcher)
- Implemented minimal REPL logic in src/repl.py: prompt, dummy parser/interpreter, error handling, English-only messages. Fixed SonarLint warnings (unused parameter, unused variable). (Task: Define REPL behavior)
