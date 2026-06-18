---
slug: "hdlc"
url: "/mobilnisite/slovnik/hdlc/"
type: "slovnik"
title: "HDLC – High Level Data Link Control"
date: 2025-01-01
abbr: "HDLC"
fullName: "High Level Data Link Control"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/hdlc/"
summary: "Bitově orientovaný synchronní protokol linkové vrstvy standardizovaný ISO. V 3GPP se používá pro rámcování a spolehlivý přenos dat přes různá rozhraní, zejména v signalizačních spojích jádra sítí UMTS"
---

HDLC je standardizovaný bitově orientovaný protokol linkové vrstvy používaný v sítích 3GPP pro spolehlivé rámcování a přenos signalizačních dat, který zajišťuje detekci chyb a řízení toku na rozhraních jádra sítě.

## Popis

High Level Data Link Control (HDLC) je základní protokol linkové vrstvy, standardizovaný [ISO](/mobilnisite/slovnik/iso/) jako ISO/[IEC](/mobilnisite/slovnik/iec/) 13239, který byl přijat ve specifikacích 3GPP pro rámcování a spolehlivý přenos dat. Funguje na vrstvě 2 [OSI](/mobilnisite/slovnik/osi/) modelu a jde o bitově orientovaný synchronní protokol. Jeho hlavní funkcí je zajistit spolehlivý přenos datových rámců mezi síťovými uzly přes fyzický spoj. HDLC definuje strukturovaný formát rámce sestávající z příznakových sekvencí pro ohraničení, adresních polí pro identifikaci stanic, řídicího pole pro správu typů rámců a sekvencování, informačního pole pro užitečná data a kontrolního součtu rámce ([FCS](/mobilnisite/slovnik/fcs/)) pro detekci chyb pomocí cyklického redundantního kódu ([CRC](/mobilnisite/slovnik/crc/)). Protokol podporuje více provozních režimů, včetně Normálního režimu odpovědi ([NRM](/mobilnisite/slovnik/nrm/)), Asynchronního režimu odpovědi (ARM) a Asynchronního vyváženého režimu ([ABM](/mobilnisite/slovnik/abm/)), které definují role primární a sekundární stanice při řízení spoje a toku dat.

V architektuře 3GPP je HDLC specifikován pro použití na různých rozhraních, zejména v jádru sítě a pro některé signalizační spoje přístupové sítě (RAN). Například v UMTS se používá pro rozhraní Iub mezi řídicím uzlem radiové sítě ([RNC](/mobilnisite/slovnik/rnc/)) a Node B, stejně jako pro některé signalizační přenosy v jádru sítě. Protokol poskytuje základní služby linkové vrstvy, jako je navázání a ukončení spojení, sekvencování a potvrzování rámců, detekce chyb a obnova prostřednictvím opakovaného vysílání a řízení toku pro zabránění přetížení přijímače. Zajišťuje transparentnost dat pomocí vkládání bitů (bit stuffing), kdy je za pět po sobě jdoucích bitů '1' v datovém poli vložen bit '0', aby se zabránilo záměně s příznakovými sekvencemi.

Úloha HDLC v sítích 3GPP spočívá v poskytování robustní, standardizované metody pro komunikaci typu point-to-point a multipoint, která tvoří spolehlivou podvrstvu pro protokoly vyšších vrstev. Ačkoli se novější technologie a protokoly, jako je přenos založený na IP a PPP, staly rozšířenějšími, HDLC zůstává kritickou součástí starších systémů a specifických definic rozhraní. Jeho implementace ve specifikacích 3GPP zajišťuje interoperabilitu a spolehlivý přenos dat pro řídicí signalizaci a uživatelská data v dřívějších generacích sítí a poskytuje stabilní základ pro síťové operace.

## K čemu slouží

HDLC byl vytvořen, aby poskytl standardizovaný, spolehlivý protokol linkové vrstvy pro synchronní sériovou komunikaci, který řešil potřebu bezchybného přenosu dat přes telekomunikační spoje. Před jeho standardizací vedly proprietární a méně robustní protokoly linkové vrstvy k problémům s interoperabilitou a nespolehlivým přenosem dat. HDLC tyto problémy vyřešil tím, že nabídl komplexní rámec pro strukturu rámce, řízení chyb a správu toku, který se stal vzorem pro mnoho následných protokolů linkové vrstvy.

V kontextu 3GPP byl HDLC přijat, aby zajistil spolehlivý signalizační a datový přenos přes různá síťová rozhraní, zejména v sítích GSM a UMTS. Poskytl osvědčený, stabilní protokol pro linkovou vrstvu, který umožnil spolehlivou výměnu řídicích zpráv a uživatelských dat mezi síťovými prvky, jako jsou RNC a Node B. Jeho zařazení do specifikací 3GPP podpořilo cíl vytvářet interoperabilní, robustní mobilní sítě využitím mezinárodně uznávaného standardu pro komunikaci na úrovni linky.

Motivace pro použití HDLC v 3GPP vycházela z jeho vyspělosti, širokého přijetí v průmyslu a schopnosti splňovat přísné požadavky na spolehlivost telekomunikačních sítí. Odstranil omezení dřívějších, jednodušších protokolů tím, že zahrnul pokročilé funkce, jako je posuvné okénko pro řízení toku a robustní detekce chyb, které byly nezbytné pro udržení integrity sítě a výkonu v rozvíjejícím se mobilním ekosystému.

## Klíčové vlastnosti

- Bitově orientované synchronní rámcování s příznakovými oddělovači
- Podpora více provozních režimů (NRM, ARM, ABM)
- Detekce chyb pomocí kontrolního součtu rámce (FCS) s CRC
- Řízení toku a číslování sekvencí pro spolehlivý přenos
- Transparentnost dat prostřednictvím vkládání nulových bitů (bit stuffing)
- Podpora komunikace s navázáním spojení i bez něj (connectionless)

## Související pojmy

- [PPP – Priority Precedence Preemption](/mobilnisite/slovnik/ppp/)
- [RNC – Radio Network Controller](/mobilnisite/slovnik/rnc/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.044** (Rel-4) — GSM Teletex Service Support
- **TS 25.412** (Rel-19) — Iu Interface Signalling Transport Specification
- **TS 25.414** (Rel-19) — UTRAN Iu Interface User Plane Transport Protocols
- **TS 25.422** (Rel-19) — Signalling Transport for Iur Interface
- **TS 25.424** (Rel-19) — UTRAN Iur Interface Data Transport & Signalling
- **TS 25.426** (Rel-19) — UTRAN Iur/Iub Transport Bearers
- **TS 25.432** (Rel-19) — Iub NBAP Signalling Transport Specification
- **TS 25.434** (Rel-19) — UTRAN Iub Interface Data Transport and Signalling
- **TS 26.110** (Rel-19) — 3G-324M Multimedia Codecs for Circuit Switched Networks
- **TS 27.060** (Rel-19) — TE-MT Interworking for Packet Domain
- **TS 37.460** (Rel-19) — Iuant Interface Introduction
- **TS 37.462** (Rel-19) — Iuant Interface Data Link Layer for RETAP/TMAAP
- **TS 37.466** (Rel-19) — Iuant Interface Introduction & RETAP/TMAAP

---

📖 **Anglický originál a plná specifikace:** [HDLC na 3GPP Explorer](https://3gpp-explorer.com/glossary/hdlc/)
