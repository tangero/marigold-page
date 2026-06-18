---
slug: "sms-pp"
url: "/mobilnisite/slovnik/sms-pp/"
type: "slovnik"
title: "SMS-PP – Short Message Service – Point to Point"
date: 2025-01-01
abbr: "SMS-PP"
fullName: "Short Message Service – Point to Point"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/sms-pp/"
summary: "SMS-PP je standardizovaný mechanismus 3GPP pro doručování krátkých textových zpráv přímo mezi dvěma mobilními účastníky. Jedná se o základní službu umožňující SMS zprávy od osoby k osobě, která tvoří"
---

SMS-PP je standardizovaný mechanismus 3GPP pro doručování krátkých textových zpráv přímo mezi dvěma mobilními účastníky.

## Popis

SMS-PP (Short Message Service – Point to Point) je přenosová služba definovaná v architektuře systému 3GPP pro přenos krátkých zpráv mezi dvěma konkrétními mobilními stanicemi ([MS](/mobilnisite/slovnik/ms/)) nebo uživatelskými zařízeními (UE). V jádru sítě funguje jako služba typu store-and-forward (ulož a předej). Architektura zahrnuje iniciující MS/UE, obsluhující ústřednu [MSC](/mobilnisite/slovnik/msc/) (Mobile Switching Centre) nebo entitu IMS (IP Multimedia Subsystem), centrum služby krátkých zpráv ([SMS-SC](/mobilnisite/slovnik/sms-sc/)), domovský registr [HLR](/mobilnisite/slovnik/hlr/) (Home Location Register) nebo server [HSS](/mobilnisite/slovnik/hss/) (Home Subscriber Server) pro směrovací informace a cílovou MSC nebo funkci [S-CSCF](/mobilnisite/slovnik/s-cscf/) (Serving-Call Session Control Function) pro doručení.

Služba funguje prostřednictvím řady standardizovaných procedur [MAP](/mobilnisite/slovnik/map/) (Mobile Application Part) nebo Diameter. Když uživatel odešle zprávu, MS/UE ji odešle prostřednictvím obsluhujícího uzlu (např. MSC pro přepojování okruhů, [MME](/mobilnisite/slovnik/mme/)/SGSN pro přepojování paketů nebo IMS uzlu) do určeného SMS-SC. SMS-SC funguje jako centrální rozbočovač, který zprávu uloží a dotazuje se HLR/HSS, aby zjistil aktuální stav a umístění (adresu obsluhujícího uzlu) příjemce. Jakmile je obsluhující uzel příjemce identifikován, SMS-SC zprávu přepošle k doručení. Pokud je příjemce dočasně nedostupný, SMS-SC zprávu uloží a opakuje pokus o doručení na základě časovačů nastavených v síti.

Mezi klíčové protokolové vrstvy patří RP (Transfer Protocol), CP (Control Protocol) a TP (Transfer Protocol), které se starají o přenos, řízení a kódování zprávy na aplikační úrovni. Služba podporuje scénáře jak s iniciací z mobilu (MO), tak s doručením do mobilu (MT). Při MO zpráva putuje z MS do SMS-SC. Při MT putuje ze SMS-SC do MS. SMS-PP je nedílnou součástí sítě nejen pro uživatelské zprávy, ale také pro doručování příkazů pro OTA (Over-The-Air) provizionování, administrativní oznámení a další služby typu stroj-osoba, což z ní činí univerzální nástroj pro operátory.

## K čemu slouží

SMS-PP byl vytvořen za účelem standardizace spolehlivé, efektivní a globálně interoperabilní metody pro odesílání krátkých textových zpráv mezi mobilními uživateli. Před jeho úplnou standardizací v 3GPP Release 5 existovaly implementace SMS, ale postrádaly jednotný architektonický rámec a schopnosti roamingu mezi operátory potřebné pro bezproblémovou globální službu. Primárním problémem, který řešil, bylo poskytnutí jednoduchého komunikačního kanálu s nízkou šířkou pásma, který mohl fungovat nezávisle na hovoru a využíval kapacitu signalizačního systému.

Motivace vycházela z obrovského komerčního úspěchu SMS v raných sítích GSM. 3GPP formalizoval procedury a rozhraní (jako MAP), aby zajistil, že jak se sítě vyvíjely z 2G GSM přes 3G UMTS a dále, SMS zůstane konzistentní a podporovanou službou napříč všemi generacemi. Odstranil omezení proprietárních implementací definováním jasných rolí síťových prvků (MSC, HLR, SMS-SC) a standardizací mechanismů pro zpracování chyb, směrování a potvrzení doručení. To umožnilo účastníkům na různých sítích a různých generacích technologií si spolehlivě vyměňovat zprávy, což podpořilo široké přijetí a vytvořilo základní platformu pro nadstavbové služby.

## Klíčové vlastnosti

- Doručování typu store-and-forward (ulož a předej) prostřednictvím SMS-SC
- Podpora operací jak s iniciací z mobilu (MO), tak s doručením do mobilu (MT)
- Využití protokolů MAP nebo Diameter pro komunikaci síťových prvků
- Hlášení o stavu doručení a potvrzení o přijetí
- Podpora zřetězených dlouhých zpráv (více segmentů SMS)
- Využití signalizačních kanálů, což umožňuje fungování bez vyhrazených přenosových kanálů

## Související pojmy

- [SMS-SC – Short Message Service - Service Centre](/mobilnisite/slovnik/sms-sc/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.048** (Rel-5) — Secured Packets for UICC Remote Management
- **TS 31.114** (Rel-8) — USAT Interpreter Transmission Protocol
- **TS 31.115** (Rel-19) — Secured Packet Structure for UICC Applications

---

📖 **Anglický originál a plná specifikace:** [SMS-PP na 3GPP Explorer](https://3gpp-explorer.com/glossary/sms-pp/)
