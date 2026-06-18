---
slug: "toawe"
url: "/mobilnisite/slovnik/toawe/"
type: "slovnik"
title: "TOAWE – Time Of Arrival Window Endpoint"
date: 2025-01-01
abbr: "TOAWE"
fullName: "Time Of Arrival Window Endpoint"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/toawe/"
summary: "Time Of Arrival Window Endpoint (TOAWE) definuje koncovou hranici časového okna, ve kterém má síť přijmout specifický uplinkový rádiový signál od uživatelského zařízení (UE). Je to kritický parametr p"
---

TOAWE je koncová hranice časového okna, ve kterém má síť přijmout specifický uplinkový signál od uživatelského zařízení pro UTDOA lokalizaci.

## Popis

Time Of Arrival Window Endpoint (TOAWE) je parametr časování na straně sítě používaný primárně v lokalizačních systémech Uplink Time Difference of Arrival ([UTDOA](/mobilnisite/slovnik/utdoa/)). V UTDOA se poloha uživatelského zařízení (UE) určuje měřením času příchodu ([TOA](/mobilnisite/slovnik/toa/)) jeho uplinkových přenosů na více geograficky rozptýlených jednotkách pro měření polohy ([LMU](/mobilnisite/slovnik/lmu/)). Aby síť mohla tyto často slabé signály efektivně a přesně detekovat, musí každé LMU sdělit, kde v čase má hledat signál UE. TOAWE spolu se svým protějškem [TOAWS](/mobilnisite/slovnik/toaws/) (Time Of Arrival Window Startpoint) definuje toto přesné vyhledávací okno.

Operačně lokalizační uzel sítě (jako [E-SMLC](/mobilnisite/slovnik/e-smlc/) nebo [LMF](/mobilnisite/slovnik/lmf/)) vypočítá očekávaný TOA signálu cílového UE na konkrétní LMU na základě známé přibližné polohy UE (např. z cell-ID) a známé polohy LMU. Poté definuje okno kolem tohoto očekávaného TOA, aby zohlednilo odhady chyb a zpoždění šíření. TOAWE určuje nejzazší možný čas (koncový bod) v rámci tohoto okna. Přijímač LMU následně koreluje příchozí rádiový signál se známým vzorkem uplinkového přenosu UE (např. pomocí Sounding Reference Signal - [SRS](/mobilnisite/slovnik/srs/)) pouze v časovém intervalu ohraničeném TOAWS a TOAWE. To drasticky snižuje zátěž zpracování signálu a zlepšuje pravděpodobnost detekce tím, že omezí vyhledávání na relevantní časový úsek.

Hodnota TOAWE je typicky sdělována z lokalizačního uzlu na LMU pomocí řídicí signalizace, jako je LTE Positioning Protocol Annex (LPPa) nebo NR Positioning Protocol Annex (NPPa). Šířka okna (TOAWE - TOAWS) je konfigurovatelný parametr, který vyvažuje výkon: příliš úzké okno riskuje ztrátu signálu, pokud je počáteční odhad polohy nepřesný, zatímco příliš široké okno prodlužuje dobu zpracování a zvyšuje potenciál falešných detekcí od šumu nebo jiných signálů. Přesné nastavení TOAWE je proto klíčové pro latenci, přesnost a spolehlivost lokalizace UTDOA.

## K čemu slouží

TOAWE byl vytvořen, aby vyřešil kritický praktický problém při implementaci [UTDOA](/mobilnisite/slovnik/utdoa/) lokalizace: hledání 'jehly v kupce sena', tedy specifického uplinkového signálu konkrétního UE v nepřetržitém proudu rádiového šumu a interference od mnoha uživatelů. Bez předdefinovaného vyhledávacího okna by musela LMU nepřetržitě skenovat a korelovat signály ve velmi velkém časovém rozsahu, což je výpočetně náročné, energeticky intenzivní a prodlužuje dobu do získání polohy. Poskytnutím ohraničeného koncového bodu pro vyhledávání umožňuje TOAWE efektivní zpracování signálu.

Tento parametr řeší omezení čistě 'naslepo' prováděné detekce signálu. V raných konceptech uplinkové lokalizace absence časového návodu pro LMU vedla k vysokým nákladům na zařízení a velké latenci, což činilo službu nepraktickou pro aplikace v reálném čase, jako je nouzové volání. Zavedení TOAWE a TOAWS jako součásti standardizovaného rámce UTDOA ve 3GPP Release 4 poskytlo řízený, sítí spravovaný mechanismus pro nasměrování měřicích zdrojů, což učinilo tuto technologii použitelnou pro komerční a regulatorní nasazení.

Jeho účel je neoddělitelně spojen se síťovou lokalizací, která nespoléhá na schopnosti UE. Zatímco downlinkové metody jako OTDOA vyžadují, aby měření provádělo UE, UTDOA (používající TOAWE) umožňuje síti lokalizovat i starší nebo jednoduchá zařízení měřením jejich uplinkových přenosů. To zajišťuje komplexní pokrytí pro nouzové služby a sledování aktiv napříč všemi typy zařízení.

## Klíčové vlastnosti

- Definuje koncovou hranici časového vyhledávacího okna pro detekci uplinkového signálu
- Používá se výhradně pro lokalizaci Uplink TDOA (UTDOA)
- Konfigurován a signalizován síťovým lokalizačním uzlem (E-SMLC/LMF) směrem k LMU
- Snižuje zátěž zpracování signálu a latenci lokalizace na LMU
- Spolupracuje s TOAWS k definování přesného korelačního intervalu
- Velikost okna je adaptabilní na základě nejistoty počátečního odhadu polohy UE

## Související pojmy

- [TOAWS – Time Of Arrival Window Startpoint](/mobilnisite/slovnik/toaws/)
- [UTDOA – Uplink Time Difference of Arrival](/mobilnisite/slovnik/utdoa/)
- [LMU – Location Measurement Unit](/mobilnisite/slovnik/lmu/)
- [SRS – Space Radiocommunication Stations](/mobilnisite/slovnik/srs/)

## Definující specifikace

- **TS 25.402** (Rel-19) — UTRAN Synchronisation Mechanisms

---

📖 **Anglický originál a plná specifikace:** [TOAWE na 3GPP Explorer](https://3gpp-explorer.com/glossary/toawe/)
