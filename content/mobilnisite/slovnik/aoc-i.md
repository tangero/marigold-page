---
slug: "aoc-i"
url: "/mobilnisite/slovnik/aoc-i/"
type: "slovnik"
title: "AOC-I – Advice Of Charge - Information"
date: 2026-01-01
abbr: "AOC-I"
fullName: "Advice Of Charge - Information"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/aoc-i/"
summary: "AOC-I je služba účtování podle 3GPP, která uživatelům během aktivních relací poskytuje informace o účtování v reálném čase. Umožňuje účastníkům sledovat náklady za využití hlasových hovorů, datových r"
---

AOC-I je služba účtování podle 3GPP, která uživatelům během aktivních hlasových, datových nebo zprávových relací poskytuje informace o nákladech v reálném čase, aby jim pomáhala spravovat výdaje.

## Popis

Advice Of Charge - Information (AOC-I) je standardizovaná služba 3GPP, která uživatelům doručuje informace o účtování v reálném čase během aktivních komunikačních relací. Služba funguje v rámci architektury IP Multimedia Subsystem (IMS) a využívá Online Charging System ([OCS](/mobilnisite/slovnik/ocs/)) pro výpočet a poskytnutí odhadu nákladů. AOC-I funguje tak, že zachycuje účtovací události během relací, vypočítává související náklady na základě tarifních informací a tyto informace doručuje na uživatelské zařízení prostřednictvím standardizovaných signalizačních protokolů.

Z architektonického hlediska se AOC-I týká několika klíčových síťových prvků včetně Serving-Call Session Control Function ([S-CSCF](/mobilnisite/slovnik/s-cscf/)) pro řízení relace, Application Server ([AS](/mobilnisite/slovnik/as/)) pro vykonávání servisní logiky a OCS pro výpočty účtování v reálném čase. Když uživatel zahájí relaci, S-CSCF na základě uživatelského servisního profilu identifikuje potřebu AOC-I a směruje relaci na příslušný AS. AS následně komunikuje s OCS prostřednictvím rozhraní Diameter Ro, aby získalo informace o účtování na základě parametrů relace, jako je cíl, typ služby a doba trvání.

Během zřizování a průběhu relace AS přijímá od OCS účtovací události a formátuje je do příslušných zpráv pro doručení na uživatelské zařízení (UE). Tyto zprávy jsou přenášeny pomocí [SIP](/mobilnisite/slovnik/sip/) (Session Initiation Protocol) zpráv se specifickými hlavičkami a parametry definovanými ve specifikacích 3GPP. Uživatelské zařízení tyto zprávy zpracuje a zobrazí informace o účtování uživateli prostřednictvím uživatelského rozhraní zařízení. Informace typicky zahrnují cenu za jednotku (minutu, megabajt nebo zprávu), kumulované poplatky během relace a údaj o měně.

AOC-I podporuje více typů služeb včetně hlasových hovorů, videohovorů, služeb zasílání zpráv a datových relací. Pro každý typ služby výpočet účtování zohledňuje různé parametry – u hlasových hovorů je typicky založen na délce trvání, u zasílání zpráv je na zprávu a u datových relací může být založen na objemu nebo času v závislosti na tarifním plánu. Systém udržuje stav relace, aby zajistil přesné kumulativní informace o účtování po celou dobu trvání relace, přičemž aktualizace jsou poskytovány v konfigurovatelných intervalech nebo při významných účtovacích událostech.

Služba funguje ve spojení s dalšími mechanismy účtování včetně Advice Of Charge - Charging ([AOC-C](/mobilnisite/slovnik/aoc-c/)), který poplatky skutečně aplikuje, a Advice Of Charge - End of Call ([AOC-E](/mobilnisite/slovnik/aoc-e/)), který poskytuje konečné informace o účtování. Reálný charakter AOC-I vyžaduje nízkou latenci komunikace mezi síťovými prvky a efektivní zpracování účtovacích událostí, aby bylo zajištěno včasné doručení informací bez narušení uživatelského zážitku během aktivních relací.

## K čemu slouží

AOC-I byl vyvinut pro řešení rostoucí potřeby transparentnosti v telekomunikačním účtování, zejména když se mobilní služby rozšířily mimo jednoduché hlasové hovory a začaly zahrnovat datové služby, zasílání zpráv a multimediální komunikaci. Před zavedením AOC-I uživatelé často získávali informace o účtování až na měsíčním vyúčtování, což vedlo k 'překvapení z výše účtu', když se nahromadily neočekávané poplatky. Tento nedostatek viditelnosti v reálném čase vedl k nespokojenosti zákazníků a zvýšeným nákladům na podporu u operátorů řešící spory o účtování.

Služba byla představena ve 3GPP Release 7 jako součást vývoje architektury IMS, která umožnila sofistikovanější doručování služeb a mechanismy účtování. Předchozí přístupy spoléhaly na účtování po skončení relace nebo vyžadovaly proprietární řešení, která nebyla interoperabilní mezi různými sítěmi a zařízeními. AOC-I standardizoval doručování informací o účtování napříč prostředími více dodavatelů, což zajišťuje konzistentní uživatelský zážitek bez ohledu na síťového operátora nebo výrobce zařízení.

Kromě ochrany spotřebitele slouží AOC-I důležitým obchodním účelům síťových operátorů. Umožňuje nové tarifní modely a propagační nabídky tím, že uživatelům dává možnost vidět v reálném čase nákladové dopady různých možností služeb. Tato transparentnost buduje důvěru zákazníků a může snížit fluktuaci tím, že demonstruje spravedlivé účtovací praktiky. AOC-I navíc podporuje regulatorní požadavky v mnoha jurisdikcích, které vyžadují jasné sdělování nákladů za služby spotřebitelům, zejména u prémiových služeb a mezinárodního roamingu.

## Klíčové vlastnosti

- Doručování informací o účtování v reálném čase během aktivních relací
- Podpora více typů služeb včetně hlasu, videa, zasílání zpráv a dat
- Integrace s Online Charging System (OCS) pro přesné tarifní výpočty
- Standardizovaná signalizace založená na SIP pro interoperabilitu napříč sítěmi
- Konfigurovatelné intervaly aktualizací a notifikace o účtování založené na událostech
- Povědomí o měně a tarifním plánu pro přesné zobrazení nákladů

## Definující specifikace

- **TS 22.173** (Rel-20) — IMS Multimedia Telephony Service Definition
- **TS 22.273** (Rel-7) — IMS Multimedia Telephony with PSTN/ISDN Simulation
- **TS 29.364** (Rel-19) — IMS AS Service Data Descriptions
- **TS 29.864** (Rel-8) — Application Server Service Data Definition for IMS Telephony

---

📖 **Anglický originál a plná specifikace:** [AOC-I na 3GPP Explorer](https://3gpp-explorer.com/glossary/aoc-i/)
