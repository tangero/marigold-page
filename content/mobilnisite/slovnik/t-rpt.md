---
slug: "t-rpt"
url: "/mobilnisite/slovnik/t-rpt/"
type: "slovnik"
title: "T-RPT – Time Resource Pattern of Transmission"
date: 2025-01-01
abbr: "T-RPT"
fullName: "Time Resource Pattern of Transmission"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/t-rpt/"
summary: "Bitmapový vzor v LTE komunikaci zařízení-zařízení (D2D) a V2X, který definuje podrámce, jež může UE použít pro sidelinkový přenos. Umožňuje efektivní plánované přidělování zdrojů pro přímou komunikaci"
---

T-RPT je bitmapový vzor v LTE D2D a V2X komunikaci, který definuje konkrétní podrámce, které může uživatelské zařízení (UE) použít pro své sidelinkové přenosy.

## Popis

Time Resource Pattern of Transmission (T-RPT) je klíčový mechanismus přidělování zdrojů definovaný ve standardu 3GPP LTE pro sidelinkovou komunikaci, konkrétně pro režim přidělování zdrojů Mode 2 v [D2D](/mobilnisite/slovnik/d2d/) ([ProSe](/mobilnisite/slovnik/prose/)) a [V2X](/mobilnisite/slovnik/v2x/). Jde o bitmapový vzor signalizovaný přes [RRC](/mobilnisite/slovnik/rrc/) nebo odvozený z plánovacích přiřazení, který vymezuje v definovaném období, které časové podrámce smí uživatelské zařízení (UE) použít pro přenos svého sidelinkového sdíleného kanálu ([PSSCH](/mobilnisite/slovnik/pssch/)). Každý bit v bitmapě T-RPT odpovídá podrámci v rámci periody fondu zdrojů, přičemž '1' typicky označuje povolenou přenosovou příležitost. Délka vzoru T-RPT je konfigurovatelná, často pokrývá více podrámců (např. v rámci periody). UE tento vzor používá k výběru konkrétních podrámců pro své přenosy, čímž vytváří časovou strukturu, která rozvádí přenosy a zmírňuje trvalé kolize.

Z architektonického hlediska T-RPT funguje v rámci sidelinkového fondu zdrojů. eNodeB nebo hlavička klastru může konfigurovat fondy zdrojů pro scénáře mimo dosah sítě nebo s částečným pokrytím. V rámci časových zdrojů fondu poskytuje T-RPT přenosovou masku specifickou pro UE nebo skupinu. Když má UE data k odeslání na sidelinku, odkazuje se na svůj přiřazený nebo vybraný T-RPT, aby identifikovalo platné podrámce. Ty pak obvykle kombinuje s výběrem zdrojů ve frekvenční oblasti (např. výběr konkrétních bloků zdrojů v povolených podrámcích), aby určilo své konečné přenosové zdroje. Toto dvourozměrné přidělování (čas a frekvence) je zásadní pro řízení zahlcení a rušení v distribuovaném, soutěživém přístupovém prostředí, jako je sidelinkový režim Mode 2.

Role T-RPT je zásadní pro škálovatelnost a spolehlivost přímé komunikace založené na LTE. Poskytnutím předvídatelného, vzorovaného přenosového plánu zabraňuje tomu, aby UE nepřetržitě vysílalo v každém podrámci, což by způsobilo nadměrné rušení ostatním. Umožňuje také časový hopping zdrojů pro dosažení frekvenční diverzity. Vzor je často kombinován s intervalem rezervace zdrojů, kdy si UE pro svůj další přenos rezervuje sadu zdrojů podle stejného T-RPT, což snižuje potřebu nepřetržitého snímání a výběru pro polotrvalé toky provozu, jako jsou periodické V2X bezpečnostní zprávy. Konfigurace a signalizace T-RPT jsou podrobně popsány v 3GPP TS 36.331 (protokol RRC) a jeho aplikace v TS 36.213 (procedury fyzické vrstvy).

## K čemu slouží

T-RPT byl zaveden v LTE Release 12 jako součást funkce Proximity Services ([ProSe](/mobilnisite/slovnik/prose/)) pro umožnění efektivní komunikace zařízení-zařízení bez nepřetržitého centralizovaného plánování z eNodeB. Základní problém, který řeší, je nekoordinovaná soutěž o zdroje v distribuovaném bezdrátovém prostředí. V sidelinkovém režimu Mode 2 (autonomní výběr zdrojů UE) si UE nezávisle vybírají zdroje z fondu. Bez časové struktury by byly kolize časté a nepředvídatelné, což by degradovalo výkon, zejména s rostoucím počtem komunikujících zařízení.

Před zavedením T-RPT mohly čistě náhodný nebo na snímání založený výběr v každém podrámci vést k problémům skrytého uzlu a trvalému rušení. T-RPT zavádí vrstvu koordinace rozdělením časového fondu zdrojů na vzorované příležitosti pro každé UE. Tím omezuje hustotu přenosů každého jednotlivého UE, uvolňuje podrámce pro ostatní a vytváří determinističtější prostředí rušení. Motivací byla potřeba spolehlivé [D2D](/mobilnisite/slovnik/d2d/) komunikace pro veřejnou bezpečnost, kde zařízení mohou fungovat mimo dosah sítě a musí se efektivně samoorganizovat.

S vývojem směrem k [V2X](/mobilnisite/slovnik/v2x/) v Release 14 a novějších ještě vzrostl význam T-RPT kvůli vysoké hustotě, vysoké mobilitě a přísným požadavkům na spolehlivost v dopravních sítích. Přístup založený na vzoru umožňuje lepší předvídatelnost a řízení poměru vytížení kanálu, což je klíčová metrika pro řízení zahlcení. Tvoří základ pro pokročilejší polotrvalé plánování (SPS) na sidelinku, kde vozidlo rezervuje vzor zdrojů pro své periodické zprávy Cooperative Awareness Messages (CAM), což zajišťuje konzistentní doručení s nízkou latencí a zároveň umožňuje vzor přizpůsobit na základě snímání vzorů ostatních vozidel.

## Klíčové vlastnosti

- Bitmapová indikace podrámců pro sidelinkový přenos
- Konfigurovatelná délka a periodicita vzoru
- Podporuje autonomní výběr zdrojů UE (Mode 2)
- Snižuje pravděpodobnost časových kolizí
- Umožňuje polotrvalé plánování pro periodický provoz
- Integruje se s konfigurací sidelinkového fondu zdrojů

## Související pojmy

- [V2X – Vehicle-to-Everything Application Server](/mobilnisite/slovnik/v2x/)
- [SPS – Semi-Persistent Scheduling](/mobilnisite/slovnik/sps/)

## Definující specifikace

- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [T-RPT na 3GPP Explorer](https://3gpp-explorer.com/glossary/t-rpt/)
