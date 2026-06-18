---
slug: "gsm"
url: "/mobilnisite/slovnik/gsm/"
type: "slovnik"
title: "GSM – Global System for Mobile Communications"
date: 2026-01-01
abbr: "GSM"
fullName: "Global System for Mobile Communications"
category: "Other"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/gsm/"
summary: "Základní standard druhé generace (2G) digitálních mobilních technologií, který přinesl revoluci v mobilní telefonii. Zavedl digitální hlas, SMS a mezinárodní roaming a vytvořil základ pro všechny násl"
---

GSM je základní standard druhé generace (2G) digitálních mobilních sítí, který zavedl digitální hlas, SMS a mezinárodní roaming, čímž vytvořil základ pro všechny následující sítě 3GPP.

## Popis

Global System for Mobile Communications (GSM) je soubor standardů původně vyvinutý Evropským institutem pro telekomunikační standardy ([ETSI](/mobilnisite/slovnik/etsi/)) pro popis protokolů sítí druhé generace (2G). Později byl přijat a spravován projektem 3rd Generation Partnership Project (3GPP) jako jeho základní vydání Release 1999 ([R99](/mobilnisite/slovnik/r99/)) a další. GSM nahradilo analogové systémy první generace (1G) plně digitální architekturou, což umožnilo zabezpečené hovory, službu krátkých zpráv ([SMS](/mobilnisite/slovnik/sms/)) a okruhově přepínané datové služby. Standard zahrnuje celý systém: rozhraní pro rádiový přenos, síťové jádro a moduly identifikace účastníka ([SIM](/mobilnisite/slovnik/sim/) karty).

Architektonicky je GSM rozděleno do tří hlavních podsystémů: podsystém základnových stanic ([BSS](/mobilnisite/slovnik/bss/)), podsystém přepojování ([NSS](/mobilnisite/slovnik/nss/)) a podsystém provozní podpory ([OSS](/mobilnisite/slovnik/oss/)). BSS se skládá z základnových přijímacích stanic ([BTS](/mobilnisite/slovnik/bts/)) a řadičů základnových stanic (BSC), které zajišťují rádiové rozhraní a připojení k mobilním zařízením. NSS zahrnuje základní prvky, jako je mobilní ústředna (MSC), domácí lokální registr (HLR), návštěvnický lokální registr (VLR) a autentizační centrum (AuC), odpovědné za směrování hovorů, správu účastníků a zabezpečení. OSS poskytuje možnosti správy a údržby sítě. Tato modulární architektura umožnila škálovatelné nasazení a interoperabilitu mezi zařízeními různých výrobců.

Na rádiové úrovni GSM původně používalo modulaci Gaussian Minimum Shift Keying (GMSK) ve spárovaných kmitočtových pásmech (např. 900 MHz a 1800 MHz v Evropě). Využívalo přístup s časovým dělením (TDMA) k rozdělení každého rádiového kanálu na osm časových slotů, což umožnilo více uživatelům sdílet stejnou frekvenci. Hlas byl digitálně kódován pomocí řečového kodeku. Klíčovou součástí je SIM karta, čipová karta, která uchovává identitu účastníka (IMSI), autentizační klíč a osobní údaje, což umožňuje mobilitu uživatele a zabezpečení prostřednictvím autentizačních a šifrovacích algoritmů (např. A5).

Role GSM přesahovala daleko za hlasové služby; zavedlo centrum služby krátkých zpráv (SMSC) pro SMS, což se stalo globálně rozšířenou funkcí. Jeho vývoj zahrnoval General Packet Radio Service (GPRS), který přidal schopnost paketového přepojování do jádra GSM prostřednictvím nových síťových uzlů, jako je podpůrný uzel SGSN a bránový podpůrný uzel GGSN, což umožnilo trvalé připojení k internetu. Enhanced Data rates for GSM Evolution (EDGE) dále zvýšilo přenosové rychlosti pomocí pokročilé modulace (8PSK). Zatímco sítě 3GPP pokročily k 3G (UMTS), 4G (LTE) a 5G (NR), principy GSM a mnoho konceptů síťového jádra (jako IMSI, HLR) přetrvávají a GSM sítě často fungují jako záložní vrstva. V dokumentech 3GPP pojem 'GSM' často zahrnuje i vylepšení GPRS a EDGE, pokud není uvedeno jinak.

## K čemu slouží

GSM bylo vytvořeno za účelem řešení kritických problémů analogových buněčných systémů první generace: nedostatečné zabezpečení (odposlech byl snadný), neefektivní využití spektra, nekompatibilita mezi zeměmi znemožňující mezinárodní roaming a omezená kapacita. Evropské státy a průmyslové subjekty usilovaly o jednotný digitální standard, který by nahradil roztříštěné analogové systémy (jako NMT, TACS) napříč kontinentem, což umožnilo úspory z rozsahu a bezproblémové služby přes hranice.

Historickým kontextem byla potřeba panevropského mobilního telefonního systému, který by mohl podporovat miliony účastníků. Před GSM byly mobilní sítě národní a proprietární, což uzamykalo uživatele k jednomu operátoru a zemi. Digitální povaha GSM umožnila silné šifrování (prostřednictvím SIM a AuC), dramaticky zlepšila kvalitu hlasu a zavedla datové služby jako SMS. Jeho otevřený standard podpořil intenzivní konkurenci mezi výrobci infrastruktury a koncových zařízení, což drasticky snížilo náklady a urychlilo celosvětové rozšíření.

GSM řešilo omezení analogových systémů zavedením digitálního TDMA rozhraní pro rádiový přenos, které bylo spektrálně efektivnější a umožnilo více současných hovorů na buňku. Oddělení identity uživatele (na SIM) od koncového zařízení také umožnilo osobní mobilitu a snadnější výměnu zařízení. Dále jeho standardizovaný signalizační systém (založený na SS7) a síťová architektura položily základy pro služby inteligentní sítě a následný vývoj k širokopásmovým mobilním datům prostřednictvím pozdějších vydání 3GPP.

## Klíčové vlastnosti

- Plně digitální rádiové rozhraní založené na TDMA s modulací GMSK v pásmech 900/1800/1900 MHz
- SIM karta pro zabezpečenou identitu účastníka, autentizaci a mobilitu
- Okruhově přepínaný hlas a data s robustním šifrováním (algoritmy A5)
- Služba krátkých zpráv (SMS) jako globálně standardizovaný systém zasílání zpráv
- Mezinárodní roaming umožněný standardizovanou signalizací (MAP) a síťovou architekturou
- Vývoj k paketově přepínaným datům prostřednictvím GPRS a vyšších rychlostí prostřednictvím EDGE ve stejném spektru

## Související pojmy

- [UMTS – Universal Mobile Telecommunications System](/mobilnisite/slovnik/umts/)
- [LTE – Local Terminal Emulator](/mobilnisite/slovnik/lte/)
- [IMSI – International Mobile Subscriber Identity](/mobilnisite/slovnik/imsi/)
- [SIM – Subscriber Identity Module / Universal Subscriber Identity Module](/mobilnisite/slovnik/sim/)
- [GPRS – CSI GPRS CAMEL Subscription Information](/mobilnisite/slovnik/gprs/)
- [EDGE – Enhanced Data rates for Global Evolution](/mobilnisite/slovnik/edge/)

## Definující specifikace

- **TS 21.133** (Rel-5) — 3G Security Requirements
- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.100** (Rel-4) — UMTS Service Requirements Phase 1
- **TS 22.101** (Rel-20) — Service Principles for PLMNs
- **TS 22.105** (Rel-19) — Telecommunication Services Framework
- **TS 22.226** (Rel-19) — Global Text Telephony (GTT) Stage 1
- **TS 22.822** (Rel-16) — Satellite Access in 5G Study
- **TR 22.907** (Rel-4) — UMTS IC Card and Terminal Concepts
- **TR 22.945** (Rel-4) — Fax Services Guidance for GSM/UMTS
- **TR 22.960** (Rel-4) — UMTS Mobile Multimedia Technical Challenges
- **TR 22.967** (Rel-19) — eCall Emergency Data Transmission
- **TS 23.039** (Rel-5) — SMSC to SME Interface Protocols
- **TS 23.057** (Rel-19) — Mobile Execution Environment (MExE) Specification
- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 23.107** (Rel-19) — UMTS QoS Framework
- … a dalších 186 specifikací

---

📖 **Anglický originál a plná specifikace:** [GSM na 3GPP Explorer](https://3gpp-explorer.com/glossary/gsm/)
