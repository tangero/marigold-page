---
slug: "dsf"
url: "/mobilnisite/slovnik/dsf/"
type: "slovnik"
title: "DSF – Domain Selection Function"
date: 2007-01-01
abbr: "DSF"
fullName: "Domain Selection Function"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/dsf/"
summary: "Funkce, která vybírá vhodnou doménu (např. přepojování okruhů nebo přepojování paketů) pro komunikační relaci. Určuje, zda má být služba poskytnuta přes CS nebo PS sítě na základě politik, preferencí"
---

DSF je funkce, která vybírá vhodnou doménu, například přepojování okruhů (circuit-switched) nebo přepojování paketů (packet-switched), pro relaci na základě politik, preferencí účastníka a možností sítě.

## Popis

Domain Selection Function (DSF) je síťová funkce definovaná ve specifikacích 3GPP, konkrétně v TS 23.206 a TS 24.206, které pokrývají kontinuitu hlasových hovorů a související protokoly. Jejím hlavním úkolem je rozhodnout, která doména – přepojování okruhů ([CS](/mobilnisite/slovnik/cs/)) nebo přepojování paketů (PS) – má být použita pro navázání komunikační relace, například hlasového hovoru. Toto rozhodnutí je klíčové v sítích podporujících obě domény, jako jsou konvergované sítě 2G/3G/4G, kde mohou služby jako Voice over LTE (VoLTE) přepínat zpět na CS z důvodu pokrytí. DSF funguje tak, že vyhodnocuje různé vstupy, včetně možností uživatelského zařízení (UE), stavu sítě, politik operátora a požadavků služby, aby provedlo optimální výběr domény, který zajišťuje kontinuitu a kvalitu služby.

Z architektonického hlediska je DSF typicky implementována v rámci jádra sítě, často jako součást IMS (IP Multimedia Subsystem) nebo integrována s entitami pro správu mobility. Například ve scénáři VoLTE, když uživatel zahájí hovor, DSF vyhodnotí, zda UE a síť podporují hlas přes PS (např. přes IMS), nebo zda je nutný CS fallback kvůli omezenému pokrytí LTE. Mezi klíčové zapojené komponenty patří policy servery ukládající pravidla pro výběr domény, [MME](/mobilnisite/slovnik/mme/) pro kontext mobility a [MSC](/mobilnisite/slovnik/msc/) (Mobile Switching Center) pro koordinaci CS domény. DSF komunikuje se signalizačními protokoly, jako jsou SIP nebo [MAP](/mobilnisite/slovnik/map/) (Mobile Application Part), aby svým rozhodnutím informovala další síťové elementy a zajistila správné směrování relace. Její role přesahuje hlasové služby a zahrnuje i další služby, kde výběr domény ovlivňuje výkon, například videohovory nebo zasílání zpráv.

V praxi DSF pracuje prostřednictvím sekvence kontrol a vyvažování. Při zahájení relace získá profily účastníka z [HSS](/mobilnisite/slovnik/hss/) (Home Subscriber Server), aby určila preference – například účastník může být nastaven tak, aby preferoval hlas přes PS z důvodu úspory nákladů. Bere také v úvahu faktory v reálném čase, jako je vytížení sítě, dostupná šířka pásma a poloha UE. Pokud jsou zdroje PS nedostatečné, může DSF spustit předání do CS domény a koordinovat to s prvky, jako je eNodeB a MSC, aby zajistila plynulý přechod. Tato funkce je zásadní pro udržení spolehlivosti hovorů, zejména v oblastech s nerovnoměrným pokrytím LTE. Inteligentním výběrem domén DSF pomáhá optimalizovat využití síťových zdrojů a zlepšuje uživatelský zážitek minimalizací přerušených hovorů nebo špatné kvality zvuku.

## K čemu slouží

DSF byla zavedena, aby řešila problém výběru domény v hybridních sítích podporujících jak [CS](/mobilnisite/slovnik/cs/), tak PS služby. Jak se sítě vyvíjely z 2G/3G (primárně CS pro hlas) na 4G (založené na PS pro všechny služby, včetně hlasu přes IMS), nastalo přechodné období, kdy obě domény koexistovaly. Bez standardizovaného mechanismu výběru mohla zařízení a sítě činit neoptimální volby, což vedlo k problémům, jako jsou zbytečné CS fallbacky, zvýšená signalizační režie nebo přerušení služby. DSF, zavedená v Release 7, poskytla centralizovanou funkci pro informovaná rozhodnutí o doméně, čímž řešila problémy související s kontinuitou služeb a efektivním využitím zdrojů.

Historicky motivace vycházela z nasazení IMS a VoLTE, které slibovaly kvalitní hlas přes IP, ale vyžadovaly přepnutí na CS v oblastech bez pokrytí LTE. Rané implementace spoléhaly na rozhodnutí na straně zařízení, která mohla být nekonzistentní a způsobovat problémy s interoperabilitou. DSF tento proces standardizovala a umožnila operátorům vynucovat politiky na základě stavu sítě a dat o účastnících. To řešilo omezení, jako je nepředvídatelné chování při přepnutí, které mohlo zhoršovat uživatelský zážitek nebo plýtvat síťovou kapacitou. Centralizací výběru domény DSF umožnila plynulejší přechody mezi doménami a podporovala funkce jako SRVCC (Single Radio Voice Call Continuity) pro předání z LTE do 2G/3G CS.

DSF navíc podporuje provozní flexibilitu a inovace služeb. Operátoři ji mohou použít ke směrování provozu na základě obchodních pravidel, například preferování PS domény pro odlehčení CS infrastruktury nebo upřednostnění CS pro tísňová volání. Usnadňuje také zavádění nových služeb, které mohou vyžadovat specifické charakteristiky domény, jako je PS s nízkou latencí pro aplikace v reálném čase. Tím, že zajišťuje, aby byl výběr domény řízen politikami a kontrolován sítí, DSF zvyšuje spolehlivost a připravuje cestu pro plně IP sítě v éře 5G, kde jsou CS domény postupně ukončovány, ale podpora starších technologií zůstává klíčová.

## Klíčové vlastnosti

- Vybírá mezi doménami přepojování okruhů (CS) a přepojování paketů (PS) pro relace
- Integruje se s IMS a elementy jádra sítě pro vynucování politik
- Podporuje funkce kontinuity služeb, jako je SRVCC
- Vyhodnocuje možnosti UE, stav sítě a profily účastníků
- Umožňuje plynulá předání mezi CS a PS doménami
- Umožňuje definovat politiky operátora pro preferenci domény a přepnutí (fallback)

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [MME – NPC MME Network Product Class](/mobilnisite/slovnik/mme/)

## Definující specifikace

- **TS 23.206** (Rel-7) — Voice Call Continuity (VCC) Functional Architecture
- **TS 24.206** (Rel-7) — Voice Call Continuity Between CS and IMS

---

📖 **Anglický originál a plná specifikace:** [DSF na 3GPP Explorer](https://3gpp-explorer.com/glossary/dsf/)
