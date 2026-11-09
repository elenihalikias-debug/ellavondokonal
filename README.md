# Cioburi de suflet · trusa de conținut

Tot ce îi trebuie **Ellei von Dokonal** ca să-și facă singură conținutul pentru
Instagram, cu ajutorul lui Claude: brandul scris pe hârtie, fundalurile celor
șapte volume, un script care face plăcile de citat, și promptul de pornire.

Pregătit de [Meleti](https://meleti.ro) în cadrul provocării AI CUVÂNTUL.

---

## De unde începi

**1. Promptul.** Deschide [`PROMPT-MASTER.md`](PROMPT-MASTER.md), copiază textul
dintre linii și lipește-l în Claude, într-o conversație nouă. Atât. De aici poți
cere primul citat.

**2. Skill-ul**, dacă vrei ca Claude să știe brandul fără să-i mai explici de
fiecare dată. Descarcă depozitul (butonul verde **Code** → **Download ZIP**),
dezarhivează-l, și copiază folderul `skills/cioburi-de-suflet` în locul unde
Claude îți ține skill-urile. Dacă nu știi unde e, lipește-i lui Claude mesajul
ăsta: *„Vreau să instalez un skill. Am folderul cioburi-de-suflet în Downloads.
Unde îl pun?"*

**3. Poeziile.** Fișierul cu cele 232 de poezii **nu e în depozitul ăsta** și nu
trebuie pus pe internet — sunt cărțile tale. Îl ții pe calculatorul tău și i-l
dai lui Claude când lucrați. Structura e descrisă în skill.

---

## Ce e în fiecare folder

```
PROMPT-MASTER.md                   promptul de lipit în Claude
skills/cioburi-de-suflet/
  SKILL.md                         brandul întreg: culori, voce, formate, reguli
  references/
    palete.css                     toate culorile, gata de lipit în cod
    formate.md                     măsurile exacte ale fiecărui material
    captionuri.md                  modele de caption și ce nu se scrie niciodată
    semn.svg                       semnul celor șapte cioburi
  assets/
    fundal-vol1..7                 fundalurile colorate ale celor șapte volume
  scripts/
    fa_placa.py                    face plăcile de citat dintr-un fișier JSON
    citate-exemplu.json            trei citate gata scrise, ca model
exemple/                           cum arată rezultatul
```

---

## Cum faci o placă de citat singură

În folderul `scripts/`:

```bash
python3 fa_placa.py citate-exemplu.json
```

Ies trei plăci PNG în `placi/`. Ca să faci ale tale, copiază fișierul JSON,
schimbă versurile, titlul poeziei, volumul și ora.

```json
{"vers": ["Nu te ascunde în tăceri",
          "Atunci când totul tace!",
          "Căci nu ajungem nicăieri",
          "Când teama loc își face."],
 "titlu": "Fii sincer!", "vol": 1, "ora": "00:15",
 "fundal": "../assets/fundal-vol1-albastru.jpg"}
```

`fundal` poate fi `"fond"` (vișiniul brandului), `"culoare"` (culoarea volumului)
sau calea către o poză.

Prima dată, scriptul are nevoie de un lucru instalat:

```bash
npm install playwright && npx playwright install chromium
```

Dacă nu merge sau nu vrei să instalezi nimic, scriptul scrie oricum
`placi/placa.html` — îl deschizi în browser și faci captură de ecran.
Fonturile se încarcă de pe Google Fonts, deci calculatorul trebuie să aibă internet.

---

## Cele două reguli de care atârnă tot

**Nu se arată fața.** Nu e un compromis, e identitatea. Tot conținutul se face
din text, culoare și grafică.

**Ora apare pe tot.** Fiecare poezie poartă ora la care a fost terminată — 03:09,
00:15, 17:10. Nimeni altcineva din poezia românească de pe Instagram nu are asta.
Un material fără oră nu e gata.

---

## Drepturi

Poeziile și cele șapte volume **Cioburi de suflet** sunt ale Ellei von Dokonal,
toate drepturile rezervate. Depozitul ăsta conține doar unelte de lucru și
câteva strofe date ca exemplu, publicate cu acordul autoarei.

Fundalurile colorate sunt prelucrate după fotografii de pe Unsplash, folosite
în baza licenței Unsplash.

Cărțile: [meleti.ro/autor/ellavondokonal](https://meleti.ro/autor/ellavondokonal)
