---
slug: "in"
url: "/mobilnisite/slovnik/in/"
type: "slovnik"
title: "IN – Intelligent Network"
date: 2026-01-01
abbr: "IN"
fullName: "Intelligent Network"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/in/"
summary: "Standardizovaná architektura, která odděluje servisní logiku od přepojovacích funkcí, umožňující rychlé vytváření a nasazování pokročilých telekomunikačních služeb, jako je bezplatné volání, předplace"
---

IN je standardizovaná síťová architektura, která odděluje servisní logiku od přepojovacích funkcí, aby umožnila rychlé vytváření a nasazování pokročilých telekomunikačních služeb.

## Popis

Intelligent Network (IN) je architektura pro služby definovaná 3GPP, vycházející z předchozích standardů [ITU-T](/mobilnisite/slovnik/itu-t/), která zavádí základní oddělení mezi základní přepojovací/servisní funkce a pokročilou servisní logiku. Toto oddělení je realizováno pomocí distribuované síťové architektury, kde řízení služeb je centralizované na specializovaných síťových uzlech, zatímco přepojování hovorů zůstává v tradičních přepojovacích uzlech. Základním principem je použití standardizovaných triggerů, známých jako Detection Points (DPs), které jsou integrovány v Basic Call State Model ([BCSM](/mobilnisite/slovnik/bcsm/)) přepojovače nebo funkce řízení hovoru. Pokud událost hovoru odpovídá nastavenému triggeru, přepojovač pozastaví zpracování hovoru a vysílá dotaz, prostřednictvím standardizovaného protokolu, na externí entitu obsahující servisní logiku.

Klíčové architektonické komponenty IN zahrnují Service Switching Point ([SSP](/mobilnisite/slovnik/ssp/)), což je přepojovací uzel (například [MSC](/mobilnisite/slovnik/msc/) nebo [GMSC](/mobilnisite/slovnik/gmsc/)) vybavený IN schopnostmi; Service Control Point ([SCP](/mobilnisite/slovnik/scp/)), což je specializovaný server hostující programy servisní logiky (SLPs) a databáze; a Service Data Point ([SDP](/mobilnisite/slovnik/sdp/)), který uchovává data související s uživateli a službami. Komunikace mezi SSP a SCP je standardizována, primárně pomocí Intelligent Network Application Protocol ([INAP](/mobilnisite/slovnik/inap/)). Servisní logika na SCP zpracuje dotaz, provede službu (například převod čísla, kontrolu kreditu) a vrátí instrukce (například spojit, zahrnout oznámení, sbírat číslice) SSP, aby mohlo pokračovat a dokončit hovor.

Role IN v síti je poskytovat nezávislé na dodavatelích, flexibilní platformu pro služby s přidanou hodnotou. Umožňuje síťovým operátorům centralizovaně nasazovat a řídit služby, snižuje čas uvedení na trh a provozní náklady. Architektura podporuje služby jako Customized Applications for Mobile network Enhanced Logic (CAMEL) pro mobilní síť, která rozšiřuje principy IN pro poskytování služeb specifických pro operátora, jako předplacené služby, služby na základě polohy nebo filtrování hovorů, přes různé síťové domény a i během roamingu. IN tvoří základní koncept pro následné platformy pro poskytování služeb a oddělení řídicí a uživatelské roviny, které je vidět v moderních sítích.

## K čemu slouží

Intelligent Network byl vytvořen, aby řešil kritický problém pomalé a nákladné inovace služeb v tradičních telefonních sítích. Historicky byly nové telekomunikační služby pevně integrovány do proprietárního software přepojovačů okruhů od dodavatelů jako Ericsson, Nokia nebo Siemens. Pro zavést službu jako bezplatné volání (800-číslo) nebo televoting museli operátorů žádat dodavatelsky specifické softwarové aktualizace pro každý přepojovač, což byl proces časově náročný, nákladný a vedl k závislosti na dodavatelů. Toto brzdilo konkurenci a oddalovalo zavádění nových funkcí generujících příjem.

IN architektura řešila tyto omezení standardizací rozhraní mezi přepojovací funkcí a funkcí servisní logiky. Toto oddělení znamenalo, že servisní logika mohla být vyvíjena a hostována na centralizovaných, standardních výpočetních platformách (SCPs) nezávisle na dodavatelů přepojovačů. Operátorů mohli nyní rychle vytvářet a modifikovat služby aktualizací logiky a dat na centralizovaných SCPs, bez nutnosti zasahovat do každého jednotlivého přepojovače v síti. Tato změna nejen zrychlila nasazení služeb, ale také podpořila více otevřený ekosystém, kde třetí strany poskytovatelů služeb mohli potenciálně vyvíjet aplikace pro síť.

V kontextu 3GPP byly principy IN klíčové pro přenesení inteligentních služeb do GSM a následných mobilních sítí. Potřeba pokročilých, operátorem řízených služeb, které fungují bez problémů v domovských sítích a během roamingu, byla klíčovým hnacím motorem. Standard CAMEL, který je implementací IN pro mobilní síť, byl vyvinut pro poskytování služeb jako předplacený roaming, který byl komerčně klíčový, ale nemožný s tradiční logikou na přepojovačích. IN tedy poskytlo architektonický návrh pro programovatelnou, službami orientovanou základní síť, která podporuje moderní telekomunikace.

## Klíčové vlastnosti

- Oddělení řízení služeb od přepojování hovorů (Service Switching Function vs. Service Control Function)
- Standardizované triggerové mechanismy (Detection Points) v Basic Call State Model
- Centralizované provádění servisní logiky na Service Control Points (SCPs)
- Použití Intelligent Network Application Protocol (INAP) pro komunikaci
- Podpora pro nezávislé na službách building blocks (SIBs) pro vytváření služeb
- Umožňuje rychlé nasazení služeb s přidanou hodnotou jako Number Translation, Freephone a Prepaid

## Související pojmy

- [CAMEL – Customised Applications for Mobile network Enhanced Logic](/mobilnisite/slovnik/camel/)
- [INAP – Intelligent Network Application Protocol](/mobilnisite/slovnik/inap/)
- [SCP – Service Communication Proxy](/mobilnisite/slovnik/scp/)
- [SSP – Satellite Service Provider](/mobilnisite/slovnik/ssp/)
- [VPN – Virtual Private Network](/mobilnisite/slovnik/vpn/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.038** (Rel-19) — USIM Application Toolkit (USAT) Stage 1
- **TS 22.057** (Rel-19) — Mobile Execution Environment (MExE) Stage 1
- **TS 22.101** (Rel-20) — Service Principles for PLMNs
- **TS 22.105** (Rel-19) — Telecommunication Services Framework
- **TS 22.121** (Rel-5) — Virtual Home Environment Requirements
- **TS 23.153** (Rel-19) — Out-of-Band Transcoder Control Stage 2
- **TS 23.228** (Rel-19) — IMS Stage-2 Service Description
- **TS 23.292** (Rel-19) — IMS Centralized Services (ICS) Architecture
- **TS 23.417** (Rel-7) — IMS Core Component for NGN Architecture
- **TS 23.517** (Rel-8) — IMS Core Component for NGN Architecture
- **TS 24.524** (Rel-19) — Hosted Enterprise Services Architecture
- **TS 29.078** (Rel-19) — CAMEL Phase 4 CAP Specification
- **TS 29.278** (Rel-19) — CAMEL Application Part (CAP) for IMS Phase 4
- **TS 32.101** (Rel-19) — Management principles and high-level requirements
- … a dalších 2 specifikací

---

📖 **Anglický originál a plná specifikace:** [IN na 3GPP Explorer](https://3gpp-explorer.com/glossary/in/)
