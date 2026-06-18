---
slug: "nml"
url: "/mobilnisite/slovnik/nml/"
type: "slovnik"
title: "NML – Network Management Layer"
date: 2025-01-01
abbr: "NML"
fullName: "Network Management Layer"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/nml/"
summary: "NML (Network Management Layer, vrstva správy sítě) je funkční vrstva v hierarchii Telekomunikační správy sítě (TMN) zodpovědná za správu celé sítě od konce ke konci. Poskytuje pohled na celou síť tím,"
---

NML je funkční vrstva v hierarchii Telekomunikační správy sítě (Telecommunications Management Network) zodpovědná za správu celé sítě od konce ke konci prostřednictvím korelace dat na úrovni prvků pro správu služeb, korelaci poruch a analýzu výkonnosti.

## Popis

NML (Network Management Layer, vrstva správy sítě) je klíčový architektonický koncept v modelu Telekomunikační správy sítě ([TMN](/mobilnisite/slovnik/tmn/)) dle [ITU-T](/mobilnisite/slovnik/itu-t/), který byl přijat a upraven 3GPP pro správu mobilních sítí. V pyramidě TMN se nachází nad vrstvou správy prvků ([EML](/mobilnisite/slovnik/eml/)) a pod vrstvou správy služeb ([SML](/mobilnisite/slovnik/sml/)). Primární odpovědností NML je správa sítě jako celku, nikoliv jednotlivých prvků. Toho dosahuje agregací a korelací dat (alarmů, metrik výkonnosti, konfiguračních dat) přijatých z různých systémů správy prvků ([EMS](/mobilnisite/slovnik/ems/)), které spravují konkrétní podsítě nebo domény dodavatelů.

Z architektonického hlediska je NML implementována v rámci systému správy sítě ([NMS](/mobilnisite/slovnik/nms/)), často jako součást systému podpory provozu ([OSS](/mobilnisite/slovnik/oss/)). S EML komunikuje prostřednictvím standardizovaných rozhraní (např. rozhraní Itf-N v 3GPP). NML obsahuje aplikace a funkce s působností pro celou síť. Mezi klíčové komponenty patří správa poruch sítě (Network Fault Management), která provádí korelaci alarmů a analýzu hlavní příčiny napříč více prvky za účelem potlačení redundantních alarmů a identifikace primárního místa poruchy. Správa výkonnosti sítě (Network Performance Management) agreguje [KPI](/mobilnisite/slovnik/kpi/) z různých segmentů sítě pro vyhodnocení výkonnosti služeb od konce ke konci a provádění traffic engineeringu. Správa konfigurace sítě (Network Configuration Management) zajišťuje správu topologie a koordinaci konfiguračních změn napříč více doménami.

Princip fungování: NML přijímá předzpracovaná data z EMS. Například EMS pro RAN může odeslat konsolidovaný alarm o degradaci skupiny buněk, zatímco EMS pro core může odeslat data o výkonnosti konkrétní služby. Korelační engine pro poruchy v NML využívá modely topologie a závislostí k propojení těchto událostí, což může vést k identifikaci problému v core síti jako hlavní příčiny problému v RAN. Její aplikace pro správu výkonnosti počítají z elementárních dat složené KPI na úrovni služeb, čímž poskytují pohled na zákaznickou zkušenost. NML poskytuje tyto syntetizované, na síť zaměřené informace výše do vrstvy správy služeb (SML) pro obchodní a zákaznicky orientované procesy a vydává koordinované příkazy směrem dolů k EML pro nápravné akce.

## K čemu slouží

NML byla koncipována k řešení výzev správy sítí složených z četných heterogenních síťových prvků od různých dodavatelů. Správa takových sítí pouze na úrovni prvků (EML) vede k provozním izolovaným celkům (silosům), informačnímu přetížení z nekorelovaných alarmů a neschopnosti porozumět celkovému chování sítě nebo dopadu poruch na služby poskytované od konce ke konci.

NML tyto problémy řeší zavedením vrstvy abstrakce a korelace. Poskytuje „pohled na síť“, který je klíčový pro efektivní provoz. Její vznik byl motivován potřebou provozní efektivity, snížení střední doby do opravy (MTTR) prostřednictvím inteligentní korelace poruch a schopnosti spravovat služby namísto pouze jednotlivých zařízení. NML umožňuje operátorům přejít od reaktivního řešení problémů zaměřeného na prvky k proaktivní správě a optimalizaci sítě s ohledem na služby. Její standardizace v rámci TMN a 3GPP zajišťuje, že EMS od různých dodavatelů mohou do NML poskytovat konzistentní informace, což umožňuje interoperabilitu mezi více dodavateli.

## Klíčové vlastnosti

- Poskytuje pohled na správu sítě od konce ke konci s působností pro celou síť nad úrovní prvků
- Provádí korelaci alarmů, jejich filtrování a analýzu hlavní příčiny napříč doménami
- Agreguje a analyzuje data o výkonnosti z více segmentů sítě za účelem výpočtu KPI na úrovni služeb
- Spravuje topologii sítě a koordinuje konfigurační změny napříč různými doménami správy
- Slouží jako zprostředkující vrstva mezi vrstvou správy prvků (EML) a vrstvou správy služeb (SML)
- Implementuje síťové politiky pro správu poruch, výkonnosti a konfigurace

## Související pojmy

- [TMN – Telecommunications Management Network](/mobilnisite/slovnik/tmn/)
- [NMS – Network Management Subsystem](/mobilnisite/slovnik/nms/)

## Definující specifikace

- **TS 32.101** (Rel-19) — Management principles and high-level requirements
- **TS 32.819** (Rel-8) — Element Management Layer OS Functions

---

📖 **Anglický originál a plná specifikace:** [NML na 3GPP Explorer](https://3gpp-explorer.com/glossary/nml/)
