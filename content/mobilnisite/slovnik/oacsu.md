---
slug: "oacsu"
url: "/mobilnisite/slovnik/oacsu/"
type: "slovnik"
title: "OACSU – Off-Air Call Set Up"
date: 2025-01-01
abbr: "OACSU"
fullName: "Off-Air Call Set Up"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/oacsu/"
summary: "Provozní a údržbový postup, při kterém se testují schopnosti mobilního zařízení zpracovávat hovory bez nutnosti aktivního rádiového spojení se živou sítí. Provádí se v řízeném, odstíněném prostředí za"
---

OACSU je provozní a údržbový postup pro testování schopností mobilního zařízení zpracovávat hovory v odstíněném prostředí bez živého rádiového spojení.

## Popis

Off-Air Call Set Up (OACSU) je typ testu shody a provozního postupu definovaného v manažerských specifikacích 3GPP. Zahrnuje navázání hovoru nebo datové relace s mobilním zařízením (UE) v laboratorním nebo odstíněném testovacím prostředí, kde je zařízení připojeno přímo k testovacímu systému přes kabelové rozhraní, například koaxiální kabel, čímž se obejde přenos přes rádiové rozhraní ([OTA](/mobilnisite/slovnik/ota/)). Primárním cílem je izolovat a otestovat zpracování v základním pásmu (baseband), implementaci protokolového zásobníku a logiku řízení hovorů v zařízení bez proměnných a možných zkreslení zavedených [RF](/mobilnisite/slovnik/rf/) kanálem.

Testovací uspořádání typicky zahrnuje simulátor systému (např. emulátor základnové stanice) a testované UE, propojené přes RF kabel s kalibrovaným atenuátorem pro simulaci útlumu na dráze. Simulátor vystupuje jako síť a generuje veškerou potřebnou signalizaci pro procedury jako připojení (attach), aktualizace polohy a navázání hovoru. Testy OACSU ověřují, že UE správně generuje a reaguje na signalizační zprávy vrstvy 3 (např. [CM](/mobilnisite/slovnik/cm/) SERVICE REQUEST, SETUP, ALERTING) podle specifikací 3GPP. Kontrolují časovače, sekvence zpráv a zpracování chyb v opakovatelném a řízeném režimu.

Tato metoda je klíčová pro testování konzistence protokolů, předcertifikační ověření interoperability a hlubokou diagnostiku problémů. Protože je RF spojení řízené a ideální, lze případné chyby přímo připsat problémům v softwaru nebo hardwaru základního pásma (baseband) v UE, nikoliv špatným rádiovým podmínkám. OACSU je často předpokladem pro komplexnější testování přes rádiové rozhraní (OTA). Umožňuje inženýrům ověřit základní shodu s protokoly před zavedením složitostí jako únik (fading), interference a mobilita. Specifikace detailně popisují přesné testovací scénáře, očekávané zprávy a kritéria úspěšnosti/neúspěšnosti, což zajišťuje standardizované měřítko pro validaci výkonu UE.

## K čemu slouží

OACSU byl vyvinut pro potřeby efektivního, spolehlivého a opakovatelného testování shody protokolů mobilních zařízení během vývoje, certifikace a výroby. Před zavedením těchto standardizovaných off-air testů se hodně validace spoléhalo na testy v živé síti nebo základní laboratorní uspořádání, což bylo časově náročné, neopakovatelné a neumožňovalo izolovat problémy s protokoly od problémů s rádiovým přenosem. To činilo ladění komplexních selhání hovorů extrémně obtížným.

Tento postup řeší problém validace základní inteligence zpracování hovorů v UE nezávisle na jejím rádiovém výkonu. Umožňuje výrobcům identifikovat a opravit chyby v protokolovém zásobníku již v rané fázi vývojového cyklu. Pro síťové operátory a certifikační orgány (jako [GCF](/mobilnisite/slovnik/gcf/) nebo PTCRB) poskytuje OACSU řízené měřítko pro zajištění, že UE splňuje základní standardy interoperability, než je povoleno v síti, čímž snižuje riziko, že zařízení způsobí nestabilitu sítě kvůli nevyhovující signalizaci. Je to základní prvek procesu schvalování zařízení, který zajišťuje základní úroveň kvality a spolehlivosti pro všechna zařízení připojující se k sítím založeným na 3GPP.

## Klíčové vlastnosti

- Umožňuje testování navazování hovorů a relací v odstíněném, kabelovém prostředí, což eliminuje proměnné spojené s rádiovým přenosem přes vzduch (over-the-air).
- Zaměřuje validaci na implementaci protokolového zásobníku v UE, sekvencování zpráv a časovače.
- Používá simulátor/emulátor základnové stanice, který vystupuje jako síť a řídí testovací procedury.
- Poskytuje opakovatelné a řízené testovací podmínky nezbytné pro certifikaci shody a ladění problémů.
- Definuje konkrétní testovací scénáře a kritéria úspěšnosti/neúspěšnosti v manažerských a testovacích specifikacích 3GPP.
- Slouží jako předpoklad a doplněk k testování RF výkonu a správy rádiových prostředků přes rádiové rozhraní (Over-The-Air - OTA).

## Definující specifikace

- **TS 32.401** (Rel-19) — Performance Management Concept & Requirements
- **TS 52.402** (Rel-19) — GSM Performance Management Measurements

---

📖 **Anglický originál a plná specifikace:** [OACSU na 3GPP Explorer](https://3gpp-explorer.com/glossary/oacsu/)
