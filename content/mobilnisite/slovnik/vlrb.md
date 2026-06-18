---
slug: "vlrb"
url: "/mobilnisite/slovnik/vlrb/"
type: "slovnik"
title: "VLRB – Visitor Location Register for the B-subscriber"
date: 2025-01-01
abbr: "VLRB"
fullName: "Visitor Location Register for the B-subscriber"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/vlrb/"
summary: "Konkrétní VLR, který v daném okamžiku obsluhuje volaného účastníka (B-subscriber) v mobilní terminované komunikaci. Jde o funkční označení používané při směrování hovoru, službách ukončení a účtování"
---

VLRB je návštěvnický lokální registr (Visitor Location Register), který v daném okamžiku obsluhuje volaného účastníka v mobilním terminovaném hovoru; jedná se o funkční označení používané pro směrování, ukončení hovoru a účtování.

## Popis

VLRB je logický protějšek k [VLRA](/mobilnisite/slovnik/vlra/) a představuje funkční roli standardního [VLR](/mobilnisite/slovnik/vlr/) v případě, že jeho obsluhovaný mobilní účastník je příjemcem (B-subscriber) hovoru nebo relace. Toto rozlišení je klíčové v procesu ukončení hovoru. Když je hovor směrován k mobilnímu účastníkovi, Gateway [MSC](/mobilnisite/slovnik/msc/) ([GMSC](/mobilnisite/slovnik/gmsc/)) dotazuje [HLR](/mobilnisite/slovnik/hlr/) účastníka na směrovací informace. HLR následně odešle do VLR, kde je účastník aktuálně registrován, [MAP](/mobilnisite/slovnik/map/) požadavek Provide Roaming Number. Tento VLR, který nyní vystupuje jako VLRB, přidělí dočasné Mobile Station Roaming Number ([MSRN](/mobilnisite/slovnik/msrn/)) a odpoví HLR, což umožní GMSC směrovat hovor k obsluhujícímu MSC (které se stává MSC-B).

Povinnosti VLRB se soustředí na ukončení hovoru. Ověřuje, zda je B-subscriberovi umožněno přijímat hovory (např. není zablokován) a zda je dostupný (není odpojen). Spravuje proceduru pagingu ve své lokalizační oblasti, aby lokalizoval konkrétní mobilní zařízení. Pro volaného účastníka VLRB také zajišťuje aktivaci případných terminujících Camel služeb, jako je přizpůsobené přesměrování hovoru nebo screening příchozích hovorů, na základě spouštěcích bodů v profilu B-subscribera načteném z HLR. VLRB interaguje se svým spolulokalizovaným MSC k dokončení sestavení hovoru k terminujícímu zařízení.

Při účtování VLRB generuje záznamy o účtovacích údajích ([CDR](/mobilnisite/slovnik/cdr/)) pro terminující větev hovoru. Tyto záznamy jsou oddělené od těch, které vytváří VLRA, a jsou klíčové pro vypořádání mezi operátory, zejména v případech mezinárodního roamingu, kdy jsou sítě volajícího a volaného různé. Jasné oddělení rolí VLRA a VLRB zajišťuje, že servisní logika, účtování a požadavky na zákonné odposlechy jsou aplikovány přesně na každou ze stran komunikace, čímž poskytuje čisté architektonické oddělení řídicích funkcí pro oba konce spojení.

## K čemu slouží

Definice VLRB, společně s VLRA, byla vedena potřebou symetrického a jednoznačného zacházení s oběma stranami mobilního hovoru v rámci síťových protokolů a procedur. Jak se mobilní sítě vyvíjely, aby podporovaly komplexní roaming a pokročilé přidané služby, ukázalo se jako nedostatečné odkazovat se v signalizačních specifikacích jednoduše na 'VLR'. Síť potřebovala přesně vědět, zda se operace (jako získání roamovacího čísla, aplikace zákazu volání nebo spuštění Camel služby) týká strany volajícího nebo volaného.

Toto rozlišení řeší kritické problémy v mezisíťové komunikaci a poskytování služeb. Například při hovoru mezi účastníkem roamujícím v Síti X a účastníkem roamujícím v Síti Y musí domovské sítě obou účastníků komunikovat se správnou návštěvnickou sítí. Identifikátor VLRB umožňuje HLR B-subscribera správně adresovat svůj dotaz na MSRN. Také umožňuje správnou aplikaci terminujících služeb (např. 'přesměrování při obsazení'), které jsou řízeny servisním profilem B-subscribera a prováděny ve VLRB/MSC-B, nezávisle na procedurách výchozí sítě.

Dále je VLRB nezbytný pro přesné účtování a právní shodu. Operátoři terminující sítě účtují za použití svých rádiových a jádrových síťových zdrojů k doručení hovoru roamujícímu účastníkovi. Záznamy o účtování z VLRB tvoří základ těchto poplatků. Podobně příkazy k zákonnému odposlechu pro cílového účastníka musí být provedeny VLR, který jej aktuálně obsluhuje, což je pro příchozí komunikace právě VLRB. Koncept VLRB tedy zajišťuje jasnost, spravedlnost a shodu v multioperátorských mobilních ekosystémech.

## Klíčové vlastnosti

- Logická role přiřazená fyzickému VLR, když jeho obsluhovaný účastník je volanou stranou (B-subscriber)
- Přiděluje Mobile Station Roaming Numbers (MSRN) pro směrování příchozích hovorů na žádost HLR
- Spravuje terminující procedury řízení hovoru, včetně pagingu a kontrol dostupnosti účastníka
- Spouští Camel servisní logiku pro B-stranu (např. přesměrování hovoru, screening)
- Generuje záznamy o účtovacích údajích (CDR) pro terminující větev hovoru
- Kritický uzel pro realizaci doručení mobilního terminovaného hovoru v roamingu

## Související pojmy

- [VLR – Visitor Location Register](/mobilnisite/slovnik/vlr/)
- [VLRA – Visitor Location Register for the A-subscriber](/mobilnisite/slovnik/vlra/)
- [MSC – Mobile Services Switching Centre](/mobilnisite/slovnik/msc/)
- [MSRN – Mobile Subscriber Roaming Number](/mobilnisite/slovnik/msrn/)
- [CAMEL – Customised Applications for Mobile network Enhanced Logic](/mobilnisite/slovnik/camel/)
- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)

## Definující specifikace

- **TS 23.018** (Rel-19) — Basic call handling in 3GPP CS domain
- **TS 23.079** (Rel-19) — Support of Optimal Routeing (SOR) Phase 1

---

📖 **Anglický originál a plná specifikace:** [VLRB na 3GPP Explorer](https://3gpp-explorer.com/glossary/vlrb/)
