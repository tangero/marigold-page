---
slug: "dlc"
url: "/mobilnisite/slovnik/dlc/"
type: "slovnik"
title: "DLC – Data Link Connection"
date: 2025-01-01
abbr: "DLC"
fullName: "Data Link Connection"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/dlc/"
summary: "Logické spojení navázané na vrstvě datového spoje (vrstva 2) mezi dvěma síťovými entitami, například mobilní stanicí a síťovým uzlem. Poskytuje spolehlivou službu přenosu dat s zachováním pořadí pro u"
---

DLC je logické spojení vrstvy 2 mezi dvěma síťovými entitami, jako například mobilním zařízením a síťovým uzlem, které poskytuje spolehlivý a pořadí zachovávající přenos dat pro uživatelská data a signalizaci v původních systémech GSM a GPRS.

## Popis

Data Link Connection (DLC) je logický komunikační kanál vrstvy 2 definovaný v rámci specifikací 3GPP, primárně pro sítě GSM a [GPRS](/mobilnisite/slovnik/gprs/). Funguje nad fyzickou vrstvou a je zodpovědný za spolehlivý, pořadí zachovávající a na chybách řízený přenos datových jednotek, známých jako rámce, mezi partnerskými entitami. DLC je navázáno, udržováno a ukončeno protokolem vrstvy datového spoje, který spravuje řízení toku, detekci a opravu chyb (např. pomocí retransmisí) a číslování sekvencí pro zajištění integrity dat. V kontextu GSM jsou DLC klíčová pro podporu různých služeb, včetně přepojování okruhů pro data a transport signalizace pro správu mobility a řízení hovorů.

Z architektonického hlediska je DLC identifikováno identifikátorem Data Link Connection Identifier ([DLCI](/mobilnisite/slovnik/dlci/)) a často je multiplexováno přes jeden fyzický prostředek. Spojení může být point-to-point nebo v některých konfiguracích point-to-multipoint. Protokol řídící DLC, jako například Link Access Protocol on the Dm channel (LAPDm) pro rádiové rozhraní nebo jiné varianty [LAP](/mobilnisite/slovnik/lap/) pro terestrické spoje, definuje strukturu rámců, řídicí procedury a časovače. Tyto procedury zahrnují navázání spojení pomocí handshake, přenos informačních rámců s potvrzeními a provádění obnovy po chybě pomocí mechanismů selektivního odmítnutí.

V rámci GPRS jádrové sítě jsou koncepty DLC rozšířeny v protokolech jako GPRS Tunneling Protocol ([GTP](/mobilnisite/slovnik/gtp/)), ale základní DLC, jak je specifikováno v dokumentech jako TS 44.060 (protokol RLC/[MAC](/mobilnisite/slovnik/mac/)) pro rádiové rozhraní, poskytuje základní službu spojové vrstvy pro přenos paketových dat mezi mobilní stanicí a sítí. Jeho úlohou je odstínit vyšší vrstvy od nedokonalostí prostředí rádiového přenosu a poskytnout virtuální bezchybový kanál. Zatímco jeho význam s vývojem směrem k 3G, 4G a 5G poklesl, kde se používají jiné paradigmata vrstvy 2, jako Packet Data Convergence Protocol (PDCP) a Radio Link Control (RLC), zůstává DLC základním konceptem v telekomunikacích pro pochopení spolehlivých služeb datového spoje.

## K čemu slouží

Data Link Connection bylo vytvořeno za účelem poskytnutí spolehlivé služby přenosu dat přes inherentně nespolehlivé fyzické kanály, zejména náchylné k chybám na rádiovém rozhraní v raných digitálních celulárních systémech jako GSM. Před standardizovanými protokoly datového spoje trpěl jednoduchý nezpracovaný přenos dat vysokou chybovostí, ztrátou dat a doručováním mimo pořadí, což jej činilo nevhodným pro signalizaci a uživatelské datové aplikace vyžadující integritu. DLC, řízené robustními protokoly spojové vrstvy, toto vyřešilo zavedením mechanismů potvrzení, sekvenčních čísel a procedur retransmisí, čímž vytvořilo virtuální bezchybný okruh.

Historicky koncept vychází z architektur sítí [ISDN](/mobilnisite/slovnik/isdn/) a X.25, kde byla spojení datového spoje (pomocí protokolů jako [LAPD](/mobilnisite/slovnik/lapd/)) nezbytná pro spolehlivou signalizaci na D-kanálu a paketová data. 3GPP tyto principy adaptovalo pro mobilní prostředí. Primární motivací bylo podpořit nejen hlas, ale také služby přepojovaných okruhů pro data (jako fax a vytáčená data) a později paketově přepojované služby [GPRS](/mobilnisite/slovnik/gprs/), které všechny vyžadovaly spolehlivý transportní mechanismus vrstvy 2 jak pro signalizaci řídicí roviny, tak pro data uživatelské roviny.

Vyřešilo to omezení absence garantovaného doručení na fyzické vrstvě. Navázáním logického spojení s definovanými stavy a procedurami mohla síť efektivně spravovat prostředky, multiplexovat více logických kanálů na jeden fyzický kanál a zajistit správné doručení kritických signalizačních zpráv pro mobilitu a sestavení hovoru. Tato spolehlivost byla klíčová pro stabilitu sítě a kvalitu služeb v systémech 2G.

## Klíčové vlastnosti

- Poskytuje spolehlivé doručování rámců v pořadí pomocí mechanismů potvrzení a retransmisí.
- Implementuje detekci chyb pomocí Frame Check Sequences (FCS) a opravu chyb prostřednictvím ARQ (Automatic Repeat Request).
- Spravuje řízení toku, aby zabránilo přetížení přijímače, a přizpůsobuje se proměnným podmínkám spoje.
- Podporuje multiplexování více logických spojení (DLC) přes jeden fyzický kanál pomocí identifikátorů.
- Definuje explicitní procedury pro navázání a uvolnění spojení, spravuje stavový automat spoje.
- Funguje nezávisle pro různé logické kanály (např. signalizace, uživatelská data), aby poskytovalo službu šitou na míru.

## Související pojmy

- [DLCI – Data Link Connection Identifier](/mobilnisite/slovnik/dlci/)
- [GPRS – CSI GPRS CAMEL Subscription Information](/mobilnisite/slovnik/gprs/)
- [GSM – Global System for Mobile Communications](/mobilnisite/slovnik/gsm/)

## Definující specifikace

- **TS 27.010** (Rel-19) — Multiplexing Protocol for UE-TE Interface
- **TS 43.051** (Rel-19) — GERAN Stage 2 Service Description
- **TS 44.060** (Rel-19) — GERAN RLC/MAC Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [DLC na 3GPP Explorer](https://3gpp-explorer.com/glossary/dlc/)
