---
slug: "lho"
url: "/mobilnisite/slovnik/lho/"
type: "slovnik"
title: "LHO – Legacy Handover"
date: 2026-01-01
abbr: "LHO"
fullName: "Legacy Handover"
category: "Mobility"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/lho/"
summary: "Funkce správy sítě pro předávání spojení zahrnující starší síťové uzly, jako jsou základnové stanice 2G/3G, v kontextu 5G sítě. Zajišťuje zpětnou kompatibilitu a plynulou mobilitu pro uživatelské zaří"
---

LHO je funkce správy sítě pro předávání spojení (handover) zahrnující starší uzly, jako jsou základnové stanice 2G/3G, která zajišťuje zpětnou kompatibilitu a plynulou mobilitu mezi 5G NR a staršími rádiovými přístupovými technologiemi.

## Popis

Legacy Handover (LHO) je koncept a soubor procedur definovaný v rámci specifikací správy 3GPP, konkrétně TS 28.552 pro správu 5G sítí. Odkazuje na procesy předávání spojení (handover), které zahrnují starší rádiové přístupové technologie ([RAT](/mobilnisite/slovnik/rat/)), jako jsou GSM, UMTS a LTE, když spolupracují s 5G New Radio (NR) jako součást více-RAT sítě. LHO není jediný protokol, ale spravovaná schopnost v rámci systému Operation, Administration, and Maintenance ([OAM](/mobilnisite/slovnik/oam/)), která se zaměřuje na konfiguraci, monitorování a optimalizaci výkonu předávání spojení mezi 5G a těmito staršími systémy.

Architektonicky je funkčnost LHO implementována v systémech Network Management ([NM](/mobilnisite/slovnik/nm/)) a Domain Management ([DM](/mobilnisite/slovnik/dm/)), jako je Network Resource Model ([NRM](/mobilnisite/slovnik/nrm/)) pro 5G. Zahrnuje spravované objekty, které reprezentují vztahy předávání spojení a měření výkonu mezi 5G Next Generation NodeB (gNB) nebo ng-eNB a staršími základnovými stanicemi, jako jsou [eNB](/mobilnisite/slovnik/enb/) (LTE), NodeB (UMTS) nebo [BTS](/mobilnisite/slovnik/bts/) (GSM). Systém OAM shromažďuje klíčové ukazatele výkonu ([KPI](/mobilnisite/slovnik/kpi/)) související s těmito předáváními spojení, jako jsou úspěšnost předání, chyby přípravy, časy provedení a selhání rádiového spojení po předání. Tyto KPI jsou definovány jako měření výkonu v NRM a jsou klíčové pro síťové operátory při hodnocení a zajišťování plynulé mobility pro UE schopná více-RAT provozu.

Jak to funguje: systém OAM poskytuje parametry politiky předávání spojení (např. prahové hodnoty, biasy pro události A2/B2 v propojení LTE-NR) k uzlům RAN přes rozhraní Itf-N. Uzly RAN (gNB a starší eNB/NodeB) pak provedou skutečné procedury předávání spojení na rádiové úrovni (např. předání založená na X2 nebo N2/N26) na základě měření od UE a těchto nakonfigurovaných politik. Funkce správy LHO v systému OAM monitoruje výsledky a spouští optimalizační akce, pokud se KPI zhorší. Například může upravit hodnoty cell individual offsets (CIO) nebo hystereze pro události předání spojení mezi 5G buňkou a 3G buňkou, aby se snížil ping-pong efekt nebo přerušení hovoru. Jejím úkolem je poskytovat nástroje na rovině správy nezbytné pro udržení robustní mobility v heterogenní síti během přechodného období, kdy se pokrývání 5G zavádí souběžně s rozsáhlou infrastrukturou 2G/3G/4G.

## K čemu slouží

LHO bylo zavedeno, aby řešilo kritickou výzvu při postupném nasazování 5G sítí: udržení plynulé mobility a kontinuity služeb pro UE, když se pohybují mezi novými oblastmi pokrytí 5G a stávajícími staršími (2G, 3G, 4G) sítěmi. Před 5G byla předávání spojení mezi různými RAT řízena v protokolech RAN a core sítě, ale správa a optimalizace těchto procedur z jednotné perspektivy OAM pro éru 5G vyžadovala novou standardizaci. Stávající modely správy pro LTE plně nezahrnovaly integraci a správu výkonu předávání spojení do/z 5G NR, zejména se zvýšenou komplexitou síťového řezání (network slicing) a duální konektivity.

Hlavní problém, který řeší, je poskytnout síťovým operátorům potřebné schopnosti správy pro monitorování, konfiguraci a optimalizaci výkonu předávání spojení zahrnujících starší RAT v prostředí 5G sítě. Bez standardizované správy LHO by operátoři postrádali přehled o klíčových mobilních KPI mezi 5G a staršími technologiemi, což by ztěžovalo řešení problémů, jako jsou selhání předání spojení, špatná kontinuita hlasových hovorů (např. EPS Fallback na LTE/UMTS) nebo neefektivní využití zdrojů při směrování síťového provozu. To je obzvláště důležité pro nasazení 5G zaměřená na pokrytí (např. využívající NR v nízkých pásmech), kde jsou předávání spojení na všudypřítomné LTE nebo 3G pro doplnění pokrytí častá.

Jeho vytvoření ve vydání Release 17 bylo motivováno praktickou realitou, že 5G NR bude po mnoho let koexistovat se staršími sítěmi. Pracovní skupina 3GPP SA5 (Management and Orchestration) rozpoznala potřebu rozšířit 5G NRM o správu výkonu pro tyto nezbytné interakce se staršími technologiemi. LHO umožňuje operátorům zajistit Quality of Experience (QoE) během tohoto přechodu, podporuje případy užití jako fallback hlasových služeb, rozšíření pokrytí a vyvažování zátěže mezi různými generacemi RAT prostřednictvím spravovaných a optimalizovaných politik předávání spojení, což je klíčové pro hladký zákaznický zážitek a efektivní provoz sítě.

## Klíčové vlastnosti

- Schopnost na rovině správy pro monitorování předávání spojení mezi 5G NR a staršími RAT (2G/3G/4G)
- Definuje klíčové ukazatele výkonu (KPI) pro úspěšnost a míru selhání předávání spojení se staršími technologiemi
- Součást 5G Network Resource Model (NRM) pro zajištění výkonu
- Umožňuje konfiguraci parametrů politiky předávání spojení prostřednictvím systémů OAM
- Podporuje optimalizaci robustnosti mobility v heterogenních sítích
- Usnadňuje řešení problémů s mobilitou mezi různými RAT v nasazeních 5G

## Související pojmy

- [NRM – Network Resource Model](/mobilnisite/slovnik/nrm/)
- [OAM – Operations, Administration, and Maintenance](/mobilnisite/slovnik/oam/)

## Definující specifikace

- **TS 28.552** (Rel-20) — 5G Performance Management Measurements

---

📖 **Anglický originál a plná specifikace:** [LHO na 3GPP Explorer](https://3gpp-explorer.com/glossary/lho/)
