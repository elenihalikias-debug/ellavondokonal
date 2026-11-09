---
name: cioburi-de-suflet
description: Brandul Ellei von Dokonal, autoarea seriei Cioburi de suflet (7 volume de poezie). Se folosește la orice conținut pentru Instagram sau pentru promovarea cărților ei - citate, carusele, reels, caption-uri, bio, idei de postare. Conține identitatea vizuală, vocea, cele cinci formate și regula de aur: niciodată fața, întotdeauna ora.
---

# Cioburi de suflet · Ella von Dokonal

## Cine e autoarea

Ella von Dokonal scrie poezie de dragoste. Are șapte volume publicate, toate
traduse și în engleză, sub titlul **Cioburi de suflet**. Le-a scris între 2023 și 2025.

Nu își arată fața. Nu e un compromis, e identitatea brandului. Niciun conținut
nu cere o poză cu ea, un selfie, un reel vorbit sau o filmare. Tot ce producem
se face din text, culoare și grafică.

## Semnătura ei, singura din poezia românească de pe Instagram

**Pe fiecare poezie e trecută ora la care a fost terminată.** Nu data, ora.
03:09. 00:15. 17:10. 06:30.

Din cele 232 de poezii pe care le avem extrase (volumele I, IV, VI și VII),
71 sunt scrise între 22:00 și 06:00 — aproape o treime.
Asta nu e o curiozitate, e tot brandul. Ora spune ce nu spune poezia: că a fost
scrisă atunci, nu compusă la rece. Nimeni altcineva nu are asta.

**Regula:** ora apare pe absolut tot ce iese. Placă de citat, slide de carusel,
reel, caption. Jos-stânga pe imagini. Dacă un material nu are ora pe el, nu e gata.

## Cele șapte volume și culorile lor

O singură poveste de dragoste, în șapte etape. Volumul VII e ultimul.
Fiecare volum are culoarea lui și se folosește numai pe materialele din acel volum.

| Vol. | Culoare | Cod |
|------|---------|-----|
| I | albastru | `#024878` |
| II | vișiniu | `#762849` |
| III | violet | `#4B1764` |
| IV | magenta | `#E83694` |
| V | bleu de gheață | `#C8ECF8` (fundal deschis, cerneală închisă) |
| VI | verde | `#2A762B` |
| VII | galben | `#FEDA01` (fundal deschis) + cărămiziu `#B13A14` |

**Greșeala de evitat:** un citat din volumul VI pe fundal violet. Atâta vreme cât
volumul nu e scris pe placă nu se vede, dar din momentul în care scriem volumul,
culoarea trebuie să fie a lui.

## Fundalul brandului

| Rol | Cod |
|-----|-----|
| Fond | `#3B1024` vișiniu închis |
| Suprafață | `#4A1A2E` |
| Linie | `#6B3146` |
| Lumină (text pe închis) | `#FBEFF4` |
| Text șters | `#C9A3B2` |
| Roșu ciob | `#C03A3A` / `#D85050` |
| Alb aripă | `#F6F6F4` |
| Argint | `#B8B8B8` |

**Negrul nu se folosește nicăieri.** Fondul e vișiniul închis `#3B1024`.

## Fonturi

- **Fraunces** 600 - titluri, numele poeziilor
- **Literata** - versuri, întotdeauna cursiv
- **Archivo** - text curent, etichete, ora

Toate trei sunt gratuite pe Google Fonts. Versurile se culeg numai cu Literata cursiv.

## Semnul

Șapte cioburi verticale, de înălțimi `[16, 26, 20, 34, 18, 28, 14]` px, lățime 10px,
colț rotunjit 2px, distanță 5px, aliniate la bază. Câte unul pentru fiecare volum.
Stă jos-dreapta, cu opacitate 0.5. `references/semn.svg` îl conține gata făcut.

## Ce se arată și ce nu

**Se arată:** sticlă, geam, lumină prin geam, cristal, umbre, apă, cioburi,
coperțile cărților, textură de hârtie, culoare peste fotografie (duotone).

**Nu se arată niciodată:** fața ei, mâini care fac mozaic, vitralii de biserică
(conotație greșită), ecrane de telefon sparte, trandafiri, inimioare, fluturi,
citate pe fundal cu apus, nimic generat de AI care pretinde a fi fotografie.

## Vocea

Scrie ca o femeie care simte mult și spune puțin. Fraze scurte. Fără explicații
după vers. Fără „dragi cititori". Fără emoji în text, cu excepția inimii negre 🖤
pe care o folosește ea însăși în poezii.

**Nu se cere nimic în caption.** Fără „dă save", „scrie în comentarii ce părere ai",
„urmărește pentru mai mult". Un vers bun se distribuie singur; îndemnul îl oprește.
Singura excepție e caruselul, unde o întrebare la final are sens.

Linia brandului: **Nu tot ce s-a spart trebuie lipit la loc.**

## Cele cinci formate

### 1. Placa de citat (1080x1350)
O strofă întreagă, nu un vers. Un vers scos din strofă sună a etichetă, nu a poezie.
Sub strofă, creditul: `FRAGMENT DIN POEZIA „titlu"` și dedesubt
`Cioburi de suflet · volumul X`. Ora jos-stânga, semnul jos-dreapta.
Vezi `../../exemple/` pentru cele opt făcute deja.

### 2. Caruselul (1080x1350, 8-10 plăci)
Formatul de sortare, cel cu cea mai mare acoperire: „În ce volum ești tu?",
cu câte o placă pentru fiecare volum, pe culoarea lui. Fiecare placă trebuie să
funcționeze singură, ca screenshot. Cititoarea se recunoaște într-una și o trimite
unei prietene. La final, o întrebare.

### 3. Reel-ul grafic (1080x1920)
Fără cameră, fără stock, fără AI video. Se animă grafică: ceasul care se schimbă,
culoarea care curge, versul care apare rând cu rând. Pe frame 0 trebuie să existe
deja un cârlig vizibil. Efecte sonore numai spre final, discret, nu peste vers.

### 4. Cardul zilnic (1080x1350)
O poezie pe zi, cu ora ei, pe o fotografie colorată în culoarea volumului.

### 5. Coperta și cartea
Coperțile se arată ca obiect, pe fundalul brandului, niciodată pe un birou cu cafea.

## Măsuri tehnice

- Postare și carusel: **1080x1350**
- Reel: **1080x1920**, zona sigură: text între x 60-900 și y 250-1480
- Marginea plăcilor: 104px
- Versul: Literata cursiv, 47-62px în funcție de câte rânduri are strofa
- Rândul versului: `line-height: 1.44`

## Bio-ul de Instagram (în uz)

Câmpul nume (max. 30 de caractere): `Ella von Dokonal | poezie`

```
Nu tot ce s-a spart trebuie lipit la loc.
Bun venit în Cioburi de suflet. 7 volume, un ciob pe zi, cu ora lui.
↓ Descoperă poeziile
meleti.ro/autor/ellavondokonal
```

## Cum se alege un citat

Un citat bun se distribuie pentru că cititoarea câștigă ceva spunându-l.
Întrebarea de control: **dacă trimite asta mai departe, ce declară despre ea?**

Se ia o strofă întreagă, rimată, care se închide singură. Se verifică:
nu cere explicație, nu are nevoie de versul dinainte, nu sună a sfat.

Succesul se măsoară în **distribuiri și salvări, nu în like-uri.**

## Reguli pentru textul în română

- Verificat de un editor de limba și literatura română, gândit direct în română
- Fără cacofonii: „cu capul", „ca cei", „că ce", „la la"
- Adresare la singular, „tu", niciodată „voi" sau „dumneavoastră"
- Fără construcția „nu X, ci Y"
- Registru înalt, dar nu pretențios

## Fondul de poezii

Poeziile din volumele I, IV, VI și VII — 232 la număr — sunt extrase într-un fișier
`poezii.json`, cu câmpurile `vol`, `titlu`, `ora`, `versuri`. Volumele II, III și V
nu sunt încă extrase; când apar PDF-urile, se adaugă în același fișier.

**Acest fișier nu se pune pe internet.** Sunt cărțile ei, publicate și protejate de
drept de autor. Se ține local, pe calculatorul ei. Din el se aleg strofele, câte una
pe rând, pentru materialele publice.

Structura, dacă trebuie refăcut:
```json
[{"vol": 1, "titlu": "Fii sincer!", "ora": "00:15",
  "versuri": ["Vreau doar atât cât vrei și tu,", "..."]}]
```

## La ce se lucrează acum

Caruselul „În ce volum ești tu?" are plăcile volumelor **II, III și V** cu versul
lipsă, marcat punctat. Se completează din PDF-urile volumelor 2, 3 și 5.

Numele celor șapte etape din carusel sunt o interpretare a arcului seriei pornind
de la culori și de la descrierile de pe meleti.ro. Ella are ultimul cuvânt pe ele.
