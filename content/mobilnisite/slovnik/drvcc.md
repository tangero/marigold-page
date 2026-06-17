---
slug: "drvcc"
url: "/mobilnisite/slovnik/drvcc/"
type: "slovnik"
title: "DRVCC – Dual Radio Voice Call Continuity"
date: 2025-01-01
abbr: "DRVCC"
fullName: "Dual Radio Voice Call Continuity"
category: "Mobility"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/drvcc/"
summary: "Mechanismus pro udržení hlasového volání při přechodu uživatelského zařízení (UE) mezi sítí 3GPP (např. LTE) a ne-3GPP sítí (např. CDMA 1x). Umožňuje plynulý předání pro zařízení nepodporující kontinu"
---

DRVCC je mechanismus, který udržuje hlasové volání při přechodu zařízení mezi sítí 3GPP a ne-3GPP sítí využitím dvou rádiových rozhraní, čímž zajišťuje kontinuitu služby pro zařízení nepodporující SRVCC.

## Popis

Dual Radio Voice Call Continuity (DRVCC) je mobilní řešení standardizované v 3GPP, které zajišťuje nepřerušenou hlasovou službu při přechodu uživatelského zařízení (UE) mezi paketovou sítí (PS) 3GPP (např. LTE) a okruhově spínanou sítí ([CS](/mobilnisite/slovnik/cs/)) ne-3GPP (např. [CDMA](/mobilnisite/slovnik/cdma/) 1xRTT). Na rozdíl od Single Radio Voice Call Continuity (SRVCC), které vyžaduje, aby UE mělo jediný rádiový transceiver schopný přepínat mezi přístupovými technologiemi, je DRVCC navrženo pro UE vybavená dvěma nezávislými rádiovými transceivery. Tato architektura umožňuje, aby jedno rádio udržovalo aktivní hlasové volání v síti CS, zatímco druhé rádio spravuje PS datovou relaci v síti LTE. Proces předání je koordinován sítí, konkrétně se na něm podílí Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)) v Evolved Packet Core (EPC) a Interworking Function ([IWF](/mobilnisite/slovnik/iwf/)), která zprostředkovává spojení s legacy CS sítí.

Klíčový technický postup zahrnuje fázi přípravy předání, která je spuštěna, když UE připojené k síti LTE pro volání Voice over LTE (VoLTE) detekuje, že opouští pokrytí LTE a vstupuje do oblasti pokrytí legacy sítě CDMA. UE hlásí tato měření eNodeB, který informace předá MME. MME, na základě zjištění podpory DRVCC v UE, zahájí proceduru přenosu relace směrem k síti IMS přes rozhraní Sv k [MSC](/mobilnisite/slovnik/msc/) Serveru rozšířenému pro SRVCC (eMSC). Klíčový rozdíl u DRVCC spočívá v tom, že UE samo použije své druhé rádio k paralelnímu vytvoření nové větve CS volání přímo s cílovou sítí CDMA, zatímco PS přenos v LTE stále probíhá. Síť následně zkoordinuje přepnutí mediální cesty v jádru IMS z větve PS přístupu na nově vytvořenou větev CS přístupu, čímž se předání dokončí.

Role DRVCC byla klíčová v raných nasazeních VoLTE, zejména v regionech, kde pokrytí LTE nebylo všudypřítomné a operátoři se spoléhali na sítě CDMA 1x jako záložní řešení pro hlas. Poskytuje standardizovaný, síťově řízený mechanismus předání, který zachovává kvalitu a kontinuitu hlasového volání bez nutnosti ukončit PS datovou relaci. Řešení je definováno v řadě specifikací 3GPP pokrývajících požadavky fáze 1, architekturu fáze 2 a protokoly fáze 3 pro chování jádra sítě a UE, což zajišťuje interoperabilitu mezi zařízeními s více rádiovými rozhraními a heterogenní síťovou infrastrukturou.

## K čemu slouží

DRVCC bylo vytvořeno za účelem řešení kritického problému kontinuity hlasového volání pro zařízení s více rádiovými rozhraními v raných nasazeních 4G LTE. Když operátoři začali uvádět LTE sítě optimalizované pro vysokorychlostní data (PS), hlasová služba zpočátku spoléhala na Circuit Switched Fallback ([CSFB](/mobilnisite/slovnik/csfb/)) k legacy sítím 2G/3G nebo na pozdější nasazení VoLTE přes IMS. Avšak na trzích dominovaných technologií [CDMA](/mobilnisite/slovnik/cdma/) (která nemá nativní [CS](/mobilnisite/slovnik/cs/) jádro kompatibilní s GSM/UMTS) bylo potřeba specifické řešení pro vzájemné propojení pro UE podporující VoLTE. Primární motivací bylo umožnit plynulý uživatelský zážitek, kdy lze hlasové volání zahájené přes VoLTE předat do všudypřítomné sítě CDMA 1x, jakmile uživatel opustí pokrytí LTE, aniž by bylo volání přerušeno.

Tím se řešila významná omezení dřívějšího řešení SRVCC, které bylo navrženo pro UE s jedním rádiovým rozhraním schopným pracovat vždy pouze na jedné přístupové technologii. Mnoho raných LTE smartphonů, zejména v Severní Americe, bylo vybaveno samostatnými rádiovými moduly pro LTE a CDMA pro podporu simultánního hlasu a dat. DRVCC poskytlo standardizované síťové procedury pro využití této hardwarové konfigurace s dvěma rádiovými rozhraními pro plynulou mobilitu. Vyřešilo to obchodní a technickou výzvu zavádění služeb VoLTE bez plošně vybudované vrstvy pokrytí LTE, což operátorům umožnilo nabízet vysokokvalitní hlas přes LTE tam, kde byl dostupný, a zároveň garantovat spolehlivost prostřednictvím robustního záložního řešení v síti CDMA, čímž se urychlila adopce VoLTE.

## Klíčové vlastnosti

- Umožňuje předání VoLTE volání ze sítě E-UTRAN do legacy okruhově spínané sítě CDMA 1x.
- Navrženo pro uživatelská zařízení (UE) s dvěma nezávislými rádiovými transceivery (LTE a CDMA).
- Udržuje paketově spínanou (PS) datovou relaci v síti LTE během a po předání hlasového volání.
- Využívá rozhraní Sv mezi MME a rozšířeným MSC (eMSC) pro koordinaci předání.
- Vyžaduje kontinuitu služeb založenou na IMS s procedurami Session Transfer Number for Single Radio (STN-SR).
- Definuje specifické chování UE pro paralelní provoz rádiových rozhraní a hlášení měření přístupové vrstvy (access stratum).

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TS 23.167** (Rel-19) — IMS Emergency Sessions
- **TS 23.237** (Rel-19) — IMS Service Continuity (ISC) Stage 2
- **TS 24.008** (Rel-19) — 3GPP TS 24008: Core Network Protocols
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 29.162** (Rel-19) — IMS-IP Network Interworking
- **TS 29.165** (Rel-19) — Inter-IMS Network to Network Interface (NNI)

---

📖 **Anglický originál a plná specifikace:** [DRVCC na 3GPP Explorer](https://3gpp-explorer.com/glossary/drvcc/)
