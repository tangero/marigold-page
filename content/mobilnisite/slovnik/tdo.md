---
slug: "tdo"
url: "/mobilnisite/slovnik/tdo/"
type: "slovnik"
title: "TDO – Triggered Declarative Object"
date: 2025-01-01
abbr: "TDO"
fullName: "Triggered Declarative Object"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/tdo/"
summary: "Triggered Declarative Object (TDO) je datová struktura definovaná v 3GPP pro vystavování servisních schopností. Reprezentuje konkrétní informaci nebo síťovou událost, kterou může vyžádat externí aplik"
---

TDO je datová struktura 3GPP pro vystavování servisních schopností, která reprezentuje konkrétní informaci nebo síťovou událost a umožňuje API deklarativně vyžádat síťová data pro externí aplikace.

## Popis

Triggered Declarative Object (TDO) je základní koncept v rámci architektury 3GPP pro vystavování síťových schopností, podrobně specifikovaný v TS 26.953. Funguje jako standardizovaný datový model nebo objekt, který zapouzdřuje konkrétní typ informace nebo detekovatelnou událost v mobilní síti. Tento objekt je 'deklarativní', protože jej externí aplikační server ([AS](/mobilnisite/slovnik/as/)) nebo server servisních schopností ([SCS](/mobilnisite/slovnik/scs/)) vyžaduje popisem *jaká* data potřebuje, nikoli *jak* je má síť získat. Síťová entita zodpovědná za vystavení (jako je Network Exposure Function, [NEF](/mobilnisite/slovnik/nef/), v 5G) tento požadavek interpretuje, namapuje jej na interní síťové funkce pro monitorování nebo reportování a spravuje doručení odpovídajících dat.

Architektonicky je TDO definován sadou atributů, podmínek a mechanismem doručení. Mezi klíčové komponenty patří identifikátor objektu, spouštěcí událost nebo podmínka (např. vstup UE do určité oblasti, změna stavu konektivity), datová část k nahlášení (např. poloha, stav) a parametry předplatného jako doba platnosti a frekvence reportování. Požadavek TDO je typicky součástí dialogu o předplatném mezi AS a funkcí pro vystavení. Po přihlášení k odběru síť monitoruje zadanou spouštěcí podmínku. Po její detekci vytvoří instanci TDO s aktuálními relevantními daty a doručí je žádající aplikaci prostřednictvím zpětného volání nebo notifikace.

Jeho role je klíčová pro Service Enabler Architecture Layer ([SEAL](/mobilnisite/slovnik/seal/)) a širší rámec vystavování schopností. Poskytnutím strukturovaného, abstrahovaného pohledu na síťové informace TDO chrání vývojáře aplikací před složitostmi podkladových síťových protokolů a správy interního stavu. Umožňují širokou škálu služeb, od upozornění založených na poloze a monitorování kvality uživatelského prožitku až po správu IoT zařízení. Mechanismus TDO zajišťuje, že síťová data jsou poskytována konzistentním, bezpečným a řízeným způsobem v souladu s politikami operátora a předpisy na ochranu soukromí uživatelů.

## K čemu slouží

TDO bylo zavedeno, aby řešilo rostoucí potřebu standardizovaného a efektivního vystavování síťových schopností aplikacím třetích stran. Před jeho definicí často vyžadovalo vystavení síťových událostí a informací vlastní, bod-od-bodu integrace, které byly složité, neškálovatelné a náchylné k nekonzistencím. To bránilo inovacím a rychlému nasazení nových služeb závislých na síťové inteligenci v reálném čase. Koncept TDO poskytuje deklarativní model, který abstrahuje síťové schopnosti.

Jeho vytvoření bylo motivováno posunem průmyslu směrem k otevřeným [API](/mobilnisite/slovnik/api/) a síťové programovatelnosti, zejména pro aplikace IoT a vertikálních trhů. Tím, že umožňuje aplikacím deklarativně vyžadovat konkrétní spouštěné informace, zjednodušuje vývojářský zážitek, snižuje dobu integrace a zajišťuje interoperabilitu napříč různými sítěmi operátorů. Řeší problém, jak bezpečně a efektivně poskytnout externím subjektům přístup k dynamickým, událostmi řízeným síťovým datům, aniž by byla ohrožena síťová bezpečnost, stabilita nebo soukromí uživatelů. Rámec TDO vytváří jasnou smlouvu mezi sítí a aplikací.

## Klíčové vlastnosti

- Deklarativní datový model pro vyžádání síťových informací
- Událostmi spouštěné nebo podmínkami řízené reportování dat
- Standardizovaná struktura objektu definovaná ve specifikacích 3GPP
- Umožňuje asynchronní notifikace aplikacím
- Abstrahuje podkladovou síťovou složitost od vývojářů služeb
- Podporuje správu předplatného s kontrolou platnosti a frekvence

## Související pojmy

- [NEF – Network Exposure Function](/mobilnisite/slovnik/nef/)
- [SCS – Subcarrier Spacing](/mobilnisite/slovnik/scs/)
- [SEAL – Service Enabler Architecture Layer for Verticals](/mobilnisite/slovnik/seal/)

## Definující specifikace

- **TR 26.953** (Rel-19) — Study on Service Interactivity for Streaming & Download

---

📖 **Anglický originál a plná specifikace:** [TDO na 3GPP Explorer](https://3gpp-explorer.com/glossary/tdo/)
