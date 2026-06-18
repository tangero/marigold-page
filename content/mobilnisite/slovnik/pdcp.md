---
slug: "pdcp"
url: "/mobilnisite/slovnik/pdcp/"
type: "slovnik"
title: "PDCP – Packet Data Convergence Protocol"
date: 2025-01-01
abbr: "PDCP"
fullName: "Packet Data Convergence Protocol"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/pdcp/"
summary: "Protokol vrstvy 2 v 3GPP rádiových přístupových sítích (UTRAN, E-UTRAN, NG-RAN) zodpovědný za kompresi hlaviček, šifrování, ochranu integrity a doručování ve správném pořadí pro data uživatelské a říd"
---

PDCP je protokol vrstvy 2 v 3GPP rádiových přístupových sítích, který poskytuje kompresi hlaviček, šifrování, ochranu integrity a doručování ve správném pořadí pro data uživatelské a řídicí roviny.

## Popis

Protokol konvergence paketových dat (PDCP) je klíčová podvrstva rádiového protokolového zásobníku v 3GPP přístupových technologiích, včetně UMTS ([UTRAN](/mobilnisite/slovnik/utran/)), LTE ([E-UTRAN](/mobilnisite/slovnik/e-utran/)) a NR (NG-RAN). Je definován pro uživatelskou rovinu ([UP](/mobilnisite/slovnik/up/)) i řídicí rovinu ([CP](/mobilnisite/slovnik/cp/)). Architektonicky se entity PDCP nacházejí v uživatelském zařízení (UE) a v síťovém uzlu (NodeB/eNodeB/gNB), jedna na každý rádiový přenosový kanál. Jejich primárními funkcemi je konvergence, což znamená, že přizpůsobují protokoly vyšších vrstev (typicky IP) pro efektivní přenos přes specifické rádiové rozhraní.

Pro uživatelskou rovinu PDCP provádí robustní kompresi hlaviček ([ROHC](/mobilnisite/slovnik/rohc/)), aby výrazně zmenšil velikost hlaviček IP paketů (např. IPv4, IPv6, [UDP](/mobilnisite/slovnik/udp/), [RTP](/mobilnisite/slovnik/rtp/)), které jsou u mnoha aplikací velké vzhledem k datové části, čímž šetří cennou šířku pásma vzdušného rozhraní. Také poskytuje zabezpečení prostřednictvím šifrování (ciphering) datové části uživatelských dat pro zajištění důvěrnosti. Dále, pro LTE a NR, PDCP zajišťuje doručování ve správném pořadí a detekci duplicit u datových paketů během procedur předávání spojení. Spravuje pořadové číslo PDCP ([SN](/mobilnisite/slovnik/sn/)) a ukládá pakety do vyrovnávací paměti, aby umožnil bezstratové předání spojení, když podkladová vrstva RLC pracuje v potvrzovaném režimu (AM).

Pro řídicí rovinu, konkrétně pro zprávy RRC a NAS, PDCP poskytuje ochranu integrity a šifrování. Ochrana integrity zaručuje, že řídicí zprávy nebyly během přenosu pozměněny. PDCP tyto bezpečnostní funkce provádí pomocí klíčů odvozených z bezpečnostních procedur NAS a AS. Protokol funguje tak, že přijímá datové jednotky služby (SDU) z vyšších vrstev (IP nebo RRC), připojí hlavičku PDCP obsahující pořadové číslo, provede nakonfigurované operace (komprese, šifrování) a výslednou datovou jednotku protokolu (PDU) předá vrstvě RLC pod sebou. Při příjmu je proces obrácený. Jeho role je zásadní pro dosažení efektivního, bezpečného a spolehlivého doručování dat v moderních mobilních sítích.

## K čemu slouží

PDCP byl zaveden, aby řešil neefektivnost a bezpečnostní nedostatky přenosu paketů internetového protokolu (IP) přímo přes rádiový spoj v 3G UMTS. V raných vydáních 3G zásobník protokolů postrádal vyhrazenou konvergenční vrstvu, což činilo přenos IP paketů přes vzdušné rozhraní náročným na prostředky kvůli velkým a opakujícím se hlavičkám. To bylo obzvláště problematické pro hlas přes IP (VoIP) a interaktivní hraní her, kde malé datové části jsou zastíněny hlavičkami IP/UDP/RTP.

Protokol řeší několik klíčových problémů. Za prvé, komprese hlaviček (poprvé zavedená v Rel-4) dramaticky zlepšuje spektrální účinnost a snižuje latenci pro služby založené na IP. Za druhé, centralizuje šifrování uživatelských dat ve vrstvě nad RLC, což zjednodušuje bezpečnostní architekturu a umožňuje šifrování i když RLC pracuje v transparentním režimu. Za třetí, s přechodem na plochou, plně IP architekturu v LTE, se role PDCP rozšířila o doručování ve správném pořadí a odstraňování duplicit, které jsou nezbytné pro zachování integrity dat během předávání spojení mezi eNodeB, zejména pro služby citlivé na zpoždění. Jeho vytvoření bylo motivováno potřebou optimalizovat rádiové rozhraní pro explozivní růst IP provozu, zajistit robustní zabezpečení a podporovat bezproblémovou mobilitu ve stále více heterogenních síťových prostředích.

## Klíčové vlastnosti

- Robustní komprese hlaviček (ROHC) pro hlavičky IP, UDP, RTP a ESP
- Šifrování (ciphering) pro data uživatelské roviny a zprávy řídicí roviny
- Ochrana integrity pro data řídicí roviny (RRC)
- Doručování ve správném pořadí a detekce duplicit během předávání spojení
- Správa pořadového čísla PDCP (SN) pro podporu bezstratového předání spojení
- Podpora datové a řídicí roviny a více rádiových přenosových kanálů

## Související pojmy

- [ROHC – Robust Header Compression](/mobilnisite/slovnik/rohc/)
- [RLC – Radio Link Control](/mobilnisite/slovnik/rlc/)
- [RRC – Radio Resource Control](/mobilnisite/slovnik/rrc/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 23.401** (Rel-19) — Evolved Packet System (EPS) Stage 2 Description
- **TS 23.725** (Rel-16) — Study on URLLC Architecture Enhancements
- **TS 25.301** (Rel-19) — UE-UTRAN Radio Interface Protocol Architecture
- **TS 25.323** (Rel-19) — Packet Data Convergence Protocol (PDCP) Specification
- **TS 25.324** (Rel-19) — Broadcast/Multicast Control Protocol
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TS 25.413** (Rel-19) — Radio Access Network Application Part (RANAP)
- **TR 25.912** (Rel-19) — Evolved UTRA and UTRAN Technical Report
- **TR 25.931** (Rel-19) — UTRAN Signalling Procedures Examples
- **TS 26.114** (Rel-19) — IMS Multimedia Telephony Media Handling
- **TR 26.926** (Rel-19) — Traffic Models & Quality Evaluation for Media/XR in 5G
- **TR 26.935** (Rel-19) — Speech Codec Performance for Packet Switched Multimedia
- **TR 26.937** (Rel-19) — 3GPP PSS Characterization
- … a dalších 32 specifikací

---

📖 **Anglický originál a plná specifikace:** [PDCP na 3GPP Explorer](https://3gpp-explorer.com/glossary/pdcp/)
