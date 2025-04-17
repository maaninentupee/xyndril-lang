# CoreFlux-kielen manifesti ja tekninen kuvaus

## 1. Manifesti: Miksi CoreFlux on olemassa?

CoreFlux on olemassa poistamaan keinotekoisia rajoja web-kehitystyössä. Perinteisesti täytyy käyttää monia eri kieliä (JavaScript/TypeScript frontend, Python/Java/jne. backend, SQL tietokantaan) ja työkaluja koko kehitysprosessissa. CoreFlux yhdistää kaikki nämä yhdeksi johdonmukaiseksi kieleksi.

### Miten CoreFlux eroaa muista kielistä?

CoreFlux eroaa muista kielistä kolmella merkittävällä tavalla:
1. **Todellinen full-stack**: Yksi syntaksi ja semantiikka kaikille kerroksille
2. **Natiivi tekoälyintegraatio**: Kielessä on sisäänrakennetut rakenteet AI-operaatioille
3. **Saumattomat rajapinnat**: API-reitit ovat kielen rakenteita, eivät erillisiä kirjastoja

### Mitä ongelmaa CoreFlux ratkaisee?

CoreFlux ratkaisee kehittäjien työnkulun pirstoutumisen. Se eliminoi tarpeen vaihtaa kontekstia eri kielten välillä, mikä nopeuttaa kehitystä, vähentää virheitä rajakohdissa, ja mahdollistaa komponenttien optimoinnin koko stackissa.

## 2. CoreFluxin syntaksi

```
// Luokan määrittely
class User {
  // Ominaisuudet ja niiden tyypit
  name: String
  email: String
  age: Number
  
  // Konstruktori
  constructor(name, email, age) {
    this.name = name
    this.email = email
    this.age = age
  }
  
  // Metodi
  greet() -> String {
    return "Hello, I'm ${this.name}!"
  }
  
  // API-reitti luokan sisällä
  route GET /user/:id {
    // ...hakukoodi
    return this
  }
}

// Funktionaalinen tyyli
let double = (x: Number) -> Number => x * 2

// Nuolisyntaksi lyhyille funktioille
let add = (a, b) => a + b

// If-else rakenne
if (user.age >= 18) {
  console.log("Adult")
} else {
  console.log("Minor")
}

// Funktionaalinen tietojen käsittely
let adults = users
  .filter(user => user.age >= 18)
  .map(user => user.name)
```

## 3. CoreFluxin runtime-arkkitehtuuri

CoreFluxin runtime perustuu tehokkaan virtuaalikoneen ympärille, joka pystyy suorittamaan koodia sekä selaimessa että palvelimella.

### Muuttujien allokointi:
- Muuttujat analysoidaan staattisesti käännösvaiheessa
- Primitiivityypit (numerot, totuusarvot) allokoidaan pinossa
- Monimutkaiset objektit hallitaan älykkäällä heap-muistinhallinnalla
- Muuttujien elinkaari optimoidaan paikallisesti funktion kontekstiin

### Garbage Collection -strategia:
1. **Generational Collection**: Useimmat objektit ovat lyhytikäisiä, joten nuori sukupolvi kerätään usein, vanhempi sukupolvi harvemmin
2. **Concurrent GC**: Muistin keräys tapahtuu rinnakkain sovelluksen suorituksen kanssa
3. **Incremental Marking**: Suuret objektit merkitään asteittain minimoiden keskeytykset
4. **Region-based Memory**: Muisti jaetaan alueisiin tiettyjen työtehtävien mukaan nopeuttaen keräystä

CoreFluxin runtime myös synkronoi tilan saumattomasti asiakas- ja palvelinympäristöjen välillä hyödyntäen reaktiivista tiedonvirtamallia.
