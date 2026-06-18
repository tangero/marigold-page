---
slug: "sms"
url: "/mobilnisite/slovnik/sms/"
type: "slovnik"
title: "SMS – Short Message Service"
date: 2026-01-01
abbr: "SMS"
fullName: "Short Message Service"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/sms/"
summary: "Globálně standardizovaná služba textových zpráv v mobilních sítích umožňující výměnu krátkých alfanumerických zpráv mezi účastníky. Jedná se o základní komunikační službu s nízkou šířkou pásma podporu"
---

SMS je globálně standardizovaná služba mobilních sítí pro výměnu krátkých alfanumerických zpráv mezi účastníky nebo od aplikací, široce používaná pro komunikaci mezi osobami, oznámení a výstrahy.

## Popis

Short Message Service (SMS) je základní telekomunikační služba definovaná 3GPP, která umožňuje přenos krátkých textových zpráv, typicky až 160 znaků na segment zprávy, mezi mobilními zařízeními nebo mezi aplikacemi a zařízeními. Funguje jako služba typu 'store-and-forward' (ulož a přepošli), což znamená, že zprávy nejsou posílány přímo od odesílatele k příjemci, ale jsou směrovány přes centrální síťový prvek nazývaný Short Message Service Centre ([SMSC](/mobilnisite/slovnik/smsc/)). SMSC zprávu uloží a přepošle ji na zařízení příjemce, když je dostupné, což zajišťuje doručení i v případě, že je příjemce dočasně nedostupný. SMS využívá signalizační kanály v mobilní síti, konkrétně [SDCCH](/mobilnisite/slovnik/sdcch/) (Standalone Dedicated Control Channel) v GSM nebo podobné řídicí kanály v pozdějších technologiích, což jí umožňuje fungovat nezávisle na hlasových nebo datových relacích, a tím je vysoce spolehlivá a efektivní.

Z architektonického hlediska se SMS účastní několik klíčových síťových komponent. Mobile Station ([MS](/mobilnisite/slovnik/ms/)) neboli User Equipment (UE) je koncový bod, který zprávy vytváří nebo přijímá. Base Station Subsystem ([BSS](/mobilnisite/slovnik/bss/)) neboli Radio Access Network (RAN) zajišťuje přenos přes rozhraní rádiové části. V jádru sítě pak Mobile Switching Centre ([MSC](/mobilnisite/slovnik/msc/)) nebo Serving [GPRS](/mobilnisite/slovnik/gprs/) Support Node ([SGSN](/mobilnisite/slovnik/sgsn/)) v sítích 2G/3G, případně Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)) v sítích 4G/5G, spravuje mobilitu a řízení relací pro doručování SMS. SMSC je centrální uzel, který zprávy ukládá, zpracovává a směruje, a komunikuje s HLR (Home Location Register) za účelem získání směrovacích informací a stavu účastníka. Pro SMS přes IP v pozdějších vydáních jsou zaváděny prvky jako IP-SM-GW (IP Short Message Gateway) pro rozhraní s IMS. Služba podporuje různé typy zpráv včetně mobile-originated (MO), mobile-terminated (MT) a zpráv typu cell broadcast pro výstrahy v celé oblasti.

SMS funguje prostřednictvím řady signalizačních procedur. Pro zprávu mobile-originated SMS odešle UE zprávu přes přístupovou síť do MSC/MME. MSC/MME ji přepošle do SMSC pomocí signalizace MAP (Mobile Application Part) v legacy sítích nebo Diameter/SIP v IP systémech. SMSC se dotazuje HLR, aby zjistil aktuální obsluhující uzel příjemce, a poté zprávu doručí do tohoto uzlu, který ji předá do UE. Zpět jsou odesílány doručovací zprávy pro potvrzení úspěchu. SMS také podporuje spojování pro delší zprávy (rozdělené na více segmentů), kompresi a kódovací schémata jako GSM 7-bitovou abecedu nebo UCS-2 pro Unicode. Její integrace do řídicí roviny sítě zajišťuje nízkou latenci a vysokou dostupnost, což z ní činí kritickou službu pro dvoufaktorovou autentizaci, nouzová upozornění a komunikaci mezi stroji (M2M).

## K čemu slouží

SMS byla vytvořena, aby poskytla jednoduchou a efektivní textovou komunikační metodu pro mobilní uživatele, využívající nevyužitou kapacitu signalizačních kanálů řídicí roviny v GSM sítích. Zavedena v raných GSM standardech (před 3GPP, později formalizována v R99), řešila potřebu nízkonákladové asynchronní zprávové služby, která mohla fungovat souběžně s hovory bez nutnosti vyhrazených datových připojení. Zpočátku umožňovala zasílání textových zpráv mezi osobami, což se rychle stalo populárním díky pohodlí a cenové dostupnosti ve srovnání s hlasovými hovory.

V průběhu času se SMS vyvinula, aby řešila širší komunikační výzvy. Poskytla spolehlivý kanál pro služební oznámení, jako jsou upozornění na hlasovou schránku a informace o roamingu, a později pro služby application-to-person (A2P), jako jsou bankovní upozornění a marketingové zprávy. Mechanismus 'store-and-forward' vyřešil problém nedostupnosti příjemce a zajistil doručení zprávy i při vypnutém zařízení. S pokrokem sítí na 3G, 4G a 5G zůstala SMS nezbytná díky své univerzálnosti a interoperabilitě mezi různými operátory a technologiemi, přičemž podporovala migraci na plně IP jádra prostřednictvím vylepšení jako SMS přes IMS. Její robustnost a globální dosah z ní učinily základní službu pro kritickou komunikaci, včetně nouzových výstrah a dvoufaktorové autentizace, navzdory vzestupu OTT zprávových aplikací.

## Klíčové vlastnosti

- Doručování typu 'store-and-forward' přes SMSC pro spolehlivost
- Využívá signalizační kanály řídicí roviny, nezávisle na hlasových/datových přenosech
- Podporuje až 160 znaků na segment s možností spojování pro delší zprávy
- Globální interoperabilita napříč mobilními sítěmi a technologiemi
- Doručovací zprávy a oznámení o stavu
- Podpora zasílání zpráv mezi osobami, od aplikací k osobě a zpráv typu cell broadcast

## Související pojmy

- [SMS-C – Short Message Service - Center](/mobilnisite/slovnik/sms-c/)
- [SMSC – Short Message Service Centre](/mobilnisite/slovnik/smsc/)
- [IP-SM-GW – IP Short Message Gateway](/mobilnisite/slovnik/ip-sm-gw/)
- [MAP – Mobile Application Protocol](/mobilnisite/slovnik/map/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.022** (Rel-19) — ME Personalisation Features for GSM/3G
- **TS 22.101** (Rel-20) — Service Principles for PLMNs
- **TS 22.105** (Rel-19) — Telecommunication Services Framework
- **TS 22.112** (Rel-8) — USAT Gateway System Specification
- **TS 22.121** (Rel-5) — Virtual Home Environment Requirements
- **TS 22.140** (Rel-19) — MMS Stage 1 Requirements
- **TS 22.242** (Rel-19) — DRM Service Requirements
- **TS 22.401** (Rel-8) — Videotelephony Service Requirements for NGN
- **TS 22.811** (Rel-7) — Network Selection Mechanisms Overview
- **TR 22.940** (Rel-19) — IMS Messaging Requirements Analysis
- **TR 22.942** (Rel-19) — SMS Value-Added Services Requirements
- **TR 22.945** (Rel-4) — Fax Services Guidance for GSM/UMTS
- **TR 22.949** (Rel-19) — Privacy Requirements Study for 3GPP Services
- **TS 23.039** (Rel-5) — SMSC to SME Interface Protocols
- … a dalších 60 specifikací

---

📖 **Anglický originál a plná specifikace:** [SMS na 3GPP Explorer](https://3gpp-explorer.com/glossary/sms/)
