---
slug: "gob"
url: "/mobilnisite/slovnik/gob/"
type: "slovnik"
title: "GOB – Group Of Blocks"
date: 2025-01-01
abbr: "GOB"
fullName: "Group Of Blocks"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/gob/"
summary: "GOB je strukturní jednotka ve video kódování, konkrétně v ITU-T H.263 a příbuzných kodecích, představující skupinu makrobloků v rámci video snímku. V 3GPP je relevantní pro specifikaci interoperabilit"
---

GOB je strukturní jednotka z video kodeku H.263, představující skupinu makrobloků v rámci snímku, a je odkazována v 3GPP pro specifikaci požadavků na video kodek v konverzačních službách.

## Popis

Group Of Blocks (GOB) je základní datová struktura ve standardech video komprese, nejvýznamněji definovaná ve video kodeku [ITU-T](/mobilnisite/slovnik/itu-t/) H.263, který byl široce přijat pro video komunikaci s nízkým datovým tokem, včetně raných 3GPP multimediálních služeb. Video snímek je rozdělen na makrobloky, což jsou typicky oblasti 16x16 pixelů obsahující informaci o jasu a barvě. GOB sdružuje sadu po sobě jdoucích makrobloků z jediného řádku (nebo více řádků v některých konfiguracích) snímku do jedné logické jednotky pro účely kódování, přenosu a odolnosti proti chybám.

V procesu kódování video kodek zpracovává makrobloky sekvenčně, aplikuje techniky jako odhad pohybu, transformaci (např. [DCT](/mobilnisite/slovnik/dct/)), kvantizaci a entropické kódování. Struktura GOB poskytuje bod resynchronizace uvnitř bitového toku. Každý GOB má hlavičku obsahující startovní kód a informace jako číslo GOB a kvantizační parametry. Tato hlavička umožňuje dekodéru znovu získat synchronizaci, pokud bitové chyby nebo ztráta paketu poškodí datový proud, čímž se zabrání ztrátě celého snímku. Dekodér může přeskočit na další hlavičku GOB a pokračovat v dekódování, byť s potenciálními vizuálními artefakty v ztracené oblasti.

V rámci specifikací 3GPP je na GOB odkazováno primárně v kontextu definování povinných schopností kodeků pro multimediální služby. Specifikace jako 26.110 (kodek pro okruhově spínanou multimediální telefonii) a 26.114 (IP Multimedia Subsystem (IMS) multimediální telefonie) vyžadují podporu konkrétních profilů video kodeků, včetně H.263, který inherentně používá strukturu GOB. Práce 3GPP zajišťuje interoperabilitu mezi UEs a sítěmi specifikací, jak mají být tyto video kodeky, s jejich rámcovým dělením založeným na GOB, používány přes transportní protokoly definované 3GPP (např. RTP/UDP/IP) a zpracovávány ve scénářích jako předávání spojení nebo adaptace šířky pásma. Jeho role tedy není role aktivního protokolu vynalezeného 3GPP, ale definované komponenty přijatých standardů video kódování, které celý systém musí podporovat.

## K čemu slouží

Účelem konceptu GOB, jak je na něj odkazováno v 3GPP, je zajistit spolehlivé a interoperabilní služby video komunikace přes mobilní sítě. Video kodeky jako H.263 byly vybrány v raných vydáních 3GPP (např. Release 99, 4) pro multimediální telefonii, protože nabízely přiměřenou kvalitu při nízkých datových tocích dostupných na sítích 2.5G a 3G. Struktura GOB uvnitř těchto kodeků řeší klíčový problém pro náchylné kanály bezdrátového přenosu: odolnost proti přenosovým chybám.

Před rozšířeným používáním pokročilejšího maskování chyb a flexibilního uspořádání makrobloků (FMO) nalezených v pozdějších kodecích jako H.264, byla primární metodou odolnosti proti chybám v H.263 struktura GOB a její resynchronizační hlavičky. V okruhově spínaných nebo raných paketově spínaných video hovorech byly bitové chyby a ztráta paketů běžné. Bez resynchronizačních bodů jako jsou hlavičky GOB by jediná chyba mohla způsobit, že dekodér ztratí přehled o syntaxi bitového toku, což by vedlo ke katastrofálnímu selhání a potenciálně k zamrznutí videa až do dalšího nezávisle zakódovaného snímku (I-snímek). Hlavičky GOB umožňují dekodéru lokalizovat chyby, zahodit jednu skupinu bloků a pokračovat v dekódování, což poskytuje postupnou degradaci kvality videa.

Zařazení specifikací vyžadujících H.263 s podporou GOB v 3GPP bylo motivováno potřebou standardizované, základní video schopnosti pro službu 3GPP Multimedia Telephony. Řešilo to omezení spočívající v absenci společného video formátu, což by bránilo interoperabilitě mezi zařízeními od různých výrobců a napříč různými síťovými operátory. Jak se vyvíjela technologie video kodeků, specifikace 3GPP se vyvíjely tak, aby vyžadovaly pokročilejší kodeky (jako MPEG-4 Visual, H.264/[AVC](/mobilnisite/slovnik/avc/)), ale základní požadavky na přenos videa odolný proti chybám, pro které byl GOB raným řešením, zůstaly klíčovým zájmem.

## Klíčové vlastnosti

- Definuje resynchronizační vrstvu uvnitř video snímku pro odolnost proti chybám
- Seskupuje po sobě jdoucí sadu makrobloků (např. jeden řádek) pod jedinou hlavičkou
- Hlavička GOB obsahuje unikátní startovní kód a prostorovou polohu (číslo GOB)
- Umožňuje lokalizované maskování chyb; dekodér může po ztrátě paketu přeskočit na další GOB
- Specifikováno jako součást povinné podpory profilu H.263 v 3GPP multimediální telefonii
- Poskytuje strukturní jednotku pro parsování a zpracování bitového toku v legacy video kodecích

## Související pojmy

- [MMTEL – Multimedia Telephony Service for IMS](/mobilnisite/slovnik/mmtel/)

## Definující specifikace

- **TS 26.110** (Rel-19) — 3G-324M Multimedia Codecs for Circuit Switched Networks
- **TS 26.114** (Rel-19) — IMS Multimedia Telephony Media Handling
- **TR 26.937** (Rel-19) — 3GPP PSS Characterization

---

📖 **Anglický originál a plná specifikace:** [GOB na 3GPP Explorer](https://3gpp-explorer.com/glossary/gob/)
