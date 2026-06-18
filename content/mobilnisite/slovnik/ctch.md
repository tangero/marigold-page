---
slug: "ctch"
url: "/mobilnisite/slovnik/ctch/"
type: "slovnik"
title: "CTCH – Common Traffic Channel"
date: 2025-01-01
abbr: "CTCH"
fullName: "Common Traffic Channel"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ctch/"
summary: "CTCH je downlinkový transportní kanál v UMTS používaný pro přenos typu point-to-multipoint pro zprávy služby Cell Broadcast. Přenáší informace služby Cell Broadcast Service (CBS) všem UE v buňce, což"
---

CTCH je downlinkový transportní kanál v UMTS používaný pro přenos vysílání typu point-to-multipoint, který slouží k distribuci zpráv služby Cell Broadcast všem UE v buňce.

## Popis

Common Traffic Channel (CTCH) je jednosměrný downlinkový transportní kanál definovaný v architektuře UMTS Radio Access Network ([UTRAN](/mobilnisite/slovnik/utran/)), určený speciálně pro vysílací služby. Funguje jako logický kanál na vrstvě Medium Access Control ([MAC](/mobilnisite/slovnik/mac/)) a je navržen pro přenos informací uživatelské roviny ze sítě k více uživatelským zařízením (UE) současně, a to způsobem point-to-multipoint. Primárním obsahem přenášeným na CTCH jsou zprávy služby Cell Broadcast Service ([CBS](/mobilnisite/slovnik/cbs/)), které zahrnují geograficky cílené veřejné informace, jako jsou nouzová varování, dopravní aktualizace nebo reklama. Na rozdíl od vyhrazených kanálů CTCH nevyžaduje individuální adresování UE ani navázání spojení, což jej činí vysoce efektivním pro distribuci informací celé populaci uživatelů v buňce.

Z architektonického hlediska je CTCH mapován na transportní kanál Forward Access Channel ([FACH](/mobilnisite/slovnik/fach/)) ve fyzické vrstvě. Podle specifikací 3GPP je CTCH asociován s konkrétní, jednoznačně identifikovanou podmnožinou sady transportních bloků přenášených na FACH. Toto mapování je řízeno vrstvou Radio Resource Control ([RRC](/mobilnisite/slovnik/rrc/)) prostřednictvím systémových informačních bloků (SIBs), které informují UE o konfiguraci a plánování CTCH v rámci buňky. Samotný FACH je přenášen na fyzickém kanálu Secondary Common Control Physical Channel ([S-CCPCH](/mobilnisite/slovnik/s-ccpch/)), který definuje fyzické zdroje (kódy, časování). Tato hierarchická struktura – od logického kanálu (CTCH) k transportnímu kanálu (FACH) a k fyzickému kanálu (S-CCPCH) – zajišťuje, že jsou vysílací data integrována do rámcové struktury UMTS a rádiového rozhraní.

Z procedurálního pohledu CTCH funguje následovně: Jádrová síť prostřednictvím Cell Broadcast Centre ([CBC](/mobilnisite/slovnik/cbc/)) odešle zprávy CBS k Radio Network Controller ([RNC](/mobilnisite/slovnik/rnc/)). RRC vrstva RNC tyto zprávy naplánuje a instruuje MAC vrstvu, aby je doručila přes logický kanál CTCH. MAC vrstva následně zformátuje data do transportních bloků, které jsou multiplexovány na transportní kanál FACH. Tyto bloky jsou součástí předdefinované 'sady bloků' výhradně rezervované pro provoz CTCH. UE kontinuálně monitorují nakonfigurovaný FACH právě pro tuto specifickou sadu bloků, jak je uvedeno v systémových informacích. Po přijetí transportního bloku z určené sady jej MAC vrstva UE identifikuje jako data CTCH a předá zprávu CBS vyšším vrstvám ke zpracování a zobrazení.

Role CTCH je klíčová pro neinteraktivní, síťou iniciované vysílací služby. Poskytuje standardizovaný mechanismus s nízkou režií pro komunikaci typu one-to-many v rámci buňky UTRAN. Mezi klíčové technické aspekty patří jeho statická nebo polo-statická konfigurace (vysílací parametry se dynamicky nemění pro každou zprávu), podpora segmentace a opětovného složení delších CBS zpráv na vrstvě RLC (typicky pomocí transparentního nebo nepotvrzovaného režimu) a jeho nezávislost na individuálním stavu UE – může oslovit UE ve stavech idle, CELL_FACH, CELL_PCH nebo URA_PCH. Díky tomu je CTCH základním prvkem systémů veřejného varování a předchůdcem později vyvinutých multimediálních vysílacích služeb, jako je MBMS.

## K čemu slouží

CTCH byl vytvořen za účelem standardizace a optimalizace doručování zpráv služby Cell Broadcast v rámci sítě 3G UMTS, čímž řešil potřebu efektivních, rozsáhlých systémů pro veřejné informace a varování. Před standardizací 3GPP byly možnosti vysílacích zpráv omezené a často proprietární. Zavedení CTCH ve verzi Release 99 poskytlo jednotný transportní mechanismus pro službu Cell Broadcast Service (CBS), což umožnilo operátorům odesílat geograficky cílené textové zprávy všem koncovým zařízením v určené oblasti bez nutnosti navazovat individuální spojení, a tím významně šetřit signalizační a rádiové zdroje.

Tato technologie vyřešila problém neefektivního hromadného oznamování. Použití vyhrazených nebo společných řídicích kanálů pro vysílání by buď spotřebovalo nadměrné zdroje, nebo by postrádalo potřebnou kapacitu a spolehlivost. CTCH, díky svému jedinečnému mapování na podmnožinu sady transportních bloků FACH, garantuje rezervovanou část downlinkové kapacity pro vysílací provoz. To zajišťuje předvídatelné doručení a zabraňuje blokování vysílacích zpráv jiným provozem. Dále řešil regulatorní požadavky vznikající na počátku roku 2000 na systémy veřejného varování a poskytl technický základ pro systémy varování před zemětřesením, tsunami nebo únosy dětí integrované do mobilních sítí.

Historicky bylo vytvoření CTCH motivováno zkušenostmi ze sítě 2G GSM, která měla základní funkci Cell Broadcast, ale s méně definovanou strukturou kanálů. 3GPP si kladlo za cíl vytvořit robustnější a škálovatelnější vysílací kanál v nové architektuře UTRAN založené na WCDMA. Definováním CTCH jako typu logického kanálu umožnilo jasné oddělení vysílacího provozu od ostatních datových toků (vyhrazený provoz, signalizace, paging) a umožnilo budoucí vylepšení v pozdějších verzích, jako jsou ta pro Multimedia Broadcast Multicast Service (MBMS), která stavěla na konceptech point-to-multipoint zavedených právě CTCH a CBS.

## Klíčové vlastnosti

- Logický kanál typu point-to-multipoint pro downlink, určený pro vysílací provoz
- Jednoznačně mapován na určenou podmnožinu sady transportních bloků FACH
- Přenáší zprávy služby Cell Broadcast Service (CBS) pro veřejná varování a informace
- Přístupný pro UE ve stavech idle a připojených (CELL_FACH, PCH)
- Konfigurován a inzerován prostřednictvím RRC systémových informačních bloků (SIBs)
- Využívá transparentní nebo nepotvrzovaný režim RLC pro efektivní přenos dat

## Související pojmy

- [FACH – Forward Access Channel](/mobilnisite/slovnik/fach/)
- [CBS – Cell Broadcast Service](/mobilnisite/slovnik/cbs/)
- [S-CCPCH – Secondary Common Control Physical Channel](/mobilnisite/slovnik/s-ccpch/)
- [UTRAN – Universal Terrestrial Radio Access Network](/mobilnisite/slovnik/utran/)
- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.301** (Rel-19) — UE-UTRAN Radio Interface Protocol Architecture
- **TS 25.322** (Rel-19) — RLC Protocol Specification
- **TS 25.324** (Rel-19) — Broadcast/Multicast Control Protocol
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [CTCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/ctch/)
