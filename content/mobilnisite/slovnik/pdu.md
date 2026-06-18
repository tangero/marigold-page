---
slug: "pdu"
url: "/mobilnisite/slovnik/pdu/"
type: "slovnik"
title: "PDU – Protocol Data Unit"
date: 2026-01-01
abbr: "PDU"
fullName: "Protocol Data Unit"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/pdu/"
summary: "Základní koncept v telekomunikacích představující jednotku dat vyměňovanou mezi partnerskými entitami na konkrétní vrstvě protokolu, skládající se z řídicích informací protokolu a uživatelských dat. J"
---

PDU je základní jednotka dat vyměňovaná mezi partnerskými entitami na konkrétní vrstvě protokolu v systémech 3GPP, která se skládá z řídicích informací protokolu a uživatelských dat.

## Popis

Protokolová datová jednotka (PDU) je standardizovaný datový blok používaný pro komunikaci mezi partnerskými entitami ve vrstvené architektuře protokolů, jako je model [OSI](/mobilnisite/slovnik/osi/) nebo zásobníky protokolů 3GPP. Každé PDU je specifické pro danou vrstvu (např. [RRC](/mobilnisite/slovnik/rrc/), [PDCP](/mobilnisite/slovnik/pdcp/), [RLC](/mobilnisite/slovnik/rlc/), [MAC](/mobilnisite/slovnik/mac/), [NAS](/mobilnisite/slovnik/nas/), [GTP-U](/mobilnisite/slovnik/gtp-u/)) a skládá se ze dvou hlavních částí: řídicích informací protokolu ([PCI](/mobilnisite/slovnik/pci/)), což je hlavička přidaná aktuální vrstvou obsahující instrukce pro partnerskou entitu, a datové jednotky služby (SDU), což je datová část přijatá z vyšší vrstvy. Například IP paket je SDU pro vrstvu PDCP, která přidá svou hlavičku a vytvoří PDCP PDU. Toto PDU se následně stává SDU pro vrstvu RLC, která zase vytvoří RLC PDU, a tak dále směrem dolů zásobníkem.

V architektuře 3GPP jsou PDU klíčové pro každé rozhraní a proceduru. Na rádiovém rozhraní (Uu) patří mezi klíčová PDU například RRC PDU pro řídicí signalizaci (např. RRCConnectionSetup) a PDU uživatelské roviny zpracovávaná vrstvami PDCP, RLC a MAC. V páteřní síti přenášejí NAS PDU signalizaci mezi UE a AMF/SMF, zatímco GTP-U PDU tunelují uživatelská data mezi gNB a UPF přes rozhraní N3. Zpracování PDU zahrnuje zapouzdření na vysílací straně (přidání hlaviček/závěrečných částí) a rozbalení na přijímací straně (jejich odstranění za účelem získání SDU pro vyšší vrstvu). Toto vrstvené zpracování zajišťuje oddělení odpovědností, modularitu a interoperabilitu.

Úlohou PDU je poskytnout standardizovaný kontejner, který zajišťuje spolehlivé, v pořádku a bezpečné doručení informací po síti. Různé vrstvy propůjčují svým PDU různé charakteristiky. Vrstva RLC může například segmentovat nebo spojovat SDU, aby vyhověla rádiovým zdrojům, čímž vytváří RLC PDU. Vrstva MAC plánuje přenos MAC PDU prostřednictvím přenosových bloků. V páteřní síti je PDU Session klíčový koncept představující asociaci pro službu PDU konektivity, kde PDU Session ID jednoznačně identifikuje relaci a uživatelská data proudí jako sekvence PDU přes zřízené tunely. PDU je tedy atomární jednotkou přenosu dat, která umožňuje všechny služby 3GPP, od hlasových hovorů po vysokorychlostní přístup k internetu.

## K čemu slouží

Koncept PDU existuje proto, aby umožnil strukturovanou, vrstvenou komunikaci v komplexních digitálních sítích. Před standardizovanými vrstvenými architekturami byly komunikační protokoly monolitické a nepružné, což ztěžovalo jejich vývoj, ladění a vývoj. Zavedení PDU jako součásti vrstevnatých modelů (jako OSI a TCP/IP) vyřešilo problém řízení složitosti rozdělením komunikačních úloh do samostatných vrstev, z nichž každá má specifickou funkci a dobře definované rozhraní k sousedním vrstvám. PDU je hmatatelný objekt předávaný přes tato rozhraní.

Historicky, jak se telekomunikace vyvíjely od přepojování okruhů pro hlas k přepojování paketů pro data, stala se potřeba robustní, vícevrstvé datové jednotky prvořadou. V 3GPP, počínaje GSM a přes UMTS, LTE až po současný 5G, poskytl rámec PDU konzistenci a zpětnou kompatibilitu. Řeší omezení spočívající v absenci společné 'datové měny' pro různé protokolové funkce. Například stejný IP paket (PDU síťové vrstvy) může být transparentně přenášen různými technologiemi rádiového přístupu (GERAN, UTRAN, E-UTRAN, NG-RAN), protože každá technologie definuje, jak jej zapouzdřit do svých vlastních PDU spojové vrstvy (např. LLC PDU, RLC PDU).

V konečném důsledku je PDU základní konstrukcí, která umožňuje interoperabilitu, efektivní zpracování (např. kompresi hlaviček v PDCP), opravu chyb (v RLC) a multiplexování (v MAC). Umožňuje síti zacházet s různými typy provozu (řídicí vs. uživatelská rovina) s odpovídající spolehlivostí a prioritou. Vývoj struktur PDU napříč releasy (např. nové hlavičky PDCP pro zabezpečení, nová RRC PDU pro funkce 5G NR) odráží průběžnou adaptaci standardů na nové služby a požadavky, při zachování základního principu vrstvené komunikace.

## Klíčové vlastnosti

- Skládá se z řídicích informací protokolu (hlavičky) a datové jednotky služby (datové části)
- Specifické pro vrstvu; každá vrstva protokolu (RRC, PDCP, RLC, MAC, NAS) definuje svou vlastní strukturu PDU
- Umožňuje zapouzdření a rozbalení ve vrstveném zásobníku protokolů
- Může být předmětem segmentace, spojování a znovusestavení vrstvami jako je RLC
- Přenáší jak uživatelská data, tak informace řídicí signalizace
- Jednoznačně identifikováno v kontextech, jako je přenosový kanál nebo PDU Session

## Související pojmy

- [SDU – Signalling Data Unit](/mobilnisite/slovnik/sdu/)
- [PDCP – Packet Data Convergence Protocol](/mobilnisite/slovnik/pdcp/)
- [RLC – Radio Link Control](/mobilnisite/slovnik/rlc/)
- [NAS – Non-Access Stratum](/mobilnisite/slovnik/nas/)
- [GTP – GPRS Tunnelling Protocols](/mobilnisite/slovnik/gtp/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.060** (Rel-19) — GPRS Stage 1 Service Description
- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 23.107** (Rel-19) — UMTS QoS Framework
- **TS 23.140** (Rel-6) — MMS Non-Realtime Service Definition
- **TS 23.207** (Rel-19) — End-to-End QoS Framework for GPRS
- **TS 23.228** (Rel-19) — IMS Stage-2 Service Description
- **TS 23.380** (Rel-19) — IMS Restoration Procedures
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TR 23.745** (Rel-17) — Study on App Layer Support for Factories of the Future in 5G
- **TR 23.758** (Rel-17) — Study on Edge Application Architecture
- **TR 23.976** (Rel-19) — Push Service Requirements Analysis
- **TS 24.065** (Rel-4) — GPRS Subnetwork Dependent Convergence Protocol
- **TS 24.193** (Rel-19) — ATSSS Procedures Specification
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- … a dalších 98 specifikací

---

📖 **Anglický originál a plná specifikace:** [PDU na 3GPP Explorer](https://3gpp-explorer.com/glossary/pdu/)
