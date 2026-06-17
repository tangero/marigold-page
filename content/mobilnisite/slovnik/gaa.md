---
slug: "gaa"
url: "/mobilnisite/slovnik/gaa/"
type: "slovnik"
title: "GAA – General Authentication Architecture"
date: 2025-01-01
abbr: "GAA"
fullName: "General Authentication Architecture"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/gaa/"
summary: "Bezpečnostní architektura 3GPP pro autentizaci uživatelů a zařízení pro přístup k síťovým službám a aplikacím mimo základní mobilní síť. Poskytuje standardizovanou metodu, která umožňuje poskytovatelů"
---

GAA je bezpečnostní architektura 3GPP pro autentizaci uživatelů u služeb třetích stran využívající robustní autentizační mechanismy mobilní sítě, jako je autentizace založená na SIM kartě.

## Popis

General Authentication Architecture (GAA) je komplexní bezpečnostní architektura 3GPP definovaná tak, aby poskytovala obecné postupy pro autentizaci a dohodu klíčů pro aplikace a služby, které nejsou součástí tradiční autentizace pro přístup k síti 3GPP. Jejím hlavním cílem je umožnit poskytovatelům služeb (což může být mobilní operátor nebo důvěryhodná třetí strana) autentizovat uživatele nebo uživatelské zařízení (UE) využitím silných, již existujících bezpečnostních přihlašovacích údajů uložených na univerzální integrované obvodové kartě (UICC) v UE, tj. na SIM kartě. GAA vytváří bootstrapovací mechanismus, kde lze sdílené tajemství vytvořené během přístupu k mobilní síti (mezi UE a Home Subscriber Server, [HSS](/mobilnisite/slovnik/hss/)) použít k odvození dalších, pro službu specifických klíčů pro zabezpečení jiných služeb.

Z architektonického hlediska je GAA postavena kolem několika klíčových funkčních komponent. Funkce bootstrapovacího serveru (Bootstrapping Server Function, [BSF](/mobilnisite/slovnik/bsf/)) je centrální síťový prvek, který interaguje s UE za účelem provedení bootstrapovací procedury a se serverem HSS za účelem získání autentizačních vektorů účastníka. Funkce síťové aplikace (Network Application Function, [NAF](/mobilnisite/slovnik/naf/)) je entita poskytující vlastní službu (např. multimediální portál, bankovní aplikaci nebo server pro správu zařízení), která potřebuje uživatele autentizovat. UE obsahuje klientskou funkcionalitu GAA. Základním postupem je bootstrapovací procedura GAA, známá také jako procedura rozhraní Ub. V tomto procesu se vzájemně autentizují UE a BSF pomocí protokolu Authentication and Key Agreement ([AKA](/mobilnisite/slovnik/aka/)) (stejného, který se používá pro přístup k síti). Po úspěšné autentizaci si vytvoří sdílené, pro relaci specifické tajemství nazvané Bootstrapping Transaction Identifier ([B-TID](/mobilnisite/slovnik/b-tid/)) a související klíčový materiál Ks. Klíč Ks je následně použit k odvození pro aplikaci specifických klíčů (Ks_NAF) pro použití mezi UE a konkrétní NAF.

GAA definuje dvě hlavní varianty použití: aplikace v UE s podporou GAA (GAA-aware) a bez podpory GAA (GAA-unaware). Pro aplikace s podporou GAA klient GAA v UE spravuje klíče a poskytuje je aplikaci. Pro aplikace bez podpory GAA lze použít uživatelská bezpečnostní nastavení architektury obecného bootstrapování (Generic Bootstrapping Architecture User Security Settings, [GUSS](/mobilnisite/slovnik/guss/)) a referenční identifikátor. Architektura dále specifikuje rozhraní Zn mezi BSF a NAF, kde si NAF může vyžádat klíčový materiál (Ks_NAF) pro daného uživatele identifikovaného pomocí B-TID. Tato architektura odděluje silnou autentizaci založenou na SIM kartě od samotné služby, což umožňuje široké škále aplikací – od autentizace [HTTP](/mobilnisite/slovnik/http/) Digest pro webové služby přes autentizaci klienta TLS až po ochranu služeb [MBMS](/mobilnisite/slovnik/mbms/) – znovu použít jedinou, robustní autentizační událost. Tvoří základ pro Generic Bootstrapping Architecture (GBA), což je nejběžnější a standardizovaná realizace principů GAA.

## K čemu slouží

GAA byla vytvořena za účelem řešení problému roztříštěné a slabé autentizace pro přidané služby v mobilních sítích. Před zavedením GAA služby jako mobilní e-mail, multimediální portály nebo správa zařízení často používaly vlastní, oddělené přihlašovací údaje (uživatelské jméno/heslo), které byly slabé, nepohodlné pro uživatele (více přihlášení) a obtížně zabezpečitelné. Motivací bylo využít silnou, dvoufaktorovou autentizaci již přítomnou v každém mobilním zařízení – SIM kartu a její sdílené tajemství s operátorovým HSS – a rozšířit její důvěryhodnost na další služby. To poskytlo lepší uživatelský zážitek (jednotné přihlašování), silnější zabezpečení (kryptografické klíče namísto hesel) a zjednodušilo poskytování služeb pro operátory a poskytovatele třetích stran.

Historicky byl vývoj GAA (začínající ve verzi 3GPP Release 6) hnán potřebou standardizované autentizační architektury pro nové služby založené na IP, jako je IMS (Multimediální subsystém), ale její užitečnost se rychle rozšířila. Odstranila omezení předchozích ad-hoc řešení tím, že poskytla obecnou, znovupoužitelnou architekturu. To umožnilo jakékoli aplikaci, ať už poskytované operátorem nebo důvěryhodným partnerem, požadovat kryptografický důkaz totožnosti uživatele bez nutnosti přímého přístupu k citlivým přihlašovacím údajům na SIM kartě. GAA umožnila nové obchodní modely, jako je zabezpečené mobilní bankovnictví nebo autentizované stahování obsahu, tím, že poskytla standardizovanou, na úrovni operátora vhodnou autentizační metodu nezávislou na podkladovém služebním protokolu. Stala se základním kamenem pro zabezpečené poskytování služeb v konvergovaném IP prostředí.

## Klíčové vlastnosti

- Bootstrapuje autentizaci pro aplikace využívající sdílené tajemství z 3GPP AKA
- Centrální funkce bootstrapovacího serveru (BSF) pro dohodu klíčů s UE
- Podporuje funkce síťových aplikací (NAF) pro odvození služebně specifických klíčů (Ks_NAF)
- Umožňuje jak klientské aplikace s podporou GAA, tak bez ní
- Poskytuje základ pro Generic Bootstrapping Architecture (GBA)
- Umožňuje bezpečné jednotné přihlašování napříč více službami operátora nebo třetích stran

## Související pojmy

- [GBA – Generic Bootstrapping Architecture](/mobilnisite/slovnik/gba/)
- [BSF – Bootstrapping Server Function](/mobilnisite/slovnik/bsf/)
- [NAF – Network Application Function](/mobilnisite/slovnik/naf/)
- [AKA – Authentication and Key Agreement](/mobilnisite/slovnik/aka/)
- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)

## Definující specifikace

- **TR 22.978** (Rel-19) — Feasibility of All-IP Network (AIPN) in 3GPP
- **TS 23.862** (Rel-12) — Interworking Solutions for Mobile Operators & Data Apps
- **TS 24.109** (Rel-19) — HTTP Digest AKA & GAA Stage 3
- **TS 24.302** (Rel-19) — Access to EPC via non-3GPP networks; Stage 3
- **TS 29.109** (Rel-19) — GAA Bootstrapping Interfaces (Zh, Dz, Zn, Zpn)
- **TS 31.213** (Rel-18) — Test specification for (U)SIM
- **TS 33.220** (Rel-19) — Generic Authentication Architecture (GAA); Generic Bootstrapping Architecture (GBA)
- **TS 33.221** (Rel-19) — Subscriber Certificate Distribution via GBA
- **TS 33.223** (Rel-19) — GBA Push Function Specification
- **TS 33.804** (Rel-12) — Non-UICC SSO using SIP Digest credentials
- **TS 33.835** (Rel-16) — Study on authentication and key management for apps
- **TR 33.919** (Rel-19) — GAA Overview TR
- **TR 33.924** (Rel-19) — GBA-OpenID Interworking Specification
- **TR 33.980** (Rel-19) — GAA & Liberty Alliance Interworking Guidelines
- **TS 34.229** (Rel-19) — IMS SIP/SDP UE Conformance Testing for 5GS

---

📖 **Anglický originál a plná specifikace:** [GAA na 3GPP Explorer](https://3gpp-explorer.com/glossary/gaa/)
