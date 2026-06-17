---
slug: "gif"
url: "/mobilnisite/slovnik/gif/"
type: "slovnik"
title: "GIF – Graphics Interchange Format"
date: 2025-01-01
abbr: "GIF"
fullName: "Graphics Interchange Format"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/gif/"
summary: "Standardizovaný formát obrázku pro multimediální služby v sítích 3GPP, který umožňuje efektivní přenos a zobrazení grafiky a jednoduchých animací. Je definován pro zajištění interoperability vizuálníh"
---

GIF je standardizovaný formát obrázku pro multimediální služby v sítích 3GPP, který umožňuje efektivní přenos a zobrazení grafiky a jednoduchých animací za účelem zajištění interoperability.

## Popis

Formát Graphics Interchange Format (GIF) v kontextu 3GPP je standardizovaný rastrový formát obrázku specifikovaný pro použití v multimediálních službách. Je definován v několika technických specifikacích (TS), včetně 26.140 (Multimedia Messaging Service ([MMS](/mobilnisite/slovnik/mms/)); Media formats and codecs) a 26.141 (Presence service; Data formats and codecs). Formát podporuje až 8 bitů na pixel, což umožňuje paletu až 256 různých barev z 24bitového barevného prostoru RGB. Klíčovou technickou vlastností je podpora bezztrátové komprese pomocí algoritmu Lempel–Ziv–Welch (LZW), který je efektivní pro grafiku s velkými plochami jednotné barvy. Dále formát umožňuje zakódovat více obrázků do jednoho souboru, které lze zobrazit v sekvenci a vytvořit tak jednoduché animace. To je řízeno prostřednictvím vyhrazeného bloku Graphics Control Extension, který definuje parametry, jako je doba zpoždění a metoda zrušení pro každý snímek.

V architektuře 3GPP je GIF definovaným typem mediálního objektu v rámci služby Multimedia Messaging Service (MMS) a dalších služeb na aplikační úrovni. Když zařízení odešle nebo přijme MMS obsahující obrázek GIF, MMS User Agent a MMS Relay/Server zpracují mediální objekt podle pravidel adaptace obsahu specifikovaných v TS 26.140. Síť může překódovat GIF do jiného formátu, pokud jej přijímací zařízení nepodporuje podle svých schopností popsaných v MMS User Agent Profile (MMS UAProf). Zařazení tohoto formátu zajišťuje, že základní grafický obsah, jako jsou loga, ikony a jednoduché animace, může být konzistentně vykreslován na široké škále 3GPP kompatibilních telefonů a síťových prvků.

Role GIF v síti je primárně na aplikační vrstvě, kde poskytuje dobře definovaný kontejner pro vizuální informace. Jeho technické specifikace pokrývají přesnou syntaxi formátu souboru, včetně hlavičky, deskriptoru logické obrazovky, globální tabulky barev, deskriptoru obrázku, lokální tabulky barev, obrazových dat a různých rozšiřujících bloků. Pro animace je přesně definováno zpracování průhlednosti a sekvencování snímků, aby bylo zajištěno předvídatelné přehrávání. Ačkoli se po jeho přijetí jedná převážně o statickou specifikaci, jeho integrace do standardů 3GPP zaručila základní úroveň interoperability pro grafický obsah v raných mobilních datových službách a tvořila část základu pro bohatší multimediální zážitky, které se později vyvinuly.

## K čemu slouží

GIF byl začleněn do standardů 3GPP, aby vyřešil problém nekompatibilních formátů obrázků napříč různými mobilními zařízeními a sítěmi v počátcích mobilních multimédií. Před standardizací mohli výrobci používat proprietární formáty, což vedlo k narušeným uživatelským zážitkům, kdy jeden telefon nemohl zobrazit obrázky odeslané z jiného. Vytvoření [MMS](/mobilnisite/slovnik/mms/) a dalších datových služeb vyžadovalo spolehlivý, lehký formát pro grafiku, který by mohl být univerzálně podporován. Formát GIF, již široce používaný na internetu, byl pragmatickou volbou díky své jednoduchosti, podpoře animací a efektivní kompresi pro typy obrázků běžné v raných mobilních službách (např. emotikony, jednoduché obrázky).

Jeho specifikace v rámci 3GPP Rel-8 poskytla konkrétní typ média, který mohly síťové prvky, jako jsou MMS centra, rozpoznat, zpracovat a případně adaptovat. Tím se odstranilo omezení předchozích ad-hoc přístupů, kde interoperabilita multimédií nebyla zaručena. Definováním GIF jako povinného nebo volitelně podporovaného formátu v konformačních specifikacích zařízení byla zajištěna základní schopnost odesílat a přijímat grafický obsah, což bylo klíčové pro komerční úspěch služeb, jako je zasílání obrázků. Role formátu spočívala v tom, že byl pracovním koněm pro základní vizuální komunikaci a umožňoval nové servisní paradigmy dříve, než byly širší měně zavedeny pokročilejší formáty, jako [JPEG](/mobilnisite/slovnik/jpeg/) a PNG, a vyšší přenosové rychlosti umožnily bohatší média.

## Klíčové vlastnosti

- Bezztrátová komprese pomocí algoritmu LZW
- Podpora až 256 barev na snímek z 24bitové palety RGB
- Schopnost více-snímkových sekvencí pro vytváření jednoduchých animací
- Podpora průhledných barv pozadí
- Definovaná struktura souboru s hlavičkami, barevnými tabulkami a bloky obrazových dat
- Specifikován jako mediální formát pro služby 3GPP MMS a Presence

## Související pojmy

- [MMS – Multimedia Messaging Service](/mobilnisite/slovnik/mms/)

## Definující specifikace

- **TS 26.140** (Rel-19) — MMS Media Formats and Codecs Specification
- **TS 26.141** (Rel-19) — IMS Messaging & Presence Media Formats
- **TS 26.233** (Rel-15) — 3GPP Packet-Switched Streaming Service (PSS)
- **TS 26.234** (Rel-19) — 3GPP PSS Protocols and Codecs Specification
- **TR 26.956** (Rel-19) — Beyond 2D Video Formats & Codecs Study

---

📖 **Anglický originál a plná specifikace:** [GIF na 3GPP Explorer](https://3gpp-explorer.com/glossary/gif/)
