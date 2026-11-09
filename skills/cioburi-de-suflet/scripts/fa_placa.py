#!/usr/bin/env python3
"""
Face o placă de citat 1080x1350 în brandul Cioburi de suflet.

    python3 fa_placa.py citate.json

citate.json e o listă:
[
  {"vers": ["Vreau doar atât cât vrei și tu,",
            "Nu vreau nimic în plus,",
            "Vreau să spui da sau să spui nu,",
            "Dar totuși, un răspuns."],
   "titlu": "Fii sincer!", "vol": 1, "ora": "00:15",
   "fundal": "fond"}
]

fundal: "fond" (vișiniul brandului), "culoare" (culoarea volumului),
        sau calea către o poză (de ex. ../assets/fundal-vol1-albastru.jpg)

Rezultatul: placi/placa-01.png ... și placi/placa.html, dacă vrei să te uiți.
Dacă playwright nu e instalat, scrie doar HTML-ul și îți spune ce să rulezi.
"""
import json, pathlib, sys, subprocess

ROM = {1:'I', 2:'II', 3:'III', 4:'IV', 5:'V', 6:'VI', 7:'VII'}
VOL = {1:'#024878', 2:'#762849', 3:'#4B1764', 4:'#E83694',
       5:'#C8ECF8', 6:'#2A762B', 7:'#FEDA01'}
INK = {1:'#EAF3FA', 2:'#FBEFF4', 3:'#F2EAF7', 4:'#FFF4F9',
       5:'#0B2430', 6:'#EBF7EC', 7:'#3B1024'}
AC  = {1:'#FEDA01', 2:'#C8ECF8', 3:'#FEDA01', 4:'#3B1024',
       5:'#C03A3A', 6:'#FEDA01', 7:'#B13A14'}
DESCHIS = {5, 7}          # volumele cu fundal deschis
SEMN = [16, 26, 20, 34, 18, 28, 14]

FONTURI = ("https://fonts.googleapis.com/css2?"
           "family=Archivo:wght@400;600"
           "&family=Fraunces:opsz,wght@9..144,600"
           "&family=Literata:ital,wght@0,400;1,400&display=block")


def marime(randuri):
    """Mărimea versului, din numărul de rânduri și din cel mai lung dintre ele."""
    n = len(randuri)
    lat = max(len(r) for r in randuri)
    din_latime = int(872 / (lat * 0.47))
    din_inaltime = int(820 / (n * 1.44))
    return max(40, min(66, din_latime, din_inaltime))


def placa(c, i, baza=None):
    vol = int(c['vol'])
    randuri = c['vers'] if isinstance(c['vers'], list) else c['vers'].split('\n')
    fs = c.get('marime') or marime(randuri)
    f = c.get('fundal', 'fond')

    if f == 'fond':
        fond, ink, cls, val = 'background:#3B1024', '#FBEFF4', '', ''
    elif f == 'culoare':
        fond, ink, cls, val = f'background:{VOL[vol]}', INK[vol], '', ''
    else:
        cale = pathlib.Path(f)
        if not cale.is_absolute():
            cale = ((baza or pathlib.Path.cwd()) / cale).resolve()
        if not cale.exists():
            sys.exit(f'Nu găsesc fundalul: {cale}')
        fond = f'background-image:url(file://{cale})'
        ink = INK[vol]
        cls = ' foto' + (' lumina' if vol in DESCHIS else '')
        val = '<div class="val"></div>'

    ac = c.get('accent') or AC[vol]
    lung = ' lung' if len(c['titlu']) > 18 else ''
    semn = ''.join(f'<i style="height:{h}px;background:{ink}"></i>' for h in SEMN)

    return f'''
<div class="placa{cls}" data-nume="placa-{i:02d}" style="{fond};color:{ink}">
  {val}
  <p class="vers" style="font-size:{fs}px">{'<br>'.join(randuri)}</p>
  <p class="sursa{lung}" style="border-color:{ac}">
    <span class="et">fragment din poezia</span>„{c['titlu']}”<em>Cioburi de suflet · volumul {ROM[vol]}</em>
  </p>
  <span class="ora" style="color:{ac}">{c['ora']}</span>
  <span class="semn">{semn}</span>
</div>'''


CSS = '''
*{box-sizing:border-box;margin:0} body{background:#3B1024}
.placa{position:relative;width:1080px;height:1350px;overflow:hidden;margin:0 0 16px;
  padding:104px;display:flex;flex-direction:column;justify-content:center;
  background-size:cover;background-position:center;font-family:"Archivo",sans-serif}
.val{position:absolute;inset:0;background:linear-gradient(180deg,
  rgba(40,6,18,.34),rgba(40,6,18,.04) 44%,rgba(40,6,18,.52))}
.placa.lumina .val{background:linear-gradient(180deg,
  rgba(255,255,255,.60),rgba(255,255,255,.50) 36%,rgba(255,255,255,.86))}
.vers{position:relative;font-family:"Literata",Georgia,serif;font-style:italic;
  line-height:1.44;margin:0;max-width:100%;letter-spacing:-.005em}
.sursa{position:relative;font-family:"Fraunces",Georgia,serif;font-weight:600;
  font-size:36px;line-height:1.16;letter-spacing:-.01em;margin:64px 0 0;
  padding-left:28px;border-left:4px solid;max-width:84%}
.sursa.lung{font-size:30px}
.sursa .et{display:block;font-family:"Archivo",sans-serif;font-weight:600;font-size:21px;
  letter-spacing:.26em;text-transform:uppercase;opacity:.6;margin:0 0 14px}
.sursa em{display:block;font-family:"Literata",Georgia,serif;font-style:italic;
  font-weight:400;font-size:25px;letter-spacing:0;opacity:.72;margin:11px 0 0}
.ora{position:absolute;left:104px;bottom:104px;font-size:26px;letter-spacing:.32em;
  font-variant-numeric:tabular-nums;font-weight:600}
.semn{position:absolute;right:104px;bottom:104px;display:flex;gap:5px;
  align-items:flex-end;opacity:.5}
.semn i{display:block;width:10px;border-radius:2px}
'''

RENDER = '''const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1200, height: 1400 } });
  await p.goto('file://' + process.argv[2]);
  await p.waitForTimeout(3000);
  for (const el of await p.$$('.placa'))
    await el.screenshot({ path: process.argv[3] + '/' +
      (await el.getAttribute('data-nume')) + '.png' });
  await b.close();
})();'''


def main():
    sursa = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else 'citate.json')
    citate = json.loads(sursa.read_text(encoding='utf-8'))
    out = pathlib.Path('placi'); out.mkdir(exist_ok=True)

    html = (f'<meta charset="utf-8"><title>Plăci</title>'
            f'<link rel="stylesheet" href="{FONTURI}">'
            f'<style>{CSS}</style>'
            + ''.join(placa(c, i + 1, sursa.resolve().parent) for i, c in enumerate(citate)))
    f_html = (out / 'placa.html').resolve()
    f_html.write_text(html, encoding='utf-8')

    (out / '_render.js').write_text(RENDER, encoding='utf-8')
    try:
        subprocess.run(['node', str(out / '_render.js'), str(f_html), str(out.resolve())],
                       check=True)
        print(f'Gata. {len(citate)} plăci în {out.resolve()}')
    except Exception:
        print(f'HTML-ul e scris: {f_html}')
        print('Ca să iasă PNG-urile, instalează o dată:  npm i playwright && npx playwright install chromium')
        print('Sau deschide fișierul în browser și fă captură de ecran.')


if __name__ == '__main__':
    main()
