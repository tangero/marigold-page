---
slug: "sdp"
url: "/mobilnisite/slovnik/sdp/"
type: "slovnik"
title: "SDP – Service Discovery Protocol"
date: 2025-01-01
abbr: "SDP"
fullName: "Service Discovery Protocol"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/sdp/"
summary: "Protokol Bluetooth používaný zařízeními k zjištění, jaké služby nabízejí jiná zařízení Bluetooth, a k určení charakteristik těchto dostupných služeb. Je základní součástí Bluetooth zásobníku (stack),"
---

SDP je protokol Bluetooth používaný zařízeními k zjištění, jaké služby nabízejí jiná zařízení Bluetooth, a k určení charakteristik těchto dostupných služeb.

## Popis

Service Discovery Protocol (SDP) je klíčový protokol ve specifikaci Bluetooth, definovaný v kontextu 3GPP primárně pro odkazy na interoperabilitu a testování (např. v 3GPP TS 36.579 pro testy propojení LTE-WLAN zahrnující Bluetooth). SDP poskytuje mechanismus, pomocí kterého mohou zařízení Bluetooth zjišťovat služby dostupné na jiných zařízeních Bluetooth a získávat atributy těchto služeb bez předchozí znalosti. Funguje v modelu klient-server: zařízení hledající služby funguje jako SDP klient, zatímco zařízení poskytující služby funguje jako SDP server. Každá služba je charakterizována sadou atributů uložených v databázi záznamů služeb (service record) SDP serveru. Nejzákladnějším atributem je univerzálně jedinečný identifikátor ([UUID](/mobilnisite/slovnik/uuid/)), který identifikuje třídu služby (např. sériový port, odeslání objektu, audio brána pro headset). SDP používá protokol typu požadavek-odpověď přes vyhrazený kanál L2CAP. Klient může vyhledávat služby na základě UUID třídy služby nebo procházet nespecifikovaný seznam služeb nabízených serverem. Jakmile je nalezena požadovaná služba, klient může získat její atributy, které zahrnují informace jako číslo kanálu RFCOMM nebo L2CAP Protocol Service Multiplexer ([PSM](/mobilnisite/slovnik/psm/)) potřebné k samotnému připojení a použití služby. Samotný SDP neposkytuje přístup ke službám; poskytuje pouze informace potřebné k navázání spojení pomocí příslušného protokolu (např. RFCOMM pro sériovou emulaci, L2CAP pro datové kanály). Tento návrh umožňuje dynamické prostředí, kde zařízení mohou vstupovat do pikosítě a opouštět ji, a v reálném čase inzerovat a zjišťovat dostupné schopnosti. Je nezbytný pro uživatelskou zkušenost typu 'připoj a hraj' (plug-and-play) spojenou s technologií Bluetooth.

## K čemu slouží

SDP byl vytvořen k řešení klíčové výzvy v ad-hoc bezdrátových osobních sítích ([PAN](/mobilnisite/slovnik/pan/)): jak mohou dvě zařízení Bluetooth, potenciálně od různých výrobců a s různými schopnostmi, automaticky zjistit, co spolu mohou dělat? Bez standardizovaného mechanismu zjišťování by uživatelé museli ručně konfigurovat připojení, což by vážně omezilo použitelnost a potenciál bezproblémové interoperability. Účelem SDP je umožnit toto automatické zjišťování služeb, které je základem pro cíl Bluetooth nahradit kabely. Řeší problém identifikace a popisu služeb v prostředí dynamických sítí s nízkým výkonem a krátkým dosahem. Před navázáním datového nebo hlasového spojení zařízení používají SDP k zodpovězení otázek jako 'Nabízí druhé zařízení profil hands-free?' nebo 'Může přijmout vizitku?'. To umožňuje aplikacím předkládat uživatelům smysluplné možnosti (např. 'Odeslat soubor' nebo 'Použít jako audio výstup') pouze tehdy, když je vzdálené zařízení podporuje. Jeho vytvoření bylo motivováno potřebou jednoduchého, efektivního protokolu, který by mohl běžet na zařízeních s omezenými prostředky a podporoval širokou škálu služeb plánovaných pro Bluetooth, od přenosu souborů po ovládání telefonie. Poskytnutím této vrstvy pro zjišťování služeb SDP umožnil rozšíření interoperabilních Bluetooth profilů a bohatého ekosystému připojených zařízení, který dnes vidíme.

## Klíčové vlastnosti

- Protokol klient-server pro zjišťování služeb na vzdálených zařízeních Bluetooth
- Používá UUID k jednoznačné identifikaci tříd služeb a atributů
- Funguje přes vyhrazený kanál L2CAP pro spolehlivou komunikaci
- Podporuje požadavky na vyhledávání služeb (service search) a procházení služeb (service browsing)
- Získává atributy služeb nezbytné pro navázání spojení (např. kanál RFCOMM, L2CAP PSM)
- Umožňuje dynamické ad-hoc sítě bez předchozí konfigurace

## Související pojmy

- [UUID – Universally Unique IDentifier](/mobilnisite/slovnik/uuid/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 22.977** (Rel-19) — Speech Enabled Services and Multimodal Framework
- **TS 23.140** (Rel-6) — MMS Non-Realtime Service Definition
- **TS 23.207** (Rel-19) — End-to-End QoS Framework for GPRS
- **TS 23.218** (Rel-19) — IMS Call Model Specification
- **TS 23.228** (Rel-19) — IMS Stage-2 Service Description
- **TS 23.231** (Rel-19) — SIP-I based CS core network stage 2
- **TS 23.333** (Rel-19) — MRFC-MRFP Mp Interface Requirements
- **TS 23.479** (Rel-19) — MBMS API for Mission Critical Services
- **TS 23.701** (Rel-12) — WebRTC Access to IMS Architecture Study
- **TR 23.758** (Rel-17) — Study on Edge Application Architecture
- **TS 23.792** (Rel-16) — MBMS API for Mission Critical Services
- **TS 23.802** (Rel-7) — Enhanced End-to-End QoS Architecture
- **TS 23.849** (Rel-11) — Study on IMS Roaming Media Optimization
- **TS 23.894** (Rel-10) — IMS Local Breakout & Optimal Media Routing Study
- … a dalších 95 specifikací

---

📖 **Anglický originál a plná specifikace:** [SDP na 3GPP Explorer](https://3gpp-explorer.com/glossary/sdp/)
