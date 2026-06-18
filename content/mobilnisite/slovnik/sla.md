---
slug: "sla"
url: "/mobilnisite/slovnik/sla/"
type: "slovnik"
title: "SLA – Spending-Limit-Answer"
date: 2026-01-01
abbr: "SLA"
fullName: "Spending-Limit-Answer"
category: "Management"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/sla/"
summary: "Spending-Limit-Answer (SLA) je zpráva protokolu Diameter používaná v systémech online účtování (OCS) jako odpověď na Spending-Limit-Request (SLR). Komunikuje udělenou kvótu nebo limit spotřeby pro vyu"
---

SLA je zpráva protokolu Diameter odeslaná systémem online účtování (online charging system) v reakci na žádost, která uděluje kvótu nebo limit spotřeby a umožňuje tak řízení kreditu účastníka v reálném čase.

## Popis

Spending-Limit-Answer (SLA) je klíčovou součástí architektury systému online účtování ([OCS](/mobilnisite/slovnik/ocs/)) dle 3GPP, která funguje v rámci referenčních bodů Ro/Rf založených na protokolu Diameter. Je to přímá odpověď na zprávu Spending-Limit-Request (SLR) iniciovanou síťovou funkcí, jako je Gateway [GPRS](/mobilnisite/slovnik/gprs/) Support Node (GGSN), Packet Data Network Gateway ([PGW](/mobilnisite/slovnik/pgw/)) nebo Session Management Function ([SMF](/mobilnisite/slovnik/smf/)). SLA přenáší rozhodnutí OCS o množství servisních jednotek (např. objem dat, časové trvání, peněžní kredit), které je účastníkovi povoleno spotřebovat. Zpráva obsahuje klíčové páry atribut-hodnota (Attribute-Value Pairs, [AVP](/mobilnisite/slovnik/avp/)), jako je Granted-Service-Unit AVP, který specifikuje přesnou kvótu (např. 10 MB dat). Může také obsahovat Validity-Time AVP, který definuje, jak dlouho je kvóta platná, a Final-Unit-Indication AVP, který signalizuje, že udělená kvóta je poslední před ukončením služby nebo přesměrováním.

Z architektonického hlediska je SLA součástí Diameter Credit-Control Application ([DCCA](/mobilnisite/slovnik/dcca/)), jak je definováno v [IETF](/mobilnisite/slovnik/ietf/) [RFC](/mobilnisite/slovnik/rfc/) 4006, které 3GPP přijalo a rozšířilo. OCS po přijetí SLR provede kontrolu zůstatku účastníka, aplikuje tarify a případně konzultuje pravidla předtím, než vytvoří SLA. Proces je stavový, přičemž OCS udržuje kontext relace pro každou aktivní relaci řízení kreditu. SLA je přenášena spolehlivě přes protokol Diameter, což zajišťuje, že účtovací klient v síti obdrží autorizační rozhodnutí.

Její role je zásadní pro účtování dat, hlasu, SMS a IMS služeb v reálném čase a na základě událostí. Tím, že poskytuje dynamický a okamžitý limit spotřeby, SLA umožňuje předplacené služby, kontrolu spotřeby u postpaid účtů a plynulé pokračování služby prostřednictvím cyklů obnovení kvóty. Integrita a včasnost SLA jsou prvořadé pro přesné zajištění příjmů a pro poskytování transparentních a aktuálních informací o spotřebě kreditu účastníkům.

## K čemu slouží

Spending-Limit-Answer existuje za účelem umožnění autorizace kreditu v reálném čase v telekomunikačních sítích, což je nezbytné pro předplacené služby a kontrolu spotřeby. Před zavedením online účtování se operátoři výrazně spoléhali na offline účtování (účtování po události), které s sebou neslo riziko nedobytných pohledávek od účastníků překračujících svůj kredit. SLA jako součást architektury OCS tento problém řeší tím, že poskytuje okamžité rozhodnutí 'ano/ne' a 'jaké množství' před tím, než jsou přiděleny síťové prostředky.

Její vznik byl motivován komerční potřebou nabízet inovativní předplacené tarify pro nově se objevující paketové služby, jako je GPRS a později 3G/4G/5G data. Tradiční přístup založený na záznamech o hovorech (CDR) měl příliš velkou latenci mezi využitím a účtováním, což jej činilo nevhodným pro řízení datových relací, které mohly rychle spotřebovat velkou hodnotu. Mechanismus SLA umožňuje operátorům nabízet flexibilní tarify v reálném čase a chránit své příjmy vynucováním pevných limitů spotřeby.

Historicky její zavedení v R99 časově souviselo se standardizací OCS založeného nejprve na CAMEL a později na Diameter. Řešila omezení pasivního účtování vytvořením interaktivního dialogu mezi sítí a účtovacím systémem, čímž se účtování transformovalo z pouhé záznamové funkce na aktivní bod vynucování pravidel pro monetizaci.

## Klíčové vlastnosti

- Přenáší Granted-Service-Unit (data, čas, peníze) z OCS do síťového prvku
- Podporuje časovače platnosti kvóty pro řízení životnosti autorizace
- Obsahuje Final-Unit-Indication pro spuštění ukončení služby nebo přesměrování po vyčerpání kvóty
- Přenášena přes spolehlivý protokol Diameter na referenčních bodech Ro/Rf
- Integrální součást stavové relace Diameter Credit-Control Application (DCCA)
- Umožňuje více typů kvót (např. objem, čas, událost) v rámci jedné odpovědi

## Související pojmy

- [OCS – Originating Call Screening](/mobilnisite/slovnik/ocs/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.495** (Rel-7) — NGN Requirements for IMS Services
- **TS 22.519** (Rel-19) — NGN Business Communication Requirements
- **TR 22.980** (Rel-19) — Network Composition Feasibility Study
- **TS 23.107** (Rel-19) — UMTS QoS Framework
- **TS 23.207** (Rel-19) — End-to-End QoS Framework for GPRS
- **TS 23.435** (Rel-19) — Network Slice Capability Exposure Procedures
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TR 23.758** (Rel-17) — Study on Edge Application Architecture
- **TS 24.525** (Rel-19) — Business Trunking Architecture & Requirements
- **TS 26.501** (Rel-19) — 5G Media Streaming (5GMS) Architecture
- **TS 26.804** (Rel-19) — 5G Media Streaming Extensions Study
- **TS 26.891** (Rel-16) — Media Distribution Services in 5G System
- **TR 26.942** (Rel-19) — Study on Media Energy Consumption Exposure & Evaluation
- **TS 28.530** (Rel-19) — Network Slicing Concepts & Requirements
- … a dalších 17 specifikací

---

📖 **Anglický originál a plná specifikace:** [SLA na 3GPP Explorer](https://3gpp-explorer.com/glossary/sla/)
