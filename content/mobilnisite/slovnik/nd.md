---
slug: "nd"
url: "/mobilnisite/slovnik/nd/"
type: "slovnik"
title: "ND – No Display capability"
date: 2025-01-01
abbr: "ND"
fullName: "No Display capability"
category: "Services"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/nd/"
summary: "Indikátor schopností v rámci UICC (SIM karty) nebo terminálu, který signalizuje, že zařízení nemá displej. Tyto informace používá síť nebo platformy pro přidané služby k přizpůsobení poskytování služe"
---

ND (No Display) je indikátor schopností v rámci SIM karty nebo terminálu, který signalizuje, že zařízení nemá displej, což umožňuje sítím přizpůsobit poskytování služeb potlačením vizuálního obsahu.

## Popis

Schopnost No Display (ND) je parametr definovaný v 3GPP TS 31.111, který je součástí specifikací (U)[SIM](/mobilnisite/slovnik/sim/) Application Toolkit ([USAT](/mobilnisite/slovnik/usat/)/[SAT](/mobilnisite/slovnik/sat/)). Jedná se o informaci o schopnostech terminálu, která může být uložena na UICC (Universal Integrated Circuit Card, tj. SIM kartě) nebo určena Mobile Equipment ([ME](/mobilnisite/slovnik/me/) – hardware telefonu nebo zařízení). Jejím hlavním účelem je explicitně indikovat, že zařízení, do kterého je UICC vložena, nedisponuje displejem pro zobrazování vizuálních informací uživateli.

Z architektonického hlediska je tato schopnost komunikována v rámci protokolového zásobníku zařízení. Během inicializace nebo při dotazu aplikací na UICC (například proaktivním příkazem) poskytuje ME informace o svých schopnostech, které zahrnují i stav displeje. UICC může uložit výchozí hodnotu pro schopnost ND, ale obvykle má přednost hodnota nahlášená ME. Tyto informace jsou pak dostupné prostředí USAT runtime. Když síť nebo poskytovatel přidané služby ([VAS](/mobilnisite/slovnik/vas/)) odešle příkaz vyžadující vizuální interakci – například proaktivní příkaz „Display Text“, požadavek na výběr z menu nebo požadavek na vstup od uživatele – může aplikace USAT na UICC zkontrolovat příznak ND.

Pokud je příznak ND nastaven na TRUE, může aplikační logika přizpůsobit své chování. Namísto pokusu o provedení příkazu vyžadujícího displej (který by selhal nebo způsobil chybu) může spustit alternativní akci. To může zahrnovat odeslání jiného příkazu zpět do sítě (například odeslání příčiny chyby), použití audio metody prostřednictvím příkazů „Play Tone“ nebo „Set Up Call“ pro sdělení informací, nebo jednoduše ignorování vizuálního příkazu. Tento mechanismus zajišťuje robustní provoz služeb v široké škále formátorů zařízení, od smartphonů po M2M komunikační moduly bez displeje.

## K čemu slouží

Schopnost ND byla zavedena, aby řešila rostoucí diverzitu zařízení připojujících se k mobilním sítím, zejména s nástupem komunikací M2M a IoT. Tradiční mobilní služby byly navrženy s předpokladem, že uživatel bude interagovat prostřednictvím obrazovky a klávesnice. Příkazy v [SIM](/mobilnisite/slovnik/sim/) Application Toolkit, jako je zobrazování menu, textových zpráv ze sítě nebo žádostí o vstup od uživatele (např. pro mobilní bankovnictví), jsou ze své podstaty vizuální. Odesílání takových příkazů do zařízení bez displeje – jako je chytrý měřič, sledovací zařízení majetku nebo nositelná zařízení pouze s LED indikátory – by bylo nesmyslné a mohlo by způsobit selhání služby nebo přechod zařízení do chybového stavu.

Účelem příznaku ND je umožnit přizpůsobivost služeb a zpětnou kompatibilitu. Umožňuje poskytovatelům služeb a síťovým aplikacím navrhovat služby, které se mohou elegantně degradovat nebo nabízet alternativní režimy interakce na základě schopností zařízení. Tím se předchází selhání služeb a zlepšuje se uživatelský zážitek (nebo zážitek stroje) zajištěním, že jsou odesílány pouze vhodné příkazy. Jeho vytvoření bylo motivováno potřebou standardizované metody signalizace na nízké úrovni pro rozlišení mezi zařízeními s plným uživatelským rozhraním a zařízeními určenými pro autonomní provoz bez displeje, čímž se usnadňuje spolehlivé nasazení automatizovaných služeb napříč heterogenními ekosystémy zařízení.

## Klíčové vlastnosti

- Definován jako parametr schopností terminálu ve specifikacích USAT/SAT (TS 31.111)
- Může být uložen na UICC (jako výchozí) a nahlášen Mobile Equipment
- Používán aplikacemi UICC k podmíněnému provedení nebo zamítnutí proaktivních příkazů závislých na displeji
- Umožňuje přizpůsobení služeb pro zařízení pouze se zvukem nebo neinteraktivní zařízení
- Klíčový pro spolehlivý provoz M2M a IoT zařízení bez uživatelského displeje
- Zabraňuje chybám a zbytečné signalizaci z neúspěšných pokusů o příkazy pro displej

## Definující specifikace

- **TS 31.111** (Rel-19) — USIM Application Toolkit (USAT) Specification

---

📖 **Anglický originál a plná specifikace:** [ND na 3GPP Explorer](https://3gpp-explorer.com/glossary/nd/)
