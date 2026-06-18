---
slug: "pp"
url: "/mobilnisite/slovnik/pp/"
type: "slovnik"
title: "PP – Antenna Port"
date: 2026-01-01
abbr: "PP"
fullName: "Antenna Port"
category: "Physical Layer"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/pp/"
summary: "PP (Antenna Port) je logický koncept ve specifikacích fyzické vrstvy 3GPP představující prostředek pro přenos signálu, definovaný specifickým referenčním signálem. Je klíčový pro operace MIMO a beamfo"
---

PP je logický koncept ve specifikacích 3GPP představující přenosový prostředek definovaný referenčním signálem, který abstrahuje mapování fyzických antén pro MIMO a beamforming.

## Popis

Ve specifikacích 3GPP, zejména pro LTE a NR, je Antenna Port (PP) základní logická entita používaná pro definici a popis downlinkových a uplinkových přenosů. Nejde o fyzickou anténu, ale o logický port asociovaný se specifickým vzorem referenčního signálu. Každý anténní port je definován svou jedinečnou sekvencí referenčního signálu a mapováním prostředků, což přijímači umožňuje nezávisle odhadnout kanál odpovídající tomuto portu. Tento koncept odděluje specifikaci přenosového schématu a zpracování signálu od skutečného počtu fyzických anténních elementů a poskytuje tak flexibilitu při implementaci.

Princip operace spočívá v tom, že všechna data a řídicí informace přenášená na stejném anténním portu procházejí stejným efektivním kanálem, což znamená, že z pohledu tohoto logického portu zažívají identické podmínky šíření. To je zajištěno, protože referenční signál pro daný port je vysílán se stejným precodingem jako data na tomto portu. Přijímač tyto referenční signály používá pro odhad kanálu, demodulaci a dekódování. Například v LTE se anténní porty 0-3 používají pro cell-specific reference signals ([CRS](/mobilnisite/slovnik/crs/)), zatímco porty 7-14 se používají pro UE-specific reference signals ([DM-RS](/mobilnisite/slovnik/dm-rs/)) podporující beamforming.

Mezi klíčové komponenty patří definice referenčních signálů (např. CRS, DM-RS, [CSI-RS](/mobilnisite/slovnik/csi-rs/)), vzory mapování na resource elementy specifikované ve specifikacích fyzické vrstvy a přidružený precoding. Počet anténních portů přímo ovlivňuje řád [MIMO](/mobilnisite/slovnik/mimo/); například přenos na dvou anténních portech umožňuje 2x2 MIMO. V NR je tento koncept rozšířen o flexibilnější návrhy referenčních signálů, jako jsou tracking reference signals ([TRS](/mobilnisite/slovnik/trs/)) a phase-tracking reference signals ([PT-RS](/mobilnisite/slovnik/pt-rs/)), z nichž každý je asociován se specifickými čísly anténních portů. Architektura podporuje různé přenosové módy, od přenosu s jednou anténou po multi-user MIMO a massive MIMO, definováním sad anténních portů pro různé účely.

Její role v síti je klíčová pro umožnění pokročilých anténních technologií. Použitím anténních portů může standard specifikovat komplexní víceanténní přenosová schémata, jako je prostorové multiplexování, transmit diversity a beamforming, jednotným způsobem bez ohledu na konfiguraci podkladového fyzického anténního pole. Tato abstrakce umožňuje výrobcům síťového vybavení a čipových sad inovovat v návrhu a implementaci antén, přičemž zajišťuje interoperabilitu prostřednictvím standardizovaného logického chování. Tvoří základ pro reportování informací o stavu kanálu ([CSI](/mobilnisite/slovnik/csi/)), výběr precoding matrix indicatoru a adaptaci ranku, což je nezbytné pro optimalizaci spektrální účinnosti a spolehlivosti spoje v moderních celulárních systémech.

## K čemu slouží

Koncept Antenna Port byl zaveden za účelem abstrakce a standardizace rozhraní pro víceanténní přenosové techniky v systémech 3GPP, primárně počínaje LTE. Před jeho formalizací byly víceanténní techniky často popisovány ve vztahu k fyzickým anténám, což omezovalo flexibilitu a vytvářelo implementační závislosti. Logický anténní port odděluje specifikaci přenosového schématu od fyzické realizace, což umožňuje vývoj sofistikovaných technologií [MIMO](/mobilnisite/slovnik/mimo/) a beamformingu bez omezování hardwarového návrhu.

Řeší problém, jak definovat referenční signály a datové kanály způsobem, který podporuje více souběžných přenosových schémat, jako je single-user MIMO, multi-user MIMO a coordinated multipoint (CoMP). Asociací každého logického datového proudu nebo paprsku se specifickým anténním portem a jeho jedinečným referenčním signálem může přijímač přesně odhadnout kanál pro tento proud, i když je více proudů prostorově multiplexováno. To bylo obzvláště důležité pro vývoj z 2G/3G, které měly omezené víceanténní schopnosti, směrem k 4G LTE a 5G NR, které silně spoléhají na MIMO pro zvýšení kapacity a pokrytí.

Motivace pramenila z potřeby efektivně škálovat víceanténní technologie. S rostoucím počtem anténních elementů u massive MIMO se přímé mapování každého fyzického elementu na standardizovaný přenosový prostředek stalo nepraktickým. Koncept anténního portu umožňuje mapování typu many-to-one, kde může být více fyzických anténních elementů kombinováno prostřednictvím analogového a digitálního beamformingu, aby vytvořily jeden logický port. To umožňuje podporu velkého počtu paprsků a uživatelů při zachování zvládnutelného počtu standardizovaných portů ve specifikaci, čímž se standardy připravují na budoucí pokročilé anténní systémy.

## Klíčové vlastnosti

- Logická abstrakce nezávislá na počtu fyzických antén
- Definován jedinečným vzorem referenčního signálu (např. CRS, DM-RS, CSI-RS)
- Umožňuje odhad kanálu pro demodulaci dat na bázi jednotlivých portů
- Podporuje prostorové vrstvy MIMO, přičemž každá vrstva je typicky asociována s portem
- Usnadňuje beamforming asociací portů se specifickými beamformingovanými referenčními signály
- Umožňuje flexibilní mapování mezi fyzickými anténními elementy a logickými přenosovými prostředky

## Související pojmy

- [CRS – Cell-specific Reference Signals](/mobilnisite/slovnik/crs/)
- [DM-RS – Demodulation Reference Signal](/mobilnisite/slovnik/dm-rs/)
- [CSI-RS – Channel State Information Reference Signal](/mobilnisite/slovnik/csi-rs/)
- [MIMO – Multiple Input Multiple Output](/mobilnisite/slovnik/mimo/)

## Definující specifikace

- **TS 23.048** (Rel-5) — Secured Packets for UICC Remote Management
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 23.875** (Rel-5) — Feasibility Study for Push Services Architecture
- **TS 31.115** (Rel-19) — Secured Packet Structure for UICC Applications
- **TS 33.805** (Rel-12) — 3GPP Network Product Security Assurance Methodology
- **TR 33.916** (Rel-19) — 3GPP Security Assurance Methodology (SECAM)
- **TS 36.211** (Rel-19) — LTE Physical Layer Specification

---

📖 **Anglický originál a plná specifikace:** [PP na 3GPP Explorer](https://3gpp-explorer.com/glossary/pp/)
