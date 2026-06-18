---
slug: "tsg-sa"
url: "/mobilnisite/slovnik/tsg-sa/"
type: "slovnik"
title: "TSG-SA – Technical Specification Group - Services and System Aspects"
date: 2025-01-01
abbr: "TSG-SA"
fullName: "Technical Specification Group - Services and System Aspects"
category: "Management"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/tsg-sa/"
summary: "TSG-SA je technická specifikační skupina 3GPP odpovědná za celkovou architekturu, schopnosti služeb a systémové aspekty systémů 3GPP. Definuje požadavky na služby, systémovou architekturu na vysoké úr"
---

TSG-SA je technická specifikační skupina 3GPP odpovědná za celkovou architekturu, schopnosti služeb a systémové aspekty, která definuje požadavky na služby, zabezpečení a řídí pracovní oblasti jako síťové řezy (network slicing) a kodeky.

## Popis

Technical Specification Group - Services and System Aspects (TSG-SA) je jeden z hlavních řídicích orgánů v rámci partnerství 3GPP s mandátem pokrývajícím pohled na systém od konce ke konci, požadavky na služby a celkovou architekturu. Na rozdíl od [TSG](/mobilnisite/slovnik/tsg/) RAN, která se zaměřuje na rozhraní rádiové části, nebo TSG [CT](/mobilnisite/slovnik/ct/), která se zaměřuje na protokoly jádra sítě, TSG-SA uplatňuje holistický, shora-dolů přístup. Je odpovědná za definování toho, co by systém měl dělat (služby), a za návrh rámce na vysoké úrovni (architektury), který tyto schopnosti umožňuje. TSG-SA je sama rozdělena do několika pracovních skupin (Working Groups, WGs), z nichž každá má specializované zaměření: SA1 (Požadavky), SA2 (Architektura), SA3 (Zabezpečení), [SA4](/mobilnisite/slovnik/sa4/) (Kodeky), SA5 (Správa, orchestraci a automatizace) a SA6 (Umožnění aplikací a kritická komunikace).

Pracovní proces v rámci TSG-SA začíná u SA1, která zachycuje požadavky na služby od zástupců trhu a vytváří popisy Fáze 1 (Stage 1), které specifikují služby z pohledu uživatele. Tyto požadavky jsou předány SA2, která navrhuje celkovou systémovou architekturu pro jejich splnění a vytváří specifikace Fáze 2 (Stage 2), které definují funkční entity, klíčové procedury a toky informací. SA3 následně analyzuje tuto architekturu za účelem definování bezpečnostních hrozeb a protokolů. SA4 standardizuje mediální kodeky (např. [EVS](/mobilnisite/slovnik/evs/), [AMR-WB](/mobilnisite/slovnik/amr-wb/)) používané pro hlasové a video služby. SA5 se zabývá správou a orchestraci síťových zdrojů, což je klíčová oblast pro automatizaci 5G a síťové řezy (network slicing). SA6 se zaměřuje na umožnění vertikálních aplikací a služeb kritické komunikace, jako je [MCPTT](/mobilnisite/slovnik/mcptt/). Výstupy těchto pracovních skupin jsou integrovány a schváleny plénem TSG-SA, což vede k základním specifikacím, jako je TS 23.501 (Architektura systému 5G) a TS 22.261 (Požadavky na služby pro systém 5G).

Role TSG-SA je zásadně integrační a architektonická. Zajišťuje, že nové funkce, ať už iniciované v [SA](/mobilnisite/slovnik/sa/) nebo požadované jinými TSG (jako nová funkce rádiové části od RAN), jsou řádně začleněny do celkového systémového návrhu. Například zavedení síťových řezů (Network Slicing) v 5G byl monumentální architektonický posun řízený SA2, který vyžadoval koordinované aktualizace požadavků na služby (SA1), zabezpečení (SA3) a správy (SA5). TSG-SA také udržuje společnou slovní zásobu a principy, které prostupují veškerou prací 3GPP, jako je oddělení uživatelské a řídicí roviny (User Plane a Control Plane), architektura založená na službách (Service-Based Architecture, [SBA](/mobilnisite/slovnik/sba/)) používaná v 5G Core a základní principy QoS a řízení politik (policy control). Její specifikace poskytují plán, který TSG RAN a TSG CT podrobně implementují pro své příslušné domény.

## K čemu slouží

TSG-SA byla vytvořena, aby zajistila, že systémy 3GPP jsou vyvíjeny s jasnou a konzistentní architektonickou vizí a jsou řízeny konkrétními potřebami služeb, namísto toho, aby byly pouhým souborem nesourodých technologií. V raných vydáních 3GPP byly architektonické a servisní aspekty řešeny v rámci jiných skupin, ale s rostoucí komplexitou systému s příchodem IP Multimedia Subsystem (IMS) a později LTE se stala nutností vyčleněná skupina, která by poskytovala silné architektonické vedení a jasný kanál pro požadavky. Formální ustavení TSG-SA (vyvinuté z dřívějších forem) tento cíl naplnilo.

Její existence řeší několik klíčových problémů. Za prvé poskytuje centrální fórum, kde mohou operátoři sítí artikulovat své servisní a provozní požadavky (prostřednictvím SA1), čímž zajišťuje, že standardy jsou vedeny trhem. Za druhé zabraňuje architektonické fragmentaci tím, že má jednu skupinu (SA2) odpovědnou za konzistentní návrh systému od konce ke konci, což je obzvláště kritické u 5G s jeho flexibilním jádrem založeným na službách. Za třetí centralizuje průřezové záležitosti, jako je zabezpečení (SA3) a kódování médií (SA4), čímž zajišťuje, že jsou tyto zásadní aspekty konzistentně aplikovány napříč všemi službami. Bez TSG-SA by existovalo vysoké riziko vzniku nekompatibilních architektur z různých domén, služeb bez jasné technické realizace a zabezpečení řešeného až dodatečně. TSG-SA zajišťuje, že systém 3GPP je jednotnou, zabezpečenou a na služby připravenou platformou.

## Klíčové vlastnosti

- Definuje celkovou systémovou architekturu a principy (např. 5G Service-Based Architecture)
- Vypracovává požadavky na služby na základě potřeb trhu od operátorů a dodavatelů
- Specifikuje architekturu zabezpečení od konce ke konci a protokoly pro systémy 3GPP
- Standardizuje mediální kodeky pro hlasové, video a imerzivní služby
- Spravuje specifikace pro správu sítě, orchestraci a automatizaci (např. OAM)
- Řídí práci na rámcích pro síťové řezy (network slicing), řízení politik (policy control) a umožnění aplikací (application enablement)

## Související pojmy

- [5GS – 5G System](/mobilnisite/slovnik/5gs/)

## Definující specifikace

- **TR 26.952** (Rel-19) — EVS Codec Selection, Verification & Characterization
- **TR 26.976** (Rel-19) — AMR-WB Codec Characterization & Verification

---

📖 **Anglický originál a plná specifikace:** [TSG-SA na 3GPP Explorer](https://3gpp-explorer.com/glossary/tsg-sa/)
