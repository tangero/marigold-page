---
slug: "mc-hsdpa"
url: "/mobilnisite/slovnik/mc-hsdpa/"
type: "slovnik"
title: "MC-HSDPA – Multi-Carrier High Speed Downlink Packet Access"
date: 2025-01-01
abbr: "MC-HSDPA"
fullName: "Multi-Carrier High Speed Downlink Packet Access"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/mc-hsdpa/"
summary: "Vylepšení HSPA podle 3GPP, které umožňuje uživatelskému zařízení (UE) přijímat data současně na více downlinkových nosných frekvencích. Agreguje kapacitu dvou nebo více 5MHz nosičů WCDMA, což výrazně"
---

MC-HSDPA je vylepšení HSPA podle 3GPP, které agreguje kapacitu dvou nebo více 5MHz nosičů WCDMA, což umožňuje uživatelskému zařízení (UE) přijímat data současně na více downlinkových frekvencích, čímž zvyšuje špičkové přenosové rychlosti a spektrální účinnost.

## Popis

Multi-Carrier [HSDPA](/mobilnisite/slovnik/hsdpa/) (MC-HSDPA) je klíčová funkce v rádiové přístupové technologii 3GPP UMTS/[HSPA](/mobilnisite/slovnik/hspa/), konkrétně definovaná od Release 10. Jedná se o vývojový krok od jednodrážďového HSDPA, který umožňuje nakonfigurovat uživatelskému zařízení (UE) více downlinkových nosičů, takže může přijímat data na nich současně. Každý nosič je standardní 5MHz nosič [WCDMA](/mobilnisite/slovnik/wcdma/) a UE agreguje zdroje fyzické vrstvy (kanalizační kódy, výkon) z těchto nosičů, aby dosáhlo vyšší celkové downlinkové propustnosti. Primární obslužná buňka, známá jako Anchor Carrier (kotvící nosič), zpracovává řídicí signalizaci jako [RRC](/mobilnisite/slovnik/rrc/), zatímco další Secondary Carriers (sekundární nosiče) se používají primárně pro přenos dat.

Z technického pohledu MC-HSDPA funguje tak, že přiřadí UE primární rušící kód a přidružené [HS-PDSCH](/mobilnisite/slovnik/hs-pdsch/) (High Speed Physical Downlink Shared Channels) na kotvícím nosiči. Síť pak může aktivovat jeden nebo více sekundárních nosičů, každý s vlastní sadou HS-PDSCH. UE musí podporovat potřebný počet přijímacích řetězců (typicky dva pro dvoudrážďový provoz), aby mohlo současně demodulovat signály z více nosičů. Plánování se provádí na každém nosiči zvlášť, což znamená, že plánovač Node B může přidělovat zdroje na každém aktivním nosiči nezávisle, ačkoliv je možná koordinace mezi nosiči pro optimalizaci výkonu. UE hlásí indikátory kvality kanálu ([CQI](/mobilnisite/slovnik/cqi/)) samostatně pro každý nakonfigurovaný nosič.

Architektura zahrnuje vylepšení jak Node B, tak UE. Node B musí podporovat vysílání na více nosičích ze stejného sektoru a spravovat funkci agregace nosičů. Schopnosti UE jsou definovány jeho HSPA multi-carrier kategorií, která specifikuje maximální počet současně podporovaných nosičů a přidruženou špičkovou přenosovou rychlost. Například [DC-HSDPA](/mobilnisite/slovnik/dc-hsdpa/) (dvoudrážďové) UE v Release 10 může agregovat dva sousední nosiče ve stejném pásmu, čímž se zdvojnásobí teoretická špičková přenosová rychlost ve srovnání s jednodrážďovým HSDPA (např. z 21 Mbps na 42 Mbps s [64QAM](/mobilnisite/slovnik/64qam/)). Pozdější release tuto možnost rozšířily na nesousední nosiče a agregaci napříč různými kmitočtovými pásmy.

Úlohou MC-HSDPA je zvýšit downlinkovou kapacitu a uživatelský komfort sítí UMTS/HSPA bez nutnosti úplné migrace na novou RAT jako LTE. Efektivněji využívá fragmentované nebo spárované spektrální držby tím, že umožňuje operátorům kombinovat nosiče. Tato funkce zahrnuje mechanismy pro správu nosičů, jako je aktivace, deaktivace a rekonfigurace prostřednictvím signalizace RRC, což síti umožňuje dynamicky upravovat konfiguraci nosičů UE na základě zatížení provozem, schopností UE a rádiových podmínek. To poskytuje plynulejší migrační cestu a prodlužuje konkurenceschopnou životnost sítí HSPA vedle se rozvíjejících nasazení 4G a 5G.

## K čemu slouží

MC-HSDPA bylo vyvinuto, aby řešilo rostoucí poptávku po vyšších přenosových rychlostech mobilního širokopásmového připojení v rámci stávajícího spektra a infrastruktury UMTS. Jak rostla uživatelská poptávka po downlinkově orientovaných službách (jako je streamování videa a prohlížení webu), jednodrážďové HSDPA s maximem 15 kódy na jednom 5MHz nosiči naráželo na praktické limity propustnosti. Operátoři potřebovali nákladově efektivní způsob, jak zvýšit špičkové rychlosti a kapacitu buněk, aniž by museli okamžitě nasazovat zcela novou rádiovou přístupovou technologii, která by vyžadovala nové spektrum a úplné síťové překrytí.

Tato technologie řeší problém fragmentace spektra a neefektivního využití spárovaných bloků spektra. Mnoho operátorů vlastnilo více 5MHz FDD nosičů ve stejném nebo různých pásmech. MC-HSDPA jim umožnilo agregovat tyto nosiče a poskytnout koncovému uživateli širší virtuální přenosovou cestu. To bylo efektivnější využití kapitálu než nasazení samostatných, neagregovaných nosičů obsluhujících různé uživatele. Také to zlepšilo uživatelský komfort snížením latence a zvýšením propustnosti, zejména pro uživatele ve středu buňky s dobrými signálovými podmínkami, kteří mohli využít celou agregovanou šířku pásma.

Historicky MC-HSDPA následovalo trajektorii vývoje HSPA a navázalo na funkce jako MIMO a modulace vyššího řádu (64QAM). Jeho vznik byl motivován potřebou udržet HSPA konkurenceschopné v době začínajícího nasazování LTE, neboť poskytovalo významné zvýšení výkonu s relativně skromnými upgrady stávajícího hardwaru Node B a čipových sad UE. Umožnilo operátorům nabízet služby 'HSPA+' s deklarovanými rychlostmi srovnatelnými s raným LTE, překlenulo tak výkonnostní propast a poskytlo vysokorychlostní datovou vrstvu v širších pokrytých oblastech během přechodu na 4G.

## Klíčové vlastnosti

- Agreguje více 5MHz downlinkových nosičů WCDMA pro jedno uživatelské zařízení (UE)
- Definuje Anchor Carrier (kotvící nosič) pro řízení a Secondary Carriers (sekundární nosiče) pro data
- Zvyšuje špičkové downlinkové přenosové rychlosti úměrně počtu nosičů
- Podporuje aktivaci/deaktivaci nosičů pro dynamické řízení zdrojů
- Vyžaduje UE s více přijímacími řetězci (např. 2 pro DC-HSDPA)
- Zvyšuje spektrální účinnost a kapacitu buněk sítí UMTS/HSPA

## Související pojmy

- [HSPA – High Speed Packet Access](/mobilnisite/slovnik/hspa/)
- [HSUPA – High Speed Uplink Packet Access](/mobilnisite/slovnik/hsupa/)
- [DC-HSDPA – Dual Cell High Speed Downlink Packet Access](/mobilnisite/slovnik/dc-hsdpa/)

## Definující specifikace

- **TS 25.102** (Rel-19) — UTRA TDD RF Characteristics
- **TS 25.142** (Rel-19) — UTRA TDD Base Station RF Test Methods

---

📖 **Anglický originál a plná specifikace:** [MC-HSDPA na 3GPP Explorer](https://3gpp-explorer.com/glossary/mc-hsdpa/)
