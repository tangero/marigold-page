---
slug: "nsc"
url: "/mobilnisite/slovnik/nsc/"
type: "slovnik"
title: "NSC – Network Slice Customer"
date: 2026-01-01
abbr: "NSC"
fullName: "Network Slice Customer"
category: "Network Slicing"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/nsc/"
summary: "Entita (např. podnik, MVNO nebo poskytovatel služeb), která si u mobilního operátora vyžádá a využívá instanci síťového řezu. NSC definuje požadavky na řez, jako jsou charakteristiky služby a SLA, a j"
---

NSC je zákaznická entita, například podnik nebo poskytovatel služeb, která si u operátora vyžádá a využívá přizpůsobenou instanci síťového řezu, definuje její požadavky a je příjemcem její izolované konektivity.

## Popis

Zákazník síťového řezu (NSC) je klíčový koncept v rámci 3GPP pro síťové řezy, zavedený ve verzi 15 jako součást systému 5G. NSC je typicky organizace nebo entita, která si předplácí a využívá jednu nebo více instancí síťových řezů poskytovaných mobilním operátorem ([MNO](/mobilnisite/slovnik/mno/)) nebo poskytovatelem síťových řezů. NSC nemusí být nutně koncový uživatel, ale spíše zákazník služby řezů – příklady zahrnují podniky (např. továrnu vyžadující ultra-spolehlivou komunikaci s nízkou latencí), mobilní virtuální operátory ([MVNO](/mobilnisite/slovnik/mvno/)) nebo dokonce interní oddělení samotného MNO. NSC specifikuje požadavky na síťový řez prostřednictvím Smlouvy o úrovni služeb ([SLA](/mobilnisite/slovnik/sla/)) nebo šablony síťového řezu, která detailně popisuje očekávaný výkon, funkčnost a úroveň izolace.

Z architektonického hlediska NSC komunikuje se systémem správy síťových řezů, který zahrnuje funkci správy komunikačních služeb (CSMF) a funkci správy síťových řezů ([NSMF](/mobilnisite/slovnik/nsmf/)). NSC poskytuje požadavky na službu CSMF, která je převádí na požadavky na síťový řez. Tyto požadavky pak NSMF využívá k návrhu a vytvoření síťového řezu napříč základními síťovými prostředky, zahrnujícími segmenty RAN a Core Network. NSC může mít prostřednictvím rozhraní pro správu přehled a určitou kontrolu nad svou instancí řezu, což jim umožňuje sledovat výkon a žádat o změny. Samotný řez je logická síť poskytující specifické schopnosti (např. rozšířené mobilní širokopásmové připojení, hromadný IoT, kritické komunikace) přizpůsobené potřebám NSC, často s vyhrazenými nebo sdílenými prostředky.

Role NSC je formalizována v 3GPP specifikacích, jako jsou 23.435 a 28.530, které definují správu životního cyklu síťových řezů. NSC je zapojen do fází jako příprava, zprovoznění, provoz a vyřazení řezů. Například automobilová společnost vystupující jako NSC může požádat o řez pro služby spojené s vozidly, specifikující nízkou latenci a vysokou spolehlivost. MNO pak zřídí řez s odpovídajícími síťovými funkcemi (např. specializovaný [UPF](/mobilnisite/slovnik/upf/), edge computing), aby těmto požadavkům vyhověl. Koncept NSC umožňuje nové obchodní modely, díky kterým mohou MNO nabízet přizpůsobené služby typu network-as-a-service, což znamená posun od jednotného připojení pro všechny k diferencovaným službám, které pohánějí monetizaci 5G.

## K čemu slouží

Koncept NSC byl vytvořen, aby řešil potřebu přizpůsobitelných a pro konkrétního nájemce specifických síťových služeb v éře 5G. Tradiční mobilní sítě nabízely jednotné připojení všem uživatelům, což bylo nedostatečné pro rozmanité požadavky vertikálních odvětví (např. průmyslová automatizace, zdravotnictví, média). Síťové řezy umožňují vytváření virtuálních sítí s přizpůsobenými charakteristikami a NSC definuje, kdo tyto řezy žádá a kdo z nich má prospěch. Řeší problém, jak formálně zachytit a splnit jedinečné požadavky různých zákazníků v rámci sdílené fyzické infrastruktury.

Historicky si podniky musely budovat privátní sítě nebo používat obecné veřejné mobilní služby, což bylo buď nákladné, nebo nedostatečné. Model NSC umožňuje [MNO](/mobilnisite/slovnik/mno/) obsluhovat více zákazníků se specifickými [SLA](/mobilnisite/slovnik/sla/) na jedné infrastruktuře, čímž zvyšuje efektivitu a otevírá nové zdroje příjmů. Řeší omezení předchozích přístupů tím, že poskytuje standardizovaný rámec pro zapojení zákazníka do správy řezů, což zajišťuje, že řezy splňují přesné technické a obchodní potřeby. Role NSC motivuje vývoj pokročilých systémů správy a orchestrace v 5G, které podporují dynamické operace životního cyklu řezů a multi-tenancy.

## Klíčové vlastnosti

- Entita, která žádá a předplácí si instance síťových řezů
- Definuje požadavky na řez prostřednictvím SLA nebo šablon (např. výkon, izolace)
- Může být podnik, MVNO nebo poskytovatel služeb, ne nutně koncový uživatel
- Komunikuje s funkcemi správy (CSMF/NSMF) pro operace životního cyklu řezu
- Umožňuje přizpůsobené obchodní modely typu network-as-a-service
- Podporuje monitorování a potenciální kontrolu přidělených prostředků řezu

## Související pojmy

- [NSMF – Network Slice Management Function](/mobilnisite/slovnik/nsmf/)
- [SLA – Spending-Limit-Answer](/mobilnisite/slovnik/sla/)

## Definující specifikace

- **TS 23.435** (Rel-19) — Network Slice Capability Exposure Procedures
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TR 26.941** (Rel-19) — 5G Media Slicing Extensions
- **TS 28.530** (Rel-19) — Network Slicing Concepts & Requirements
- **TS 28.531** (Rel-20) — Management and Orchestration
- **TR 28.836** (Rel-18) — Technical Report on Intent Driven Management
- **TR 32.847** (Rel-18) — Technical Report

---

📖 **Anglický originál a plná specifikace:** [NSC na 3GPP Explorer](https://3gpp-explorer.com/glossary/nsc/)
