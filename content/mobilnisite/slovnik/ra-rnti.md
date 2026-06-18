---
slug: "ra-rnti"
url: "/mobilnisite/slovnik/ra-rnti/"
type: "slovnik"
title: "RA-RNTI – Random Access Radio Network Temporary Identifier"
date: 2025-01-01
abbr: "RA-RNTI"
fullName: "Random Access Radio Network Temporary Identifier"
category: "Identifier"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ra-rnti/"
summary: "RA-RNTI je dočasný identifikátor používaný v proceduře náhodného přístupu (Random Access) v LTE a NR. Vypočítává jej UE na základě časově-frekvenčního zdroje přenosu své přístupové preambule. Síť použ"
---

RA-RNTI je dočasný identifikátor vypočítaný uživatelským zařízením (UE) z časově-frekvenčního zdroje jeho přístupového preambule, který síť používá k adresování tohoto UE v počáteční odpovědní zprávě.

## Popis

Random Access Radio Network Temporary Identifier (RA-RNTI) je klíčový dočasný identifikátor používaný během procedury kanálu náhodného přístupu ([RACH](/mobilnisite/slovnik/rach/)) v systémech 3GPP LTE a NR. Jeho primární funkcí je adresovat konkrétní uživatelské zařízení (UE) nebo skupinu UE v počáteční downlinkové zprávě (Random Access Response, [RAR](/mobilnisite/slovnik/rar/)) ze sítě předtím, než je navázán nebo potvrzen jedinečný, pro UE specifický identifikátor jako [C-RNTI](/mobilnisite/slovnik/c-rnti/). RA-RNTI není síťovou signalizací přiřazen; místo toho je algoritmicky určen jak UE, tak základnovou stanicí (eNodeB/gNB) na základě fyzických rádiových zdrojů použitých pro přenos preambule.

Jeho fungování je nedílnou součástí procesu náhodného přístupu s možností kolizí (contention-based). Když potřebuje UE zahájit komunikaci (např. při počátečním přístupu, předávání spojení nebo synchronizaci uplinku), vybere a vyšle přístupovou preambuli na konkrétním výskytu (occasion) fyzického kanálu náhodného přístupu ([PRACH](/mobilnisite/slovnik/prach/)). PRACH výskyt je definován konkrétním časovým (systémový rámec a podrámec/slot) a frekvenčním zdrojem. UE následně vypočítá RA-RNTI pomocí standardizovaného vzorce: RA-RNTI = 1 + s_id + 14 * t_id + 14 * 80 * f_id + 14 * 80 * 8 * ul_carrier_id (pro LTE, s obměnami pro NR). Zde s_id, t_id a f_id jsou indexy pro podrámec, časový a frekvenční zdroj preambule. UE poté monitoruje downlinkový řídicí kanál ([PDCCH](/mobilnisite/slovnik/pdcch/)) zakódovaný (scrambled) tímto vypočteným RA-RNTI kvůli zprávě RAR.

Síť (gNB/eNodeB) po detekci preambule na daném konkrétním PRACH výskytu vypočítá stejný RA-RNTI. Následně přenese zprávu RAR na downlinkovém sdíleném kanálu ([PDSCH](/mobilnisite/slovnik/pdsch/)) a signalizuje její přítomnost odesláním downlinkové řídicí informace ([DCI](/mobilnisite/slovnik/dci/)) formátu na PDCCH zakódované tímto RA-RNTI. To umožní všem UE, které vyslaly preambuli na tomto zdroji, tuto zprávu detekovat, ale RAR obsahuje dočasný identifikátor (Temporary C-RNTI) a příkaz časového předstihu (timing advance) určený pro úspěšné UE. RA-RNTI tedy slouží jako na zdroj specifická adresa pro počáteční krok řešení kolizí, propojující neidentifikovaný uplinkový přenos s cílenou downlinkovou odpovědí.

## K čemu slouží

RA-RNTI byl zaveden s LTE v 3GPP Release 8, aby vyřešil klíčový problém v proceduře náhodného přístupu s možností kolizí: jak může síť odeslat odpověď UE, jejíž identita ještě není známa? V předchozích systémech byly mechanismy počátečního přístupu méně efektivní. RA-RNTI poskytuje elegantní adresovací schéma založené na zdrojích, které se vyhýbá potřebě explicitní signalizace identity v první uplinkové zprávě (preambuli, která neobsahuje ID UE).

Toto řešení je motivováno potřebou efektivity a škálovatelnosti. Preambule je krátký, jednoduchý signál pro minimalizaci interference a složitosti detekce. Vložení plného identifikátoru UE by ji prodloužilo a zkomplikovalo. Místo toho RA-RNTI využívá jedinečnost časově-frekvenčního zdroje použitého pro preambuli jako dočasnou, implicitní adresu. To umožňuje, aby byla odpověď sítě efektivně vysílána všem UE, která mohla tento zdroj použít (adresování potenciálních kolizí), a zároveň je dostatečně cílená, aby nezahlcovala všechna UE všemi odpověďmi.

Řeší omezení plynoucí z neexistence navázaného signalizačního spojení. Před procedurou [RACH](/mobilnisite/slovnik/rach/) nemusí mít UE C-RNTI (v případě počátečního přístupu) nebo může mít zastaralé (v případě selhání rádiového spoje). RA-RNTI poskytuje nezbytný prostředek pro první downlinkovou řídicí zprávu, což umožňuje navázání nebo obnovení vlastního RRC spojení a přiřazení trvalého nebo semi-perzistentního identifikátoru, což je zásadní pro mobilitu v síti a správu zdrojů.

## Klíčové vlastnosti

- Dočasný identifikátor odvozený z časově-frekvenčních zdrojů PRACH (systémový rámec, podrámec/slot, frekvenční index)
- Používá se ke kódování (scrambling) DCI na PDCCH pro adresování zprávy Random Access Response (RAR)
- Umožňuje náhodný přístup s možností kolizí tím, že poskytuje na zdroj specifickou adresu před přiřazením UE-specifického C-RNTI
- Výpočetní vzorec standardizován v technických specifikacích 36.321 (LTE) a 38.321 (NR)
- Nezbytný pro počáteční synchronizaci uplinku a úpravu časového předstihu (timing advance)
- Podporuje jak LTE, tak NR přístupové technologie na základě podobných principů

## Související pojmy

- [PRACH – Physical Random Access Channel](/mobilnisite/slovnik/prach/)
- [C-RNTI – Cell Radio Network Temporary Identifier](/mobilnisite/slovnik/c-rnti/)
- [PDCCH – Physical Downlink Control Channel](/mobilnisite/slovnik/pdcch/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.321** (Rel-19) — E-UTRA MAC Protocol Specification
- **TS 36.401** (Rel-19) — E-UTRAN Overall Architecture Description
- **TS 38.300** (Rel-19) — NG-RAN Overall Description

---

📖 **Anglický originál a plná specifikace:** [RA-RNTI na 3GPP Explorer](https://3gpp-explorer.com/glossary/ra-rnti/)
