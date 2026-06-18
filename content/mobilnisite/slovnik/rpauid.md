---
slug: "rpauid"
url: "/mobilnisite/slovnik/rpauid/"
type: "slovnik"
title: "RPAUID – Restricted ProSe Application User ID"
date: 2026-01-01
abbr: "RPAUID"
fullName: "Restricted ProSe Application User ID"
category: "Identifier"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/rpauid/"
summary: "Identifikátor zachovávající soukromí používaný v ProSe (služby bezprostřední blízkosti) pro přímou komunikaci mezi zařízeními. Umožňuje identifikaci uživatelské aplikace pro autorizaci služby a zjišťo"
---

RPAUID je ochranu soukromí zachovávající identifikátor aplikace ProSe (služby bezprostřední blízkosti), používaný pro autorizaci služby a zjišťování v přímé komunikaci mezi zařízeními, který chrání trvalou identitu předplatitele uživatele.

## Popis

Restricted [ProSe](/mobilnisite/slovnik/prose/) Application User ID (RPAUID) je klíčový identifikátor zvyšující soukromí, definovaný v architektuře služeb bezprostřední blízkosti (ProSe) 3GPP. Slouží jako dočasný alias na aplikační vrstvě pro uživatele v kontextu konkrétní aplikace s podporou ProSe. RPAUID je odvozen z trvalého identifikátoru předplatitele uživatele (jako je [IMSI](/mobilnisite/slovnik/imsi/) nebo [SUPI](/mobilnisite/slovnik/supi/)) pomocí kryptografických funkcí spravovaných funkcí ProSe v síti, ale není na něj přímo zpětně dohledatelný. Jeho hlavní úlohou je umožnit zjišťování a komunikaci mezi uživatelskými zařízeními (UE) s podporou ProSe, přičemž zastírá skutečnou identitu uživatele před ostatními UE a v některých scénářích i před aplikačními servery.

Z architektonického hlediska je RPAUID generován a spravován funkcí ProSe, což je entita jádra sítě specifikovaná pro ProSe. Když se UE zaregistruje pro služby ProSe, může funkce ProSe ve spolupráci s Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) přiřadit nebo autorizovat použití RPAUID pro konkrétní ProSe Application ID. Tento identifikátor se pak používá v procedurách zjišťování ProSe (Model A nebo Model B) a při navazování přímé komunikace. Ve zprávách pro zjišťování je RPAUID zahrnut, aby naznačil, která aplikace na zjišťujícím UE hledá nebo oznamuje dostupnost, což umožňuje aplikační vrstvě přijímajícího UE porovnat ji s autorizovanými nebo zajímavými aplikacemi bez znalosti globální identity zjišťujícího zařízení.

RPAUID funguje v rámci širšího rámce identifikátorů ProSe, který zahrnuje ProSe Application Code a ProSe Restricted Code. Je 'restricted' (omezený), protože jeho rozsah a platnost jsou omezeny – typicky na konkrétní aplikaci, určitou geografickou oblast nebo časové okno. Toto omezení je klíčovým mechanismem ochrany soukromí, který zabraňuje dlouhodobému sledování uživatele napříč různými službami nebo lokalitami. Správa životního cyklu RPAUID – včetně generování, přiřazení, obnovy a odvolání – je podrobně popsána v dokumentech jako TS 23.303 (architektura ProSe) a TS 33.303 (zabezpečení ProSe). Jeho použití je nezbytné pro splnění regulatorních požadavků na ochranu soukromí při současném umožnění inovativních služeb peer-to-peer a služeb pro veřejnou bezpečnost, které spoléhají na přímé zjišťování zařízení.

## K čemu slouží

RPAUID byl zaveden, aby vyřešil inherentní konflikt ochrany soukromí ve službách zjišťování mezi zařízeními. Rané koncepty přímé komunikace riskovaly odhalení trvalého, jedinečného identifikátoru uživatele (jako je [IMSI](/mobilnisite/slovnik/imsi/)) během procesů zjišťování založených na vysílání, což umožňovalo neoprávněné sledování a profilování. Hlavní motivací bylo umožnit komerční a veřejně bezpečnostní aplikace [ProSe](/mobilnisite/slovnik/prose/) – jako je sociální síťování, zjišťování místních služeb a přímá komunikace pro záchranáře – bez narušení soukromí uživatele.

Před RPAUID mohly podobné služby spoléhat na identifikátory specifické pro aplikaci spravované pouze na aplikační vrstvě, bez integrace s autentizací a autorizací na síťové úrovni. To mohlo vést k bezpečnostním slabinám a nekonzistentní uživatelské zkušenosti. RPAUID poskytuje standardizovanou, síťově asistovanou metodu, kde je ochrana soukromí vestavěna do architektury. Umožňuje, aby funkce ProSe operátora sítě fungovala jako důvěryhodná třetí strana, vydávající dočasné identifikátory platné pouze v kontrolovaném kontextu. Tím řeší omezení předchozích ad-hoc řešení tím, že poskytuje bezpečný, škálovatelný mechanismus s ochranou soukromí integrovanou do návrhu, který je nedílnou součástí standardů 3GPP, a zajišťuje interoperabilitu a soulad s globálními předpisy na ochranu dat.

## Klíčové vlastnosti

- Zachování soukromí oddělením od trvalých identifikátorů předplatitele
- Rozsah specifický pro aplikaci, vázaný na ProSe Application ID
- Generován a spravován sítí prostřednictvím funkce ProSe
- Používá se v otevřených i omezených modelech zjišťování ProSe
- Podporuje omezení platnosti na základě času a umístění
- Umožňuje bezpečné zjišťování bez odhalení identity uživatele ostatním UE

## Související pojmy

- [ProSe – Proximity-based Services](/mobilnisite/slovnik/prose/)

## Definující specifikace

- **TS 23.303** (Rel-19) — Proximity Services (ProSe) Stage 2
- **TS 23.304** (Rel-20) — 5G Proximity Services (ProSe) Stage 2
- **TS 24.334** (Rel-19) — ProSe Protocols and Procedures
- **TS 24.554** (Rel-19) — 5G Proximity Services (ProSe) Protocols
- **TS 29.343** (Rel-19) — PC2 Reference Point Stage 3 Specification
- **TS 29.345** (Rel-19) — Diameter-based PC6/PC7 interfaces for ProSe
- **TS 29.555** (Rel-19) — 5G Direct Discovery Name Management Services
- **TS 29.557** (Rel-19) — 5G AF ProSe Service Stage 3 Protocol
- **TS 29.559** (Rel-19) — 5G PKMF Service Based Interface Stage 3
- **TS 33.303** (Rel-19) — ProSe Security Specification for EPS
- **TS 33.503** (Rel-19) — Security for Proximity Services (ProSe) in 5G

---

📖 **Anglický originál a plná specifikace:** [RPAUID na 3GPP Explorer](https://3gpp-explorer.com/glossary/rpauid/)
