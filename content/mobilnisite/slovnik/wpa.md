---
slug: "wpa"
url: "/mobilnisite/slovnik/wpa/"
type: "slovnik"
title: "WPA – Wrong Password Attempts"
date: 2025-01-01
abbr: "WPA"
fullName: "Wrong Password Attempts"
category: "Security"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/wpa/"
summary: "Bezpečnostní čítač sledující počet po sobě jdoucích nesprávných zadání hesla během autentizačních procedur. Jedná se o základní mechanismus pro prevenci útoků hrubou silou a neoprávněných pokusů o pří"
---

WPA (Wrong Password Attempts – pokusy o zadání nesprávného hesla) je bezpečnostní čítač, který sleduje po sobě jdoucí nesprávné zadání hesla během autentizace, aby zabránil útokům hrubou silou v sítích 3GPP, a spouští ochranné akce při překročení stanoveného prahu.

## Popis

Wrong Password Attempts (WPA – pokusy o zadání nesprávného hesla) je bezpečnostní čítač definovaný ve specifikacích 3GPP, primárně pro IP Multimedia Subsystem (IMS) a související služby. Funguje jako stavová proměnná udržovaná sítí, typicky v rámci Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) nebo aplikačního serveru, za účelem monitorování neúspěšných autentizací pro konkrétní uživatelskou identitu, jako je Private User Identity ([IMPI](/mobilnisite/slovnik/impi/)). Čítač se zvýší pokaždé, když autentizační požadavek (např. během registrace v IMS nebo vyvolání služby) selže kvůli nesprávnému heslu nebo sdílenému tajemství v odpovědi. Tento mechanismus je nedílnou součástí rámce Authentication and Key Agreement ([AKA](/mobilnisite/slovnik/aka/)) a poskytuje první linii obrany proti systematickým útokům hádáním.

Operační logika zahrnuje přednastavený maximální práh. Když čítač WPA dosáhne tohoto limitu, síť vynutí bezpečnostní politiku, která obvykle zahrnuje uzamčení autentizační schopnosti uživatele. Toto uzamčení zabrání dalším pokusům o autentizaci po definované období nebo dokud není proveden administrativní reset, čímž efektivně znemožní automatizovaným skriptům nekonečně zkoušet kombinace hesel. Čítač se typicky resetuje na nulu po úspěšné autentizaci, čímž legitimní uživatelé po opravě svého vstupu opět získají přístup. Jeho správa je specifikována v protokolech mezi Serving-Call Session Control Function ([S-CSCF](/mobilnisite/slovnik/s-cscf/)) a HSS, jako je rozhraní Cx využívající příkazy Diameter.

Z architektonického hlediska je WPA součástí širší správy dat účastníků a vynucování bezpečnostních politik. Funguje ve spojení s dalšími bezpečnostními mechanismy, jako je generování autentizačních vektorů v HSS a ochrana integrity signalizace. Poskytnutím jednoduché, ale účinné funkce omezování rychlosti doplňuje WPA kryptografickou bezpečnost přidáním provozní bariéry. Jeho implementace je klíčová pro splnění regulatorních a komerčních požadavků na zabezpečený přístup a tvoří základní, avšak nezbytnou část vrstveného bezpečnostního modelu v sítích 3GPP, který chrání jak síťové prostředky, tak uživatelská data před útoky založenými na přihlašovacích údajích.

## K čemu slouží

Čítač WPA byl zaveden, aby řešil zranitelnost systémů autentizace založených na hesle vůči útokům hrubou silou a slovníkovým útokům. Před jeho standardizací mohly být sítě náchylné k útočníkům opakovaně zkoušejícím běžná hesla bez bezprostředních následků, což mohlo vést k neoprávněnému přístupu. Primární problém, který řeší, je automatizované vysokorychlostní hádání uživatelských přihlašovacích údajů, což představuje významnou hrozbu vzhledem k tomu, že uživatelsky volená hesla jsou často slabá.

Jeho vytvoření bylo motivováno potřebou standardizované, sítí vynucované bezpečnostní politiky, která jde nad rámec kryptografické síly. Zatímco protokol [AKA](/mobilnisite/slovnik/aka/) poskytuje robustní vzájemnou autentizaci, předpokládá, že sdílené tajemství není snadno uhodnutelné. WPA přidává nekryptografickou vrstvu ochrany pro scénáře, kdy by tajemství mohlo být kompromitováno hádáním. Poskytuje jasný, implementovatelný mechanismus pro operátory, jak takovým útokům bránit a detekovat je, čímž naplňuje požadavky na zodpovědnou správu bezpečnosti.

Historicky, jak se sítě 3GPP vyvíjely k poskytování služeb založených na IP, jako je IMS, rozšířila se škála hrozeb za tradiční podvody v přepojování okruhů. Zavedení WPA ve verzi Release 5 spolu s ranými specifikacemi IMS poskytlo základní bezpečnostní kontrolu pro tyto nové služby. Řeší omezení spočívající v pouhém spoléhání se na složitost sdíleného tajemství vynucením pevného limitu pokusů, čímž činí útoky nepraktickými prostřednictvím časových zpoždění a uzamčení, a chrání tak jak síť, tak dostupnost služeb pro uživatele.

## Klíčové vlastnosti

- Sleduje po sobě jdoucí neúspěšné autentizace pro uživatelskou identitu
- Zvyšuje se po přijetí nesprávného hesla v autentizační odpovědi
- Porovnává se s konfigurovatelnou hodnotou maximálního prahu
- Při překročení prahu spouští uzamčení účastníka nebo jinou bezpečnostní politiku
- Po úspěšné autentizaci se resetuje na nulu
- Spravuje se jako součást dat účastníka v HSS/HLR nebo aplikačním serveru

## Související pojmy

- [AKA – Authentication and Key Agreement](/mobilnisite/slovnik/aka/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 24.623** (Rel-19) — XCAP Protocol for Supplementary Services

---

📖 **Anglický originál a plná specifikace:** [WPA na 3GPP Explorer](https://3gpp-explorer.com/glossary/wpa/)
