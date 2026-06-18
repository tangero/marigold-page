---
slug: "ttt"
url: "/mobilnisite/slovnik/ttt/"
type: "slovnik"
title: "TTT – Time To Trigger"
date: 2025-01-01
abbr: "TTT"
fullName: "Time To Trigger"
category: "Mobility"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ttt/"
summary: "TTT je časovač používaný v procedurách předání spojení a převýběru buňky v LTE a 5G NR. Definuje, jak dlouho musí být měřicí podmínka (např. že signál sousední buňky je lepší než signál obsluhující bu"
---

TTT je časovač, který definuje, jak dlouho musí být měřicí podmínka trvale splněna, než UE zahájí předání spojení (handover) nebo převýběr buňky, čímž se zabraňuje ping-pong efektům v LTE a 5G NR.

## Popis

Time To Trigger (TTT) je klíčový hysterezní parametr v procedurách správy mobility na vrstvě 3 (Layer 3) v uživatelském zařízení (UE) v LTE ([E-UTRAN](/mobilnisite/slovnik/e-utran/)) a NR (NG-RAN). Jde o konfigurovatelný časovač, který síť vysílá v systémových informacích (např. SIB3, SIB4, SIB5 v LTE) nebo poskytuje prostřednictvím dedikované signalizace [RRC](/mobilnisite/slovnik/rrc/). TTT funguje ve spojení s hlášením měření spouštěným událostmi. Například pro událost [A3](/mobilnisite/slovnik/a3/) (sousední buňka se stane o offset lepší než obsluhující buňka) UE kontinuálně vyhodnocuje podmínku. Teprve když je tato podmínka splněna *nepřerušovaně* po celou dobu trvání časovače TTT, odešle UE hlášení měření do sítě, což může spustit příkaz k předání spojení.

Architektura zahrnuje entitu protokolu RRC v UE, která spravuje konfiguraci měření přijatou od gNB nebo [eNB](/mobilnisite/slovnik/enb/). Tato konfigurace obsahuje identifikátor měřicí události, offsety, hysterézi a hodnotu TTT. Fyzická vrstva UE provádí měření Reference Signal Received Power ([RSRP](/mobilnisite/slovnik/rsrp/)) nebo Reference Signal Received Quality ([RSRQ](/mobilnisite/slovnik/rsrq/)). Tato surová měření jsou filtrována (filtrování vrstvy 3) a následně vyhodnocena entitou RRC vůči vstupní podmínce události. Trvalé splnění podmínky spustí časovač TTT. Pokud podmínka přestane být splněna kdykoli před vypršením časovače, je časovač resetován. Tento mechanismus přidává vrstvu filtrování proti krátkodobým výkyvům signálu způsobeným rychlým únikem (fast fading), pohybem uživatele nebo rušením v prostředí.

Jak to funguje v praxi: UE se pohybuje směrem k sousední buňce. RSRP sousední buňky pomalu stoupne nad RSRP obsluhující buňky (plus jakýkoli nakonfigurovaný offset). Podmínka události A3 se stane pravdivou. UE spustí časovač TTT (např. nastavený na 320 ms). Pokud po těchto 320 ms zůstane sousední buňka lepší, je odesláno hlášení měření. Pokud se během této doby signál obsluhující buňky krátce znovu zlepší, podmínka přestane platit, časovač se resetuje a žádné hlášení se neodešle. Tím se zabrání zbytečným předáním spojení během přechodných stavů. Úlohou TTT je zavést záměrné zpoždění do procesu rozhodování o mobilitě, což obětuje mírné zpoždění v dosažení optimální konektivity ve prospěch výrazně lepší stability sítě, snížení signalizační zátěže a vyšší celkové uživatelské zkušenosti díky vyhýbání se přerušením hovorů kvůli ukvapeným nebo oscilujícím předáním spojení.

## K čemu slouží

TTT bylo zavedeno, aby vyřešilo kritický problém ping-pong předání spojení a nestabilní mobility v celulárních sítích. V raných mobilních algoritmech, které reagovaly okamžitě na prahové hodnoty měření, mohly rychlé výkyvy síly rádiového signálu – způsobené rychlým únikem (fast fading), tím, že se uživatel otočí za roh, nebo dočasnými překážkami – způsobit, že se UE opakovaně předávala mezi dvěma buňkami během sekund. Tento 'ping-pong' efekt vytváří nadměrnou signalizační zátěž na síti, spotřebovává baterii UE, zvyšuje riziko selhání předání spojení a přerušení hovoru a zhoršuje uživatelsky vnímaný výkon.

Účelem TTT je přidat hysterezi v časové oblasti. Tím, že vyžaduje, aby potenciální cílová buňka byla konzistentně lepší po definované období, síť odfiltruje krátkodobé, nevýznamné výkyvy signálu a reaguje pouze na setrvalé trendy naznačující skutečný pohyb uživatele. Tím se zajistí, že předání spojení jsou spouštěna pouze pro stabilní, dlouhodobější změny v rádiovém prostředí. Motivací byla potřeba automatizovaného, robustního řízení mobility v ploché IP architektuře LTE a v 5G NR se stala ještě důležitější kvůli použití vyšších frekvencí (náchylnějších k blokování a výkyvům) a hustým nasazením. TTT umožňuje síťovým operátorům jemně ladit agresivitu předání spojení; krátký TTT činí systém citlivým pro vysokorychlostní uživatele, zatímco delší TTT podporuje stabilitu u pomalu se pohybujících nebo stacionárních uživatelů s kolísavým signálem.

## Klíčové vlastnosti

- Konfigurovatelný časovač, který zavádí hysterézi do hlášení měření spouštěného událostmi
- Vysílán v systémových informacích nebo konfigurován prostřednictvím dedikované signalizace RRC
- Funguje s měřicími událostmi jako A3 (sousední buňka lepší než obsluhující) a B1/B2 (inter-RAT)
- Okamžitě se resetuje, pokud se spouštěcí podmínka stane nepravdivou před vypršením časovače
- Klíčový parametr pro optimalizaci výkonu předání spojení a minimalizaci míry ping-pong efektů
- Hodnoty se pohybují od milisekund po sekundy, což umožňuje kompromis mezi rychlostí odezvy a stabilitou

## Definující specifikace

- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification
- **TS 38.321** (Rel-19) — NR MAC Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [TTT na 3GPP Explorer](https://3gpp-explorer.com/glossary/ttt/)
