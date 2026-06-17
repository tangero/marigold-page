---
slug: "adtf"
url: "/mobilnisite/slovnik/adtf/"
type: "slovnik"
title: "ADTF – Absolute Data Throughput Framework"
date: 2025-01-01
abbr: "ADTF"
fullName: "Absolute Data Throughput Framework"
category: "Management"
segment: "Testing"
canonical: "https://3gpp-explorer.com/glossary/adtf/"
summary: "Standardizovaný rámec pro měření a vykazování absolutní datové propustnosti v sítích LTE a 5G. Poskytuje konzistentní, na dodavateli nezávislé metriky pro hodnocení výkonu sítě, což umožňuje přesné sr"
---

ADTF je standardizovaný rámec pro měření a vykazování absolutní datové propustnosti v sítích LTE a 5G, který poskytuje konzistentní, na dodavateli nezávislé metriky pro hodnocení a porovnávání sítí.

## Popis

Rámec absolutní datové propustnosti (ADTF) je komplexní systém měření a vykazování definovaný ve specifikacích 3GPP pro hodnocení výkonu datové propustnosti sítí LTE a 5G NR za standardizovaných podmínek. Stanovuje společnou metodologii testování a vykazování metrik propustnosti, která zajišťuje, že měření výkonu jsou konzistentní, opakovatelná a srovnatelná napříč různými dodavateli síťového vybavení a nasazeními operátorů. Rámec specifikuje podrobné testovací konfigurace, postupy měření a formáty vykazování, které musí být dodrženy pro generování platných výsledků ADTF.

Architektonicky ADTF funguje prostřednictvím koordinovaného testovacího prostředí sestávajícího z řadiče testovacího systému, vybavení základnové stanice (eNodeB pro LTE nebo gNB pro 5G NR) a testovacího uživatelského zařízení (UE). Rámec definuje specifické referenční měřicí kanály, včetně konfigurací pro uplink i downlink, s přesně specifikovanými parametry pro šířku pásma, modulační schémata, kódovací rychlosti a přidělování zdrojů. Tyto standardizované kanály slouží jako základ pro měření propustnosti a odstraňují proměnné, které by jinak mohly zkreslit srovnání výkonu různých implementací.

Proces měření zahrnuje navázání vyhrazeného testovacího spojení mezi testovacím UE a základnovou stanicí, následované přenosem dat přes předdefinované referenční kanály za současného sledování výkonu propustnosti. Rámec specifikuje přesné doby trvání měření, průměrovací období a požadavky na statistické vykazování, aby zajistil konzistentní výsledky. Mezi klíčové ukazatele výkonu patří špičková propustnost, udržitelná propustnost a propustnost za různých podmínek kanálu. Rámec také definuje environmentální parametry, jako jsou úrovně rušení, modely kanálů a scénáře mobility, které musí být během testování simulovány.

Role ADTF v síťovém ekosystému přesahuje rámec prostého měření výkonu. Slouží jako kritický nástroj pro plánování sítě, optimalizaci a výběr dodavatele tím, že poskytuje objektivní, srovnatelné údaje o výkonu. Síťoví operátoři používají výsledky ADTF k ověření, že nasazené vybavení splňuje výkonnostní specifikace, zatímco výrobci zařízení jej používají k validaci svých implementací vůči požadavkům 3GPP. Standardizovaný přístup tohoto rámce zajišťuje, že měření propustnosti odrážejí skutečné síťové schopnosti, aniž by byla ovlivněna rozdíly v testovací konfiguraci nebo variacemi v metodice měření.

## K čemu slouží

Rámec absolutní datové propustnosti (ADTF) byl vytvořen, aby řešil rostoucí potřebu standardizovaného, objektivního měření výkonu v sítích LTE a 5G. Před zavedením ADTF používali dodavatelé síťového vybavení a operátoři proprietární testovací metodiky s různými konfiguracemi, což činilo smysluplné srovnání výkonu obtížným nebo nemožným. Tento nedostatek standardizace vedl v odvětví ke zmatení, kdy různé strany vykazovaly čísla propustnosti za různých podmínek, což ztěžovalo hodnocení skutečných výkonnostních schopností sítě.

ADTF tento problém řeší vytvořením společného měřicího rámce, který mohou používat všichni zúčastnění. Zajišťuje, že tvrzení o výkonu propustnosti jsou založena na konzistentních testovacích podmínkách, což umožňuje spravedlivé srovnání různých síťových implementací. Tato standardizace je obzvláště důležitá pro síťové operátory během procesů zadávání zakázek, protože jim umožňuje objektivně hodnotit konkurenční zařízení na základě standardizovaných výkonnostních metrik namísto tvrzení specifických pro jednotlivé dodavatele.

Rámec také podporuje vývoj mobilních sítí tím, že poskytuje konzistentní měřicí základnu napříč různými releasy 3GPP. Jak se sítě vyvíjejí z LTE na 5G NR a dále, ADTF zajišťuje, že zlepšení výkonu lze přesně měřit a srovnávat s předchozími generacemi. Toto historické sledování výkonu pomáhá odvětví pochopit reálné výhody nových technologií a směruje budoucí standardizační úsilí do oblastí, kde jsou zlepšení výkonu nejvíce potřebná.

## Klíčové vlastnosti

- Standardizované referenční měřicí kanály pro konzistentní testování
- Metodologie hodnocení výkonu nezávislá na dodavateli
- Komplexní měření propustnosti pro uplink i downlink
- Podrobná specifikace testovacích prostředí a podmínek kanálu
- Požadavky na statistické vykazování pro spolehlivá data o výkonu
- Podpora pro síťové technologie LTE i 5G NR

## Definující specifikace

- **TR 37.977** (Rel-19) — MIMO OTA Test Methodology

---

📖 **Anglický originál a plná specifikace:** [ADTF na 3GPP Explorer](https://3gpp-explorer.com/glossary/adtf/)
