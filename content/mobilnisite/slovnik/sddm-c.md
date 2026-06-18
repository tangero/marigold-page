---
slug: "sddm-c"
url: "/mobilnisite/slovnik/sddm-c/"
type: "slovnik"
title: "SDDM-C – SEAL Data Delivery Management Client"
date: 2025-01-01
abbr: "SDDM-C"
fullName: "SEAL Data Delivery Management Client"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/sddm-c/"
summary: "SDDM-C je klientská funkční entita v rámci architektury SDDM. Funguje jako spotřebitel dat, který se přihlašuje k odběru datových zdrojů (SDDM-S) a přijímá publikovaná data nebo oznámení. Implementuje"
---

SDDM-C je klientská funkční entita, která se přihlašuje k odběru datových zdrojů a přijímá publikovaná data nebo oznámení, což aplikacím umožňuje využívat spravované služby doručování dat prostřednictvím klientských API.

## Popis

[SEAL](/mobilnisite/slovnik/seal/) Data Delivery Management Client (SDDM-C) je klíčová funkční role definovaná v rámci servisního rámce SDDP 3GPP. Představuje entitu, která chce spotřebovávat data poskytovaná služebním enablerem nebo aplikací fungující jako datový zdroj. SDDM-C je typicky integrován v uživatelském zařízení (UE), aplikačním serveru nebo jiné síťové funkci, která vyžaduje přístup ke konkrétním datovým proudům. Jeho hlavní odpovědností je interakce s ekosystémem [SDDM](/mobilnisite/slovnik/sddm/) za účelem vyhledání dostupných dat, navázání odběrů a následného přijímání doručených dat nebo oznámení o nové dostupnosti dat.

Operačně SDDM-C funguje tak, že nejprve vyhledá relevantní servery SDDM ([SDDM-S](/mobilnisite/slovnik/sddm-s/)), které nabízejí potřebná data. Toto vyhledávání může být usnadněno síťovou funkcí nebo předkonfigurací. Jakmile je cílový SDDM-S identifikován, SDDM-C zahájí proceduru přihlášení k odběru. Ta zahrnuje odeslání zprávy s žádostí o odběr na SDDM-S (nebo na mezilehlou správní funkci SDDM), která specifikuje požadovanou datovou sadu, preference doručování (např. push nebo pull) a případné filtry. Žádost je ověřena a autorizována na základě přihlašovacích údajů klienta a síťových politik. Po úspěšném přihlášení k odběru SDDM-C přejde do stavu, ve kterém je oprávněn data přijímat.

Způsob přijímání dat závisí na přihlášeném režimu doručování. Pro doručování typu push SDDM-S (nebo doručovací funkce) proaktivně odešle oznámení o datech nebo samotná datová užitečná zatížení na zpětnovazební adresu SDDM-C, když jsou nová data publikována. Pro doručování typu pull SDDM-C periodicky dotazuje nebo vyžaduje data ze SDDM-S. SDDM-C musí implementovat potřebná rozhraní, typicky RESTful [API](/mobilnisite/slovnik/api/) založená na [HTTP](/mobilnisite/slovnik/http/)/2, pro odesílání žádostí o odběr a přijímání zpětných volání. Také zvládá správu životního cyklu, jako je aktualizace nebo ukončení odběrů. Jeho role je klíčová pro umožnění široké škále klientských aplikací – od mobilních aplikací po zařízení IoT – aby se bezproblémově integrovaly se síťovými datovými službami, aniž by samy musely implementovat složitou distribuční logiku.

## K čemu slouží

SDDM-C existuje jako standardizovaný klientský koncový bod pro spotřebu datových služeb v rámci architektury [SEAL](/mobilnisite/slovnik/seal/) 3GPP. Před jeho standardizací používaly klientské aplikace interagující se síťovými datovými zdroji různorodá, často proprietární [API](/mobilnisite/slovnik/api/), což komplikovalo vývoj aplikací, jejich přenositelnost a škálování. SDDM-C definuje jednotné chování klienta, což umožňuje jakékoli kompatibilní aplikaci přihlásit se k odběru jakéhokoli kompatibilního datového zdroje.

Řeší problém fragmentace na straně klienta při přístupu k datům vystaveným sítí. Poskytnutím jasné specifikace pro roli klienta zajišťuje předvídatelnou interakci se serverem [SDDM-S](/mobilnisite/slovnik/sddm-s/) a zvládá aspekty jako vyjednávání odběru, zabezpečená komunikace a příjem dat. To je motivováno potřebou konzistentně podporovat rozsáhlý ekosystém různorodých klientů (např. vozidla, senzory, smartphony), což je zásadní pro rozsáhlá nasazení IoT a služeb.

Vytvoření SDDM-C spolu se SDDM-S umožňuje čistou architekturu založenou na službách. Vývojářům aplikací umožňuje soustředit se na obchodní logiku na straně klienta, zatímco se mohou spolehnout na standardizovanou knihovnu nebo modul SDDM-C, který zvládá veškerou síťovou komunikaci pro přihlášení k odběru dat a jejich doručování. To zkracuje dobu vývoje, zvyšuje spolehlivost a zajišťuje interoperabilitu mezi implementacemi SDDM různých dodavatelů.

## Klíčové vlastnosti

- Zahajuje a spravuje odběry datových zdrojů SDDM-S
- Podporuje jak push (zpětné volání), tak pull (vyžádání) režimy doručování dat
- Implementuje klientská API pro přihlášení k odběru, jeho aktualizaci a ukončení
- Zpracovává a obsluhuje oznámení o datech a datové užitečné zatížení ze sítě
- Umí vyhledat dostupné servery SDDM nabízející relevantní data
- Interaguje s bezpečnostními rámci 3GPP pro ověřování a autorizaci

## Související pojmy

- [SDDM – SEAL Data Delivery Management](/mobilnisite/slovnik/sddm/)
- [SDDM-S – SEAL Data Delivery Management Server](/mobilnisite/slovnik/sddm-s/)
- [SEAL – Service Enabler Architecture Layer for Verticals](/mobilnisite/slovnik/seal/)
- [UE – User Equipment](/mobilnisite/slovnik/ue/)

## Definující specifikace

- **TS 24.538** (Rel-19) — MSGin5G Service Protocol Specification
- **TS 24.543** (Rel-19) — SEAL Data Delivery Management Protocol

---

📖 **Anglický originál a plná specifikace:** [SDDM-C na 3GPP Explorer](https://3gpp-explorer.com/glossary/sddm-c/)
