---
slug: "sddm-s"
url: "/mobilnisite/slovnik/sddm-s/"
type: "slovnik"
title: "SDDM-S – SEAL Data Delivery Management Server"
date: 2025-01-01
abbr: "SDDM-S"
fullName: "SEAL Data Delivery Management Server"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/sddm-s/"
summary: "SDDM-S je funkční entita na straně serveru v rámci SDDM frameworku. Vystupuje jako producent (publisher) dat, publikuje konkrétní datové sady a spravuje odběry od klientů (SDDM-C). Je zodpovědný za au"
---

SDDM-S je server v rámci frameworku SEAL Data Delivery Management, který publikuje datové sady, spravuje a autorizuje odběry klientů, ukládá publikovaná data a spouští jejich doručování autorizovaným odběratelům.

## Popis

[SEAL](/mobilnisite/slovnik/seal/) Data Delivery Management Server (SDDM-S) je protějšek na straně serveru ke klientovi [SDDM-C](/mobilnisite/slovnik/sddm-c/) v rámci 3GPP [SDDM](/mobilnisite/slovnik/sddm/) frameworku. Ztělesňuje roli producenta nebo vydavatele dat. SDDM-S je typicky síťová funkce nebo služební prvek, který vytváří nebo vlastní data hodnotná pro jiné entity, jako jsou informace o poloze, hodnoty ze senzorů, stav skupiny nebo konfigurační aktualizace. Jeho klíčovou funkcí je zpřístupnit tato data k odběru, spravovat životní cyklus těchto odběrů a organizovat doručování dat všem autorizovaným odebírajícím klientům.

Z architektonického hlediska SDDM-S hostuje jednu nebo více datových sad, z nichž každá je identifikovatelná jedinečnou adresou zdroje. Vystavuje rozhraní založené na službách (např. Nsddm_DataPublication), které mu umožňuje přijímat požadavky na publikaci, ať už od vlastní interní logiky nebo od přidružené aplikace. Když jsou publikována nová data, SDDM-S je zpracuje vůči svému seznamu aktivních odběrů. Pro každý odběr vyhodnotí, zda nová data odpovídají filtrům odběratele a zda je odběratel autorizován je přijmout. Na základě režimu doručení odběru pak SDDM-S buď odešle notifikaci (nebo samotná data) na zpětnovazební adresu odběratele, nebo zpřístupní data k vyzvednutí (pull) odběratelem.

SDDM-S úzce spolupracuje s dalšími SDDM správními funkcemi při úkolech, jako je autorizace odběrů, která může zahrnovat dotazování na uživatelské profily v jednotném datovém úložišti ([UDR](/mobilnisite/slovnik/udr/)). Udržuje stav odběru, včetně identit odběratelů, zpětnovazebních [URL](/mobilnisite/slovnik/url/), kritérií filtrování a časů vypršení. Klíčovým provozním aspektem je jeho schopnost efektivně zvládat velký počet souběžných odběrů a škálovat události publikace dat. Jeho úlohou v síti je být autoritativním zdrojem a distributorem pro konkrétní datové domény, poskytovat standardizovaný, bezpečný a spolehlivý přístupový bod pro klientské aplikace, čímž umožňuje vytváření bohatých síťových služeb řízených daty.

## K čemu slouží

SDDM-S byl vytvořen za účelem standardizace role vydavatele dat ve služební vrstvě 3GPP. Historicky síťové funkce produkující data (např. server polohy, server přítomnosti) zpřístupňovaly svá data prostřednictvím proprietárních rozhraní, což klientům ztěžovalo integraci s více zdroji. SDDM-S poskytuje společný model pro vystavení dat, správu odběrů a spouštění doručování.

Řeší problém nekonzistentních mechanismů publikování dat napříč různými služebními prvky. Dodržováním specifikace SDDM-S se může jakákoli funkce produkující data bezproblémově integrovat do širšího ekosystému doručování dat [SEAL](/mobilnisite/slovnik/seal/), čímž okamžitě zpřístupní svá data k objevení a odběru libovolným klientům [SDDM-C](/mobilnisite/slovnik/sddm-c/). To podporuje opakované použití a interoperabilitu. Motivací je potřeba zacházet s daty jako se spravovaným síťovým zdrojem s řízeným přístupem, záznamy o činnostech a vynucováním politik, nikoli jako s ad-hoc vlastností služby.

SDDM-S navíc centralizuje logiku pro správu odběrů a rozhodování o doručování. Tím odstraňuje složitost z klientských aplikací a ze samotné základní logiky produkce dat služebního prvku. Umožňuje funkce jako rozesílání (jedna publikace mnoha odběratelům) a podmíněné doručování na základě síťových politik nebo atributů odběratele, které jsou nezbytné pro efektivní nasazení služeb ve velkém měřítku v oblastech jako připojené automobily nebo masivní IoT.

## Klíčové vlastnosti

- Hostuje a publikuje identifikovatelné datové sady pro odběr klienty
- Spravuje životní cyklus odběrů klientů (vytvoření, změna, zrušení)
- Autorizuje žádosti o odběr na základě síťových politik a uživatelských profilů
- Spouští doručování dat odběratelům při publikaci nových dat
- Podporuje konfigurovatelné filtrování dat pro odběry
- Vystavuje standardizovaná rozhraní založená na službách pro správu publikace a odběrů

## Související pojmy

- [SDDM – SEAL Data Delivery Management](/mobilnisite/slovnik/sddm/)
- [SDDM-C – SEAL Data Delivery Management Client](/mobilnisite/slovnik/sddm-c/)
- [SEAL – Service Enabler Architecture Layer for Verticals](/mobilnisite/slovnik/seal/)
- [NEF – Network Exposure Function](/mobilnisite/slovnik/nef/)

## Definující specifikace

- **TS 24.538** (Rel-19) — MSGin5G Service Protocol Specification
- **TS 24.543** (Rel-19) — SEAL Data Delivery Management Protocol

---

📖 **Anglický originál a plná specifikace:** [SDDM-S na 3GPP Explorer](https://3gpp-explorer.com/glossary/sddm-s/)
