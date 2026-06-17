---
slug: "asy"
url: "/mobilnisite/slovnik/asy/"
type: "slovnik"
title: "ASY – ASYmmetric conditions"
date: 2025-01-01
abbr: "ASY"
fullName: "ASYmmetric conditions"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/asy/"
summary: "ASY označuje síťové podmínky, kdy se charakteristiky přenosu ve směrech uplink (UL) a downlink (DL) výrazně liší. Tato asymetrie ovlivňuje síťový výkon a alokaci zdrojů, což v systémech 3GPP vyžaduje"
---

ASY je termín 3GPP pro síťové podmínky, kdy se charakteristiky přenosu ve směru uplink (UL) a downlink (DL) výrazně liší, což ovlivňuje výkon a vyžaduje speciální zpracování pro zachování kvality služeb.

## Popis

ASY (ASYmmetric conditions, asymetrické podmínky) popisuje scénáře v telekomunikačních sítích, kdy přenosové cesty uplink (UL) a downlink ([DL](/mobilnisite/slovnik/dl/)) vykazují podstatně odlišné charakteristiky z hlediska kapacity, latence, míry chyb nebo dostupné šířky pásma. Tato asymetrie může být způsobena různými faktory, včetně použití různých kmitočtových pásem, omezení výkonu vysílání, charakteru rušení nebo omezení síťové architektury. V systémech 3GPP je třeba podmínky ASY explicitně rozpoznávat a spravovat, protože mnoho síťových funkcí, protokolů a mechanismů alokace zdrojů předpokládá relativně symetrické podmínky mezi cestami UL a DL.

Technické zpracování podmínek ASY zahrnuje více vrstev protokolového zásobníku. Na fyzické vrstvě mohou být pro UL a DL při existenci asymetrie vyžadovány různé modulační a kódovací schémy. Vrstva řízení přístupu k médiu ([MAC](/mobilnisite/slovnik/mac/)) musí přizpůsobit plánovací algoritmy, aby zohlednila rozdílné kapacity UL/DL, což může zahrnovat implementaci různých konfigurací hybridního automatického opakování na vyžádání ([HARQ](/mobilnisite/slovnik/harq/)) nebo strategií sdružování přenosových časových intervalů (TTI) pro každý směr. Procedury řízení rádiových zdrojů ([RRC](/mobilnisite/slovnik/rrc/)) mohou potřebovat asymetrické konfigurační parametry pro zřizování, udržování a uvolňování spojení.

Úvahy o síťové architektuře pro ASY zahrnují potenciální potřebu asymetrické konfigurace přenosového kanálu (bearer), kde se parametry kvality služeb (QoS) liší mezi směry UL a DL. To ovlivňuje způsob zřizování a udržování přenosových kanálů systému rozšířených paketů (EPS bearers) nebo toků kvality služeb (QoS flows) v systémech 5G. Funkce jádra sítě, jako je funkce pravidel pro řízení zásad a účtování (PCRF) nebo funkce řízení zásad ([PCF](/mobilnisite/slovnik/pcf/)), mohou potřebovat podporovat asymetrické vynucování zásad, zatímco funkce uživatelské roviny musí zvládat potenciální rozdíly v požadavcích na zpracování paketů UL/DL.

Mechanismy měření a hlášení se musí pro podmínky ASY přizpůsobit. Uživatelské zařízení (UE) může potřebovat provádět samostatná měření pro kanály UL a DL, s potenciálně různými periodami měření a kritérii hlášení. Síťové uzly musí tyto asymetrická měření správně interpretovat pro rozhodování o předávání spojení, vyvažování zátěže a řízení rušení. Celkový návrh systému musí zajistit, aby podmínky ASY nezhoršovaly uživatelský komfort nebo efektivitu sítě, což vyžaduje pečlivou koordinaci napříč protokolovými vrstvami a síťovými funkcemi.

## K čemu slouží

Podmínky ASY existují jako základní uznání skutečnosti, že reálné telekomunikační sítě jen zřídka vykazují dokonalou symetrii mezi cestami uplink a downlink. Tato asymetrie může být důsledkem technických omezení (jako různá kmitočtová pásma s odlišnými charakteristikami šíření), regulatorních požadavků (například omezení výkonu vysílání) nebo praktických aspektů nasazení (včetně konfigurace antén a prostředí s rušením). Bez explicitního zpracování podmínek ASY by se síťový výkon zhoršoval, protože systémy navržené pro symetrický provoz by činily suboptimální rozhodnutí o alokaci zdrojů, opravě chyb a řízení kvality služeb.

Historicky rané celulární systémy často předpokládaly relativní symetrii mezi UL a [DL](/mobilnisite/slovnik/dl/), zejména u přepojování okruhů pro hlasové služby, kde byl provoz více vyvážený. S vývojem směrem k paketově přepínaným datovým službám a nástupem aplikací s vysoce asymetrickými charakteristikami provozu (jako je streamování videa nebo stahování souborů) se však omezení plynoucí z předpokladů symetrie stávala stále zřetelnějšími. Zavedení zpracování ASY v normách 3GPP řeší tato omezení tím, že poskytuje standardizované mechanismy pro rozpoznání, měření a přizpůsobení se asymetrickým podmínkám.

Technická motivace pro zpracování ASY zahrnuje zlepšení spektrální efektivity v asymetrických scénářích, zvýšení uživatelského komfortu pro aplikace s nevyváženými požadavky na UL/DL a umožnění flexibilnějšího nasazení sítí. Explicitním zohledněním asymetrie mohou sítě efektivněji alokovat zdroje, implementovat vhodné mechanismy opravy chyb pro každý směr a udržovat kvalitu služeb i při podstatně odlišných podmínkách UL a DL. To je obzvláště důležité v moderních sítích podporujících různé služby s různými požadavky na UL/DL, od nahrávání dat ze senzorů IoT po stahování videa ve vysokém rozlišení.

## Klíčové vlastnosti

- Explicitní rozpoznání asymetrie UL/DL v síťových podmínkách
- Adaptivní konfigurace fyzické vrstvy pro asymetrické kanály
- Asymetrické plánování MAC a procedury HARQ
- Diferenciální konfigurace parametrů QoS pro přenosové kanály UL a DL
- Samostatné měření a hlášení pro kanály UL a DL
- Podpora asymetrického vynucování zásad v síťové architektuře

## Související pojmy

- [HARQ – Hybrid Automatic Repeat Request](/mobilnisite/slovnik/harq/)

## Definující specifikace

- **TR 26.935** (Rel-19) — Speech Codec Performance for Packet Switched Multimedia

---

📖 **Anglický originál a plná specifikace:** [ASY na 3GPP Explorer](https://3gpp-explorer.com/glossary/asy/)
