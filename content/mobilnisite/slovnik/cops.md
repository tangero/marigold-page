---
slug: "cops"
url: "/mobilnisite/slovnik/cops/"
type: "slovnik"
title: "COPS – Common Open Policy Service"
date: 2025-01-01
abbr: "COPS"
fullName: "Common Open Policy Service"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/cops/"
summary: "COPS je klientsko-serverový protokol definovaný IETF a přijatý 3GPP pro řízení politik a správu zdrojů v mobilních sítích. Umožňuje bodům rozhodování o politikách (PDP) komunikovat rozhodnutí o politi"
---

COPS je klientsko-serverový protokol přijatý 3GPP pro řízení politik, který umožňuje bodům rozhodování o politikách komunikovat rozhodnutí k vymáhacím bodům za účelem konzistentní QoS, účtování a řízení přístupu.

## Popis

Common Open Policy Service (COPS) je protokol typu dotaz-odpověď standardizovaný [IETF](/mobilnisite/slovnik/ietf/) v RFC 2748 a RFC 3084, který 3GPP přijalo jako klíčový protokol pro rozhraní řízení politik. Funguje na modelu klient-server, kde Bod vymáhání politik (PEP) vystupuje jako klient, který žádá o rozhodnutí o politikách od serveru Bod rozhodování o politikách (PDP). Protokol používá pro spolehlivý přenos TCP a podporuje jak model outsourcingu, tak model provisioning. V modelu outsourcingu PEP deleguje rozhodování na PDP pro každou událost, zatímco v modelu provisioning PDP zasílá pravidla politik PEPu pro lokální vymáhání.

Architektura COPS v sítích 3GPP typicky zahrnuje Funkci pravidel pro politiky a účtování (PCRF) jako PDP a různé síťové elementy jako [P-GW](/mobilnisite/slovnik/p-gw/), S-GW nebo Aplikační funkci ([AF](/mobilnisite/slovnik/af/)) jako PEP. Protokol definuje několik typů zpráv: Request (REQ), Decision (DEC), Report State (RPT) a Delete Request State ([DRQ](/mobilnisite/slovnik/drq/)). Když PEP narazí na událost vyžadující rozhodnutí o politikách (jako je zřízení nové [IP-CAN](/mobilnisite/slovnik/ip-can/) session), odešle zprávu REQ obsahující kontextové informace. PDP zpracuje tento požadavek na základě pravidel politik a profilů účastníka a vrátí zprávu DEC s instrukcemi pro PEP k vymáhání.

Klíčové součásti COPS zahrnují identifikátor Client-Type, který rozlišuje různé politické klienty (např. politiku QoS versus řízení přístupu), a objekt Context, který specifikuje typ požadavku (např. konfigurace, řízení přístupu, alokace zdrojů). Protokol udržuje stavová spojení mezi PEP a PDP, což umožňuje PDP sledovat stav každého PEP klienta a zasílat aktualizace politik při změně podmínek. Tato stavová povaha umožňuje efektivní synchronizaci a snižuje režii zpráv ve srovnání s bezstavovými protokoly.

V implementacích 3GPP se COPS primárně používá pro rozhraní Gq mezi PCRF a Aplikační funkcí (AF) v sítích IMS a pro rozhraní Gx mezi PCRF a PCEF v architektuře PCC. Protokol podporuje rozšiřitelnost prostřednictvím objektů specifických pro dodavatele (VSO), což umožňuje operátorům implementovat vlastní rozšíření politik. COPS také zahrnuje mechanismy pro zpracování chyb, keep-alive zprávy (KA) a synchronizaci mezi PEP a PDP, aby zajistil konzistentní vymáhání politik i po selhání spojení.

Návrh protokolu klade důraz na škálovatelnost a spolehlivost prostřednictvím svého spojením orientovaného přístupu a podpory více domén politik. Každé spojení COPS může současně obsluhovat více politických kontextů, což snižuje potřebu více TCP spojení mezi stejným PEP a PDP. PDP může dynamicky instalovat, aktualizovat nebo odstraňovat rozhodnutí politik na základě měnících se síťových podmínek, stavu účastníka nebo externích podnětů z aplikací, což umožňuje adaptaci politik v reálném čase v mobilních sítích.

## K čemu slouží

COPS byl vytvořen, aby řešil potřebu standardizovaného, interoperabilního protokolu pro řízení politik v IP sítích, což se stalo klíčovým s vývojem sítí 3GPP směrem k plně IP architekturám. Před COPS byly mechanismy řízení politik často proprietární nebo založené na jednoduchých protokolech jako RADIUS, kterým chyběla stavová, obousměrná komunikace potřebná pro dynamické řízení politik. [IETF](/mobilnisite/slovnik/ietf/) vyvinulo COPS, aby poskytlo flexibilní rámec, kde by rozhodování o politikách mohlo být centralizováno, zatímco vymáhání zůstalo distribuováno napříč síťovými elementy.

V sítích 3GPP COPS vyřešil několik klíčových problémů: umožnil konzistentní uplatňování politik QoS napříč různými síťovými doménami (přístup, jádro, IMS), poskytl mechanismus pro aktualizace politik v reálném čase na základě měnících se síťových podmínek nebo akcí účastníka a vytvořil čisté oddělení mezi logikou rozhodování o politikách a mechanismy vymáhání. Toto oddělení umožnilo operátorům implementovat sofistikovaná pravidla politik v centralizovaných serverech, zatímco vymáhání zůstalo efektivní v okrajových zařízeních. Přijetí protokolu v 3GPP R99 bylo motivováno potřebou řízení politik v nově zaváděném IP Multimedia Subsystem (IMS), kde byla dynamická QoS a účtovací politika nezbytná pro multimediální služby.

Omezení předchozích přístupů, která COPS řešil, zahrnovala nedostatek stavové komunikace v protokolech jako RADIUS, což ztěžovalo aktualizace politik v reálném čase; proprietární povahu mnoha řešení řízení politik, která bránila interoperabilitě mezi více dodavateli; a neschopnost podporovat jak model outsourcingu, tak model provisioning v jediném protokolu. COPS poskytlo standardizované řešení, které se mohlo škálovat do velkých sítí při zachování flexibility potřebné pro vyvíjející se požadavky služeb. Jeho přijetí 3GPP zajistilo, že řízení politik může být implementováno konzistentně napříč různými releasy a síťovými architekturami.

## Klíčové vlastnosti

- Klientsko-serverová architektura s rolemi PEP (klient) a PDP (server)
- Stavová správa spojení umožňující efektivní synchronizaci politik
- Podpora jak modelu outsourcingu (na základě událostí), tak modelu provisioning (na základě pravidel)
- Rozšiřitelnost prostřednictvím objektů specifických pro dodavatele (VSO) pro vlastní implementace
- Spolehlivý přenos přes TCP s vestavěnými mechanismy pro zpracování chyb a keep-alive
- Podpora více typů klientů pro různé domény politik (QoS, řízení přístupu atd.)

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TS 23.207** (Rel-19) — End-to-End QoS Framework for GPRS
- **TS 23.802** (Rel-7) — Enhanced End-to-End QoS Architecture
- **TR 23.976** (Rel-19) — Push Service Requirements Analysis
- **TS 24.228** (Rel-5) — IP Multimedia Call Control Signaling Flows
- **TS 32.101** (Rel-19) — Management principles and high-level requirements

---

📖 **Anglický originál a plná specifikace:** [COPS na 3GPP Explorer](https://3gpp-explorer.com/glossary/cops/)
