---
slug: "msu"
url: "/mobilnisite/slovnik/msu/"
type: "slovnik"
title: "MSU – Message Signalling Unit"
date: 2025-01-01
abbr: "MSU"
fullName: "Message Signalling Unit"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/msu/"
summary: "MSU je základní datová jednotka v systému SS7 (Signalling System No. 7) a jeho adaptacích pro mobilní sítě (jako MAP). Přenáší signalizační informace mezi síťovými uzly pro řízení hovorů, správu mobil"
---

MSU je základní datová jednotka signalizace SS7, která přenáší informace pro řízení hovorů, správu mobility a služeb mezi síťovými uzly v legacy systémech 3GPP a při propojování s nimi.

## Popis

Message Signalling Unit (MSU) je primární paketová struktura používaná k přenosu signalizačních zpráv v rámci sady protokolů SS7 (Signalling System No. 7), která tvoří páteř tradiční telekomunikační signalizace. Ve specifikacích 3GPP, zejména těch zabývajících se propojením s legacy jádrovými sítěmi (např. TS 29.163 o propojení SIP a [ISUP](/mobilnisite/slovnik/isup/)) a účtováním (např. TS 32.407), je MSU klíčovým konceptem. MSU se skládá z několika odlišných polí: sekvence Flag pro ohraničení, Checksum pro detekci chyb, ukazatele délky (Length Indicator), oktetu služebních informací (Service Information Octet, SIO) a jádrového pole signalizačních informací (Signalling Information Field, SIF), které obsahuje skutečnou protokolovou zprávu, například zprávu ISUP ([ISDN](/mobilnisite/slovnik/isdn/) User Part) pro zřízení hovoru nebo zprávu [MAP](/mobilnisite/slovnik/map/) (Mobile Application Part) pro aktualizaci polohy.

Architektura signalizace SS7 zahrnuje signalizační body (Signalling Points, SPs) propojené přes signalizační linky (Signalling Links). MSU jsou přenášeny přes tyto linky pomocí přenosové části zpráv (Message Transfer Part, [MTP](/mobilnisite/slovnik/mtp/)) úrovně 2, která zajišťuje detekci a opravu chyb prostřednictvím opakovaného přenosu. MTP úroveň 3 poskytuje směrovací funkce, přičemž využívá směrovací štítek (Routing Label) uvnitř SIF k nasměrování MSU z jeho výchozího kódového bodu (Origin Point Code, OPC) do cílového kódového bodu (Destination Point Code, [DPC](/mobilnisite/slovnik/dpc/)). Oktet služebních informací (SIO) udává typ uživatelské části (např. ISUP, SCCP, TUP) obsažené uvnitř, což umožňuje přijímacímu uzlu předat datovou část správné entitě protokolu vyšší vrstvy ke zpracování.

V kontextu mobilní sítě 3GPP jsou MSU nezbytné pro všechny okruhově komutované služby v jádrech 2G (GSM) a 3G (UMTS). Přenášejí zprávy MAP mezi [MSC](/mobilnisite/slovnik/msc/), [HLR](/mobilnisite/slovnik/hlr/) a VLR pro správu mobility (např. aktualizace polohy, předávání hovorů) a získávání dat o účastnících. Také přenášejí zprávy [CAP](/mobilnisite/slovnik/cap/) (CAMEL Application Part) pro služby inteligentní sítě. I když se sítě vyvíjejí směrem k plně IP jádřům s protokoly Diameter a HTTP/2, znalost MSU zůstává klíčová pro funkce propojení (Interworking Functions, IWF), které překládají mezi legacy sítěmi založenými na SS7 a IP síťovými funkcemi (Network Functions, NFs). Spolehlivá, spojením orientovaná povaha přenosu MSU prostřednictvím MTP umožnila po desetiletí robustní globální telefonní služby.

## K čemu slouží

Message Signalling Unit existuje jako základní nosič signalizačních informací v zásobníku protokolů SS7, který byl vytvořen pro poskytování mimopásmové signalizace pro globální veřejnou telefonní síť (PSTN). Před SS7 byla signalizace často v pásmu (používala stejný kanál jako hlas), což bylo neefektivní, pomalé a náchylné k podvodům. SS7 zavedlo samostatnou, vysoce spolehlivou paketově komutovanou síť věnovanou výhradně signalizaci, přičemž MSU je její základní datovou jednotkou. Toto oddělení umožnilo rychlejší zřizování hovorů, pokročilé služby (jako přesměrování hovorů) a efektivnější využití hlasových okruhů.

V kontextu mobilních sítí 3GPP (GSM, UMTS) bylo účelem MSU adaptovat osvědčený paradigma signalizace SS7 pro potřeby specifické pro mobilní komunikaci. Řešilo problém, jak provádět komplexní správu mobility (sledování pohybujícího se účastníka), směrování hovorů na mobilní zařízení a integraci se službami inteligentní sítě pro předplacené služby nebo roaming. MSU poskytlo standardizovaný, spolehlivý kontejner pro mobilní aplikační protokoly, jako jsou MAP a CAP, což zajišťovalo interoperabilitu mezi síťovými prvky od různých výrobců napříč mezinárodními hranicemi. Jeho robustní mechanismy kontroly chyb a doručování byly klíčové pro udržení kontinuity služeb a přesnosti účtování.

Pokračující odkazování na MSU v pozdějších vydáních 3GPP (např. ve specifikacích pro propojení) zdůrazňuje potřebu propojit legacy okruhově komutované sítě s novými IP jádry. Když operátoři přecházejí na LTE a 5G, musí často udržovat konektivitu ke starším sítím 2G/3G a k PSTN. Proto je pochopení a zpracování MSU nezbytné pro funkce jako Media Gateway Control Function (MGCF), která převádí signalizaci SIP na/zprávy ISUP přenášené v rámci MSU. MSU představuje základní kámen tradiční telekomunikační techniky, s nímž se moderní architektury musí rozhranit během vývoje sítě.

## Klíčové vlastnosti

- Standardizovaná struktura s poli Flag, Checksum, Length Indicator, SIO a SIF
- Přenáší signalizační zprávy vyšších vrstev (např. ISUP, MAP, CAP) v poli signalizačních informací (Signalling Information Field, SIF)
- Používá směrovací štítek (Routing Label) (OPC, DPC) pro směrování zpráv v celé síti prostřednictvím MTP úrovně 3
- Poskytuje spolehlivé doručování ve správném pořadí prostřednictvím opravy chyb na MTP úrovni 2
- Podporuje více uživatelských částí, které jsou indikovány oktetem služebních informací (Service Information Octet, SIO)
- Základní jednotka pro globální signalizaci SS7 v okruhově komutovaných mobilních a pevných sítích

## Související pojmy

- [MTP – Message Transfer Part](/mobilnisite/slovnik/mtp/)
- [MAP – Mobile Application Protocol](/mobilnisite/slovnik/map/)
- [ISUP – MIME ISDN User Part Multi-purpose Internet Mail Extension](/mobilnisite/slovnik/isup/)

## Definující specifikace

- **TS 29.163** (Rel-19) — Interworking between 3GPP IM CN and CS networks
- **TS 32.407** (Rel-19) — PM; CN CS Domain; UMTS/GSM measurements

---

📖 **Anglický originál a plná specifikace:** [MSU na 3GPP Explorer](https://3gpp-explorer.com/glossary/msu/)
