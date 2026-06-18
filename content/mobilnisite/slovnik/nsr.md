---
slug: "nsr"
url: "/mobilnisite/slovnik/nsr/"
type: "slovnik"
title: "NSR – Network Status Request"
date: 2025-01-01
abbr: "NSR"
fullName: "Network Status Request"
category: "Core Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/nsr/"
summary: "Signalizační procedura používaná k vyžádání stavu síťové entity nebo služby. Je to základní mechanismus, který umožňuje síťovým prvkům dotazovat se na provozní stav nebo dostupnost jiných prvků, čímž"
---

NSR je signalizační procedura používaná k vyžádání provozního stavu nebo dostupnosti síťové entity nebo služby.

## Popis

Network Status Request (NSR) je základní signalizační procedura v jádrové síti definovaná ve specifikacích 3GPP. Je to obecný mechanismus, kdy jedna síťová entita odešle druhé požadavek na zjištění jejího aktuálního provozního stavu, dostupnosti nebo informací o konkrétních schopnostech. Tato procedura je klíčová pro udržování přehledu o stavu sítě a umožňuje inteligentní směrování, vyvažování zátěže a rozhodování při převzetí služeb při selhání. Požadavek je typicky přenášen standardními signalizačními protokoly, jako je Diameter nebo [MAP](/mobilnisite/slovnik/map/) (Mobile Application Part), v závislosti na síťové doméně a vydání specifikací.

Během provozu zpráva NSR obsahuje identifikátory pro dotazující se a cílový uzel spolu s parametry určujícími typ požadovaných stavových informací. Cílová entita požadavek zpracuje a vrátí Network Status Response obsahující požadovaná data. Tato data mohou zahrnovat jednoduchou binární dostupnost (např. dosažitelný/nedosažitelný), podrobnější informace o zátěži (např. aktuální využití [CPU](/mobilnisite/slovnik/cpu/), počet relací) nebo specifické indikátory podpory služeb. Proceduru často používají síťové prvky jako Serving [GPRS](/mobilnisite/slovnik/gprs/) Support Nodes ([SGSN](/mobilnisite/slovnik/sgsn/)), Mobility Management Entities ([MME](/mobilnisite/slovnik/mme/)) nebo Home Subscriber Servers ([HSS](/mobilnisite/slovnik/hss/)) k určení nejvhodnějšího protějšku pro směrování signalizačních zpráv nebo k ověření stavu síťové cesty před zahájením transakce.

Mechanismus NSR podporuje proaktivní i reaktivní kontrolu stavu. Proaktivně mohou síťové prvky pravidelně dotazovat své protějšky, aby vytvořily dynamickou mapu stavu sítě. Reaktivně může prvek odeslat NSR, když potřebuje vybrat protějšek pro novou proceduru, například pro směrování žádosti o aktualizaci polohy. Tím se zvyšuje spolehlivost a efektivita sítě, protože se zabrání pokusům o komunikaci s nefunkčními nebo přetíženými uzly, což snižuje výskyt signalizačních selhání a zlepšuje celkovou spolehlivost služeb. Jeho implementace je základním kamenem pro funkce jako síťová redundance a řízené postupy vypínání.

## K čemu slouží

Procedura NSR byla vytvořena, aby řešila potřebu dynamického povědomí o stavu sítě v stále složitějších a distribuovaných mobilních jádrových sítích. Rané sítě s přepojováním okruhů měly relativně statickou konfiguraci, ale s vývojem směrem k paketově přepínaným a plně IP jádrovým sítím v 2.5G ([GPRS](/mobilnisite/slovnik/gprs/)) a 3G se sítě staly dynamičtějšími s prvky, které mohly selhat, být přetížené nebo být vyřazeny z provozu z důvodu údržby. Bez standardizovaného mechanismu pro dotazování na stav sítě se sítě spoléhaly na statické směrování nebo detekci selhání pomocí časových limitů, což bylo neefektivní a vedlo ke špatnému uživatelskému zážitku při výpadcích.

NSR tento problém řeší tím, že poskytuje přímou metodu s nízkou režií, pomocí které se síťové prvky mohou vzájemně dotazovat na svůj stav. To umožňuje inteligentní chování sítě, jako je sdílení zátěže mezi více instancemi síťové funkce nebo automatické přeměrování kolem selhání. Je to klíčový prostředek pro vysokou dostupnost a efektivní využití zdrojů. Standardizace této procedury napříč vydáními specifikací zajišťuje interoperabilitu mezi síťovými prvky od různých výrobců, což je zásadní pro vícevýrobcová ekosystémová prostředí běžná v telekomunikačních sítích.

## Klíčové vlastnosti

- Standardizovaná signalizační procedura pro dotazování na stav síťové entity
- Lze přenášet přes protokoly jako Diameter a MAP
- Podporuje dotazy na dostupnost, zátěž a schopnosti služeb
- Umožňuje dynamický výběr protějšků a vyvažování zátěže
- Zvyšuje spolehlivost sítě tím, že se vyhýbá nefunkčním uzlům
- Usnadňuje řízené vypínání a údržbové operace

## Související pojmy

- [MAP – Mobile Application Protocol](/mobilnisite/slovnik/map/)
- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)
- [MME – NPC MME Network Product Class](/mobilnisite/slovnik/mme/)

## Definující specifikace

- **TS 29.153** (Rel-19) — Ns Reference Point Protocol between SCEF and RCAF
- **TS 45.860** (Rel-11) — Precoded EGPRS2 Downlink Study
- **TS 45.871** (Rel-14) — MIMO for GSM/EDGE Downlink Study

---

📖 **Anglický originál a plná specifikace:** [NSR na 3GPP Explorer](https://3gpp-explorer.com/glossary/nsr/)
