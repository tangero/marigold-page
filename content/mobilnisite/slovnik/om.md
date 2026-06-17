---
slug: "om"
url: "/mobilnisite/slovnik/om/"
type: "slovnik"
title: "OM – Optimisation Mode supported"
date: 2025-01-01
abbr: "OM"
fullName: "Optimisation Mode supported"
category: "Management"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/om/"
summary: "Optimisation Mode supported (OM) je indikátor schopností uživatelského zařízení (UE) zavedený ve specifikaci 3GPP Release 5, definovaný v dokumentech TS 23.153 a TS 28.062. Signalizuje, zda uživatelsk"
---

OM je indikátor schopností uživatelského zařízení (UE), který signalizuje, zda uživatelské zařízení podporuje určité síťové optimalizační funkce pro mezisystémovou mobilitu a předávání hovoru.

## Popis

Optimisation Mode supported (OM) je parametr nebo příznak schopností ve specifikacích 3GPP, který udává, zda uživatelské zařízení (UE) podporuje specifické optimalizační procedury pro mobilitu a předávání hovoru mezi různými rádiovými přístupovými technologiemi (RAT). Je součástí rádiových přístupových schopností UE, které si vyměňuje se sítí. Primárním kontextem pro OM je mobilita mezi různými RAT, konkrétně mezi GSM/[EDGE](/mobilnisite/slovnik/edge/) Radio Access Network ([GERAN](/mobilnisite/slovnik/geran/)) a UMTS Terrestrial Radio Access Network (UTRAN), zejména pro procedury předávání hovoru a převýběru buňky.

Z architektonického hlediska je indikátor OM uložen v UE a hlášen síti. V obvodu přepínaných ([CS](/mobilnisite/slovnik/cs/)) doménách k tomu dochází během procedur aktualizace polohy, připojení s [IMSI](/mobilnisite/slovnik/imsi/) nebo aktualizace směrovací oblasti. Tuto schopnost přijímá Serving [GPRS](/mobilnisite/slovnik/gprs/) Support Node (SGSN) nebo Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)). Síť tuto informaci využívá k rozhodnutí, zda vyvolat optimalizované procedury předávání hovoru. Pokud je OM podporován, může síť použít specifické mechanismy, které mohou snížit dobu přerušení při předávání hovoru a zlepšit úspěšnost. Například může umožnit "Network Assisted Cell Change" ([NACC](/mobilnisite/slovnik/nacc/)) z GERAN do UTRAN nebo naopak, kdy síť poskytne UE systémové informace cílové buňky před předáním hovoru, čímž urychlí přístupový proces.

Funguje to procedurálně. UE zahrne indikátor OM do své zprávy s informacemi o schopnostech pro základnovou síť. Síťový prvek (SGSN/MSC) tuto informaci uloží. Později, když se připravuje předání hovoru na jinou RAT, síť zkontroluje, zda UE podporuje OM. Pokud je podpora přítomna a pokud cílové RAT a síť také podporují odpovídající optimalizační funkce, může síť zvolit optimalizovanou cestu pro předání hovoru. To může zahrnovat odlišné signalizační sekvence nebo předzásobení informacemi. Klíčovými komponentami jsou protokolový zásobník UE, který generuje informaci o schopnostech, rádiová přístupová síť a uzly základnové sítě, které ji ukládají a využívají. Jeho úlohou je usnadnit efektivnější mezisystémovou mobilitu, což je zásadní pro bezproblémový uživatelský zážitek v nasazeních s více RAT.

## K čemu slouží

Schopnost Optimisation Mode supported byla zavedena ve specifikaci 3GPP Release 5, aby řešila výzvy spojené s předáváním hovoru a správou mobility mezi sítěmi 2G ([GERAN](/mobilnisite/slovnik/geran/)) a 3G (UTRAN). Raná předání hovoru mezi různými RAT byla často "naslepo" nebo méně asistovaná, což znamenalo, že si UE muselo po příchodu do cílové buňky samo získat všechny potřebné systémové informace, což vedlo k delším dobám přerušení služby a vyššímu riziku selhání předání hovoru. To zhoršovalo uživatelský zážitek při přechodech mezi technologiemi.

Problémem byl nedostatek standardizovaného mechanismu, pomocí kterého by síť mohla zjistit, zda UE zvládne pokročilejší, síťově asistované procedury předání hovoru. Vytvoření indikátoru OM to vyřešilo poskytnutím jednoduchého signalizačního příznaku. Umožnil síti identifikovat UE schopná podporovat optimalizované procedury pro mezisystémové předání hovoru, jako jsou ty definované v TS 43.129 a TS 25.331. To síti umožnilo přizpůsobit svou strategii předávání hovoru: pro UE s podporou OM mohla použít rychlejší a spolehlivější metody, zatímco pro starší UE přešla na základní procedury. Motivací bylo zlepšit plynulost mobility v rozvíjejících se sítích, kde koexistovaly 2G a 3G, a zvýšit tak úspěšnost hovorů a výkon předávání hovoru při nasazování sítí UMTS vedle stávajících sítí GSM.

## Klíčové vlastnosti

- Indikátor schopností UE pro optimalizaci mezi různými RAT
- Signalizováno z UE do základnové sítě (SGSN/MSC)
- Umožňuje síti používat optimalizované procedury předávání hovoru
- Cílí na snížení doby přerušení při předávání hovoru
- Použitelné pro mobilitu mezi GERAN a UTRAN
- Uloženo v síti pro budoucí rozhodnutí o předání hovoru

## Související pojmy

- [GERAN – GSM EDGE Radio Access Network](/mobilnisite/slovnik/geran/)

## Definující specifikace

- **TS 23.153** (Rel-19) — Out-of-Band Transcoder Control Stage 2
- **TS 28.062** (Rel-19) — Tandem Free Operation (TFO) Service Description

---

📖 **Anglický originál a plná specifikace:** [OM na 3GPP Explorer](https://3gpp-explorer.com/glossary/om/)
