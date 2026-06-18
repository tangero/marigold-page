---
slug: "urrp-sgsn"
url: "/mobilnisite/slovnik/urrp-sgsn/"
type: "slovnik"
title: "URRP-SGSN – UE Reachability Request Parameter for SGSN"
date: 2025-01-01
abbr: "URRP-SGSN"
fullName: "UE Reachability Request Parameter for SGSN"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/urrp-sgsn/"
summary: "Parametr používaný SGSN k žádosti MME o provedení procedury dosažitelnosti UE. Je klíčovým prvkem v interoperabilitě mezi sítěmi 2G/3G GPRS a 4G EPC, který umožňuje efektivní paging a správu mobility"
---

URRP-SGSN (parametr žádosti o dosažitelnost UE pro SGSN) je parametr používaný SGSN k žádosti MME o provedení procedury dosažitelnosti UE, který umožňuje efektivní paging a správu mobility napříč sítěmi 2G/3G a 4G.

## Popis

UE Reachability Request [Parameter](/mobilnisite/slovnik/parameter/) for [SGSN](/mobilnisite/slovnik/sgsn/) (URRP-SGSN) je specifický informační prvek definovaný ve specifikacích 3GPP pro rozhraní S3, které spojuje Serving [GPRS](/mobilnisite/slovnik/gprs/) Support Node (SGSN) paketového jádra 2G/3G s Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)) jádra 4G Evolved Packet Core (EPC). Jeho primární funkcí je sloužit jako spouštěč a řídicí mechanismus pro procedury dosažitelnosti UE v případě, že je UE registrována v EPC, ale jejím posledním známým obslužným uzlem byl SGSN. Když SGSN obdrží downlink data pro UE, která je v idle stavu (např. PMM-IDLE v GPRS), ale je známo, že je registrována v EPC, nemůže sama provést paging UE přes [GERAN](/mobilnisite/slovnik/geran/)/[UTRAN](/mobilnisite/slovnik/utran/), pokud je poslední známá poloha UE spravována MME. Místo toho SGSN zahrne parametr URRP-SGSN do zprávy (konkrétně procedury Context Request) odeslané MME přes rozhraní S3. Tento parametr informuje MME, že SGSN žádá MME o provedení procedury síťově iniciovaného service requestu za účelem opětovného navázání spojení s UE. MME po přijetí této žádosti následně iniciuje paging UE v jejím registrovaném tracking area/oblastech v rámci [E-UTRAN](/mobilnisite/slovnik/e-utran/). Tento mechanismus je klíčový pro zajištění doručení downlink dat k mobilnímu zařízení, které se přesunulo mezi oblastmi pokrytí 2G/3G a 4G, aniž by provedlo plnohodnotnou Tracking Area Update ([TAU](/mobilnisite/slovnik/tau/)) zpět do sítě 4G. Optimalizuje signalizaci tím, že umožňuje SGSN delegovat zodpovědnost za paging na uzel, který v cílové rádiové přístupové technologii aktuálně disponuje nejpřesnější informací o poloze UE. Parametr je součástí širší sady procedur mobility a dosažitelnosti mezi RAT, které zajišťují bezproblémovou kontinuitu služeb, jak je definováno v 3GPP TS 23.060, „General Packet Radio Service (GPRS); Service description.“

## K čemu slouží

URRP-SGSN byl zaveden, aby vyřešil konkrétní problém v interoperabilitě mezi sítěmi 2G/3G GPRS a novým systémem 4G Evolved Packet System (EPS). Před zavedením EPS byly paging a mobilita řešeny v rámci jedné domény jádrové sítě (GPRS). Se zavedením EPC a rozhraní S3 pro propojení jader bylo zapotřebí mechanismu pro zpracování příchozích downlink dat v situaci, kdy posledním známým bodem připojení UE byl starší systém, ale její aktuální registrace byla v novém systému. Bez URRP-SGSN by SGSN přijímající data pro UE známou jako EPS-registrovaná mohla neúspěšně pokusit o její paging v GERAN/UTRAN, což by vedlo ke ztrátě dat nebo nadměrné, neefektivní signalizaci při pokusech o lokalizaci UE. Parametr poskytuje standardizovaný a efektivní způsob, jakým SGSN signalizuje MME, že MME má podniknout kroky k opětovnému navázání spojení s UE, a využívá přitom znalosti MME o stavu EPS registrace a poloze UE. Toto byla kritická součást pro dosažení bezproblémové mobility a kontinuity služeb u prvních nasazení LTE, která spoléhala na handovery mezi RAT a mobilitu v idle módu se stávajícími sítěmi GSM/UMTS.

## Klíčové vlastnosti

- Spouští proceduru service request iniciovanou MME pro EPS-registrovaná UE
- Používá se v signalizaci rozhraní S3 mezi SGSN a MME
- Umožňuje efektivní doručování downlink dat během mobility mezi RAT v idle módu
- Součást procedury Context Request/Response
- Zabraňuje zbytečnému pagingu v nesprávné RAT
- Podporuje optimalizaci sítě delegováním pagingu na správný uzel jádrové sítě

## Související pojmy

- [SGSN – Serving GPRS Support Node](/mobilnisite/slovnik/sgsn/)
- [MME – NPC MME Network Product Class](/mobilnisite/slovnik/mme/)

## Definující specifikace

- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2

---

📖 **Anglický originál a plná specifikace:** [URRP-SGSN na 3GPP Explorer](https://3gpp-explorer.com/glossary/urrp-sgsn/)
