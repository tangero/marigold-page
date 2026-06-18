---
slug: "qfi"
url: "/mobilnisite/slovnik/qfi/"
type: "slovnik"
title: "QFI – QoS Flow Identifier"
date: 2026-01-01
abbr: "QFI"
fullName: "QoS Flow Identifier"
category: "QoS"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/qfi/"
summary: "Identifikátor toku QoS (QFI) je skalární hodnota používaná v systému 5G k jednoznačné identifikaci toku QoS v rámci PDU (Protocol Data Unit) relace. Je to základní konstrukt pro jemně odstupňovanou di"
---

QFI je skalární identifikátor, který jednoznačně označuje tok QoS (Quality of Service) v rámci PDU (Protocol Data Unit) relace 5G, aby umožnil jemně odstupňované zacházení s kvalitou služeb při přeposílání paketů.

## Popis

Identifikátor toku QoS (QFI) je 6bitové pole (hodnoty 0–63), které slouží jako hlavní nástroj pro správu QoS v uživatelské rovině 5G. Podrobně definovaný v dokumentech 3GPP TS 23.501 (systémová architektura) a TS 38.415 (protokol [NG](/mobilnisite/slovnik/ng/) uživatelské roviny) představuje tok QoS nejjemnější úroveň diferenciace QoS v rámci [PDU](/mobilnisite/slovnik/pdu/) relace 5G. Každý tok QoS je charakterizován souborem parametrů QoS, jako je identifikátor QoS 5G ([5QI](/mobilnisite/slovnik/5qi/)), priorita přidělení a udržení ([ARP](/mobilnisite/slovnik/arp/)), garantovaný bitový tok toku (GFBR) a maximální bitový tok toku ([MFBR](/mobilnisite/slovnik/mfbr/)). QFI jednoznačně označuje všechny pakety patřící do konkrétního toku QoS mezi funkcí uživatelské roviny ([UPF](/mobilnisite/slovnik/upf/)) a základnovou stanicí gNodeB (gNB).

Z architektonického hlediska je QFI přidělen funkcí správy relací ([SMF](/mobilnisite/slovnik/smf/)) během zřizování nebo modifikace toku QoS. SMF určuje potřebu nového toku QoS na základě požadavků zásad od funkce řízení politik ([PCF](/mobilnisite/slovnik/pcf/)) nebo aplikační funkce, nebo od uživatelského zařízení (UE) prostřednictvím pravidel QoS. Po přidělení je QFI sdělen gNB a UPF. V datové rovině je QFI zapouzdřeno v hlavičce protokolu GTP-U (General Packet Radio Service Tunneling Protocol for the user plane) na rozhraních N3 (gNB-UPF) a N9 (mezi UPF), konkrétně v rozšiřující hlavičce kontejneru PDU relace. To umožňuje každému mezilehlému uzlu identifikovat tok bez nutnosti hluboké kontroly paketů.

Jak to funguje, zahrnuje konzistentní mapování v celé datové cestě. Když UPF přijímá uplink data, klasifikuje pakety do toku QoS na základě pravidel detekce paketů (PDR), označí je odpovídajícím QFI v hlavičce GTP-U a přepošle je gNB. gNB používá QFI k mapování paketů na příslušný datový rádiový přenos (DRB) pro přenos vzduchem, přičemž aplikuje odpovídající profil QoS (plánování, konfigurace linkové vrstvy). V downlinku může gNB také označit QFI na základě pravidel QoS od UE. Toto end-to-end označování zajišťuje, že zacházení s QoS je konzistentní napříč segmenty rádiové a jádrové sítě, což umožňuje funkce jako reflexivní QoS a efektivní podporu síťového řezání.

## K čemu slouží

Identifikátor toku QoS (QFI) byl představen ve verzi 3GPP Release 15 jako základní kámen nového modelu QoS pro 5G, navržený k překonání omezení modelu přenašeče 4G Evolved Packet System (EPS). V LTE byla QoS vázána na přenašeče EPS, což byly relativně statické konstrukty spojující identifikátor třídy QoS (QCI) s konkrétním tunelem (GTP TEID). Tento model byl neefektivní pro relace vyžadující více souběžných služeb s dynamickými požadavky na QoS, protože každý nový požadavek na QoS často vyžadoval nový přenašeč, což zvyšovalo signalizační režii a složitost rádiových zdrojů.

QFI to řeší oddělením logiky QoS od transportního tunelu. Jedna PDU relace (obdoba přenašeče EPS) může podporovat více toků QoS, z nichž každý je identifikován QFI a má nezávislé charakteristiky QoS. To umožňuje dynamické přidávání, modifikaci nebo odebírání toků QoS v rámci existující relace s minimální signalizací. Primárním motivem byla podpora rozmanité palety služeb 5G – od masivního IoT po kritické komunikace – kde jedno zařízení (např. autonomní vozidlo) může současně provozovat navigaci, přenos senzorových dat a infotainment aplikace, z nichž každá má zcela odlišné požadavky na latenci, spolehlivost a šířku pásma.

Dále QFI umožňuje flexibilnější síťové řezání. Různé řezy mohou používat různá mapování mezi QFI a rádiovými zdroji. Také usnadňuje edge computing a scénáře místního průniku tím, že poskytuje jasný identifikátor QoS, kterému rozumí jak jádrová, tak přístupová síť. Tím, že jde o malé pole v hlavičce přenášené v pásmu, umožňuje QFI efektivní a škálovatelné zpracování paketů ve vysokorychlostních funkcích uživatelské roviny, což je klíčové pro dosažení výkonnostních cílů 5G. Představuje posun k pružnější, službami řízené architektuře QoS.

## Klíčové vlastnosti

- 6bitový identifikátor jednoznačně označující tok QoS v rámci PDU relace
- Přenášený v rozšiřující hlavičce GTP-U na rozhraních N3/N9 pro identifikaci v pásmu
- Umožňuje více toků QoS s odlišnými profily v rámci jedné PDU relace
- Používaný gNB k mapování toků QoS na příslušné datové rádiové přenosy (DRB)
- Přidělený SMF a může být dynamicky změněn během relace
- Základní pro reflexivní QoS, kde UE může odvodit pravidla QoS pro uplink z downlink QFI

## Související pojmy

- [5QI – 5G QoS Identifier](/mobilnisite/slovnik/5qi/)
- [DRB – Data Radio Bearer](/mobilnisite/slovnik/drb/)
- [GTP-U – GPRS Tunnelling Protocol for User Plane](/mobilnisite/slovnik/gtp-u/)
- [SMF – Service Management Function](/mobilnisite/slovnik/smf/)

## Definující specifikace

- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 24.193** (Rel-19) — ATSSS Procedures Specification
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 24.502** (Rel-19) — 5G Core Access via Non-3GPP Networks; Stage 3
- **TS 24.890** (Rel-16) — 5G NAS Protocol for 5GS Stage 3
- **TS 26.510** (Rel-19) — Media Delivery APIs for 5GMS and RTC Systems
- **TS 26.804** (Rel-19) — 5G Media Streaming Extensions Study
- **TR 26.806** (Rel-18) — Technical Report on Smartly Tethering AR Glasses
- **TS 26.891** (Rel-16) — Media Distribution Services in 5G System
- **TR 26.926** (Rel-19) — Traffic Models & Quality Evaluation for Media/XR in 5G
- **TR 26.928** (Rel-19) — Study on eXtended Reality (XR) in 5G
- **TS 29.503** (Rel-19) — UDM Service Based Interface Stage 3
- **TS 29.508** (Rel-19) — 5G Session Management Event Exposure Service
- **TS 29.513** (Rel-19) — 5G PCC Signalling Flows & QoS Mapping
- **TS 29.890** (Rel-16) — CT3 5G System Technical Report
- … a dalších 6 specifikací

---

📖 **Anglický originál a plná specifikace:** [QFI na 3GPP Explorer](https://3gpp-explorer.com/glossary/qfi/)
