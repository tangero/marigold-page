---
slug: "sl"
url: "/mobilnisite/slovnik/sl/"
type: "slovnik"
title: "SL – Sidelink Positioning Reference Signal"
date: 2025-01-01
abbr: "SL"
fullName: "Sidelink Positioning Reference Signal"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/sl/"
summary: "Referenční signál definovaný pro kanály přímé komunikace mezi zařízeními (sidelink), konkrétně používaný pro účely polohování. Umožňuje uživatelským zařízením (UE) odhadnout relativní polohu, vzdáleno"
---

SL je referenční signál pro kanály přímé komunikace mezi zařízeními (sidelink), který umožňuje uživatelským zařízením (UE) odhadnout relativní polohu, vzdálenost nebo úhel příchodu od jiných blízkých zařízení.

## Popis

Sidelink Positioning Reference Signal ([SL-PRS](/mobilnisite/slovnik/sl-prs/)) je specifická sekvence symbolů vysílaná na fyzickém sdíleném kanálu přímé komunikace ([PSSCH](/mobilnisite/slovnik/pssch/)) nebo řídicím kanálu přímé komunikace ([PSCCH](/mobilnisite/slovnik/pscch/)) za účelem usnadnění polohovacích měření mezi zařízeními. Na rozdíl od downlink nebo uplink [PRS](/mobilnisite/slovnik/prs/), které zahrnují koordinaci základnovou stanicí (gNB), je SL-PRS navržen pro scénáře přímé komunikace mezi zařízeními ([D2D](/mobilnisite/slovnik/d2d/)) jako součást rozhraní přímé komunikace (sidelink, SL) podle 3GPP, což je klíčové pro služby Vehicle-to-Everything ([V2X](/mobilnisite/slovnik/v2x/)), veřejnou bezpečnost a komerční služby založené na blízkosti. Jeho struktura na fyzické vrstvě zahrnuje specifické mapování na zdrojové prvky v rámci bloků zdrojů přímé komunikace podle vzorů konfigurovaných vyššími vrstvami, aby se zabránilo kolizi s jinými signály a daty přímé komunikace.

Signál je generován pomocí pseudonáhodných sekvencí, často Goldových sekvencí, které jsou odvozeny od parametrů, jako je identita vysílajícího UE, index slotu a typ cyklické předpony. Tento návrh zajišťuje dobré vlastnosti autokorelace a vzájemné korelace, což umožňuje přijímajícímu UE detekovat signál přesně i v šumovém prostředí a rozlišovat mezi SL-PRS z různých vysílajících UE. Konfigurace SL-PRS – včetně jeho periodicity v časové doméně, hřebenové struktury ve frekvenční doméně, šířky pásma a vzorů utlumení – je signalizována prostřednictvím řídicí informace přímé komunikace ([SCI](/mobilnisite/slovnik/sci/)) nebo předkonfigurována v UE, což umožňuje flexibilní přizpůsobení různým požadavkům služeb (např. polohování s vysokou přesností pro autonomní řízení versus nižší přesnost pro určování blízkosti chodců).

Během provozu UE vysílá SL-PRS na svých přidělených zdrojích přímé komunikace. Sousední UE tyto signály přijímají a provádějí měření, jako je čas příchodu ([TOA](/mobilnisite/slovnik/toa/)), časový rozdíl referenčního signálu (RSTD) nebo úhel příchodu (AoA). Tato nezpracovaná měření mohou být použita přímo pro relativní polohování mezi UE nebo nahlášena polohovacímu serveru (např. Location Management Function - LMF) v síti pro výpočet absolutní polohy pomocí technik jako je multilaterace. Integrace SL-PRS s jinými polohovacími signály (např. GNSS, downlink PRS) umožňuje hybridní polohování, což zvyšuje přesnost a dostupnost, zejména v prostředích bez GNSS, jako jsou městské kaňony nebo tunely. Díky tomu je SL-PRS základním kamenem pro pokročilé aplikace V2X vyžadující přesnou relativní lokalizaci, jako je formování kolon, zabránění kolizím a kooperativní vnímání okolí.

## K čemu slouží

SL-PRS byl zaveden, aby řešil rostoucí potřebu přesného a spolehlivého polohování mezi zařízeními, která je primárně hnána vývojem služeb V2X a novými komerčními aplikacemi D2D v 5G a dalších generacích. Tradiční metody buněčného polohování (např. Observed Time Difference of Arrival - OTDOA využívající downlink PRS) spoléhají na infrastrukturu základnových stanic, která může být nedostupná, nedostatečně hustá nebo geometricky nevhodná pro relativní polohování mezi pohybujícími se vozidly nebo zařízeními v těsné blízkosti. Toto omezení se stává kritickým pro bezpečnostní aplikace V2X, jako je autonomní řízení, kde je znalost přesné relativní polohy blízkých vozidel zásadní.

SL-PRS to řeší tím, že umožňuje přímé měření vzdálenosti a polohování mezi UE bez nutnosti neustálého zapojení síťové infrastruktury. Umožňuje vozidlům nebo zařízením nezávisle určovat jejich relativní polohy, čímž podporuje decentralizovaný a robustní provoz. Jeho vytvoření bylo motivováno prací 3GPP na rozšířeném V2X (eV2X) v Release 16 a pozdějších, které definovaly požadavky na přesnost na úrovni pod metr a vysokou spolehlivost. Poskytnutím standardizovaného referenčního signálu pro polohování specifického pro přímou komunikaci umožnilo 3GPP interoperabilní, vysoce výkonné polohování D2D, které doplňuje metody založené na síti a satelitech, a stává se tak klíčovým prvkem pro bezpečnostní a automatizační případy užití plánované pro 5G Advanced a 6G.

## Klíčové vlastnosti

- Specificky navržen pro vysílání na kanálech přímé komunikace (PSSCH/PSCCH)
- Konfigurovatelné časové/frekvenční vzory včetně hřebenové struktury a utlumení
- Podporuje měření jako čas příchodu (TOA) a úhel příchodu (AoA) mezi UE
- Umožňuje jak relativní polohování D2D, tak hybridní polohování se sítí/GNSS
- Používá pseudonáhodné sekvence pro robustní detekci a nízké rušení
- Konfigurovatelný prostřednictvím řídicí informace přímé komunikace (SCI) pro dynamické přizpůsobení

## Související pojmy

- [V2X – Vehicle-to-Everything Application Server](/mobilnisite/slovnik/v2x/)

## Definující specifikace

- **TR 22.804** (Rel-16) — 5G Automation in Vertical Domains Study
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TR 28.845** (Rel-18) — Technical Report on Charging for Ranging and Sidelink Positioning
- **TS 29.078** (Rel-19) — CAMEL Phase 4 CAP Specification
- **TS 33.533** (Rel-19) — Security for 5G Ranging & Sidelink Positioning
- **TR 33.893** (Rel-18) — Security and Privacy Aspects of Ranging and Sidelink Positioning
- **TS 38.212** (Rel-19) — NR Multiplexing and Channel Coding
- **TS 38.213** (Rel-19) — NR Physical Layer Control Procedures
- **TS 38.214** (Rel-19) — NR Physical Layer Procedures for Data

---

📖 **Anglický originál a plná specifikace:** [SL na 3GPP Explorer](https://3gpp-explorer.com/glossary/sl/)
