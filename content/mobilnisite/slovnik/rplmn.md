---
slug: "rplmn"
url: "/mobilnisite/slovnik/rplmn/"
type: "slovnik"
title: "RPLMN – Registered Public Land Mobile Network"
date: 2025-01-01
abbr: "RPLMN"
fullName: "Registered Public Land Mobile Network"
category: "Mobility"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/rplmn/"
summary: "Veřejná pozemní mobilní síť (PLMN), ve které je uživatelské zařízení (UE) aktuálně registrováno a smí přijímat služby. Je to základní koncept pro výběr sítě, roaming a správu mobility, který zajišťuje"
---

RPLMN je veřejná pozemní mobilní síť, ve které je uživatelské zařízení (UE) aktuálně registrováno a autorizováno pro příjem mobilních služeb.

## Popis

Registered Public Land Mobile Network (RPLMN) je klíčový identifikátor v protokolech pro správu mobility 3GPP. Představuje konkrétní veřejnou pozemní mobilní síť (identifikovanou kódem mobilní země a kódem mobilní sítě – MCC-MNC), u které uživatelské zařízení (UE) úspěšně provedlo registrační proceduru a je aktuálně považováno za 'připojené' nebo 'registrované'. Tato registrace uděluje UE autorizaci pro přístup ke službám této sítě, včetně hlasových, datových a doplňkových služeb. RPLMN je uložena v nevolatilní paměti UE a v síťové databázi účastníků (např. [HSS](/mobilnisite/slovnik/hss/)/[UDM](/mobilnisite/slovnik/udm/)). Je to klíčový parametr, který UE a síť používají pro správu stavu UE a kontinuity služeb.

Z architektonického hlediska je RPLMN ústřední pro procesy výběru a převýběru sítě definované v protokolech Non-Access Stratum ([NAS](/mobilnisite/slovnik/nas/)). Když je UE zapnuto nebo ztratí pokrytí, vyhledává dostupné [PLMN](/mobilnisite/slovnik/plmn/). Výběrový algoritmus upřednostňuje RPLMN, pokud je dostupná, protože to je síť, ke které je UE již předplaceno. Tento koncept je nedílnou součástí všech generací 3GPP, od GSM/[GPRS](/mobilnisite/slovnik/gprs/) (kde může být zmiňován v kontextu lokální oblasti) přes UMTS a LTE až po 5G. V 5G je RPLMN udržována jako součást kontextu 5G Mobility Management ([5GMM](/mobilnisite/slovnik/5gmm/)) UE a je klíčová pro počáteční registraci a aktualizace registrace mobility.

Jak to funguje, zahrnuje vícestupňovou interakci mezi UE a jádrem sítě. Po úspěšné autentizaci a registraci v síti se identifikátor PLMN této sítě stane RPLMN UE. Síť tuto registraci potvrdí ve svých entitách jádra sítě. UE pak bude této RPLMN periodicky nebo při specifických událostech (jako je pohyb) hlásit svou polohu. Pokud UE opustí oblast pokrytí své RPLMN, může se zaregistrovat u nové PLMN (která se pak stane novou RPLMN), pokud existuje roamingová dohoda, nebo se může pokusit o převýběr původní RPLMN, když se vrátí do oblasti pokrytí. RPLMN se liší od, ale souvisí se seznamem ekvivalentních PLMN ([EPLMN](/mobilnisite/slovnik/eplmn/)), který obsahuje sítě považované za ekvivalentní k RPLMN pro účely převýběru buňky a předávání hovoru, což usnadňuje plynulou mobilitu.

## K čemu slouží

Koncept RPLMN byl vytvořen, aby poskytl jasný a jednoznačný referenční bod pro 'domovskou' nebo aktuálně aktivní síť mobilního zařízení v globálním ekosystému více nezávislých operátorských sítí. Řeší základní problém identity sítě a autorizace služeb v roamingovém prostředí. Před zavedením takových standardizovaných konceptů by bylo řízení mobility účastníků napříč různými operátorskými doménami chaotické a nejisté.

Historicky, jak se mobilní sítě vyvíjely z nasazení jednotlivých operátorů k národním a mezinárodním roamingovým konsorciím, byl potřebný mechanismus pro sledování, kde je účastník registrován a která síť je v daném okamžiku odpovědná za poskytování služeb a jejich účtování. RPLMN tento kotvící bod poskytuje. Odstraňuje omezení pouhého detekování rádiového signálu tím, že váže přístup ke službám k formálnímu registračnímu a předplatitelskému vztahu. Umožňuje funkce jako roaming (díky tomu, že navštívená [PLMN](/mobilnisite/slovnik/plmn/) zná domovskou PLMN účastníka pro účtování a načtení profilu služeb), prioritní výběr sítě (vždy se nejprve pokusit použít svou registrovanou síť) a efektivní správu mobility (síť ví, která skupina buněk a oblastí sledování je spojena s danou RPLMN). Její trvalé uložení v paměti UE umožňuje rychlejší obnovení služeb po vypnutí a zapnutí zařízení nebo po dočasné ztrátě signálu.

## Klíčové vlastnosti

- Definuje PLMN, u které je UE aktuálně registrováno a autorizováno pro služby.
- Trvale uložena v nevolatilní paměti UE a v síťové databázi účastníků.
- Používána jako síť s nejvyšší prioritou v automatickém algoritmu výběru sítě UE.
- Slouží jako klíčový parametr pro procedury správy mobility, jako jsou aktualizace oblasti sledování (TAU) a aktualizace směrovací oblasti (RAU).
- Základní pro roamingové dohody, umožňuje navštíveným sítím identifikovat domovskou síť uživatele.
- Liší se od, ale používá se společně se seznamem ekvivalentních PLMN (EPLMN).

## Související pojmy

- [PLMN – Public Land Mobile Network](/mobilnisite/slovnik/plmn/)
- [EPLMN – Equivalent PLMN](/mobilnisite/slovnik/eplmn/)
- [VPLMN – Visited Public Land Mobile Network](/mobilnisite/slovnik/vplmn/)
- [NAS – Non-Access Stratum](/mobilnisite/slovnik/nas/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification
- **TS 37.320** (Rel-19) — Minimization of Drive Tests (MDT) Overview
- **TS 38.331** (Rel-19) — NR Radio Resource Control (RRC) Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [RPLMN na 3GPP Explorer](https://3gpp-explorer.com/glossary/rplmn/)
