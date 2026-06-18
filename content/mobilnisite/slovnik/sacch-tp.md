---
slug: "sacch-tp"
url: "/mobilnisite/slovnik/sacch-tp/"
type: "slovnik"
title: "SACCH/TP – SACCH for enhanced power control"
date: 2025-01-01
abbr: "SACCH/TP"
fullName: "SACCH for enhanced power control"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/sacch-tp/"
summary: "Specializovaná varianta pomalého přidruženého řídicího kanálu (Slow Associated Control Channel) navržená pro přenos rozšířených informací o řízení výkonu v sítích GSM. Dynamičtěji než standardní SACCH"
---

SACCH/TP je specializovaná varianta kanálu GSM navržená pro přenos rozšířených informací o řízení výkonu, která umožňuje dynamičtější optimalizaci výkonu ve směru uplink a downlink než standardní SACCH.

## Popis

[SACCH](/mobilnisite/slovnik/sacch/) pro rozšířené řízení výkonu (SACCH/[TP](/mobilnisite/slovnik/tp/)) je logický kanál definovaný ve specifikacích GSM rádiového rozhraní, zavedený speciálně pro podporu pokročilých algoritmů řízení výkonu. Podobně jako standardní [SACCH/T](/mobilnisite/slovnik/sacch-t/) jde o přidružený řídicí kanál, ale jeho informační obsah a použití jsou přizpůsobeny signalizaci pro řízení výkonu. Funguje na stejném principu multiplexování s kanálem pro přenos hovoru, přičemž využívá vyhrazené rámce v rámci struktury mnohorámce pro přenos zpráv souvisejících s řízením výkonu. SACCH/TP umožňuje častější a podrobnější příkazy pro řízení výkonu ve srovnání s možnostmi standardního SACCH, což síti umožňuje upravovat vysílací výkon mobilní stanice a výkon downlinku základnové stanice s vyšší přesností a rychlejší odezvou.

Z architektonického hlediska je SACCH/TP integrován do protokolů GSM vrstvy 1 a vrstvy 2. Je definován pro spolupráci s kanály pro přenos hovoru (Traffic Channels) a využívá stejné principy přidělování fyzických zdrojů. Klíčový rozdíl spočívá v sadě zpráv a spouštěcích mechanismech. Zatímco standardní SACCH přenáší obecné měřicí reporty a periodické příkazy pro řízení výkonu, SACCH/TP může být použit pro přenos rozšířených měřicích informací specificky zaměřených na rozhodování o řízení výkonu, jako jsou podrobné měření interference nebo indikátory kvality z pohledu mobilní stanice ([MS](/mobilnisite/slovnik/ms/)) i základnové stanice ([BTS](/mobilnisite/slovnik/bts/)). Tato data zpracovává řadič základnových stanic ([BSC](/mobilnisite/slovnik/bsc/)), který spouští rozšířené algoritmy řízení výkonu pro určení optimálních úrovní výkonu.

Kanál funguje tak, že umožňuje síti nařizovat rychlejší úpravy vysílacího výkonu. Ve směru uplink může BSC posílat prostřednictvím SACCH/TP příkazy pro řízení výkonu k MS na základě vyhodnocení kvality spoje v reálném čase. Ve směru downlink může MS poskytovat rozšířenou zpětnou vazbu o přijímaném downlink signálu, což síti umožňuje upravovat vysílací výkon BTS. Tato obousměrná, rozšířená regulační smyčka pomáhá udržovat minimální nezbytný výkon pro uspokojivé spojení, čímž se snižuje celková interference na společném kanálu v síti. Provoz SACCH/TP je zvláště cenný v hustých městských nasazeních nebo scénářích s vysokou kapacitou, kde je přesné řízení výkonu klíčové pro výkon systému a kvalitu služeb.

## K čemu slouží

[SACCH](/mobilnisite/slovnik/sacch/)/[TP](/mobilnisite/slovnik/tp/) byl zaveden, aby řešil omezení standardního mechanismu řízení výkonu v GSM, který byl primárně založen na periodických měřicích reportech odesílaných prostřednictvím běžného SACCH. Jak se sítě vyvíjely a požadavky na kapacitu rostly, hrubé řízení výkonu vedlo k neoptimálním úrovním interference a snížené spektrální účinnosti. Obnovovací frekvence standardního SACCH (přibližně každých 480 ms) byla někdy příliš pomalá na sledování rychlého útlumu (fast fading) nebo rychle se měnících podmínek interference, zejména pro vysokorychlostní mobilní stanice nebo v prostředích s omezením interference.

Motivováno potřebou zlepšit výkon a kapacitu sítě, zavedla 3GPP SACCH/TP ve vydání 8 jako součást vylepšení GSM/EDGE. Poskytuje vyhrazený kanál pro rozšířenou signalizaci řízení výkonu, což umožňuje dynamičtější a rychlejší úpravy výkonu. Tím se řeší klíčové problémy: efektivněji se snižuje interference ve směru uplink i downlink, což zvyšuje celkovou kapacitu systému a zlepšuje kvalitu hovoru. Také přispívá k delší výdrži baterie mobilní stanice tím, že umožňuje přesnější snížení výkonu, když je to možné. SACCH/TP představuje vývoj technik řízení rádiových zdrojů, který umožňuje GSM sítím zůstat konkurenceschopné začleněním pokročilejších řídicích mechanismů podobných těm, které se používají v systémech 3G a 4G.

## Klíčové vlastnosti

- Vyhrazený logický kanál pro rozšířenou signalizaci řízení výkonu
- Umožňuje častější a podrobnější příkazy pro řízení výkonu než standardní SACCH
- Přenáší rozšířené měřicí informace pro rozhodování o řízení výkonu
- Podporuje optimalizaci řízení výkonu pro směr uplink (MS) i downlink (BTS)
- Snižuje interferenci na společném kanálu, čímž zvyšuje kapacitu sítě
- Integrován s mnohorámcovou strukturou GSM kanálu pro přenos hovoru

## Související pojmy

- [SACCH/T – Slow Associated Control CHannel/Traffic channel](/mobilnisite/slovnik/sacch-t/)
- [GSM – Global System for Mobile Communications](/mobilnisite/slovnik/gsm/)
- [EDGE – Enhanced Data rates for Global Evolution](/mobilnisite/slovnik/edge/)

## Definující specifikace

- **TS 43.051** (Rel-19) — GERAN Stage 2 Service Description

---

📖 **Anglický originál a plná specifikace:** [SACCH/TP na 3GPP Explorer](https://3gpp-explorer.com/glossary/sacch-tp/)
