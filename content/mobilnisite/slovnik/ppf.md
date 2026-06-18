---
slug: "ppf"
url: "/mobilnisite/slovnik/ppf/"
type: "slovnik"
title: "PPF – Paging Proceed Flag"
date: 2026-01-01
abbr: "PPF"
fullName: "Paging Proceed Flag"
category: "Mobility"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ppf/"
summary: "Příznak na straně sítě používaný při správě mobility k řízení, zda mají pokračovat pokusy o paging mobilního zařízení. Pomáhá optimalizovat pagingové procedury a spravovat síťové zdroje tím, že indiku"
---

PPF je příznak na straně sítě používaný při správě mobility k řízení, zda mají pokračovat pokusy o paging mobilního zařízení, čímž optimalizuje procedury a využití zdrojů.

## Popis

Paging Proceed Flag (PPF, příznak pokračování pagingu) je logický indikátor udržovaný sítí, konkrétně v rámci Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)) v EPS nebo funkce Access and Mobility Management Function ([AMF](/mobilnisite/slovnik/amf/)) v 5GC. Jeho primární funkcí je řídit pagingovou proceduru zahájenou, když síť potřebuje navázat spojení s uživatelským zařízením (UE), které je v klidovém nebo neaktivním stavu. Příznak funguje jako strážce, který rozhoduje, zda má být proces pagingu pro konkrétní UE povolen pokračovat, nebo má být zastaven. Stav PPF je vyhodnocován v kritických bodech během pagingové sekvence, typicky před každým novým pokusem o paging vysílaným napříč oblastí sledování (Tracking Area) nebo oblastí registrace (Registration Area).

Stav PPF je nastavován a aktualizován na základě různých událostí správy mobility a časovačů. Například pokud síť obdrží indikaci, že UE není dosažitelné (např. kvůli neúspěšnému předchozímu pokusu o paging, odpojení nebo vypršení periodického registračního časovače), může být PPF vynulován, aby se zabránilo marným, zdroje spotřebovávajícím opakováním pagingu. Naopak, když UE úspěšně provede aktualizaci polohy nebo služební požadavek, je PPF nastaven, aby umožnil budoucí paging. Logika zahrnuje časovače jako mobile reachable timer a implicit detach timer, definované v technických specifikacích jako 23.060 ([GPRS](/mobilnisite/slovnik/gprs/)) a 23.501 (5G System). Síťová entita kontroluje PPF před přidělením zdrojů pro vysílání pagingové zprávy.

Z architektonického pohledu je PPF součástí kontextu UE uloženého v jádru sítě. Je klíčovým prvkem pro efektivní správu rádiových zdrojů a signalizace. Tím, že brání zbytečným vysíláním pagingu pro UE, která jsou pravděpodobně nedosažitelná, PPF snižuje signalizační zatížení rádiové přístupové sítě a uzlů jádra sítě. Tato optimalizace je zásadní pro škálovatelnost sítě, zachování životnosti baterie (vyhýbáním se zbytečnému probouzení jiných UE) a celkovou kvalitu služeb. Jeho fungování je těsně integrováno s dalšími stavy mobility, jako jsou EMM-REGISTERED, ECM-IDLE a CM-IDLE, což zajišťuje, že paging je prováděn pouze tehdy, existuje-li přiměřená pravděpodobnost úspěchu.

## K čemu slouží

Příznak PPF byl zaveden, aby řešil neefektivitu a plýtvání zdroji v pagingových procedurách mobilních sítí. Rané celulární systémy mohly opakovaně pagingovat zařízení, které bylo vypnuté, mimo pokrytí nebo v chybovém stavu, a spotřebovávat tak cennou šířku rádiového pásma a výpočetní výkon jádra sítě bez šance na úspěch. To vytvářelo zbytečné signalizační přetížení a mohlo ovlivnit kapacitu pagingu pro jiné, dosažitelné uživatele. PPF poskytuje síťově řízený mechanismus pro inteligentní pozastavení pokusů o paging, když jsou považovány za pravděpodobně neúspěšné.

Řeší problém 'slepých' retransmisí pagingu. Začleněním znalosti o nedávné aktivitě správy mobility UE (nebo její absenci) může síť učinit informované rozhodnutí pokračovat nebo zastavit. To je obzvláště důležité pro funkce jako extended discontinuous reception (eDRX) a Power Saving Mode ([PSM](/mobilnisite/slovnik/psm/)) v IoT, kde zařízení mohou být po velmi dlouhou dobu nedosažitelná. Neustálý paging takových zařízení by byl vysoce neefektivní. PPF, řízený časovači dosažitelnosti, umožňuje síti respektovat tyto cykly šetření energií při zachování platného kontextu relace.

Vytvoření PPF bylo motivováno potřebou chytřejší správy mobility, jak se sítě vyvíjely od okruhově přepínané hlasové služby k paketově přepínaným datům a masivnímu IoT. Představuje posod od jednoduchých, na časovačích založených mechanismů opakování k více stavové, na kontextu založené řídicí logice. Poprvé standardizován v 3GPP Release 4 pro [GPRS](/mobilnisite/slovnik/gprs/), byl jeho koncept zachován a upřesňován přes LTE (EPS) a 5G, což demonstruje jeho zásadní roli v optimalizaci využití síťových zdrojů a umožnění efektivních režimů spánku zařízení, které jsou klíčové pro moderní celulární služby.

## Klíčové vlastnosti

- Řídicí příznak na straně sítě, který povoluje zahájení nebo pokračování pagingových procedur.
- Stav je dynamicky aktualizován na základě událostí dosažitelnosti UE a časovačů správy mobility.
- Integruje se s časovači implicitního odpojení (implicit detach) a dosažitelnosti mobilního zařízení (mobile reachable) pro správu kontextu UE.
- Snižuje zbytečné signalizační zatížení rádiové přístupové sítě (RAN) a jádra sítě.
- Nezbytný pro podporu efektivních stavů šetření energií zařízení, jako jsou PSM a eDRX.
- Udržován v rámci kontextu UE v MME (4G) nebo AMF (5G).

## Související pojmy

- [MME – NPC MME Network Product Class](/mobilnisite/slovnik/mme/)
- [AMF – Access and Mobility Management Function](/mobilnisite/slovnik/amf/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2

---

📖 **Anglický originál a plná specifikace:** [PPF na 3GPP Explorer](https://3gpp-explorer.com/glossary/ppf/)
