---
slug: "rfid"
url: "/mobilnisite/slovnik/rfid/"
type: "slovnik"
title: "RFID – Radio-Frequency Identification"
date: 2026-01-01
abbr: "RFID"
fullName: "Radio-Frequency Identification"
category: "IoT"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/rfid/"
summary: "Bezdrátová technologie využívající elektromagnetická pole k automatické identifikaci a sledování štítků připevněných k objektům. Ve specifikaci 3GPP Rel-18 je integrována do systému 5G, aby umožnila v"
---

RFID je bezdrátová technologie využívající elektromagnetická pole k automatické identifikaci a sledování štítků připevněných k objektům, která je integrována do systémů 5G pro vylepšené sledování majetku a aplikace IoT.

## Popis

Radio-Frequency Identification (RFID) je metoda automatické identifikace a sběru dat (AIDC), při níž jsou digitálně zakódovaná data uložená v RFID štítcích snímána čtečkou pomocí rádiových vln. Základní RFID systém se skládá ze tří komponent: RFID štítku (nebo transpondéru), který obsahuje mikročip a anténu; RFID čtečky (nebo interrogátoru) s anténou; a backendové databáze nebo systému pro zpracování dat. Štítky mohou být pasivní (napájené elektromagnetickým polem čtečky), aktivní (s vlastní baterií) nebo polopasivní (baterií asistované). V kontextu standardů 3GPP, počínaje Release 18, je pozornost zaměřena na integraci RFID systémů se síťovým jádrem 5G (5G Core) a rádiovou přístupovou sítí (RAN) za účelem vytvoření škálovatelných IoT řešení pro rozsáhlé oblasti.

Architektura 3GPP pro integraci RFID zahrnuje definici toho, jak může být funkce RFID čtečky hostována v rámci ekosystému 5G. To může znamenat vestavění schopností čtečky do uživatelského zařízení (UE), stanice gNodeB (gNB) nebo vyhrazeného síťového uzlu. RFID čtečka komunikuje s blízkými štítky pomocí specifických rádiových rozhraní (např. založených na standardech [ISO](/mobilnisite/slovnik/iso/)/[IEC](/mobilnisite/slovnik/iec/) nebo EPCglobal) v nelicencovaných kmitočtových pásmech. Identita a senzorová data získaná ze štítků jsou následně hlášena do síťového jádra 5G prostřednictvím standardních protokolů 3GPP. Síťové jádro, konkrétně funkce Network Exposure Function ([NEF](/mobilnisite/slovnik/nef/)) a Application Functions ([AF](/mobilnisite/slovnik/af/)), může tato data odvozená z RFID zpřístupnit autorizovaným aplikacím třetích stran pro sledování majetku, správu zásob nebo automatizaci dodavatelského řetězce.

Klíčové technické specifikace, jako TS 38.191, 38.769 a 38.848, definují rádiové požadavky a aspekty výkonu pro zařízení obsahující RFID funkcionalitu. To zahrnuje mechanismy koexistence s operacemi 5G NR, zejména když RFID čtečky pracují v blízkosti 5G transceiverů. Specifikace řeší potenciální scénáře rušení a definují minimální výkonnostní kritéria, aby bylo zajištěno, že přidání schopnosti čtení RFID nezhorší primární komunikační funkce 5G zařízení. TS 23.700 nastiňuje servisní požadavky a architektonická vylepšení potřebná v systému 5G pro podporu služeb založených na RFID, včetně nových servisních modelů a [API](/mobilnisite/slovnik/api/) pro interakci s aplikacemi.

Integrace umožňuje výkonné případy užití. Například průmyslový IoT senzor 5G (fungující jako RFID čtečka) může periodicky skenovat sklad, číst stovky pasivních štítků na paletách. Poté využije své 5G připojení k nahrání dat o zásobách v reálném čase do cloudové logistické platformy. Síť 5G poskytuje spolehlivé, nízkolatenční a zabezpečené propojení (backhaul), které tradiční samostatné RFID systémy postrádají, a umožňuje tak globální viditelnost majetku. Dále lze použít síťové segmentování (network slicing) k vytvoření vyhrazených logických sítí pro RFID provoz, čímž je zajištěna kvalita služby pro kritické aplikace sledování.

## K čemu slouží

Integrace RFID do standardů 3GPP, zahájená v Release 18, byla motivována rostoucí konvergencí operačních technologií ([OT](/mobilnisite/slovnik/ot/)) a informačních technologií ([IT](/mobilnisite/slovnik/it/)) v rámci Průmyslu 4.0 a chytré logistiky. Tradiční RFID systémy fungují jako izolované ostrůvky automatizace, vyžadující samostatnou infrastrukturu pro čtečky, brány a síťovou konektivitu. To vede k vysokým nákladům na nasazení, složitosti správy a omezené škálovatelnosti pro globální sledovací aplikace. Práce 3GPP si klade za cíl využít všudypřítomné pokrytí, zabezpečení a rámce pro správu sítí 5G ke zjednodušení a posílení nasazení RFID.

Před integrací v 3GPP se podniková RFID řešení často spoléhala na krátkodosahové technologie (jako Bluetooth nebo proprietární protokoly) pro připojení čteček k lokální bráně, která poté používala kabelový Ethernet nebo Wi-Fi pro propojení (backhaul). Tento přístup měl omezení v mobilitě, pokrytí v náročných průmyslových prostředích a v zabezpečení od konce ke konci. Definováním standardů pro 5G-integrované RFID tyto mezery 3GPP řeší. Umožňuje, aby RFID čtečky byly inherentně mobilní (např. na dronech nebo vysokozdvižných vozících) s plynulým předáváním mezi buňkami (handover), poskytuje vestavěnou autentizaci účastníka a šifrování dat prostřednictvím bezpečnostních mechanismů 5G a umožňuje centralizované zřizování a řízení politik prostřednictvím síťového jádra 5G (5G Core).

Vytvoření této pracovní položky bylo hnací silou poptávky vertikálních odvětví, zejména z logistiky, výroby a maloobchodu, která hledala jednotné konektivní řešení pro IoT masového měřítka. Řeší problém vytvoření standardizované, provozovatelské platformy (carrier-grade) pro inteligenci majetku. Tím, že se z RFID stane nativní služba v rámci architektury 5G, snižuje se celková cena vlastnictví, urychluje se nasazení a otevírají se nové zdroje příjmů pro mobilní síťové operátory na trhu podnikového IoT.

## Klíčové vlastnosti

- Integrace funkce RFID čtečky do architektury systému 5G
- Podpora komunikace s pasivními, aktivními a polopasivními RFID štítky
- Standardizované zpřístupnění RFID dat aplikacím prostřednictvím funkce Network Exposure Function (NEF) síťového jádra 5G
- Definované požadavky na rádiový výkon a koexistenci pro kombinovaná zařízení 5G/RFID
- Umožňuje sledování a správu majetku v široké geografické oblasti s podporou mobility
- Využívá zabezpečení, mobility a síťového segmentování (network slicing) 5G pro RFID služby

## Definující specifikace

- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 38.191** (Rel-19) — NR Ambient IoT RF Characteristics
- **TS 38.769** (Rel-20) — Ambient IoT Solutions in NR
- **TR 38.848** (Rel-18) — Technical Report on Ambient IoT

---

📖 **Anglický originál a plná specifikace:** [RFID na 3GPP Explorer](https://3gpp-explorer.com/glossary/rfid/)
