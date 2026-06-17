---
slug: "hcp"
url: "/mobilnisite/slovnik/hcp/"
type: "slovnik"
title: "HCP – Horizontal Coupling Plane"
date: 2025-01-01
abbr: "HCP"
fullName: "Horizontal Coupling Plane"
category: "Other"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/hcp/"
summary: "Horizontal Coupling Plane je konceptuální rozhraní definované v 3GPP pro správu síťového řezání. Usnadňuje komunikaci a koordinaci mezi systémy řízení různých administrativních domén, například mezi s"
---

HCP je konceptuální rozhraní pro správu síťového řezání (network slicing), které umožňuje komunikaci mezi systémy řízení různých administrativních domén, například mezi systémy nájemce a operátora.

## Popis

Horizontal Coupling Plane (HCP) je koncept architektury řízení definovaný v rámci standardů 3GPP pro síťové řezání, konkrétně v kontextu řízení a orchestrace. Nejde o fyzické rozhraní, ale o logickou rovinu, která standardizuje interakce a výměnu informací mezi službami řízení (Management Services – MnS) náležejícími různým doménám řízení. Tyto domény jsou typicky doména zákazníka komunikační služby (Communication Service Customer – [CSC](/mobilnisite/slovnik/csc/), např. podnik či vertikální odvětví jako nájemce) a doména poskytovatele komunikační služby (Communication Service Provider – [CSP](/mobilnisite/slovnik/csp/), např. mobilní síťový operátor). HCP umožňuje systému řízení CSC žádat o vytvoření, sledovat a spravovat životní cyklus instancí síťových řezů, které jsou zřízeny v síti CSP. Technicky je HCP realizováno prostřednictvím sady standardizovaných rozhraní služeb řízení, často založených na RESTful [API](/mobilnisite/slovnik/api/) definovaných pomocí specifikací OpenAPI. Tato rozhraní umožňují operace jako nahrání šablony síťového řezu, zřízení, aktivaci, deaktivaci, ukončení a reportování monitorování výkonu instance síťového řezu. Informační modely vyměňované přes HCP zahrnují deskriptory (např. šablonu síťového řezu) a běhové informace (např. identifikátory a stav instance síťového řezu). HCP pracuje spolu s rovinou vertikálního propojení (Vertical Coupling Plane – VCP), která zajišťuje interakce řízení v rámci jedné administrativní domény (např. mezi funkcí řízení síťového řezu (NSMF) a funkcí řízení podsítě síťového řezu (NSSMF) u operátora). Tím, že poskytuje toto horizontální rozhraní, HCP odděluje operační a obchodní podpůrné systémy nájemce od interních, potenciálně proprietárních, systémů řízení síťového operátora, což umožňuje správu řezů ve více‑dodavatelském a více‑doménovém prostředí.

## K čemu slouží

HCP bylo vytvořeno, aby řešilo základní výzvu v komercializaci a provozu síťového řezání v 5G: jak může externí zákazník (nájemce) bezproblémově spravovat své vyhrazené prostředky řezu, aniž by měl přímý přístup k interním síťovým systémům řízení operátora. Před jeho definicí byly interakce řízení mezi zákazníky a poskytovateli ad‑hoc, proprietární a neškálovatelné pro budoucnost s potenciálně tisíci řezy pro různá vertikální odvětví. Účelem HCP je poskytnout standardizované, zabezpečené a automatizované rozhraní pro správu životního cyklu řezů napříč administrativními hranicemi. Tím řeší problém operační složitosti a umožňuje nové obchodní modely, kde vertikály mohou samy obsluhovat své potřeby a dynamicky žádat o prostředky řezů či je upravovat. Motivací byla vize 5G sítě‑jako‑služba a potřeba technických podpůrných prvků pro nabídky řez‑jako‑služba. Definováním HCP 3GPP usnadňuje interoperabilitu mezi systémy řízení různých dodavatelů v doménách zákazníka a poskytovatele, čímž urychluje adopci síťového řezání pro podnikové a průmyslové use cases.

## Klíčové vlastnosti

- Standardizované logické rozhraní pro mezidoménovou správu síťových řezů
- Definuje sadu producentů a konzumentů služeb řízení (Management Services – MnS)
- Používá RESTful API se specifikacemi založenými na OpenAPI
- Podporuje operace životního cyklu instancí síťových řezů (vytvoření, změna, monitorování, ukončení)
- Umožňuje zabezpečenou komunikaci a autorizaci mezi doménami zákazníka a poskytovatele
- Pracuje spolu s rovinou vertikálního propojení (Vertical Coupling Plane – VCP) pro end‑to‑end správu

## Definující specifikace

- **TS 38.124** (Rel-19) — NR UE EMC Requirements

---

📖 **Anglický originál a plná specifikace:** [HCP na 3GPP Explorer](https://3gpp-explorer.com/glossary/hcp/)
