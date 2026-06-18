---
slug: "pduid"
url: "/mobilnisite/slovnik/pduid/"
type: "slovnik"
title: "PDUID – ProSe Discovery UE ID"
date: 2026-01-01
abbr: "PDUID"
fullName: "ProSe Discovery UE ID"
category: "Identifier"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/pduid/"
summary: "Jedinečný identifikátor přiřazený uživatelskému zařízení (UE) pro přímé zjišťování v rámci služeb blízkosti (ProSe), který umožňuje jednomu UE zjišťovat další UE ve svém okolí bez využití infrastruktu"
---

PDUID je jedinečný identifikátor přiřazený uživatelskému zařízení (UE) pro přímé zjišťování v rámci služeb ProSe, který mu umožňuje zjišťovat další blízká uživatelská zařízení bez využití buněčné infrastruktury pro komunikaci mezi zařízeními a služby veřejné bezpečnosti.

## Popis

[ProSe](/mobilnisite/slovnik/prose/) Discovery UE ID (PDUID) je dočasný identifikátor vrstvy 2 používaný výhradně pro procedury přímého zjišťování ProSe v sítích 3GPP počínaje Release 13. Přiřazuje jej funkce ProSe v jádru sítě uživatelskému zařízení (UE), které je pro služby ProSe autorizováno. PDUID se používá ve skutečných zjišťovacích zprávách vysílaných přes rozhraní PC5 (přímé rádiové propojení mezi zařízeními) a monitorovaných jinými UE. Slouží k maskování trvalé identity UE (jako je [IMSI](/mobilnisite/slovnik/imsi/) nebo [SUPI](/mobilnisite/slovnik/supi/)) z důvodu ochrany soukromí a poskytuje ukazatel pro proces zjišťování. Existují dva základní modely: Model A („Jsem tady“), kde oznamující UE vysílá svůj PDUID, a Model B („Kdo je tam?/Jsi tam?“), kde zjišťující UE vysílá PDUID obsahující informace o UE, které hledá.

Z architektonického hlediska zahrnuje přiřazení a správa PDUID několik síťových funkcí. UE požaduje autorizaci pro zjišťování ProSe od funkce ProSe přes referenční bod PC3. Po úspěšné autorizaci může funkce ProSe přiřadit UE jeden nebo více PDUID spolu s přidruženými parametry, jako je časovač platnosti a filtry zjišťování. UE pak používá PDUID ve své zásobníku protokolu ProSe k formulaci zjišťovacích zpráv. Na fyzické vrstvě jsou tyto zprávy odesílány pomocí specifických fyzických kanálů a prostředků přidělených pro postranní spojení (např. v LTE [SL-DCH](/mobilnisite/slovnik/sl-dch/) nebo v NR [SL-SCH](/mobilnisite/slovnik/sl-sch/)). ProSe aplikační vrstva přijímajícího UE zpracovává přijatý PDUID, často s použitím filtrů zjišťování poskytnutých funkcí ProSe, aby určila, zda je zjištěné UE relevantní.

Úlohou PDUID v síti je umožnit bezpečné, soukromé a efektivní zjišťování zařízení pro služby blízkosti. Funguje jako dočasný alias, který brání dlouhodobému sledování UE na základě jejích zjišťovacích vysílání. Funkce ProSe může PDUID zpětně mapovat na skutečnou identitu UE pro síťově asistované zjišťování nebo pro účely účtování. Ve scénářích veřejné bezpečnosti, kde může chybět síťové pokrytí (mimo pokrytí), mohou UE používat předkonfigurované nebo samo-přiřazené PDUID. Tento identifikátor je tedy klíčovým prvkem pro širokou škálu aplikací od sociálních sítí (hledání přátel v okolí) až po kritickou komunikaci pro záchranné složky a představuje počáteční krok před navázáním přímé relace komunikace ProSe.

## K čemu slouží

PDUID byl vytvořen, aby řešil specifickou potřebu po identifikátoru pro přímé zjišťování zařízení v sítích LTE a 5G, který zachovává soukromí a je spravován sítí. Před standardizací [ProSe](/mobilnisite/slovnik/prose/) se zjišťování mezi zařízeními spoléhalo na ad-hoc metody, jako je Bluetooth nebo Wi-Fi Direct, kterým chyběla integrace s bezpečností buněčné sítě, správou předplatného a koordinací v široké oblasti. Nebyl standardizovaný způsob, jak by buněčná síť mohla usnadňovat zjišťování mezi svými účastníky při zachování kontroly a soukromí. PDUID tento problém řeší tím, že poskytuje dočasný ukazatel vydávaný sítí.

Historický kontext představuje práce 3GPP na službách blízkosti (ProSe), zahájená pro podporu požadavků veřejné bezpečnosti a komerčních [D2D](/mobilnisite/slovnik/d2d/) aplikací. Základní výzvou bylo umožnit zjišťování bez neustálého vystavování trvalých, sledovatelných identifikátorů přes vzdušné rozhraní. PDUID spolu s funkcí ProSe byly navrženy tak, aby tento problém soukromí vyřešily. Řeší také škálovatelnost; síť může přidělovat různé PDUID pro různé účely zjišťování (např. různé aplikace na stejném UE) a spravovat jejich životní cyklus, čímž předchází vyčerpání nebo konfliktu identifikátorů.

Navíc PDUID umožňuje optimalizaci síťově asistovaného zjišťování. Řízením přiřazování může síť pomáhat UE filtrovat irelevantní zjišťovací zprávy, čímž šetří životnost baterie a rádiové prostředky. Je to základní prvek, který umožňuje buněčné síti rozšířit své služby na přímá propojení mezi zařízeními a vytvořit tak hybridní komunikační paradigma. To představovalo významný vývoj oproti tradičním buněčným architekturám, kde veškerá komunikace nutně procházela základnovou stanicí, a umožnilo nové případy použití s nízkou latencí a nezávislé na síti.

## Klíčové vlastnosti

- Dočasný identifikátor přiřazený funkcí ProSe na omezenou dobu platnosti
- Používaný přes rozhraní PC5 v oznámeních a výzvách zjišťovacích zpráv
- Podporuje jak Model A, tak Model B přímého zjišťování ProSe
- Mapuje se na konkrétní UE a kód aplikace ProSe pro korelaci na straně sítě
- Lze obnovovat nebo měnit pro zvýšení soukromí uživatele
- Používá se ve scénářích s pokrytím i bez pokrytí sítě (s předkonfigurací)

## Související pojmy

- [ProSe – Proximity-based Services](/mobilnisite/slovnik/prose/)
- [SL-SCH – Sidelink Shared Channel](/mobilnisite/slovnik/sl-sch/)

## Definující specifikace

- **TS 23.303** (Rel-19) — Proximity Services (ProSe) Stage 2
- **TS 23.304** (Rel-20) — 5G Proximity Services (ProSe) Stage 2
- **TS 23.503** (Rel-20) — 5G Policy and Charging Control Framework
- **TS 24.334** (Rel-19) — ProSe Protocols and Procedures
- **TS 24.554** (Rel-19) — 5G Proximity Services (ProSe) Protocols
- **TS 29.343** (Rel-19) — PC2 Reference Point Stage 3 Specification
- **TS 29.345** (Rel-19) — Diameter-based PC6/PC7 interfaces for ProSe
- **TS 29.513** (Rel-19) — 5G PCC Signalling Flows & QoS Mapping
- **TS 29.534** (Rel-19) — 5G Access & Mobility Policy Authorization Service
- **TS 29.555** (Rel-19) — 5G Direct Discovery Name Management Services
- **TS 29.557** (Rel-19) — 5G AF ProSe Service Stage 3 Protocol
- **TS 29.559** (Rel-19) — 5G PKMF Service Based Interface Stage 3

---

📖 **Anglický originál a plná specifikace:** [PDUID na 3GPP Explorer](https://3gpp-explorer.com/glossary/pduid/)
