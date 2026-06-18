---
slug: "smrse"
url: "/mobilnisite/slovnik/smrse/"
type: "slovnik"
title: "SMRSE – Short Message Relay Service Element"
date: 2025-01-01
abbr: "SMRSE"
fullName: "Short Message Relay Service Element"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/smrse/"
summary: "Síťový prvek definovaný v 3GPP pro přeposílání krátkých zpráv, zejména pro vzájemné propojení různých domén zasílání zpráv. Zajišťuje spolehlivé doručování SMS přes hranice sítí, například mezi GSM a"
---

SMRSE je síťový prvek, který přeposílá krátké zprávy mezi různými doménami zasílání zpráv, například mezi GSM a IP systémy, tím, že zajišťuje převod protokolů a směrování pro spolehlivé doručení SMS.

## Popis

Short Message Relay Service Element (SMRSE) je funkční entita specifikovaná v architektuře 3GPP, primárně dokumentovaná v TS 23.078. Působí jako přepínač nebo brána pro provoz služby krátkých zpráv ([SMS](/mobilnisite/slovnik/sms/)), usnadňuje vzájemné propojení a přenos SMS zpráv mezi různými síťovými doménami. Jejím hlavním úkolem je zajistit, aby SMS zprávy mohly být spolehlivě doručeny i v případě, že zdrojová a cílová síť používají různé protokoly nebo jsou odděleny síťovými hranicemi, například mezi tradiční přepojovanou okruhovou GSM sítí a paketovou IP sítí, jako je internet nebo doména IMS (IP Multimedia Subsystem).

Z architektonického hlediska je SMRSE často implementována jako součást větší brány pro zasílání zpráv, například SMS Gateway [MSC](/mobilnisite/slovnik/msc/) ([SMS-GMSC](/mobilnisite/slovnik/sms-gmsc/)) nebo [IP-SM-GW](/mobilnisite/slovnik/ip-sm-gw/) (IP Short Message Gateway). Obsahuje potřebnou logiku pro provádění převodu protokolů, adaptaci formátu zpráv a překlad adres. Například, když SMS pochází z GSM telefonu a je určena uživateli v IP síti, SMRSE může přeložit signalizaci [MAP](/mobilnisite/slovnik/map/) (Mobile Application Part) používanou v GSM jádrové síti na vhodný IP protokol, například [SIP](/mobilnisite/slovnik/sip/) (Session Initiation Protocol) pro IMS nebo jiný protokol pro zasílání zpráv. Zpracovává klíčové funkce, jako je segmentace zpráv, opětovné složení delších zpráv (zřetězené SMS) a zpracování chyb pro zajištění úspěšného doručení.

Při provozu SMRSE přijímá SMS zprávu od zdrojového síťového prvku, například od MSC (Mobile Switching Centre) nebo [SMSC](/mobilnisite/slovnik/smsc/) (Short Message Service Centre). Poté prozkoumá cílovou adresu a určí vhodnou trasu a protokol pro přeposlání. To zahrnuje dotazování databází, jako je [HLR](/mobilnisite/slovnik/hlr/) (Home Location Register), pro směrovací informace nebo použití ENUM (Telephone Number Mapping) pro převod telefonních čísel na IP adresy. SMRSE také spravuje doručovací zprávy a převádí je mezi doménami, aby odesílatel obdržel potvrzení. Její umístění v síti je strategické, často na okraji jádrové sítě, aby sloužila jako most mezi staršími sítěmi založenými na SS7 a moderními infrastrukturami založenými na IP, čímž rozšiřuje dosah a spolehlivost služeb SMS.

## K čemu slouží

SMRSE byla představena ve 3GPP Release 5, aby řešila rostoucí potřebu vzájemného propojení SMS při vývoji mobilních sítí. Původně byla SMS navržena pro GSM sítě používající signalizaci SS7 a protokoly MAP. S příchodem paketově přepínaných jader a IMS však vznikla potřeba doručovat SMS přes IP sítě pro podporu nových služeb a snížení závislosti na starší infrastruktuře s přepojováním okruhů. SMRSE řeší problém nekompatibility protokolů tím, že funguje jako překladač, a umožňuje tak bezproblémové doručování SMS přes heterogenní sítě.

Historicky, bez takového přepínacího prvku, by byly služby SMS omezeny na jedinou síťovou technologii, což by omezovalo interoperabilitu. Například odeslání SMS od uživatele GSM uživateli VoIP v síti IMS by bez převodu protokolů bylo nemožné. SMRSE tento převod poskytuje, čímž zajišťuje zpětnou kompatibilitu a kontinuitu služeb. Také podporuje migraci směrem k plně IP sítím tím, že umožňuje provozu SMS procházet IP páteřními sítěmi a zároveň komunikovat s tradičními síťovými prvky, čímž usnadňuje modernizaci sítě bez narušení stávajících příjmových toků z SMS a uživatelských zkušeností.

## Klíčové vlastnosti

- Převod protokolů mezi MAP a IP protokoly (např. SIP)
- Vzájemné propojení mezi doménami s přepojováním okruhů a paketovými doménami
- Směrování zpráv a překlad adres přes hranice sítí
- Podpora zřetězených SMS a doručovacích zpráv
- Zpracování chyb a mechanismy opakování pro spolehlivé doručení
- Integrace s bránami pro zasílání zpráv, jako je IP-SM-GW

## Související pojmy

- [SMS – Short Message Service](/mobilnisite/slovnik/sms/)
- [IP-SM-GW – IP Short Message Gateway](/mobilnisite/slovnik/ip-sm-gw/)
- [MAP – Mobile Application Protocol](/mobilnisite/slovnik/map/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [SMS-GMSC – Short Message Service Gateway MSC](/mobilnisite/slovnik/sms-gmsc/)

## Definující specifikace

- **TS 23.078** (Rel-19) — CAMEL Phase 4 Stage 2 Specification

---

📖 **Anglický originál a plná specifikace:** [SMRSE na 3GPP Explorer](https://3gpp-explorer.com/glossary/smrse/)
