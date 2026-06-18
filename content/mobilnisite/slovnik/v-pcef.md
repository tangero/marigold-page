---
slug: "v-pcef"
url: "/mobilnisite/slovnik/v-pcef/"
type: "slovnik"
title: "V-PCEF – Visited Policy and Charging Enforcement Function"
date: 2025-01-01
abbr: "V-PCEF"
fullName: "Visited Policy and Charging Enforcement Function"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/v-pcef/"
summary: "Funkce vynucování politik a účtování (PCEF) umístěná ve visited veřejné pozemní mobilní síti (VPLMN). Vynucuje pravidla politik a účtování pro roamujícího účastníka, komunikuje s PCRF domovské sítě, a"
---

V-PCEF (Visited Policy and Charging Enforcement Function) je funkce vynucování politik a účtování umístěná ve visited síti, která vynucuje pravidla politik a účtování pro roamujícího účastníka prostřednictvím rozhraní s PCRF domovské sítě.

## Popis

V-PCEF je kritická síťová funkce v architektuře řízení politik a účtování ([PCC](/mobilnisite/slovnik/pcc/)) podle 3GPP, určená speciálně pro roamingové scénáře. Nachází se ve visited veřejné pozemní mobilní síti ([VPLMN](/mobilnisite/slovnik/vplmn/)), což je síť, ke které je účastník fyzicky připojen, když je mimo geografické pokrytí své domovské veřejné pozemní mobilní sítě ([HPLMN](/mobilnisite/slovnik/hplmn/)). Primární rolí V-PCEF je vynucovat dynamická pravidla politik a účtování na provoz v uživatelské rovině pro roamujícího účastníka. Typicky je společně umístěna s uzlem GGSN v [GPRS](/mobilnisite/slovnik/gprs/) jádru nebo s branou [PGW](/mobilnisite/slovnik/pgw/) ve vyvinutém paketovém jádru (EPC). V-PCEF komunikuje s domovským [PCRF](/mobilnisite/slovnik/pcrf/) ([H-PCRF](/mobilnisite/slovnik/h-pcrf/)) přes roamingové rozhraní S9, které je založeno na protokolu Diameter. Prostřednictvím tohoto rozhraní H-PCRF poskytuje V-PCEF pravidla PCC odvozená z profilu účastníka a servisních dat. Tato pravidla PCC obsahují instrukce pro řízení přístupu (povolení/blokování provozu), parametry QoS (jako garantovaný bitový tok a priorita alokace/zachování) a informace pro účtování (např. účtovací klíče a metody měření). V-PCEF tato pravidla nainstaluje a uplatní je na příslušném nosiči [IP-CAN](/mobilnisite/slovnik/ip-can/). Provádí funkce jako inspekce paketů, filtrování a označování, aby zajistila, že provoz obdrží smluvně dohodnutou QoS. Také generuje záznamy o účtovacích datech (CDR) na základě uplatněných pravidel a předává je příslušnému účtovacímu systému ve VPLMN. Toto vynucování zajišťuje, že uživatelská zkušenost a účtování roamujícího uživatele jsou konzistentní s jeho předplatným v domovské síti, i když je obsluhován infrastrukturou zahraničního operátora.

## K čemu slouží

V-PCEF byla zavedena, aby řešila složitost uplatňování konzistentního řízení politik a účtování pro účastníky roamující mezi různými operátory mobilních sítí. Před její standardizací představovaly roamingové scénáře významné výzvy pro vynucování servisních politik domovského operátora (jako QoS pro specifické aplikace) a přesné účtování ve visited síti. Navštívená síť neměla kontext profilu předplatného účastníka v jeho domovské síti. V-PCEF jako součást architektury PCC to řeší vytvořením standardizovaného řídicího rozhraní (S9) mezi domovskou a navštívenou sítí. To umožňuje domovskému operátorovi zachovat kontrolu nad rozhodnutími o politikách (přijímanými H-PCRF), zatímco vynucování těchto rozhodnutí deleguje na důvěryhodnou funkci uvnitř visited sítě. Toto oddělení řízení a vynucování napříč administrativními doménami umožňuje pokročilé, dynamické poskytování služeb pro roamující uživatele, podporuje mezifiremní QoS dohody a usnadňuje přesné a transparentní účtování, což je zásadní pro komerční roamingové dohody. Zajišťuje, že služby jako hlas nebo video založené na IMS, které mají striktní požadavky na QoS, fungují pro roamujícího uživatele plynule stejně jako v domovské síti.

## Klíčové vlastnosti

- Vynucuje pravidla PCC z domovského PCRF na provoz roamujícího uživatele.
- Umístěna na bráně (GGSN/PGW) ve visited PLMN.
- Komunikuje s H-PCRF přes referenční bod S9 založený na Diameter.
- Aplikuje řízení přístupu, označování QoS a správu šířky pásma podle pravidel PCC.
- Generuje záznamy o účtovacích datech (CDR) za roamingové využití.
- Podporuje dynamické řízení politik pro toky servisních dat (SDF).

## Související pojmy

- [PCEF – Policy and Charging Enforcement Function](/mobilnisite/slovnik/pcef/)
- [PCRF – Policy and Charging Rules Function](/mobilnisite/slovnik/pcrf/)

## Definující specifikace

- **TS 23.203** (Rel-19) — Policy and charging control architecture

---

📖 **Anglický originál a plná specifikace:** [V-PCEF na 3GPP Explorer](https://3gpp-explorer.com/glossary/v-pcef/)
