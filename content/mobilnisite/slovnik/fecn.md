---
slug: "fecn"
url: "/mobilnisite/slovnik/fecn/"
type: "slovnik"
title: "FECN – Forward Explicit Congestion Notification"
date: 2025-01-01
abbr: "FECN"
fullName: "Forward Explicit Congestion Notification"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/fecn/"
summary: "Mechanismus pro řízení zahlcení používaný v sítích Frame Relay, standardizovaný konsorciem 3GPP pro rozhraní Gb mezi BSS a SGSN v sítích 2G/GSM a GPRS. Jedná se o bit v hlavičce Frame Relay nastavený"
---

FECN je bit v hlavičce Frame Relay standardizovaný konsorciem 3GPP pro rozhraní Gb, který má za úkol informovat přijímací stranu o zahlcení v dopředném směru od BSS k SGSN v sítích 2G/GPRS.

## Popis

Forward Explicit Congestion Notification (FECN) je funkce pro řízení toku dat v protokolu Frame Relay, který byl zvolen jako technologie linkové vrstvy (layer 2) pro rozhraní Gb v jádrových sítích 2G/GSM a [GPRS](/mobilnisite/slovnik/gprs/). Rozhraní Gb spojuje subsystém základnových stanic ([BSS](/mobilnisite/slovnik/bss/)), který zahrnuje [BTS](/mobilnisite/slovnik/bts/) a [BSC](/mobilnisite/slovnik/bsc/), s uzlem [SGSN](/mobilnisite/slovnik/sgsn/). FECN funguje v rámci hlavičky Frame Relay každého rámce. Jedná se o jednobitové pole, které může být nastaveno na hodnotu '1' libovolným mezilehlým Frame Relay přepínačem (nebo sítí), který na cestě od zdroje k cíli zaznamená zahlcení. Když je tento bit nastaven, explicitně signalizuje cílovému koncovému bodu rámce (např. SGSN nebo BSS), že na tomto konkrétním virtuálním okruhu došlo k zahlcení v dopředném směru.

Z architektonického hlediska používá rozhraní Gb trvalé virtuální okruhy ([PVC](/mobilnisite/slovnik/pvc/)) Frame Relay pro přenos signalizačních a uživatelských datových paketů mezi BSS a SGSN. Síťové prvky, jako jsou Frame Relay přepínače, monitorují stav front a vytížení spojení. Při detekci zahlcení – například když délka fronty překročí stanovený práh – přepínač nastaví bit FECN v hlavičce rámců procházejících zahlceným prostředkem. Přijímající strana (např. SGSN) tento bit zpracuje. Podle specifikací 3GPP je primární reakcí na indikaci FECN potenciální aktivace mechanismů řízení toku na vyšších vrstvách. SGSN může například zmenšit velikost okna pro protokol [BSSGP](/mobilnisite/slovnik/bssgp/) (BSS GPRS Protocol) nebo spustit řízení toku [LLC](/mobilnisite/slovnik/llc/) (Logical Link Control), čímž nepřímě sníží datový tok ze zdroje.

Princip činnosti je nedílnou součástí lehkého přístupu Frame Relay ke správě zahlcení. Na rozdíl od implicitní detekce zahlcení v protokolu TCP, která je založena na ztrátě paketů, poskytuje FECN explicitní, včasné upozornění. Když cíl přijme rámec s FECN=1, typicky tuto informaci přepošle zpět původnímu zdroji pomocí bitu Backward Explicit Congestion Notification (BECN) v rámcích putujících zpětným směrem. Tím informuje zdroj (např. BSS), aby snížil rychlost vysílání. V kontextu rozhraní Gb dle 3GPP může SGSN po přijetí FECN také využít protokol BSSGP nebo jiné protokoly specifické pro GPRS k regulaci toku dat ze sítě směrem k BSS a následně k mobilní stanici. To pomáhá předcházet ztrátě paketů v jádrové síti a udržovat kvalitu služeb pro datové služby GPRS.

## K čemu slouží

FECN existuje pro správu zahlcení v spojově orientovaných paketových sítích, jako je Frame Relay, který byl pro rozhraní Gb vybrán pro svou efektivitu a vhodnost pro přenos dat s prázdninovým charakterem v sítích 2.5G GPRS. Základním problémem, který řeší, je souběžný přístup ke zdrojům sítě bez režie spojené s potvrzováním na úrovni jednotlivých spojení nebo složitými schématy pro opakovaný přenos. V raných datových službách bylo zabránění kolapsu sítě v důsledku zahlcení klíčové pro udržení dostupnosti služby. FECN poskytuje jednoduchý, explicitní signál, že dochází k zahlcení, což koncovým bodům umožňuje reagovat proaktivně, než dojde k přetečení vyrovnávacích pamětí a ztrátě paketů.

Historický kontext spočívá ve vývoji od sítí GSM s přepojováním okruhů k sítím GPRS s přepojováním paketů. Rozhraní Gb potřebovalo nákladově efektivní, spolehlivou technologii linkové vrstvy. Frame Relay, široce používaný v rozlehlých sítích, nabízel statistické multiplexování a garantované přenosové rychlosti. Jeho minimální kontrola chyb a absence vestavěného mechanismu pro řízení zahlcení však vyžadovaly mechanismy jako FECN/BECN. Konsorcium 3GPP standardizovalo jeho použití, aby zajistilo interoperabilní správu zahlcení mezi zařízeními BSS a SGSN od různých výrobců. To bylo klíčové pro komerční úspěch GPRS, protože umožnilo sítím zvládat rostoucí datový provoz bez degradace hlasových služeb sdílejících stejnou infrastrukturu.

FECN řeší omezení implicitního řízení zahlcení, které spoléhá na ztrátu paketů jako ukazatel – což je nevhodná metoda pro časově citlivý nebo na ztráty citlivý provoz. Poskytnutím explicitního oznámení umožňuje rychlejší a přesnější formování provozu. Umožňuje síti přímo komunikovat svůj stav, což usnadňuje stabilnější provoz a efektivní využití šířky pásma rozhraní Gb. Zatímco pozdější technologie 3GPP (Iu-PS, S1-U) přešly na přenos založený na IP, FECN zůstává klíčovou součástí architektury starších sítí GPRS/EDGE, zajišťujíc zpětnou kompatibilitu a spolehlivý provoz pro miliony zařízení 2G pro datový přenos, která jsou stále v provozu.

## Klíčové vlastnosti

- Jednobitový indikátor v hlavičce Frame Relay pro explicitní signalizaci zahlcení
- Nastavován zahlcenými síťovými uzly (Frame Relay přepínači) na dopředné cestě
- Používán konkrétně na rozhraní Gb mezi BSS a SGSN v sítích 2G/GPRS
- Spouští reakce řízení toku ve vyššívrstvových protokolech, jako jsou BSSGP nebo LLC
- Funguje ve spolupráci s Backward Explicit Congestion Notification (BECN)
- Poskytuje včasnou prevenci zahlcení za účelem snížení ztráty paketů v jádrové síti

## Související pojmy

- [BECN – Backward Explicit Congestion Notification](/mobilnisite/slovnik/becn/)
- [BSSGP – Base Station System GPRS Protocol](/mobilnisite/slovnik/bssgp/)
- [SGSN – Serving GPRS Support Node](/mobilnisite/slovnik/sgsn/)
- [GPRS – CSI GPRS CAMEL Subscription Information](/mobilnisite/slovnik/gprs/)

## Definující specifikace

- **TS 48.016** (Rel-19) — Gb Interface Network Service Specification

---

📖 **Anglický originál a plná specifikace:** [FECN na 3GPP Explorer](https://3gpp-explorer.com/glossary/fecn/)
