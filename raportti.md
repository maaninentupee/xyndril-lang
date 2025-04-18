
# Raportti: MkDocs 404-virheet ja sisällön päivittymättömyys

## Ongelman kuvaus

Projektin dokumentaatiota rakennettaessa MkDocsilla ilmeni kaksi pääongelmaa:

1. **404-virheet (sivua ei löydy):**
   - Navigaatiossa ja/tai markdown-tiedostoissa oli useita viittauksia tiedostoihin, jotka eivät olleet MkDocs:n käytettävissä.
   - MkDocs näyttää vain docs/-kansion sisällä olevat tiedostot. Jos mkdocs.yml- tai markdown-linkeissä viitataan tiedostoihin projektin muissa kansioissa (esim. ../design/parser_spec.md), syntyy 404-virhe.
   - Konsolilogeissa näkyi varoituksia puuttuvista tiedostoista ja linkeistä, jotka eivät löydy dokumentaatiosta.

2. **Dokumentaation sisällön päivittymättömyys:**
   - Vaikka tiedostoja muokattiin tai siirrettiin, MkDocs ei aina päivittänyt sisältöä oikein selaimessa.
   - Tämä johtui siitä, että osa tiedostoista oli väärässä kansiossa, eikä MkDocs tunnistanut niitä osaksi dokumentaatiota.
   - Lisäksi selain saattoi näyttää välimuistista vanhaa sisältöä, vaikka tiedostot oli päivitetty.

## Ratkaisut ja toimenpiteet

- Kaikki dokumentaatiossa tarvittavat tiedostot (parser_spec.md, ast.cld.py, interpreter.cld.py, xyndril.g4) kopioitiin docs/-kansioon.
- mkdocs.yml päivitettiin niin, että nav-viittaukset osoittavat vain docs/-kansion sisällä oleviin tiedostoihin.
- Kaikki markdown-linkit tulee päivittää vastaamaan docs/-kansion rakennetta.
- Selaimen välimuisti kannattaa tyhjentää, jos sisältö ei päivity odotetusti.
- MkDocs-palvelin kannattaa käynnistää uudelleen muutosten jälkeen.

## Yhteenveto

MkDocs-dokumentaatio toimii luotettavasti vain, kun kaikki viitattavat tiedostot ovat docs/-kansion sisällä ja nav-polut sekä markdown-linkit on päivitetty vastaamaan tätä rakennetta. Ongelmat johtuivat projektin ulkopuolisiin kansioihin viittaavista poluista sekä selain- ja palvelinvälimuistista. Oikeilla kansio- ja polkuasetuksilla sekä palvelimen uudelleenkäynnistyksellä 404-virheet ja sisällön päivittymättömyys saatiin ratkaistua.

---
