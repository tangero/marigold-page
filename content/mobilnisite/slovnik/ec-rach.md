---
slug: "ec-rach"
url: "/mobilnisite/slovnik/ec-rach/"
type: "slovnik"
title: "EC-RACH – Extended Coverage Random Access Channel"
date: 2025-01-01
abbr: "EC-RACH"
fullName: "Extended Coverage Random Access Channel"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ec-rach/"
summary: "Kanál GSM/EDGE, který umožňuje IoT zařízením ve slabém pokrytí navázat kontakt se sítí. Používá opakované přístupové výbuchy a robustní modulaci pro překonání vysokého útlumu na dráze, což umožňuje za"
---

EC-RACH je kanál GSM/EDGE, který umožňuje IoT zařízením ve slabém pokrytí navázat kontakt se sítí pomocí opakovaných přístupových výbuchů a robustní modulace pro překonání vysokého útlumu na dráze.

## Popis

Extended Coverage Random Access Channel (EC-RACH) je logický uplinkový kanál v GSM/[EDGE](/mobilnisite/slovnik/edge/) rádiové přístupové síti ([GERAN](/mobilnisite/slovnik/geran/)) specifikovaný v 3GPP TS 44.060. Je základní součástí systému Extended Coverage GSM (EC-GSM), navrženého speciálně pro aplikace Cellular Internet of Things (CIoT). EC-RACH používá uživatelské zařízení (UE), typicky IoT zařízení, k vyžádání počátečního připojení nebo přidělení zdrojů od sítě. Tento postup náhodného přístupu je prvním uplinkovým přenosem zařízení a je klíčový pro scénáře jako odesílání senzorových dat, navázání spojení po pagingu nebo provedení aktualizace polohy. Kanál je optimalizován pro prostředí s extrémním útlumem signálu, kde by standardní postup GSM [RACH](/mobilnisite/slovnik/rach/) selhal kvůli nedostatečné síle signálu na přijímači základnové stanice.

Z architektonického hlediska je EC-RACH mapován na specifické fyzické zdroje v rámci struktury GSM multiframe. Funguje na stejném fyzickém kanálu jako legacy RACH, ale používá odlišný, robustnější formát známý jako Coverage Enhanced Access Burst (CEAB). Přenosový mechanismus je založen na principu opakování a přeskakování kmitočtů. Zařízení pokoušející se o náhodný přístup vysílá sekvenci identických CEABů, nikoliv pouze jeden výbuch. Počet vyslaných výbuchů je určen pokrytím zařízení (coverage class), které je odhadnuto na základě přijímané úrovně signálu downlinkových vysílacích kanálů ([EC-BCCH](/mobilnisite/slovnik/ec-bcch/)/[EC-SCH](/mobilnisite/slovnik/ec-sch/)). Například zařízení ve Coverage Class 3 může vyslat 16 po sobě jdoucích CEABů. Tyto výbuchy jsou rozprostřeny přes různé časové sloty a kmitočty podle předdefinovaného vzoru, což poskytuje diverzitu v čase i kmitočtu pro potlačení úniků a rušení.

Technický provoz zahrnuje několik klíčových kroků. Nejprve se zařízení synchronizuje se sítí pomocí EC-SCH a načte systémové informace z EC-BCCH, které zahrnují parametry pro přístup k EC-RACH, jako jsou dostupné kmitočty a mapování pokrytí. Zařízení poté vybere pokrytí na základě změřeného útlumu na downlinku. Když potřebuje přistoupit k síti, vysílá požadovaný počet opakování CEAB na EC-RACH. Každý CEAB nese zkrácenou tréninkovou sekvenci a 8bitovou část dat, která přenáší náhodné referenční číslo. Základnová stanice po detekci těchto opakovaných výbuchů je může kombinovat, aby zvýšila pravděpodobnost detekce. Po detekci síť odpoví zprávou Immediate Assignment na Extended Coverage Access Grant Channel ([EC-AGCH](/mobilnisite/slovnik/ec-agch/)), která přiděluje vyhrazené zdroje pro zařízení, aby mohlo pokračovat v navazování spojení. Robustní návrh CEABu v kombinaci s opakováním umožňuje EC-RACH spolehlivě fungovat při ztrátách na trase až do 164 dB.

## K čemu slouží

EC-RACH byl vyvinut k řešení kritického problému, jak mohou IoT zařízení umístěná v extrémně špatných podmínkách pokrytí navázat počáteční kontakt s GSM sítí. V tradičních mobilních sítích je Random Access Channel ([RACH](/mobilnisite/slovnik/rach/)) branou pro jakékoli zařízení k vyžádání služby. Standardní GSM RACH však používá jediný, krátký přístupový výbuch, který je velmi náchylný k selhání při významném útlumu na dráze, rušení nebo únicích. Pro IoT zařízení nasazená v náročných prostředích, jako jsou podzemní šachty, hluboko v průmyslových provozech nebo ve venkovských oblastech na okraji pokrytí buňky, to znamenalo, že byla efektivně izolována – nemohla odesílat data ani se registrovat v síti. Toto omezení bylo hlavní překážkou pro využití stávající GSM infrastruktury pro spolehlivá hromadná IoT nasazení.

Vytvoření EC-RACH bylo hnací silou iniciativy 3GPP Cellular IoT v Release 13, jejímž cílem bylo přizpůsobit GSM sítě pro aplikace s nízkým výkonem a širokou oblastí pokrytí ([LPWA](/mobilnisite/slovnik/lpwa/)). Klíčovým výkonnostním cílem byla podpora maximální ztráty na trase (MCL) 164 dB, což vyžadovalo 20 dB zlepšení oproti legacy GSM. Proces náhodného přístupu je nejzranitelnějším článkem na uplinku, protože probíhá před jakoukoli uzavřenou smyčkou řízení výkonu nebo přesným časovým zarovnáním. EC-RACH to řeší zavedením robustního, opakovaného přístupového výbuchu (CEAB), který dává síti více šancí detekovat pokus zařízení o přístup. To zajišťuje, že i zařízení na samé hranici pokrytí mohou úspěšně zahájit komunikaci.

Před EC-GSM měli operátoři omezené možnosti pro obsluhu zařízení na takových místech, což často vedlo k mrtvým zónám pro MTC. Proprietární řešení nebo prosté nasazení více základnových stanic bylo nákladné a neefektivní. EC-RACH poskytuje standardizovanou, síťově efektivní metodu. Umožňuje síti podporovat mix legacy zařízení a nových CIoT zařízení na stejném nosiči. Mechanismus pokrytí zajišťuje, že zařízení používají pouze nezbytnou úroveň opakování, čímž šetří životnost baterie zařízení a snižuje uplinkové rušení. Řešením problému počátečního přístupu umožňuje EC-RACH plné využití potenciálu EC-GSM pro aplikace, jako jsou chytré měření, sledování majetku a monitorování životního prostředí, kde musí zařízení fungovat autonomně po mnoho let a prakticky z jakéhokoli místa.

## Klíčové vlastnosti

- Používá Coverage Enhanced Access Bursts (CEAB) s robustní modulací pro lepší detekci při nízkém SNR
- Využívá opakování přenosu na základě pokrytí zařízení (např. 4, 8, 16, 32 výbuchů) pro překonání vysokého útlumu na dráze
- Začleňuje přeskakování kmitočtů mezi opakovanými výbuchy pro zajištění kmitočtové diverzity a zmírnění rušení
- Nese v každém výbuchu 8bitový náhodný reference pro jedinečnou identifikaci pokusu o přístup
- Navrženo pro provoz při maximální ztrátě na trase (MCL) 164 dB, což umožňuje přístup z extrémních lokalit
- Spolupracuje s EC-AGCH pro odezvu sítě, čímž dokončuje proceduru náhodného přístupu s rozšířeným pokrytím

## Související pojmy

- [EC-PCH – Extended Coverage Paging Channel](/mobilnisite/slovnik/ec-pch/)
- [EC-SCH – Extended Coverage Synchronization Channel](/mobilnisite/slovnik/ec-sch/)
- [EC-AGCH – Extended Coverage Access Grant CHannel](/mobilnisite/slovnik/ec-agch/)

## Definující specifikace

- **TS 44.060** (Rel-19) — GERAN RLC/MAC Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [EC-RACH na 3GPP Explorer](https://3gpp-explorer.com/glossary/ec-rach/)
