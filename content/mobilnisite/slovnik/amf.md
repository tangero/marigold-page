---
slug: "amf"
url: "/mobilnisite/slovnik/amf/"
type: "slovnik"
title: "AMF – Access and Mobility Management Function"
date: 2026-01-01
abbr: "AMF"
fullName: "Access and Mobility Management Function"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/amf/"
infografika: "/assets/slovnik/amf.svg"
summary: "AMF je funkce jádra sítě v 5G, která zpracovává registraci, připojení, dosažitelnost a správu mobility uživatelského zařízení. Působí jako primární koncový bod signalizace NAS a je oddělena od správy"
---

AMF je funkce jádra sítě v 5G, která zpracovává registraci, připojení, dosažitelnost a správu mobility uživatelského zařízení a je primárním koncovým bodem signalizace NAS.

## Popis

Access and Mobility Management Function (AMF) je základní síťová funkce ([NF](/mobilnisite/slovnik/nf/)) řídicí roviny v architektuře 5G Core (5GC), definovaná 3GPP od verze 15. Slouží jako primární koncový bod signalizace Non-Access Stratum ([NAS](/mobilnisite/slovnik/nas/)), což je protokolová vrstva mezi uživatelským zařízením (UE) a jádrem sítě, nezávislá na podkladové technologii rádiového přístupu (např. NG-RAN, non-3GPP přístup). AMF je zodpovědná za soubor procedur souvisejících s přístupem a mobilitou UE, včetně počáteční registrace, správy připojení (navázání a uvolnění signalizačního spojení), správy dosažitelnosti (včetně mobility v režimu nečinnosti a pagingu) a správy mobility (aktualizace sledovací oblasti, předávání). Autentizuje UE a autorizuje její přístup k síti, přičemž funguje jako bezpečnostní kotva interakcí s Authentication Server Function ([AUSF](/mobilnisite/slovnik/ausf/)) a Security Anchor Function ([SEAF](/mobilnisite/slovnik/seaf/)). Klíčovým architektonickým principem v 5G je oddělení funkcí řídicí roviny pro přístup/mobilitu (AMF) a správu relací ([SMF](/mobilnisite/slovnik/smf/)). Toto oddělení umožňuje vybrat AMF na základě polohy UE a požadavků na mobilitu, zatímco jiný SMF lze vybrat podle požadavků služby datové relace, což umožňuje větší flexibilitu, škálovatelnost a podporu síťového řezání.

Z procedurálního hlediska, když UE zahájí registraci v 5G síti, rádiová přístupová síť (RAN) směruje počáteční zprávu NAS k instanci AMF. AMF následně řídí proces autentizace UE. Po úspěšné autentizaci a registraci AMF udržuje kontext UE, který zahrnuje její identitu ([SUPI](/mobilnisite/slovnik/supi/)/[SUCI](/mobilnisite/slovnik/suci/)), stav registrace, přidělený dočasný identifikátor ([5G-GUTI](/mobilnisite/slovnik/5g-guti/)), bezpečnostní kontext a obsluhující SMF pro její aktivní Protocol Data Unit (PDU) relace. Pro mobilitu AMF spravuje mobilitu UE v rámci 5G systému, zpracovává procedury jako předávání (s asistencí dalších funkcí) a aktualizace sledovací oblasti. Hraje také ústřední roli v síťovém řezání tím, že je součástí procesu výběru řezu, a zajišťuje, že UE je obsluhována příslušnou instancí síťového řezu na základě jejího předplatného a požadované služby.

AMF rozhraní s mnoha dalšími 5GC NF. Její klíčová rozhraní zahrnují N1 (k UE přes RAN), N2 (k NG-RAN pro signalizaci řídicí roviny) a N11 (k SMF). Komunikuje také s AUSF (N12), Unified Data Management (UDM) (N8), Network Slice Selection Function (NSSF) (N22) a Network Exposure Function (NEF) (N29) a dalšími. Tato síť rozhraní umožňuje AMF působit jako centrální uzel, který koordinuje mezi UE, RAN a dalšími funkcemi jádra sítě pro správu životního cyklu přístupu UE. Její princip bezstavového návrhu, kde lze kontext UE ukládat externě v Unified Data Repository (UDR), zvyšuje spolehlivost a umožňuje efektivní vyvažování zátěže a redundanci napříč více instancemi AMF.

## K čemu slouží

AMF byla vytvořena jako součást Service-Based Architecture (SBA) 5G Core, aby řešila omezení předchozích architektur jádra sítě, konkrétně 4G Evolved Packet Core (EPC). V EPC kombinovala Mobility Management Entity (MME) signalizaci pro přístup, mobilitu a správu relací. Tento monolitický design omezoval flexibilitu, ztěžoval efektivní škálování síťových funkcí a bránil nasazení různorodých služeb s odlišnými požadavky na sdílené infrastruktuře. Primárním účelem AMF je oddělit správu přístupu a mobility od správy relací, což je oddělení zásadní pro cíle 5G v oblasti síťové flexibility, služebního návrhu a podpory síťového řezání.

Izolací správy stavu mobility a připojení v AMF může 5GC nezávisle škálovat AMF a SMF na základě různých síťových zátěží (např. obrovský počet nečinných IoT zařízení versus relace s vysokou šířkou pásma). Toto oddělení přímo umožňuje efektivní síťové řezání, protože různé řezy mohou sdílet společný fond AMF pro základní konektivitu a zároveň využívat vyhrazené instance SMF přizpůsobené specifickým výkonnostním charakteristikám řezu (např. ultra-nízká latence, masivní IoT). Dále, návrh AMF jako bezstavové funkce (s kontextem uloženým externě) zlepšuje odolnost sítě, zjednodušuje obnovu po havárii a umožňuje agilnější vyvažování zátěže ve srovnání se stavovou MME. Její vytvoření bylo motivováno potřebou jádra sítě, které by mohlo podporovat mnohem širší škálu případů užití – od vylepšeného mobilního širokopásmového připojení až po komunikace s kritickým nasazením a masivní IoT – s požadovanou agilitou, škálovatelností a efektivitou, které architektura předchozí generace nemohla poskytnout.

## Klíčové vlastnosti

- Koncový bod pro signalizaci NAS od UE (rozhraní N1)
- Spravuje procedury registrace, připojení a správy mobility UE
- Řídí autentizaci UE a působí jako bezpečnostní kotva
- Oddělena od správy relací (SMF) pro nezávislé škálování a flexibilitu
- Ústřední role ve výběru síťového řezu pro UE
- Princip bezstavového návrhu s externím ukládáním kontextu pro odolnost

## Související pojmy

- [SMF – Service Management Function](/mobilnisite/slovnik/smf/)
- [AUSF – Authentication Server Function](/mobilnisite/slovnik/ausf/)
- [UDM – Unified Data Management](/mobilnisite/slovnik/udm/)
- [NAS – Non-Access Stratum](/mobilnisite/slovnik/nas/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.822** (Rel-16) — Satellite Access in 5G Study
- **TS 23.003** (Rel-19) — Numbering, addressing and identification in 3GPP
- **TS 23.222** (Rel-19) — Common API Framework for 3GPP Northbound APIs
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 23.527** (Rel-19) — 5G System Restoration Procedures
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TR 23.758** (Rel-17) — Study on Edge Application Architecture
- **TR 23.958** (Rel-19) — EDGEAPP alignment with ETSI MEC and GSMA OP
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 24.502** (Rel-19) — 5G Core Access via Non-3GPP Networks; Stage 3
- **TS 24.571** (Rel-19) — Control Plane LCS Procedures
- **TS 24.890** (Rel-16) — 5G NAS Protocol for 5GS Stage 3
- **TS 26.501** (Rel-19) — 5G Media Streaming (5GMS) Architecture
- **TS 26.804** (Rel-19) — 5G Media Streaming Extensions Study
- … a dalších 86 specifikací

---

📖 **Anglický originál a plná specifikace:** [AMF na 3GPP Explorer](https://3gpp-explorer.com/glossary/amf/)
