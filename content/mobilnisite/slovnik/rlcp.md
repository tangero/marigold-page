---
slug: "rlcp"
url: "/mobilnisite/slovnik/rlcp/"
type: "slovnik"
title: "RLCP – Radio Link Control Protocol"
date: 2025-01-01
abbr: "RLCP"
fullName: "Radio Link Control Protocol"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/rlcp/"
summary: "Protokol vrstvy 2 zodpovědný za přenos dat mezi uživatelským zařízením (UE) a sítí přes rádiové rozhraní. Poskytuje opravu chyb prostřednictvím ARQ, segmentaci, zpětné sestavení a doručování ve správn"
---

RLCP je protokol řízení rádiového spoje vrstvy 2, který je zodpovědný za přenos dat, poskytování opravy chyb, segmentaci a doručování ve správném pořadí mezi uživatelským zařízením (UE) a sítí.

## Popis

Protokol řízení rádiového spoje (Radio Link Control Protocol, RLCP) je základní protokol vrstvy 2 (linkové vrstvy) v zásobníku protokolů přístupové vrstvy (access stratum) 3GPP, který se nachází mezi protokolem konvergence paketových dat (Packet Data Convergence Protocol, [PDCP](/mobilnisite/slovnik/pdcp/)) nad ním a protokolem řízení přístupu k médiu (Medium Access Control, [MAC](/mobilnisite/slovnik/mac/)) pod ním. Jeho primární funkcí je zajistit spolehlivý nebo včasný přenos dat (jak uživatelské, tak řídicí roviny) přes inherentně nespolehlivý rádiový spoj. K dosažení tohoto cíle RLCP funguje ve třech odlišných režimech, z nichž každý je přizpůsoben pro konkrétní typ provozu a požadavky na kvalitu služby (QoS). Transparentní režim (Transparent Mode, [TM](/mobilnisite/slovnik/tm/)) se používá pro řídicí signalizaci kritickou na zpoždění, jako je vysílání systémových informací nebo paging, kde jsou data předána bez přidání hlavičky protokolu nebo provádění retransmisí. Nepotvrzovaný režim (Unacknowledged Mode, [UM](/mobilnisite/slovnik/um/)) se používá pro uživatelská data citlivá na zpoždění, jako je VoIP nebo streamování, kde poskytuje segmentaci/zpětné sestavení a doručování ve správném pořadí, ale bez retransmisí, a toleruje určitou ztrátu paketů pro zachování nízké latence. Potvrzovaný režim (Acknowledged Mode, [AM](/mobilnisite/slovnik/am/)) se používá pro data netolerující chyby, jako jsou přenosy souborů nebo provoz založený na TCP, kde poskytuje plnou opravu chyb prostřednictvím mechanismu automatického opakovaného dotazu (Automatic Repeat Request, [ARQ](/mobilnisite/slovnik/arq/)) spolu se segmentací, doručováním ve správném pořadí a detekcí duplicit.

Z architektonického hlediska je entita RLCP konfigurována na každý rádiový přenosový kanál (radio bearer). Přijímá jednotky dat služby (Service Data Units, [SDU](/mobilnisite/slovnik/sdu/)) z vrstvy PDCP. Její základní operace zahrnují segmentaci a konkatenaci, při kterých přizpůsobuje velikost SDU tak, aby odpovídala transportním blokům přiděleným vrstvou MAC. Poté přidá hlavičku RLCP a vytvoří jednotku dat protokolu RLCP (RLCP Protocol Data Unit, [PDU](/mobilnisite/slovnik/pdu/)). Tato hlavička obsahuje klíčové informace, jako je pořadové číslo (Sequence Number, SN), které se používá pro řazení a v režimu AM také pro potvrzování přijatých dat. RLCP PDU je následně předáno vrstvě MAC pro přenos přes logický kanál. Na přijímací straně protějšková entita RLCP používá informace z hlavičky k opětovnému sestavení SDU, k jejich doručení ve správném pořadí do PDCP a v režimu AM ke generování stavových hlášení (ACK/NACK), která jsou odeslána zpět vysílači s žádostí o retransmisi chybějících PDU, čímž implementuje funkci ARQ.

RLCP úzce spolupracuje s vrstvami MAC a fyzickou vrstvou. Zatímco fyzická vrstva používá hybridní ARQ (Hybrid ARQ, HARQ) pro rychlé retransmise na fyzické vrstvě, ARQ protokolu RLCP funguje na vyšší vrstvě, aby opravil případné zbytkové chyby, které HARQ nedokáže opravit, a poskytuje tak robustnější záruku integrity dat na koncích. Toto dvouvrstvé schéma retransmisí je klíčovým konstrukčním principem. Dále RLCP poskytuje řízení toku mezi sebou a vrstvou PDCP a provádí detekci a obnovu po chybách protokolu. Jeho konfigurace (režim, velikost pole SN, hodnoty časovačů) je řízena protokolem řízení rádiových prostředků (Radio Resource Control, RRC), což síti umožňuje optimalizovat výkon pro každý typ služby.

## K čemu slouží

Protokol řízení rádiového spoje (RLCP) byl vytvořen, aby řešil základní výzvu poskytování spolehlivého přenosu dat přes nepředvídatelný a náchylný k chybám bezdrátový rádiový kanál. Rané celulární systémy byly primárně okruhově přepínané pro hlas, který má jiné tolerance vůči zpoždění a chybám. S příchodem paketově přepínaných datových služeb ve 3G UMTS (kde byl RLCP formálně pojmenován a ustálen), vznikla kritická potřeba linkového protokolu, který by mohl podporovat rozmanité aplikace – od hlasu v reálném čase po prohlížení webu – z nichž každá má odlišné požadavky na spolehlivost, zpoždění a propustnost. RLCP to řeší tím, že nabízí více provozních režimů (TM, UM, AM), což síti umožňuje přizpůsobit službu linkové vrstvy konkrétnímu profilu QoS každého datového rádiového přenosového kanálu.

Jeho vytvoření bylo motivováno omezeními spoléhání se pouze na techniky fyzické vrstvy nebo jednodušší linkové protokoly. Kódování na fyzické vrstvě a HARQ jsou rychlé, ale ne neomylné. Mechanismus ARQ protokolu RLCP poskytuje pro kritická data bezpečnostní síť na vyšší vrstvě, která je robustnější. Protokol také řeší problém nevyváženosti velikostí paketů mezi aplikacemi vyšších vrstev a dynamicky velikostně přidělovanými transportními bloky fyzické vrstvy prostřednictvím svých funkcí segmentace a konkatenace. Historicky se RLCP vyvinul z linkových protokolů 2G GSM (např. Radio Link Protocol, RLP v GPRS), ale byl výrazně vylepšen pro vyšší přenosové rychlosti a nižší latence vyžadované 3G a následujícími generacemi. Poskytuje standardizovaný, efektivní a flexibilní mechanismus pro řízení chyb, který je základním kamenem pro umožnění spolehlivých služeb založených na IP, jež definují moderní celulární sítě.

## Klíčové vlastnosti

- Tři provozní režimy: Transparentní režim (Transparent Mode, TM), Nepotvrzovaný režim (Unacknowledged Mode, UM), Potvrzovaný režim (Acknowledged Mode, AM)
- Automatický opakovaný dotaz (Automatic Repeat Request, ARQ) pro opravu chyb v režimu AM
- Segmentace, zpětné sestavení a konkatenace datových jednotek
- Doručování dat vyšším vrstvám ve správném pořadí
- Detekce a zahození duplicit
- Řízení toku mezi vrstvami RLC a PDCP

## Související pojmy

- [RLC-PDU – Radio Link Control - Protocol Data Unit](/mobilnisite/slovnik/rlc-pdu/)
- [PDCP – Packet Data Convergence Protocol](/mobilnisite/slovnik/pdcp/)
- [MAC – Message Authentication Code](/mobilnisite/slovnik/mac/)
- [ARQ – Automatic Repeat Request](/mobilnisite/slovnik/arq/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [RLCP na 3GPP Explorer](https://3gpp-explorer.com/glossary/rlcp/)
