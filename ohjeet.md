















































Kehittäjäohjeet kielen käytöstä ja SonarLint-ongelmien automaattisesta korjauksesta
1. Yleiset viestintä- ja koodausstandardit

Kaikki koodi on kirjoitettava englanniksi.
Kaikkien muuttujien nimet, funktiot, virheilmoitukset, lokiviestit ja inline-kommentit tulee olla englanninkielisiä.
Agentin oletusviestintäkielenä tulee olla englanti.
Kaikki agentin antamat vastaukset ja tekniset viestit ovat englanniksi, ellei käyttäjä erikseen pyydä kielen vaihtoa.
Suomen kielen käyttö:
Suomen kieltä saa käyttää ainoastaan testitapauksissa, joissa testi nimenomaisesti liittyy lokalisaatioon. Muissa tilanteissa kaikki viestintä ja testit on kirjoitettava englanniksi.
2. Kielen vaihtaminen käyttäjän pyynnöstä

Käyttäjän kielipyyntö:
Jos käyttäjä antaa käskyn "puhu suomeksi" tai muun vastaavan pyynnön, agentin tulee vaihtaa keskustelun kieleksi suomi. Tämä koskee ainoastaan vuorovaikutusta käyttäjän kanssa, mutta kaikki koodi ja tekniset viestit säilyvät englanniksi.
3. SonarLintin ilmoittamien ongelmien automaattinen korjaus

Automaattinen virheenkorjaus:
Agentin tulee automaattisesti analysoida koodia ja huomioida SonarLintin ilmoittamat varoitukset ja virheilmoitukset.
Esimerkiksi, jos koodi sisältää käyttämättömiä importteja tai virheellisen tyyppimääritelmän (kuten "error is of type 'unknown'"), agentin tulee automaattisesti poistaa tai korjata ne.
Agentin on huolehdittava siitä, että se ei tee samoja virheitä toistuvasti, eli se tarkistaa aiemmin SonarLintin ilmoittamat ongelmat ennen koodin commitointia tai pushausta.
Integraatio koodin generoinnissa:
Agentin on sisällytettävä SonarLintin ilmoitukset osaksi koodin generointiprosessia. Tämä tarkoittaa, että ennen koodin tallentamista tai commitointia agentin tulee tarkistaa, ettei koodi sisällä aiemmin tunnistettuja virheitä, ja tehdä tarvittavat korjaukset automaattisesti.
4. Versionhallinta ja synkronointi

Reaaliaikainen kehitystyö Gitin avulla:
Molempien editorien (Windsurf Editorin Cascade-agentti ja VS Code Copilot) tekemät muutokset viedään yhteiseen Git-repoon.
Ennen muokkaamista agentti suorittaa git pull varmistaakseen, että paikallinen kopio on ajan tasalla.
Muutosten jälkeen tehdään commit ja push, jolloin molemmat ympäristöt saavat päivitykset lähes reaaliaikaisesti.
Näin varmistetaan, että agentti huomioi sekä Windsurfissa että VS Codessa tehdyt koodimuutokset ja ettei mikään korjaus tapahdu ylimääräisesti ylikirjoittaen toisen tekemät parannukset.

