---
slug: "no"
url: "/mobilnisite/slovnik/no/"
type: "slovnik"
title: "NO – Network Operator"
date: 2025-01-01
abbr: "NO"
fullName: "Network Operator"
category: "Management"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/no/"
summary: "Subjekt, který vlastní a provozuje infrastrukturu mobilní sítě a poskytuje služby účastníkům. Jde o základní obchodní a administrativní koncept v telekomunikacích, zodpovědný za nasazení sítě, její sp"
---

NO (síťový operátor) je subjekt, který vlastní a provozuje infrastrukturu mobilní sítě, poskytuje služby účastníkům a je zodpovědný za její nasazení, správu a komerční nabídku.

## Popis

Síťový operátor (NO) je právní a obchodní subjekt zodpovědný za nasazení, správu a provoz veřejné pozemní mobilní sítě ([PLMN](/mobilnisite/slovnik/plmn/)). To zahrnuje celý životní cyklus sítě, od počátečního získání kmitočtového spektra a výstavby infrastruktury přes každodenní provoz a údržbu až po poskytování zákaznické podpory. Operátor vlastní licenci na využívání konkrétních rádiových kmitočtů v určité geografické oblasti a je odpovědný za to, aby síť splňovala regulatorní požadavky a závazky týkající se kvality služeb vůči svým účastníkům.

Z architektonického hlediska síťový operátor vlastní prvky základní sítě (CN) a rádiové přístupové sítě (RAN). To zahrnuje uzly jako Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)), Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)), Serving a Packet Gateways (S/[PGW](/mobilnisite/slovnik/pgw/)) a v 5G také Access and Mobility Management Function ([AMF](/mobilnisite/slovnik/amf/)), Session Management Function ([SMF](/mobilnisite/slovnik/smf/)) a User Plane Function ([UPF](/mobilnisite/slovnik/upf/)). V RAN to zahrnuje základnové stanice (NodeB, eNodeB, gNB) a jejich řadiče. Operátor tyto prvky konfiguruje, monitoruje a optimalizuje prostřednictvím systémů pro správu sítě, jako je Operations Support System ([OSS](/mobilnisite/slovnik/oss/)).

Role síťového operátora je pro celý ekosystém klíčová. Vyjednává roamingové dohody s dalšími operátory, implementuje systémy účtování a fakturace a definuje portfolio služeb (např. hlas, data, IoT). Také zajišťuje kritické bezpečnostní funkce, jako je autentizace účastníků a správa klíčů. Zásady operátora, nasazené prostřednictvím uzlů jako Policy and Charging Rules Function (PCRF) nebo Policy Control Function (PCF), řídí uživatelský zážitek, včetně rychlostí dat a kvality služeb. Ve scénářích s více operátory koncepty jako Mobile Virtual Network Operator (MVNO) a roaming závisí na základní infrastruktuře poskytované NO.

## K čemu slouží

Koncept síťového operátora existuje, aby formalizoval vlastnictví, kontrolu a odpovědnost za telekomunikační síť. Řeší problém odpovědnosti v komplexním technickém systému a zajišťuje, že jediný subjekt je právně i provozně odpovědný za poskytování služeb, dodržování regulatorních požadavků a zákaznickou podporu. Mobilní ekosystém se svou potřebou masivních investic do infrastruktury, licencování spektra a standardů interoperability vyžaduje jasně definovanou roli operátora.

Historicky telekomunikační služby poskytovaly státní monopoly. Liberalizace trhů zavedla více konkurenčních síťových operátorů, což pohánělo inovace a snižování nákladů. Standardy 3GPP definují technickou architekturu, ale předpokládají existenci jednoho nebo více operátorů, kteří ji implementují. Model operátora řeší omezení nekoordinovaného systému tím, že zajišťuje celoplošné pokrytí, konzistentní kvalitu služeb a rámec pro propojení mezi operátory (roaming). Vytváří obchodní základnu, která umožňuje, aby technologické standardy poskytovaly služby v reálném světě.

## Klíčové vlastnosti

- Vlastní a spravuje licencované rádiové spektrum na vymezeném území
- Nasazuje a provozuje fyzickou a logickou síťovou infrastrukturu (RAN a Core)
- Poskytuje správu účastníků, včetně zřizování, autentizace a účtování
- Definuje a implementuje komerční nabídky služeb a tarifní plány
- Zajišťuje výkon sítě, bezpečnost a dodržování regulatorních požadavků
- Uzavírá roamingové dohody s dalšími tuzemskými a mezinárodními operátory

## Související pojmy

- [PLMN – Public Land Mobile Network](/mobilnisite/slovnik/plmn/)
- [MVNO – Mobile Virtual Network Operator](/mobilnisite/slovnik/mvno/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.038** (Rel-19) — USIM Application Toolkit (USAT) Stage 1
- **TS 22.057** (Rel-19) — Mobile Execution Environment (MExE) Stage 1
- **TR 22.907** (Rel-4) — UMTS IC Card and Terminal Concepts
- **TS 33.107** (Rel-19) — Lawful Interception Architecture & Functions
- **TS 33.108** (Rel-19) — LI Handover Interface Specification

---

📖 **Anglický originál a plná specifikace:** [NO na 3GPP Explorer](https://3gpp-explorer.com/glossary/no/)
