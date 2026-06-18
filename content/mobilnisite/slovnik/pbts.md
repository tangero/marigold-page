---
slug: "pbts"
url: "/mobilnisite/slovnik/pbts/"
type: "slovnik"
title: "PBTS – Priority Based Transmission Scheduling"
date: 2025-01-01
abbr: "PBTS"
fullName: "Priority Based Transmission Scheduling"
category: "QoS"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/pbts/"
summary: "Priority Based Transmission Scheduling (PBTS) je plánovací mechanismus v LTE a 5G, který stanovuje prioritu přenosů dat na základě identifikátoru třídy služeb QoS (QCI) nebo 5QI. Zajišťuje, že kritick"
---

PBTS je plánovací mechanismus v sítích LTE a 5G, který stanovuje prioritu přenosů dat na základě identifikátorů QoS, aby zajistil, že kritický provoz získá prostředky dříve než best-effort data, a optimalizoval tak výkon při zahlcení.

## Popis

Priority Based Transmission Scheduling (PBTS) je základní algoritmus používaný LTE eNodeB a 5G gNodeB v rádiové přístupové síti (RAN) pro správu přidělování rádiových prostředků (času a frekvence) mezi konkurenční uživatelská zařízení (UE) a datové toky. Funguje v rámci plánovače vrstvy Medium Access Control ([MAC](/mobilnisite/slovnik/mac/)), který je zodpovědný za dynamické plánování na sdíleném kanálu. Základním principem PBTS je přiřazovat příležitosti k přenosu na základě úrovně priority spojené s každým datovým rádiovým přenosem (bearerem), jak je definováno parametry QoS, jako je identifikátor třídy služeb QoS ([QCI](/mobilnisite/slovnik/qci/)) v LTE nebo identifikátor QoS 5G ([5QI](/mobilnisite/slovnik/5qi/)) v 5G.

Z architektonického hlediska je PBTS implementován v modulu plánovače základnové stanice. Přijímá od uživatelských zařízení (UE) hlášení o stavu vyrovnávací paměti, která udávají množství dat čekajících na přenos. Pro každý plánovací interval (např. každý Transmission Time Interval - [TTI](/mobilnisite/slovnik/tti/)) plánovač vyhodnocuje všechny aktivní přenosy (bearery). Nejprve je seřadí nebo filtruje na základě jejich priority. Vysokoprioritní přenosy, jako jsou ty pro služby s garantovanou přenosovou rychlostí ([GBR](/mobilnisite/slovnik/gbr/)), například Voice over LTE (VoLTE) nebo pro kritickou komunikaci, jsou naplánovány dříve než přenosy bez GBR. V rámci stejné úrovně priority mohou být pro jemné doladění přidělování prostředků použity další metriky, jako jsou indikátory kvality kanálu ([CQI](/mobilnisite/slovnik/cqi/)), spravedlnost a požadavky na propustnost.

Mechanismus funguje tak, že mapuje standardizované hodnoty QCI/5QI, které definují charakteristiky jako typ prostředku, priorita, rozpočet zpoždění paketu a míra ztráty paketů, na interní priority plánování. Plánovač udržuje samostatné logické fronty pro přenosy s různými prioritami. Při přidělování mřížky rádiových prostředků se plánovač nejprve snaží uspokojit požadavky na prostředky fronty s nejvyšší prioritou. Teprve pokud po obsloužení veškerého vysokoprioritního provozu zbývají prostředky, přidělí je provozu s nižší prioritou (best-effort). Tím je zajištěno, že aplikace citlivé na zpoždění a kritické aplikace zaznamenají minimální zpoždění a kolísání i při zahlcení sítě.

PBTS je klíčovým prvkem pro diferencovanou QoS v paketových mobilních sítích. Umožňuje síti dodržovat smlouvy o úrovni služeb ([SLA](/mobilnisite/slovnik/sla/)) pro prémiové služby a poskytuje základ pro síťové řezy (network slicing) v 5G, kde různé řezy (např. rozšířené mobilní širokopásmové připojení - eMBB, ultra-spolehlivá komunikace s nízkou latencí - [URLLC](/mobilnisite/slovnik/urllc/)) vyžadují odlišné chování plánování. Parametry a přesná implementace algoritmu mohou být specifické pro dodavatele, ale jeho chování musí být v souladu se standardy rámce QoS, aby byla zajištěna výkonnost služby od konce ke konci.

## K čemu slouží

PBTS existuje k řešení základního problému soupeření o prostředky ve sdílených paketových rádiových sítích. V časných systémech mobilních dat bylo plánování často čistě závislé na stavu kanálu (upřednostňovalo uživatele s dobrými signálovými podmínkami) nebo čistě spravedlivé (stejný podíl prostředků), což nesplňovalo různé požadavky na latenci a spolehlivost moderních aplikací, jako je hraní her v reálném čase, průmyslový IoT a komunikace pro veřejnou bezpečnost. Účelem PBTS je zavést do rozhodování o plánování povědomí o službě.

Řeší omezení předchozích best-effort internetových modelů aplikovaných na bezdrátové sítě, kde byl veškerý provoz zacházen stejně, což vedlo ke špatnému výkonu aplikací citlivých na zpoždění při zahlcení. Díky využití standardizovaného rámce QoS (QCI/5QI) umožňuje PBTS operátorům sítí vynucovat diferenciaci provozu. To je klíčové pro podporu více služeb na jedné infrastruktuře RAN a umožňuje konvergenci hlasu, videa a dat.

Vytvoření PBTS bylo motivováno potřebou, aby LTE a 5G podporovaly nejen vysokorychlostní data, ale také hlas na úrovni operátora (VoLTE) a služby pro kritické nasazení. Tyto služby mají přísné výkonnostní limity, které nelze garantovat bez preemptivního plánování. PBTS poskytuje mechanismus pro stanovení priority kritických paketů a zajišťuje jejich přenos v rámci povoleného rozpočtu zpoždění. To je nezbytné pro efektivitu sítě a uživatelský zážitek, což operátorům umožňuje nabízet služby ve více úrovních a zajišťovat spolehlivý výkon pro nouzové služby a průmyslové aplikace.

## Klíčové vlastnosti

- Plánuje rádiové prostředky na základě úrovní priority QCI/5QI
- Zajišťuje preemptivní přidělení prostředků pro provoz s GBR před provozem bez GBR
- Integruje se s plánováním zohledňujícím stav kanálu pro efektivitu v rámci tříd priority
- Podporuje rozpočty latence a míry ztráty paketů definované v profilech QoS
- Umožňuje diferenciaci služeb a síťové řezy (network slicing) v RAN
- Dynamický provoz na základě stavu vyrovnávací paměti a podmínek kanálu v reálném čase

## Související pojmy

- [QCI – Quality of Service Class Identifier](/mobilnisite/slovnik/qci/)
- [5QI – 5G QoS Identifier](/mobilnisite/slovnik/5qi/)
- [GBR – Generic Binaural Renderer](/mobilnisite/slovnik/gbr/)

## Definující specifikace

- **TR 26.904** (Rel-19) — Future video capability requirements for streaming and MBMS

---

📖 **Anglický originál a plná specifikace:** [PBTS na 3GPP Explorer](https://3gpp-explorer.com/glossary/pbts/)
