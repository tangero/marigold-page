---
slug: "eci"
url: "/mobilnisite/slovnik/eci/"
type: "slovnik"
title: "ECI – Edge and Cloud Interworking"
date: 2026-01-01
abbr: "ECI"
fullName: "Edge and Cloud Interworking"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/eci/"
summary: "ECI je rámec pro integraci platformy edge computingu s centrálními cloudovými infrastrukturami, který umožňuje aplikace s nízkou latencí a vysokou přenosovou rychlostí. Definuje architekturu a procedu"
---

ECI je rámec pro integraci platformy edge computingu s centrálními cloudovými infrastrukturami, který umožňuje aplikace s nízkou latencí definováním architektury a procedur pro bezproblémové nasazení služeb a směrování.

## Popis

Edge and Cloud Interworking (ECI) je architektonický a služební rámec 3GPP navržený k propojení distribuovaných prostředí edge computingu s centralizovanými cloudovými datovými centry. Řeší problém nasazení aplikací, které vyžadují jak ultranízkou latenci a lokalizované zpracování dat na síťovém okraji (edge), tak obrovskou škálovatelnost a výpočetní zdroje centrálního cloudu. Rámec ECI, vyvinutý v kontextu 5G systému (5GS) a edge computingu ([EDGE](/mobilnisite/slovnik/edge/)), standardizuje způsob, jakým mohou být aplikační funkce distribuovány napříč těmito dvěma doménami, a jak síť může dynamicky směrovat uživatelský provoz na příslušnou instanci.

Architektura zahrnuje několik klíčových komponent: Edge Application Server ([EAS](/mobilnisite/slovnik/eas/)), Edge Enabler Server ([EES](/mobilnisite/slovnik/ees/)) a Edge Configuration Server ([ECS](/mobilnisite/slovnik/ecs/)) v doméně edge spolu s jejich protějšky nebo funkcemi pro vzájemnou spolupráci v centrálním cloudu. Jádrová síť, konkrétně User Plane Function ([UPF](/mobilnisite/slovnik/upf/)), hraje klíčovou roli. ECI definuje procedury pro objevování EAS, při kterých může UE nebo aplikační klient objevit dostupné instance edge aplikací na základě polohy, schopností nebo požadavků služby. Dále specifikuje pravidla pro směrování provozu, kdy Session Management Function ([SMF](/mobilnisite/slovnik/smf/)) konfiguruje UPF pomocí filtrů pro směrování konkrétních datových toků do místní edge datové sítě ([LADN](/mobilnisite/slovnik/ladn/)) nebo centrální datové sítě.

Jak to funguje, zahrnuje úzkou koordinaci mezi aplikační vrstvou a jádrem 5G sítě. Poskytovatel aplikace může nasadit aplikaci s komponentami jak na edge, tak v cloudu. Síť 3GPP zpřístupňuje schopnosti (prostřednictvím Network Exposure Function - [NEF](/mobilnisite/slovnik/nef/)), aby aplikace mohla ovlivňovat směrování provozu. Například u interaktivní herní služby může být komponenta vyžadující nízkou latenci pro vykreslování hostována na edge, zatímco databáze hráčů a logika pro hledání protihráčů zůstává v cloudu. Mechanizmy ECI zajišťují, že provoz z UE je odpovídajícím způsobem rozdělen: pakety vyžadující řízení hry v reálném čase jsou směrovány na lokální EAS, zatímco data nezávislá na latenci (jako statistiky hráčů) putují do cloudu. Tato vzájemná spolupráce je řízena prostřednictvím standardizovaných rozhraní a API založených na službách, což zajišťuje interoperabilitu mezi zařízeními od různých výrobců a poskytovatelů cloudových služeb.

## K čemu slouží

ECI bylo vytvořeno k vyřešení problému aplikačních sil a neefektivního využívání zdrojů v raných nasazeních edge computingu. Zpočátku byl edge computing často chápán jako izolovaná platforma, což vedlo ke scénářům, kdy aplikace musely být nasazeny buď kompletně na edge, nebo kompletně v cloudu, bez možnosti elegantně kombinovat výhody obou přístupů. To bylo neefektivní a omezovalo typy aplikací, které mohly být účinně podporovány. Motivací pro ECI bylo poznání, že většina pokročilých případů užití – jako autonomní vozidla, průmyslový IoT a rozšířená realita – vyžaduje hybridní výpočetní model. Tyto aplikace potřebují okamžité zpracování na edge pro úlohy kritické na reakční čas, ale také spoléhají na cloud pro masivní analýzu dat, trénování AI modelů a centralizované řízení.

Historicky, bez standardizovaného rámce pro vzájemnou spolupráci, čelili operátoři a podniky proprietárním a složitým integračním výzvám při pokusech o propojení edge lokalit s centrálními cloudy, což bránilo škálovatelnosti a nasazení s více dodavateli. ECI, zavedené ve verzi 3GPP Release 16 a dále vylepšované, poskytuje standardizovaný „tmel“, který definuje role, odpovědnosti a rozhraní mezi doménami edge a cloudu v rámci 5G systému. Řeší omezení předchozích přístupů formální integrací edge computingu jako nativní schopnosti jádra 5G sítě, což umožňuje dynamickou, na politikách založenou a bezproblémovou kontinuitu služeb při pohybu uživatelů nebo při potřebě migrace stavu aplikace mezi zdroji na edge a v cloudu. Toto odemyká plný ekonomický a technický potenciál distribuovaných výpočtů.

## Klíčové vlastnosti

- Standardizovaná architektura pro integraci aplikačních vrstev edge a centrálního cloudu
- Procedury pro objevování a registraci Edge Application Server (EAS)
- Síťově asistované směrování provozu a řízení směrování mezi edge a cloudovými datovými sítěmi
- Podpora pro přenos aplikačního kontextu a kontinuitu služeb
- Zpřístupnění schopností edge aplikačním funkcím prostřednictvím API 3GPP
- Umožňuje hybridní modely nasazení aplikací (split computing)

## Související pojmy

- [MEC – Multi-Access Edge Computing](/mobilnisite/slovnik/mec/)
- [UPF – User Plane Function](/mobilnisite/slovnik/upf/)
- [LADN – Local Area Data Network](/mobilnisite/slovnik/ladn/)
- [NEF – Network Exposure Function](/mobilnisite/slovnik/nef/)
- [SMF – Service Management Function](/mobilnisite/slovnik/smf/)

## Definující specifikace

- **TS 22.810** (Rel-13) — Enhanced Calling Information Presentation Requirements
- **TS 23.558** (Rel-20) — Architecture for Edge Applications
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 29.558** (Rel-19) — Enabling Edge Applications
- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification
- **TS 38.331** (Rel-19) — NR Radio Resource Control (RRC) Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [ECI na 3GPP Explorer](https://3gpp-explorer.com/glossary/eci/)
