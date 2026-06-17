---
slug: "na-esrk"
url: "/mobilnisite/slovnik/na-esrk/"
type: "slovnik"
title: "NA-ESRK – North American - Emergency Service Routing Key"
date: 2025-01-01
abbr: "NA-ESRK"
fullName: "North American - Emergency Service Routing Key"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/na-esrk/"
summary: "Směrovací klíč používaný v Severní Americe k nasměrování nouzových volání (např. na číslo 911) na příslušné středisko tísňového volání (PSAP). Je to klíčový identifikátor, který zajišťuje, že záchrann"
---

NA-ESRK je směrovací klíč používaný v Severní Americe k nasměrování nouzového volání na příslušné středisko tísňového volání (Public Safety Answering Point) na základě polohy volajícího a typu požadované záchranné služby.

## Popis

North American Emergency Service Routing Key (NA-ESRK) je základní součástí architektury služeb určování polohy ([LCS](/mobilnisite/slovnik/lcs/)) definované 3GPP pro zpracování nouzových volání, která je speciálně přizpůsobena regulatornímu prostředí v Severní Americe. Funguje jako dočasný, dynamicky přidělený identifikátor, který je spojen s konkrétní relací nouzového volání a přibližnou zeměpisnou polohou volajícího. NA-ESRK je generován Gateway Mobile Location Centre ([GMLC](/mobilnisite/slovnik/gmlc/)) nebo vyhrazeným Emergency Call Server ([ECS](/mobilnisite/slovnik/ecs/)) po přijetí žádosti o nouzovou službu z mobilní sítě. Tento klíč je pak sítí použit k směrování nouzového volání spolu s přidruženými údaji o poloze na správné středisko tísňového volání (PSAP) odpovědné za danou geografickou oblast.

Z architektonického hlediska NA-ESRK funguje v rámci řídicí roviny jádra sítě, rozhraní se subjekty jako je Mobile Switching Centre ([MSC](/mobilnisite/slovnik/msc/)), Serving [GPRS](/mobilnisite/slovnik/gprs/) Support Node (SGSN) a GMLC. Když mobilní zařízení zahájí nouzové volání, MSC nebo SGSN aktivuje žádost o polohu směrem k GMLC. GMLC po získání odhadované polohy ze sítě (např. pomocí Cell-ID, [OTDOA](/mobilnisite/slovnik/otdoa/) nebo [A-GPS](/mobilnisite/slovnik/a-gps/)) vygeneruje pro toto volání jedinečný NA-ESRK. Tento klíč je pak vrácen MSC/SGSN a je zahrnut do signalizace při sestavování volání (např. v rámci Initial Address Message v [ISUP](/mobilnisite/slovnik/isup/) nebo SIP INVITE v IMS). Klíč v podstatě funguje jako korelační token po celou dobu trvání volání.

Hlavní úlohou NA-ESRK je umožnit efektivní a přesné směrování v legacy okruhově přepínaných nouzových službách, kde signalizační cesta pro řízení volání je oddělena od cesty používané k doručení informace o poloze. Vložením NA-ESRK do signalizace volání jej může selektivní router nebo síť nouzových služeb použít jako vyhledávací klíč k získání informace o poloze volajícího z vyhrazené databáze, jako je Location Information Server (LIS) nebo samotný GMLC, ještě předtím, než je volání přijato na PSAP. Tento proces, známý jako 'směrování na základě polohy', zajišťuje, že volání dorazí na PSAP, který má jurisdikci nad polohou volajícího, což je klíčové pro vyslání policie, hasičů nebo zdravotnické služby. Klíč je typicky platný pouze po dobu trvání relace nouzového volání a je po jejím skončení uvolněn pro opětovné použití.

## K čemu slouží

NA-ESRK byl vytvořen, aby řešil kritickou potřebu přesného a spolehlivého směrování bezdrátových nouzových volání na příslušné místní středisko tísňového volání (PSAP) v Severní Americe. Před jeho standardizací bylo směrování nouzových volání pro mobilní uživatele primárně založeno na poloze buňky, což mohlo být nepřesné, zejména pokud buňka pokrývala širokou oblast nebo více hranic jurisdikcí. To často vedlo k nesprávně směrovaným voláním, zpožděním v reakci záchranných služeb a potenciálně život ohrožujícím situacím. Stávající infrastruktura telefonní sítě pro nouzové služby (E911) byla navržena pro pevné linky, kde je adresa volajícího statická a známá.

Zavedení NA-ESRK v rámci standardů 3GPP poskytlo standardizovaný mechanismus pro propojení dynamických schopností určování polohy mobilní sítě s legacy infrastrukturou nouzových služeb. Řeší problém korelace živého hlasového volání s dynamicky získanými údaji o poloze v síti, kde tyto dvě informace putují různými cestami. Poskytnutím jedinečného směrovacího klíče umožňuje mechanismus 'zpětného volání'; pokud je volání přerušeno, může PSAP použít NA-ESRK k dotazování sítě na poslední známou polohu volajícího. Jeho vytvoření bylo silně motivováno regulatorními požadavky ve Spojených státech (požadavky FCC E911 Fáze II) a v Kanadě, které nutily bezdrátové operátory poskytovat přesnější informace o poloze pro nouzová volání.

## Klíčové vlastnosti

- Dynamicky generovaný jedinečný identifikátor pro každou relaci nouzového volání
- Umožňuje korelaci nouzového hlasového volání s údaji o poloze účastníka
- Umožňuje směrování na základě polohy na správnou jurisdikci PSAP
- Integruje se s legacy selektivními routery severoamerické sítě E911
- Podporuje zpětné volání a získání polohy u přerušených nouzových volání
- Definován v rámci architektury 3GPP LCS pro splnění regulatorních požadavků

## Související pojmy

- [GMLC – Gateway Mobile Location Center](/mobilnisite/slovnik/gmlc/)
- [LCS – Location Services](/mobilnisite/slovnik/lcs/)

## Definující specifikace

- **TS 22.071** (Rel-19) — 3GPP TS 22.071: Location Services (LCS) Stage 1
- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TS 32.272** (Rel-19) — Charging for Push-to-Talk over Cellular (PoC)

---

📖 **Anglický originál a plná specifikace:** [NA-ESRK na 3GPP Explorer](https://3gpp-explorer.com/glossary/na-esrk/)
