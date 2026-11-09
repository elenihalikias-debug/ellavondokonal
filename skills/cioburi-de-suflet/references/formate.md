# Formate · măsurile exacte

| Material | Mărime | Observații |
|---|---|---|
| Placă de citat | 1080 x 1350 | margine 104px |
| Carusel | 1080 x 1350 | 8-10 plăci, fiecare să țină singură |
| Card zilnic | 1080 x 1350 | o poezie, o oră |
| Reel | 1080 x 1920 | text între x 60-900 și y 250-1480 |
| Copertă de reel | 1080 x 1350 | separată de reel |

## Placa de citat, structura

```
┌──────────────────────────────────┐
│                                  │  margine 104px
│                                  │
│   Strofa întreagă                │  Literata cursiv, 47-62px
│   în Literata cursiv,            │  line-height 1.44
│   patru sau opt rânduri.         │
│                                  │
│   │ FRAGMENT DIN POEZIA          │  Archivo 21px, majuscule,
│   │ „Titlul"                     │  spațiere .26em, opacitate .6
│   │ Cioburi de suflet · vol. X   │  Fraunces 600 36px
│                                  │  Literata cursiv 25px
│                                  │
│  03:09                    ▁▃▂▅▂▄▁│  ora stânga, semnul dreapta
└──────────────────────────────────┘
```

Linia verticală din stânga creditului are 4px și culoarea de accent a plăcii.

## Mărimea versului, după câte rânduri are strofa

| Rânduri | Mărime |
|---|---|
| 4 rânduri scurte | 62px |
| 4 rânduri lungi | 55-58px |
| 8 rânduri scurte | 47-52px |

Dacă cel mai lung vers depășește lățimea, se coboară mărimea, nu se taie versul.

## Fundal deschis (volumele V și VII)

Peste fotografiile deschise, cerneala e închisă, iar vălul se inversează:
alb în loc de negru, altfel textul nu se citește.

```css
.placa.lumina .val{
  background:linear-gradient(180deg,
    rgba(255,255,255,.60), rgba(255,255,255,.50) 36%, rgba(255,255,255,.86));
}
```
