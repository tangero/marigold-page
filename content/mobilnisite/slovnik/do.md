---
slug: "do"
url: "/mobilnisite/slovnik/do/"
type: "slovnik"
title: "DO – Declarative Object"
date: 2025-01-01
abbr: "DO"
fullName: "Declarative Object"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/do/"
summary: "Deklarativní objekt (DO) je datová struktura definovaná ve specifikacích 3GPP, zejména pro aplikace USIM, která popisuje službu nebo funkci deklarativním způsobem. Umožňuje dynamickou konfiguraci a pr"
---

DO je datová struktura definovaná 3GPP pro aplikace USIM, která deklarativně popisuje službu a umožňuje její dynamickou konfiguraci a provizionování na UICC bez nutnosti nízkoúrovňového procedurálního programování.

## Popis

Deklarativní objekt (DO) je základní koncept ve specifikacích 3GPP týkající se aplikací Univerzálního modulu identifikace účastníka ([USIM](/mobilnisite/slovnik/usim/)) a platformy UICC. Definován ve specifikacích jako TS 31.102 (charakteristiky USIM) a TS 26.953 (služba IMS Multimedia Telephony), je DO strukturovaný datový objekt, který používá deklarativní jazyk k popisu chování, konfigurace nebo prezentace služby. Na rozdíl od procedurálních objektů, které specifikují instrukce krok za krokem, DO deklaruje, 'co' má být dosaženo, přičemž 'jak' to provést, nechává na interpretující entitě (např. USIM nebo terminálu). DO jsou typicky konstruovány pomocí schématu kódování tag-délka-hodnota ([TLV](/mobilnisite/slovnik/tlv/)), kde tagy identifikují typ objektu, délka udává velikost pole hodnoty a hodnota obsahuje vlastní deklarativní data. Používají se k definování prvků, jako jsou položky menu, pravidla řízení hovorů, parametry služeb nebo bezpečnostní politiky v rámci aplikace USIM. Například DO může popsat strukturu menu pro přidané služby, což umožňuje mobilnímu terminálu vykreslit uživatelské rozhraní přímo z dat USIM. Souborový systém USIM ([EF](/mobilnisite/slovnik/ef/), [DF](/mobilnisite/slovnik/df/)) často obsahuje soubory složené z jednoho nebo více DO. Terminál tyto DO čte, interpretuje jejich význam na základě standardizovaných tagů a provádí odpovídající akce. Tento mechanismus umožňuje personalizaci služeb a aktualizace řízené sítí, protože operátoři mohou upravovat DO prostřednictvím provizionování Over-The-Air ([OTA](/mobilnisite/slovnik/ota/)) a měnit tak chování služby bez výměny fyzické [SIM](/mobilnisite/slovnik/sim/) karty. DO jsou klíčové pro umožnění standardizovaných, interoperabilních přidaných služeb napříč různými výrobci telefonů a síťovými operátory.

## K čemu slouží

Deklarativní objekty byly zavedeny, aby překonaly omezení pevně zabudované, procedurální logiky služeb na [SIM](/mobilnisite/slovnik/sim/)/[USIM](/mobilnisite/slovnik/usim/) kartách, která činila nasazení a aktualizace služeb těžkopádnými a nepružnými. Před DO často vyžadovalo přidání nebo úprava služby vydání nových fyzických SIM karet nebo použití proprietárních, neinteroperabilních metod. Hlavní motivací bylo vytvořit standardizovaný, flexibilní mechanismus pro popis a provizionování služeb na UICC způsobem, který je nezávislý na implementačních detailech terminálu. DO umožňují jasné oddělení mezi popisem služby (na USIM) a její exekucí (na terminálu), což podporuje interoperabilitu. Tento deklarativní přístup umožňuje síťovým operátorům dynamicky konfigurovat služby, jako jsou nastavení multimediální telefonie, struktury adresářů nebo servisní menu, prostřednictvím aktualizací OTA. Zjednodušuje zavádění nových služeb, zkracuje čas uvedení na trh a zlepšuje uživatelský zážitek umožněním personalizovaných konfigurací služeb. DO jsou základním kamenem ekosystémů SIM Application Toolkit (SAT) a USIM Application Toolkit (USAT), které umožňují širokou škálu přidaných služeb od základního řízení hovorů po pokročilé aplikace založené na IMS.

## Klíčové vlastnosti

- Používá deklarativní jazyk k popisu chování a konfigurace služby, nikoli procedurálních kroků
- Kódován ve standardizovaném formátu Tag-Délka-Hodnota (TLV) pro kompaktní reprezentaci a parsování
- Ukládán v rámci souborového systému USIM (např. v elementárních souborech) pro trvalou definici služby
- Umožňuje dynamické provizionování a aktualizace služeb prostřednictvím mechanismů Over-The-Air (OTA)
- Usnadňuje interoperabilitu mezi aplikacemi USIM a mobilními terminály od různých výrobců
- Podporuje širokou škálu aplikací včetně struktur menu, řízení hovorů a parametrů služeb IMS

## Související pojmy

- [USIM – Universal Subscriber Identity Module](/mobilnisite/slovnik/usim/)
- [OTA – Over The Air](/mobilnisite/slovnik/ota/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 26.953** (Rel-19) — Study on Service Interactivity for Streaming & Download
- **TS 31.102** (Rel-19) — USIM Application Specification

---

📖 **Anglický originál a plná specifikace:** [DO na 3GPP Explorer](https://3gpp-explorer.com/glossary/do/)
