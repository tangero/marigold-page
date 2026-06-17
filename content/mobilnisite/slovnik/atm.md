---
slug: "atm"
url: "/mobilnisite/slovnik/atm/"
type: "slovnik"
title: "ATM – Asynchronous Transfer Mode"
date: 2025-01-01
abbr: "ATM"
fullName: "Asynchronous Transfer Mode"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/atm/"
summary: "ATM je protokol pro přepojování buněk a spojově orientované síťování používaný v raných vydáních 3GPP pro přenos v přístupové a jádrové síti. Poskytoval deterministickou kvalitu služeb (QoS) pro hlas"
---

ATM je spojově orientovaný protokol s přepojováním buněk používaný v raných mobilních sítích 3GPP k zajištění deterministické kvality služeb (Quality of Service) pro přenos pomocí buněk pevné velikosti 53 bajtů.

## Popis

Asynchronous Transfer Mode (ATM) je vysokorychlostní, spojově orientovaný protokol pro přepojování a multiplexování standardizovaný [ITU-T](/mobilnisite/slovnik/itu-t/) a přijatý 3GPP pro přenosovou infrastrukturu sítí 2,5G a 3G, zejména v éře UMTS. Na rozdíl od paketově přepínaných sítí používajících rámce proměnné délky ATM segmentuje všechna data do malých jednotek pevné velikosti 53 bajtů zvaných buňky. Každá buňka se skládá z 5bajtové hlavičky a 48bajtového užitečného zatížení. Hlavička obsahuje klíčové řídicí informace, včetně polí Virtual Path Identifier (VPI) a Virtual Channel Identifier (VCI) používaných pro směrování, Payload Type Identifier (PTI), bitu Cell Loss Priority (CLP) a Header Error Control ([HEC](/mobilnisite/slovnik/hec/)). Tato pevná struktura buňky umožňuje předvídatelnou latenci a efektivní hardwarové přepojování, což je klíčové pro služby v reálném čase, jako je hlas a video.

V architektuře 3GPP sloužil ATM jako primární transportní technologie vrstvy 2 pro jádrovou síť (CN) i rádiovou přístupovou síť (RAN). V rámci UTRAN (UMTS Terrestrial Radio Access Network) používala rozhraní Iub mezi Node B a Radio Network Controller (RNC), rozhraní Iur mezi RNC a rozhraní Iu mezi RNC a jádrovou sítí ATM jako podkladový transport. Uživatelská data a signalizace řídicí roviny (např. RANAP, [NBAP](/mobilnisite/slovnik/nbap/)) byly přenášeny přes protokoly ATM Adaptation Layer ([AAL](/mobilnisite/slovnik/aal/)). [AAL2](/mobilnisite/slovnik/aal2/) byl specificky optimalizován pro zpoždění citlivý provoz s proměnnou přenosovou rychlostí, jako je komprimovaný hlas v okruhově přepínaných hovorech, zatímco [AAL5](/mobilnisite/slovnik/aal5/) byl používán pro dávkový datový provoz a signalizační zprávy.

Protokol funguje tak, že před zahájením přenosu dat mezi koncovými body naváže virtuální okruhy (VC). Ty mohou být Permanentní virtuální okruhy (PVC), které jsou staticky konfigurovány, nebo Komutované virtuální okruhy (SVC), které jsou dynamicky nastavovány a rušeny pomocí signalizace. Spojově orientovaná povaha v kombinaci s mechanismy správy provozu a QoS definovanými ATM Forum (např. Constant Bit Rate ([CBR](/mobilnisite/slovnik/cbr/)), Variable Bit Rate (VBR), Available Bit Rate ([ABR](/mobilnisite/slovnik/abr/))) umožňovala síťovým operátorům garantovat specifické charakteristiky šířky pásma, zpoždění, chvění a ztrát. Díky tomu byl ATM výjimečně vhodný pro požadavky na více služeb v raných sítích 3G, které potřebovaly současně podporovat tradiční okruhově přepínané hlasové služby a nově vznikající paketově přepínané datové služby s přísnými požadavky na QoS.

Role ATM se rozšířila i na jádrovou síť, kde byl používán v okruhově přepínané (CS) doméně pro přenos hlasového provozu a v rané paketově přepínané (PS) doméně GPRS jako přenosová možnost pro rozhraní Gn a Gp mezi GSN (GPRS Support Nodes). Jeho integrace do 3GPP byla komplexní a pokrývala přenos v uživatelské rovině, přenos signalizace řídicí roviny a správu sítě. Jeho složitost, relativně vysoká režie kvůli hlavičce buňky (asi 9,4 %) a celkový posun odvětví směrem k 'All-IP' sítím však vedly k jeho postupnému vyřazování ve prospěch Ethernetu a IP/MPLS v pozdějších vydáních 3GPP.

## K čemu slouží

ATM byl vyvinut za účelem vytvoření jednotné, vysoce výkonné síťové technologie schopné integrovat různé typy provozu – hlas, video a data – na jedné infrastruktuře. Před ATM používaly telekomunikační sítě samostatné systémy: okruhové přepínání pro hlas (s garantovanou kvalitou, ale neefektivní pro dávkový přenos dat) a paketové přepínání jako X.25 pro data (které bylo flexibilní, ale příliš pomalé a nespolehlivé pro hlas v reálném čase). Cílem ATM bylo spojit to nejlepší z obou světů: deterministický výkon s nízkou latencí okruhového přepínání s efektivitou a flexibilitou paketového přepínání. Tato vize integrované sítě digitálních služeb (ISDN) byla klíčová pro vznikající širokopásmovou ISDN (B-ISDN) a dokonale odpovídala potřebě 3GPP po robustní přenosové páteři pro UMTS, která by zvládla smíšené profily provozu mobilních služeb.

Když 3GPP standardizovalo UMTS ve vydání 99, klíčovým požadavkem byla přenosová síť schopná poskytovat přísnou QoS pro konverzační hlasové a videohovory v reálném čase a zároveň efektivně zpracovávat interaktivní a na pozadí probíhající datové relace. ATM se svými zralými standardy, osvědčeným hardwarem a sofistikovanými možnostmi správy provozu byla přirozenou volbou. Vyřešila problém, jak vybudovat škálovatelný RAN backhaul, který by splňoval specifikace zpoždění a chvění pro komprimovaný hlas (kodek AMR) přes paketizovanou infrastrukturu. Její spojově orientovaná povaha poskytovala nezbytné řízení provozu a řízení přístupu, aby se zabránilo zahlcení sítě a zajistily smlouvy o úrovni služeb.

Zavedení ATM řešilo omezení čistě IP-based internetu, kterému v té době chyběly robustní, standardizované mechanismy QoS (IntServ/RSVP bylo složité a neširoce nasazené). ATM poskytovala řízenou, telekomunikační přenosovou vrstvu, přes kterou mohly být IP služby spolehlivě provozovány. Umožnila časnou komercializaci služeb 3G tím, že nabídla stabilní a předvídatelnou transportní technologii, kterou výrobci síťových zařízení a operátoři již znali z nasazení pevných širokopásmových sítí. Jejím účelem však bylo nakonec přechodné řešení, protože dlouhodobá vize vždy směřovala ke zjednodušené, nákladově efektivní a všudypřítomné přenosové vrstvě založené na IP.

## Klíčové vlastnosti

- Struktura buněk pevné velikosti 53 bajtů pro předvídatelnou latenci přepojování
- Spojově orientované virtuální okruhy (PVC/SVC) pro garantované přidělování zdrojů
- Komplexní třídy QoS (CBR, rt-VBR, nrt-VBR, ABR, UBR) pro správu provozu
- Segmentace a znovusestavení pomocí ATM Adaptation Layers (AAL2 pro hlas, AAL5 pro data)
- Integrovaná podpora pro přenos jak okruhově přepínaných, tak paketově přepínaných služeb
- Hardwarové přepojování umožňující vysokorychlostní přeposílání s nízkou latencí

## Související pojmy

- [AAL2 – ATM Adaptation Layer type 2](/mobilnisite/slovnik/aal2/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 23.107** (Rel-19) — UMTS QoS Framework
- **TS 23.207** (Rel-19) — End-to-End QoS Framework for GPRS
- **TS 23.221** (Rel-19) — 3GPP System Architectural Requirements
- **TR 23.910** (Rel-5) — UMTS Circuit Switched Bearer Services Overview
- **TS 25.401** (Rel-19) — UTRAN Overall Architecture
- **TS 25.410** (Rel-19) — Iu Interface Introduction for UTRAN
- **TS 25.411** (Rel-19) — Iu Interface Layer 1 Specification
- **TS 25.412** (Rel-19) — Iu Interface Signalling Transport Specification
- **TS 25.413** (Rel-19) — Radio Access Network Application Part (RANAP)
- **TS 25.414** (Rel-19) — UTRAN Iu Interface User Plane Transport Protocols
- **TS 25.420** (Rel-19) — Iur Interface Introduction for UTRAN
- **TS 25.422** (Rel-19) — Signalling Transport for Iur Interface
- **TS 25.424** (Rel-19) — UTRAN Iur Interface Data Transport & Signalling
- … a dalších 21 specifikací

---

📖 **Anglický originál a plná specifikace:** [ATM na 3GPP Explorer](https://3gpp-explorer.com/glossary/atm/)
