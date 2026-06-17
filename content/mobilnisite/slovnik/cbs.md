---
slug: "cbs"
url: "/mobilnisite/slovnik/cbs/"
type: "slovnik"
title: "CBS – Cell Broadcast Service"
date: 2026-01-01
abbr: "CBS"
fullName: "Cell Broadcast Service"
category: "Services"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/cbs/"
summary: "Služba typu point-to-multipoint, která vysílá krátké zprávy všem mobilním zařízením v určité geografické oblasti (buňce). Používá se pro systémy veřejného varování, lokalizační výstrahy a nouzová ozná"
---

CBS je služba typu point-to-multipoint, která vysílá krátké zprávy všem mobilním zařízením v určité geografické oblasti pro účely veřejných varování a nouzových oznámení, aniž by způsobila zahlcení sítě.

## Popis

Cell Broadcast Service (CBS) je standardizovaná služba zasílání zpráv v sítích 3GPP, která umožňuje současné doručení krátkých, nepotvrzovaných zpráv všem uživatelským zařízením (UE) v definované geografické oblasti, známé jako oblast pro vysílání zpráv (Cell Broadcast Area, [CBA](/mobilnisite/slovnik/cba/)). Na rozdíl od SMS typu point-to-point funguje CBS na principu jednosměrného vysílání, kdy síť zprávy odešle jednou a přijmou je všechna kompatibilní zařízení v cílové oblasti bez nutnosti individuální adresace nebo vytváření vyhrazených spojení. Díky tomu je služba vnitřně efektivní pro scénáře hromadného oznamování. Službu spravuje Cell Broadcast Centre ([CBC](/mobilnisite/slovnik/cbc/)), entita v jádru sítě odpovědná za vytváření zpráv, jejich plánování a cílení oblasti.

Architektonická implementace CBS zahrnuje několik klíčových síťových prvků. CBC komunikuje s jádrem sítě, konkrétně s Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)) v LTE nebo s funkcí Access and Mobility Management Function ([AMF](/mobilnisite/slovnik/amf/)) v 5GC, přes rozhraní SBc. Uzel jádra sítě pak přepošle zprávy CBS příslušným uzlům rádiového přístupového sítě (RAN) – jako je eNodeB v LTE nebo gNB v 5G NR – obsluhujícím cílovou geografickou oblast. RAN tyto zprávy vysílá přes rozhraní vzduch pomocí specifických logických kanálů a bloků systémových informací. V LTE jsou například zprávy vysílány na kanálech SC-MCCH (Single Cell Multicast Control Channel) a SC-MTCH (Single Cell Multicast Traffic Channel) pro doručení pomocí SC-PTM (Single Cell Point-to-Multipoint), nebo prostřednictvím bloku systémových informací typu 20 (SIB20).

Z pohledu UE je příjem CBS typicky proces na pozadí. Zařízení monitorují určené vysílací kanály pro zprávy označené specifickými identifikátory zpráv (Message Identifiers) a sériovými čísly (Serial Numbers). Každá zpráva je spojena s geografickým rozsahem (např. buňka, PLMN nebo oblast sledování) a identifikátorem zprávy CBS (Message ID), který kategorizuje typ zprávy (např. 4370 pro systém varování před zemětřesením a tsunami, ETWS). Uživatelé mohou obvykle příjem pro různé kategorie zpráv ve svém zařízení povolit nebo zakázat. Klíčovým technickým rysem je použití 16bitového sériového čísla, které umožňuje UE identifikovat a ignorovat duplicitní vysílání stejné zprávy, čímž šetří životnost baterie.

Role služby v síti přesahuje rámec jednoduchého zasílání zpráv a stává se kritickou součástí systémů veřejného varování (Public Warning Systems, PWS), jak vyžadují regulátoři v mnoha zemích. Poskytuje garantované mechanismy doručení pro nouzová upozornění, jako jsou varování před tsunami (ETWS) a komerční mobilní výstražné systémy ([CMAS](/mobilnisite/slovnik/cmas/)). Její vysílací povaha zajišťuje, že nepřispívá k signalizačnímu zahlcení během mimořádných událostí – což je významné omezení výstražných systémů založených na SMS. Protokol podporuje spojování zpráv pro delší upozornění, indikaci více jazyků a různé úrovně priority, aby bylo zajištěno, že kritická varování mohou přerušit činnost zařízení.

## K čemu slouží

CBS byla vytvořena k řešení základní potřeby efektivní, současné komunikace s masivním počtem mobilních uživatelů v určité geografické oblasti, což je schopnost, která chyběla tradičním službám typu point-to-point. Před CBS byla jedinou rozšířenou metodou hromadného mobilního oznamování SMS, která trpí vážnými omezeními během mimořádných událostí: vyžaduje individuální adresaci pro každého příjemce, generuje masivní signalizační zátěž, která může zahltit síť, a doručuje zprávy s významným a nepředvídatelným zpožděním kvůli frontám. V katastrofických scénářích, kde je včasné varování kritické, tato omezení činí výstražné systémy založené na SMS neúčinnými a potenciálně nebezpečnými.

Historický kontext vývoje CBS zahrnuje rostoucí regulatorní požadavky na veřejnou bezpečnost. Po velkých katastrofách vlády po celém světě uznaly potřebu spolehlivých výstražných systémů založených na mobilních sítích. 3GPP standardizovalo CBS, aby poskytlo nativní vysílací schopnost sítě, která funguje nezávisle na hovorovém a SMS provozu. Řeší problém zahlcení sítě pomocí modelu vysílání typu one-to-many, který spotřebovává minimální dodatečné rádiové prostředky bez ohledu na počet příjemců. Služba také řeší potřebu lokalizačního cílení, což umožňuje vysílat varování pouze do oblastí zasažených mimořádnou událostí (jako je záplavová zóna nebo oblast silného počasí), a vyhnout se tak zbytečným upozorněním pro uživatele mimo ohroženou oblast.

Dále CBS umožňuje komerční a poskytovatelské aplikace přesahující nouzová upozornění, jako je vysílání dopravních informací, aktualizací počasí nebo místní reklamy účastníkům v konkrétním městě nebo čtvrti. Její vytvoření bylo motivováno vizí proměny celulární sítě ve všestranné vysílací médium, využívající stávající infrastrukturu k doručování jak kritických veřejných informací, tak služeb s přidanou hodnotou, aniž by to ovlivnilo kapacitu pro individuální hlasové a datové komunikace.

## Klíčové vlastnosti

- Geograficky cílené vysílání do definovaných oblastí pro vysílání zpráv (Cell Broadcast Areas, CBA)
- Současné doručení všem zařízením v oblasti bez individuální adresace
- Funguje nezávisle, aby se předešlo zahlcení síťové signalizace
- Podporuje systémy veřejného varování (ETWS, CMAS) s řízením priority
- Používá identifikátory zpráv (Message Identifiers) a sériová čísla (Serial Numbers) pro kategorizaci zpráv a detekci duplicit
- Umožňuje jak nouzová upozornění, tak komerční informační služby

## Související pojmy

- [CMAS – Commercial Mobile Alert Service](/mobilnisite/slovnik/cmas/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.268** (Rel-20) — Public Warning System (PWS) Requirements
- **TS 23.048** (Rel-5) — Secured Packets for UICC Remote Management
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 25.324** (Rel-19) — Broadcast/Multicast Control Protocol
- **TS 25.401** (Rel-19) — UTRAN Overall Architecture
- **TS 25.410** (Rel-19) — Iu Interface Introduction for UTRAN
- **TS 25.419** (Rel-19) — Service Area Broadcast Protocol (SABP)
- **TS 25.703** (Rel-12) — HNB Emergency Warning Area Study for UTRA
- **TS 29.168** (Rel-19) — SBc-AP Protocol Specification
- **TS 29.199** (Rel-9) — Multimedia Messaging Web Services
- **TS 31.115** (Rel-19) — Secured Packet Structure for UICC Applications
- **TS 32.102** (Rel-19) — Telecom Management Physical Architecture Framework
- **TR 43.901** (Rel-19) — Generic Access to A/Gb Interface Feasibility Study
- **TS 44.318** (Rel-19) — Generic Access Network (GAN) Interface Procedures
- … a dalších 1 specifikací

---

📖 **Anglický originál a plná specifikace:** [CBS na 3GPP Explorer](https://3gpp-explorer.com/glossary/cbs/)
