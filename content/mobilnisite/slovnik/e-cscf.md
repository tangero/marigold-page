---
slug: "e-cscf"
url: "/mobilnisite/slovnik/e-cscf/"
type: "slovnik"
title: "E-CSCF – Emergency – Call Session Control Function"
date: 2025-01-01
abbr: "E-CSCF"
fullName: "Emergency – Call Session Control Function"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/e-cscf/"
summary: "Funkce jádra sítě v rámci IMS, která zajišťuje zřizování a směrování nouzových relací. Je zodpovědná za určení příslušného bodu pro přijímání tísňových hovorů (PSAP) na základě polohy uživatele a poža"
---

E-CSCF je funkce jádra sítě IMS, která zajišťuje zřizování a směrování nouzových hovorových relací tím, že na základě polohy uživatele a požadavků na službu určí správné PSAP.

## Popis

Emergency – Call Session Control Function (E-CSCF) je klíčová komponenta v architektuře IP Multimedia Subsystem (IMS), speciálně navržená pro správu nouzových relací. Funguje jako specializovaný SIP proxy server. Když IMS přijme požadavek na zahájení nouzové relace (např. zprávu INVITE s nouzovou služební URN), obvykle přes Proxy-CSCF ([P-CSCF](/mobilnisite/slovnik/p-cscf/)), je tento požadavek předán E-CSCF. Primární úlohou E-CSCF je zjistit polohu volajícího, a to buď z informací vložených do signalizace SIP (např. PANI, [CAI](/mobilnisite/slovnik/cai/) nebo adresa místa), nebo dotazem na jiné síťové entity, jako je funkce pro získání polohy ([LRF](/mobilnisite/slovnik/lrf/)).

Pomocí získaných informací o poloze E-CSCF komunikuje se serverem pro překlad polohy na službu (LoST) nebo podobnou funkční entitou. Tato interakce převede zeměpisné souřadnice nebo adresu místa na uniformní identifikátor prostředku (URI) pro příslušný bod pro přijímání tísňových hovorů (PSAP). PSAP je kontaktním bodem pro tísňové služby, jako jsou policie, hasiči nebo záchranná služba. E-CSCF poté směruje požadavek na nouzovou relaci (SIP INVITE) na tento URI PSAP, čímž zajistí, že hovor dorazí ke správné místní tísňové autoritě.

E-CSCF navíc hraje zásadní roli ve scénářích, kdy by běžná registrace v IMS nebo kontroly předplatného mohly selhat. Pro nouzové relace může E-CSCF obejít určité postupy ověřování a autorizace, aby zajistil, že hovor bude zřízen i pro neregistrované uživatele nebo uživatele bez platného předplatného, v souladu s regulačními požadavky na univerzální přístup k tísňovým službám. Také koordinuje s LRF případné následné požadavky na polohu od PSAP, což usnadňuje zpětné dovolání tísňového hovoru a přesné vyslání záchranných složek.

## K čemu slouží

E-CSCF byl zaveden, aby řešil kritickou potřebu spolehlivého, na poloze založeného zpracování tísňových hovorů v IP sítích, konkrétně v rámci architektury 3GPP IMS. Tradiční mobilní sítě s přepojováním okruhů měly pro tísňové hovory zavedené mechanismy, ale migrace na plně IP jádra sítí, jako je IMS, přinesla nové výzvy. V prostředí IP není směrování inherentně vázáno na fyzickou síťovou polohu, což ztěžuje určení, které místní centrum tísňových služeb by mělo hovor přijmout.

Jeho vytvoření bylo motivováno regulačními a bezpečnostními požadavky, které nařizují, aby byly tísňové hovory směrovány na správný místní PSAP na základě aktuální polohy volajícího, bez ohledu na jeho domovskou síť nebo stav registrace. E-CSCF řeší problém převodu polohy uživatelského zařízení (která může být v mobilní síti dynamická) na směrovatelnou adresu pro příslušný koncový bod tísňové služby. Zajišťuje, že pokročilé schopnosti řízení relací IMS jsou využity pro tísňové služby, a poskytuje tak standardizovanou, robustní a budoucím vývojem odolnou architekturu pro nouzovou komunikaci v sítích LTE, 5G a následujících generací mobilních sítí.

## Klíčové vlastnosti

- Přijímá a zpracovává požadavky na zahájení nouzových relací založené na SIP v rámci IMS.
- Získává informace o poloze volajícího ze signalizace SIP nebo dotazem na funkci pro získání polohy (LRF).
- Převádí geografická data o poloze na URI pro správný bod pro přijímání tísňových hovorů (PSAP) pomocí protokolu LoST nebo podobného.
- Směruje nouzovou relaci (SIP INVITE) na určený PSAP.
- Může obejít běžné ověřování/autorizaci IMS pro neregistrované uživatele, aby zajistil univerzální přístup k tísňovým hovorům.
- Koordinuje s LRF případné požadavky na polohu od tísňových služeb po zřízení hovoru.

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [CSCF – Call Session Control Function](/mobilnisite/slovnik/cscf/)
- [P-CSCF – Proxy Call Session Control Function](/mobilnisite/slovnik/p-cscf/)
- [LRF – Location Retrieval Function](/mobilnisite/slovnik/lrf/)

## Definující specifikace

- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TS 23.517** (Rel-8) — IMS Core Component for NGN Architecture
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 28.705** (Rel-19) — IMS NRM IRP Information Service
- **TS 29.165** (Rel-19) — Inter-IMS Network to Network Interface (NNI)
- **TR 29.949** (Rel-19) — VoLTE IMS Roaming Architecture & Procedures
- **TS 32.409** (Rel-19) — IMS Performance Management Measurements
- **TS 33.127** (Rel-19) — Lawful Interception Architecture and Functions

---

📖 **Anglický originál a plná specifikace:** [E-CSCF na 3GPP Explorer](https://3gpp-explorer.com/glossary/e-cscf/)
