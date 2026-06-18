---
slug: "rnau"
url: "/mobilnisite/slovnik/rnau/"
type: "slovnik"
title: "RNAU – RAN-based Notification Area Update"
date: 2025-01-01
abbr: "RNAU"
fullName: "RAN-based Notification Area Update"
category: "Mobility"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/rnau/"
summary: "Procedura v 5G NR pro UE ve stavu RRC_INACTIVE, která umožňuje aktualizaci polohy v rámci notifikační oblasti RAN (RNA) bez přechodu do stavu RRC_CONNECTED. Umožňuje efektivní, síťově řízenou mobilitu"
---

RNAU je procedura pro UE ve stavu RRC_INACTIVE, která umožňuje aktualizaci jeho polohy v rámci notifikační oblasti RAN bez přechodu do stavu RRC_CONNECTED, a tím podporuje efektivní mobilitu a paging.

## Popis

RAN-based Notification Area Update (RNAU) je zásadní procedura správy mobility definovaná pro systém 5G New Radio (NR), konkrétně pro uživatelské zařízení (UE) pracující ve stavu [RRC](/mobilnisite/slovnik/rrc/)_INACTIVE. Tento stav, zavedený v 5G, je stav s nízkou spotřebou, kdy je kontext přístupové vrstvy ([AS](/mobilnisite/slovnik/as/)) UE uložen jak v UE, tak v poslední obsluhující stanici gNB (nebo uzlu NG-RAN), ale UE aktivně nepřenáší ani nepřijímá datové přenosy. UE je přidělena notifikační oblast RAN ([RNA](/mobilnisite/slovnik/rna/)), což je logická oblast definovaná RAN, typně zahrnující jednu nebo více buněk. Účelem procedury RNAU je, aby UE periodicky nebo na základě události aktualizovalo síť, když se přesune mimo svou nakonfigurovanou RNA, a zajistilo tak, že síť zná oblast pro paging, kde lze UE vyhledat, pokud dorazí downlink data nebo pro další síťově iniciované akce.

Architektonicky je procedura RNAU iniciována UE při splnění spouštěcí podmínky, například při opuštění aktuální RNA, po vypršení periodického RNAU časovače nebo při převzetí služeb buňkou, která není součástí aktuálního seznamu RNA. UE proceduru provádí iniciováním přechodu ze stavu RRC_INACTIVE do stavu RRC_CONNECTED, konkrétně pomocí zprávy RRC Resume Request. Tato zpráva obsahuje Resume ID, které umožňuje přijímající stanici gNB (která může být odlišná od poslední obsluhující gNB) načíst kontext AS UE od předchozí gNB prostřednictvím rozhraní Xn. Procedura zahrnuje načtení kontextu, ověření integrity ochrany a aktualizaci bezpečnostních klíčů. Po úspěšném dokončení může síť ponechat UE ve stavu RRC_CONNECTED, pokud čekají data, nebo může překonfigurovat novou RNA a převést UE zpět do stavu RRC_INACTIVE.

Role RNAU je klíčová pro vyvážení efektivity správy mobility s úsporou energie UE. Odděluje časté aktualizace polohy od core sítě (5GC) a řeší je v rámci RAN. Tím se snižuje signalizační zátěž na rozhraních [N2](/mobilnisite/slovnik/n2/) a N3 směrem k funkci správy přístupu a mobility ([AMF](/mobilnisite/slovnik/amf/)) a funkci uživatelské roviny ([UPF](/mobilnisite/slovnik/upf/)). RNA je spravována RAN, což umožňuje dynamičtější a provozu přizpůsobené vymezení oblastí ve srovnání s oblastmi sledování ([TA](/mobilnisite/slovnik/ta/)) core sítě. Procedura funguje ve spojení s RAN-based pagingem, kdy může gNB provést paging UE v rámci poslední známé RNA bez zapojení core sítě pro počáteční paging, což vede k rychlejším časům sestavení hovoru a snížené latenci pro služby iniciované sítí.

## K čemu slouží

RNAU byla vytvořena, aby řešila omezení starších systémů správy mobility, zejména pro obrovský počet IoT zařízení a smartphonů s trhavým datovým provozem očekávaným v 5G. V 4G LTE UE ve stavu [RRC](/mobilnisite/slovnik/rrc/)_IDLE provádělo proceduru aktualizace oblasti sledování (TAU) s core sítí (MME) pokaždé, když se přesunulo mimo svůj seznam oblastí sledování. To vždy zahrnovalo navázání RRC spojení a provádění NAS signalizace, což způsobovalo značnou signalizační režii, zátěž core sítě a spotřebu baterie UE za často velmi krátké a řídké datové přenosy.

Zavedení stavu RRC_INACTIVE v 5G NR si vyžádalo odpovídající mechanizmus správy mobility řízený RAN. Účelem RNAU je umožnit efektivní a lehkou lokalizaci pro UE, která jsou neaktivní, ale mají platný kontext AS uložený v RAN. Řeší problém časté signalizace s core sítí tím, že udržuje aktualizace polohy lokální v rámci RAN. To je motivováno potřebou podporovat rozšířené mobilní širokopásmové připojení (eMBB) s očekáváním trvalého připojení a masivní komunikaci strojového typu (mMTC) s obrovským počtem zařízení s nízkou spotřebou. RNAU umožňuje síti udržovat dosažitelnost těchto UE a zároveň optimalizovat kompromis mezi přesností lokalizace, náklady na signalizaci a spotřebou energie UE, což nebylo v předchozích generacích optimálně vyváženo.

## Klíčové vlastnosti

- Umožňuje aktualizace polohy pro UE ve stavu RRC_INACTIVE bez zapojení core sítě (AMF) pro samotnou aktualizaci.
- Spouští se pohybem UE mimo nakonfigurovanou notifikační oblast RAN (RNA) nebo periodickým časovačem.
- Používá proceduru RRC Resume pro načtení kontextu a reaktivaci zabezpečení.
- Umožňuje RAN dynamicky konfigurovat a spravovat velikost a složení RNA.
- Snižuje signalizační režii na rozhraní N2 a spotřebu baterie UE ve srovnání s aktualizacemi oblasti sledování (TAU) řízenými core sítí.
- Podporuje RAN-based paging tím, že udržuje polohu UE známou na úrovni RNA.

## Definující specifikace

- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.304** (Rel-19) — UE Idle Mode Procedures in E-UTRA
- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TS 38.304** (Rel-19) — UE RRC_IDLE and RRC_INACTIVE Procedures

---

📖 **Anglický originál a plná specifikace:** [RNAU na 3GPP Explorer](https://3gpp-explorer.com/glossary/rnau/)
