#!/usr/bin/env python3
"""Generuje technické infografiky/schémata pro vybrané pojmy slovníku 3GPP
jako SVG (přes OpenRouter/qwen).

Proč SVG: text je nativní, takže čeština vč. diakritiky je bezchybná — obrazové
modely (gpt-image-1) text renderují jako pixely a diakritiku komolí. SVG je
navíc ostré v každém rozlišení, malé a editovatelné.

Dvoukrokový postup:
  1) destilace českého popisu pojmu → strukturovaná osnova diagramu
  2) osnova → profesionální SVG diagram (jednotný house-style: paleta
     #2563EB/#EA580C/#16A34A, layout zleva doprava, legenda)

Zdroj obsahu: markdown pojmu v content/mobilnisite/slovnik/<slug>.md
(úvodní definice + sekce Popis / K čemu slouží).
Výstup: static/assets/slovnik/<slug>.svg + doplnění pole `infografika:`
do front matteru daného pojmu.
Pojmy: ručně udržovaný allowlist scripts/infographic-terms.txt.

Použití (mimo sandbox kvůli síti; vyžaduje OPENROUTER_API_KEY v .env):
    .venv-img/bin/python scripts/generate_infographics.py --dry-run
    .venv-img/bin/python scripts/generate_infographics.py --only amf
    .venv-img/bin/python scripts/generate_infographics.py            # celý allowlist
    .venv-img/bin/python scripts/generate_infographics.py --force    # přegeneruj i existující
"""
from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path

# Kořen repa = rodič adresáře scripts/
ROOT = Path(__file__).resolve().parent.parent
SLOVNIK_DIR = ROOT / "content" / "mobilnisite" / "slovnik"
OUT_DIR = ROOT / "static" / "assets" / "slovnik"
ALLOWLIST = ROOT / "scripts" / "infographic-terms.txt"
ASSET_URL_PREFIX = "/assets/slovnik"

# Diagramy generujeme jako SVG přes LLM (OpenRouter) — text je nativní, takže
# čeština vč. diakritiky je bezchybná (na rozdíl od obrazových modelů, které
# text renderují jako pixely a diakritiku komolí). Ostré, malé, editovatelné.
OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"
# Claude Sonnet drží prostorová omezení a SVG layout výrazně líp než qwen
# (bez přetékání textu, bohatší a přesnější diagramy). Lze přepsat --model.
DIAGRAM_MODEL = "anthropic/claude-sonnet-4-6"

# Krok 1 — destilace českého popisu pojmu do strukturované osnovy diagramu.
DISTILL_SYSTEM = (
    "Jsi technický ilustrátor telekomunikačních schémat. Z českého popisu pojmu "
    "vytvoříš STRUČNOU strukturovanou osnovu pro infografiku — žádnou prózu. "
    "Vrať POUZE: (1) číslovaný seznam 5–10 komponent/kroků zleva doprava "
    "(vstup → zpracování → výstup), každý 1–4 slova; (2) řádek 'Toky:' s 2–4 "
    "vztahy mezi komponentami (např. 'AMF → SMF: správa relace'); (3) řádek "
    "'Parametry:' s klíčovými hodnotami, pokud existují (rychlosti, rozhraní). "
    "Vše česky, krátce, bez vysvětlujících vět. Žádný markdown, žádné nadpisy. "
    "Buď fakticky přesný — neuváděj smyšlená čísla rozhraní ani parametry."
)

# Krok 2 — vykreslení osnovy jako profesionální SVG diagram (jednotný styl).
SVG_SYSTEM = """Jsi expert na tvorbu technických SVG diagramů pro telekomunikační dokumentaci.
Z dodané osnovy vytvoříš jeden čistý, profesionální infografický diagram jako VALIDNÍ SVG kód.

PLÁTNO A ZÓNY (viewBox 0 0 1536 1024, bílé pozadí):
- Titulek: pás y=0–110, text-anchor="middle" na x=768.
- Diagram (bloky + šipky): pás y=130–700. Jen sem patří komponenty a toky.
- Číslovaný postup (pokud je v osnově): vyhrazený pás y=720–900, NIKDY ne přes diagram.
- Legenda barev: pás y=940–1010 dole.
- Levý/pravý okraj 80px. Nic nesmí přesáhnout viewBox.

STYL (jednotný napříč všemi pojmy):
- Flat vektor, BEZ gradientů/stínů/3D. Boxy rx="8", stroke-width="2".
- Paleta — pouze tři akcentní barvy:
  - modrá #2563EB = funkční bloky/komponenty (výplň, bílý text uvnitř)
  - oranžová #EA580C = šipky a datové/signálové toky (čáry i jejich popisky)
  - zelená #16A34A = výstupy/parametry
- Font: font-family="Inter, Arial, sans-serif". DŮLEŽITÉ — písmo musí být velké, protože
  diagram se na webu zobrazuje zmenšený: text v blocích MIN. 30px, popisky šipek MIN. 26px,
  titulek ~46px, podtitulek ~26px, legenda ~24px. NIKDY písmo menší než 24px.
- Drž méně textu, ať se velké písmo vejde: krátké popisky (1–4 slova), zkratky místo dlouhých názvů.
- Šipky jako <line>/<path> s marker-end (definuj <marker> s oranžovou hlavičkou).

PRAVIDLA PROTI PŘEKRÝVÁNÍ (klíčové — diagram musí být čitelný):
- Bloky rozmísti ŠTĚDŘE: vodorovně min. 180px volného místa mezi sloupci bloků
  (popisek šipky se musí vejít DO mezery, ne na blok), svisle min. 80px mezi řadami.
- Popisek šipky NESMÍ překrývat žádný blok ani jinou čáru. Umísti ho do prázdné
  mezery mezi bloky, vycentrovaný na čáru, s odstupem min. 40px od kraje obou bloků.
- Pokud je popisek delší a do mezery se nevejde, ZKRAŤ ho (použij jen číslo rozhraní,
  např. "N12") nebo rozděl na 2 řádky (<tspan>) — nikdy ho netlač přes blok.
- U svislých/šikmých šipek dej popisek vedle čáry do volného prostoru, ne přes cílový blok.
- Bloky dost velké, aby se text vešel dovnitř bez přetečení (šířka ≥ 160px).
- Číslovaný postup vykresli jako prostý levý sloupec textu ve vyhrazeném pásu (y=720–900),
  ne vedle diagramu; nesmí zasahovat do legendy (y=940+).
- NEVYTVÁŘEJ prázdné boxy — každý box musí mít text. Pokud osnova nemá parametry, zelený panel vynech.
- Než vrátíš SVG, mentálně zkontroluj: leží nějaký <text> popisku přes obdélník bloku? Pokud ano, posuň ho do volné mezery.

OBSAH: VŠECHNY popisky česky včetně diakritiky, přesně podle osnovy. Buď fakticky věrný osnově.

Vrať POUZE čistý <svg>...</svg> kód. Žádný markdown, žádné ```, žádný komentář mimo SVG."""

# Fallback osnova, když LLM destilace selže — holý text z markdownu.
CONTENT_FALLBACK = "Pojem: {abbr} ({full_name})\n{summary}"


def read_term(slug: str) -> tuple[str, str, str] | None:
    """Vrátí (abbr, fullName, summary_text) z markdownu pojmu, nebo None."""
    path = SLOVNIK_DIR / f"{slug}.md"
    if not path.exists():
        return None
    text = path.read_text(encoding="utf-8")
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None
    front, body = parts[1], parts[2]

    def fm(key: str) -> str:
        m = re.search(rf'^{key}:\s*"?(.*?)"?\s*$', front, re.M)
        return m.group(1) if m else ""

    abbr = fm("abbr") or slug.upper()
    full_name = fm("fullName")

    # Odstraň markdown odkazy [text](url) → text, a sekce, které nejsou popisné.
    def strip_links(s: str) -> str:
        return re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", s)

    # Úvodní definice = text mezi front matterem a prvním "## ".
    intro_m = re.search(r"^\s*(.+?)\n##\s", body, re.S)
    intro = strip_links(intro_m.group(1).strip()) if intro_m else ""

    # Sekce Popis a K čemu slouží (bez Definujících specifikací / Souvisejících pojmů).
    def section(title: str) -> str:
        m = re.search(rf"^##\s+{re.escape(title)}\s*\n(.+?)(?=\n##\s|\Z)", body, re.S | re.M)
        return strip_links(m.group(1).strip()) if m else ""

    popis = section("Popis")
    ucel = section("K čemu slouží")
    summary = "\n\n".join(p for p in (intro, popis, ucel) if p)
    # Omez délku promptu (gpt-image bere řádově tisíce znaků; držíme stručné).
    summary = summary[:2500]
    return abbr, full_name, summary


def distill_content(client, model: str, abbr: str, full_name: str, summary: str) -> str:
    """Krok 1: přes LLM destiluje český popis do strukturované osnovy diagramu.
    Při chybě vrátí fallback z holého textu."""
    try:
        resp = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": DISTILL_SYSTEM},
                {"role": "user", "content": f"Pojem: {abbr} ({full_name})\n\nPopis:\n{summary}"},
            ],
            temperature=0.2,
        )
        out = (resp.choices[0].message.content or "").strip()
        return out if out else CONTENT_FALLBACK.format(abbr=abbr, full_name=full_name, summary=summary)
    except Exception as e:  # noqa: BLE001
        print(f"    [pozn.] LLM destilace selhala ({e}), použiji holý popis", file=sys.stderr)
        return CONTENT_FALLBACK.format(abbr=abbr, full_name=full_name, summary=summary)


def render_svg(client, model: str, abbr: str, full_name: str, content: str) -> str:
    """Krok 2: osnova → SVG diagram. Vrátí očištěný <svg>…</svg> řetězec."""
    resp = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": SVG_SYSTEM},
            {"role": "user", "content": (
                f"Vytvoř diagram pro pojem {abbr} ({full_name}) podle této osnovy:\n\n{content}"
            )},
        ],
        temperature=0.3,
    )
    out = (resp.choices[0].message.content or "").strip()
    m = re.search(r"<svg.*?</svg>", out, re.S)
    svg = m.group(0) if m else out
    # Sanitizace: odstraň XML komentáře (model do nich občas dá '--', což je
    # nevalidní XML a rozbije render). V produkčním SVG nejsou potřeba.
    svg = re.sub(r"<!--.*?-->", "", svg, flags=re.S)
    return svg.strip()


def set_front_matter_image(slug: str) -> bool:
    """Doplní `infografika:` do front matteru pojmu, pokud tam ještě není.
    Vrátí True, pokud soubor změnil."""
    path = SLOVNIK_DIR / f"{slug}.md"
    text = path.read_text(encoding="utf-8")
    if re.search(r"^infografika:", text, re.M):
        return False
    url = f"{ASSET_URL_PREFIX}/{slug}.svg"
    # Vlož za řádek canonical: (nebo za fullName: jako fallback).
    for anchor in ("canonical", "fullName", "abbr"):
        m = re.search(rf"^({anchor}:.*)$", text, re.M)
        if m:
            text = text[: m.end()] + f'\ninfografika: "{url}"' + text[m.end():]
            path.write_text(text, encoding="utf-8")
            return True
    return False


def load_slugs(args) -> list[str]:
    if args.only:
        return [args.only]
    if not ALLOWLIST.exists():
        print(f"Chybí allowlist {ALLOWLIST}", file=sys.stderr)
        sys.exit(1)
    slugs = []
    for line in ALLOWLIST.read_text(encoding="utf-8").splitlines():
        line = line.split("#", 1)[0].strip()
        if line:
            slugs.append(line)
    if args.limit:
        slugs = slugs[: args.limit]
    return slugs


def main() -> None:
    ap = argparse.ArgumentParser(description="Generování SVG infografik pojmů slovníku (OpenRouter/qwen)")
    ap.add_argument("--dry-run", action="store_true", help="jen vypiš destilovanou osnovu, negeneruj SVG")
    ap.add_argument("--force", action="store_true", help="přegeneruj i existující SVG")
    ap.add_argument("--only", metavar="SLUG", help="jen jeden pojem")
    ap.add_argument("--limit", type=int, help="omez počet pojmů z allowlistu")
    ap.add_argument("--out", default=str(OUT_DIR), help="cílový adresář SVG")
    ap.add_argument("--model", default=DIAGRAM_MODEL, help="OpenRouter model pro destilaci i SVG")
    args = ap.parse_args()

    out_dir = Path(args.out)
    slugs = load_slugs(args)
    print(f"Pojmů ke zpracování: {len(slugs)}{' | DRY RUN' if args.dry_run else ''}\n")

    try:
        from dotenv import load_dotenv
        load_dotenv(ROOT / ".env")
    except ImportError:
        pass

    if not os.environ.get("OPENROUTER_API_KEY"):
        print("CHYBÍ OPENROUTER_API_KEY (vlož do .env). Bez něj nelze generovat.", file=sys.stderr)
        sys.exit(1)
    from openai import OpenAI
    client = OpenAI(base_url=OPENROUTER_BASE_URL, api_key=os.environ["OPENROUTER_API_KEY"])
    if not args.dry_run:
        out_dir.mkdir(parents=True, exist_ok=True)

    generated = skipped = errors = 0
    for slug in slugs:
        term = read_term(slug)
        if term is None:
            print(f"  [CHYBÍ] {slug}: markdown pojmu nenalezen")
            errors += 1
            continue
        abbr, full_name, summary = term
        if not summary:
            print(f"  [PŘESKOK] {slug}: prázdný popis")
            skipped += 1
            continue

        svg_path = out_dir / f"{slug}.svg"
        if svg_path.exists() and not args.force and not args.dry_run:
            print(f"  [PŘESKOK] {slug}: SVG už existuje (--force pro přepis)")
            skipped += 1
            continue

        content = distill_content(client, args.model, abbr, full_name, summary)

        if args.dry_run:
            print(f"  === {slug} ({abbr} – {full_name}) ===")
            print("  [destilovaná osnova pro diagram]:")
            print("    " + content.replace("\n", "\n    "))
            print()
            generated += 1
            continue

        try:
            print(f"  [GENERUJI] {slug} ({abbr})…", flush=True)
            svg = render_svg(client, args.model, abbr, full_name, content)
            if not svg.lstrip().startswith("<svg"):
                raise ValueError("odpověď neobsahuje validní <svg>")
            svg_path.write_text(svg, encoding="utf-8")
            changed = set_front_matter_image(slug)
            print(f"    → {svg_path.name} ({len(svg)} B){' + front matter' if changed else ''}")
            generated += 1
        except Exception as e:  # noqa: BLE001
            print(f"  [CHYBA] {slug}: {e}", file=sys.stderr)
            errors += 1

    print(f"\n{'Připraveno' if args.dry_run else 'Vygenerováno'}: {generated} | Přeskočeno: {skipped} | Chyb: {errors}")


if __name__ == "__main__":
    main()
