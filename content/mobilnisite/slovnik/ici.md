---
slug: "ici"
url: "/mobilnisite/slovnik/ici/"
type: "slovnik"
title: "ICI – Interception Configuration Information"
date: 2025-01-01
abbr: "ICI"
fullName: "Interception Configuration Information"
category: "Security"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ici/"
summary: "Interception Configuration Information (ICI, informace o konfiguraci odposlechu) je standardizovaná sada dat používaná ke konfiguraci funkcí zákonného odposlechu (LI) v síti 3GPP. Definuje cíl (účastn"
---

ICI je standardizovaná sada dat používaná ke konfiguraci funkcí zákonného odposlechu definováním cíle, obsahu, který má být shromažďován, a parametrů doručení pro orgány činné v trestním řízení.

## Popis

Interception Configuration Information (ICI, informace o konfiguraci odposlechu) je klíčová součást architektury zákonného odposlechu ([LI](/mobilnisite/slovnik/li/)) dle 3GPP, definovaná v mnoha technických specifikacích. Představuje strukturovaná data, která autorizovaný subjekt (typicky orgán činný v trestním řízení prostřednictvím příslušného úřadu) poskytne řídicímu prvku odposlechu ([ICE](/mobilnisite/slovnik/ice/)) operátora sítě za účelem aktivace, změny nebo deaktivace příkazu k odposlechu. ICI je v podstatě 'příkaz' ve strojově čitelném formátu, obsahující všechny potřebné instrukce pro síť, aby odposlech provedla legálně a správně.

ICI se skládá z několika klíčových informačních prvků. Primárně zahrnuje Identifikátor cíle, který jednoznačně specifikuje účastníka (např. [IMSI](/mobilnisite/slovnik/imsi/), [MSISDN](/mobilnisite/slovnik/msisdn/)) nebo službu, jež mají být monitorovány. Definuje Rozsah odposlechu, který určuje typy komunikací, jež mají být odposlouchávány – například hovory v přepojování okruhů, datové relace v přepojování paketů, SMS nebo IMS relace. Dále obsahuje Akci odposlechu, která udává, zda se má odposlech aktivovat, deaktivovat nebo upravit. Zásadně poskytuje Parametry doručení, které detailně popisují adresu (IP adresu a port) monitorovacího zařízení orgánů činných v trestním řízení ([LEMF](/mobilnisite/slovnik/lemf/)), kam musí být zachycený obsah ([CC](/mobilnisite/slovnik/cc/)) a informace související s odposlechem ([IRI](/mobilnisite/slovnik/iri/)) bezpečně doručeny.

Z architektonického hlediska ICI přijímá Administrační funkce ([ADMF](/mobilnisite/slovnik/admf/)) nebo přímo příslušné ICE (např. v jádru sítě nebo v přístupové síti). ADMF ICI ověří a distribuuje příslušné konfigurační příkazy k síťovým prvkům zapojeným do odposlechu (např. MSC, SGSN, PGW, PCF). Tyto prvky pak používají parametry v ICI k identifikaci provozu cíle, duplikaci relevantních paketů nebo signalizačních zpráv a jejich předání určené Doručovací funkci (DF), která data formátuje a odesílá do LEMF. ICI zajišťuje, že odposlech je přesně vymezen, aby nedocházelo k nadměrnému shromažďování, a že mechanismus doručení splňuje požadované standardy zabezpečení a spolehlivosti. Jeho standardizovaný formát umožňuje interoperabilitu mezi různými síťovými dodavateli a systémy orgánů činných v trestním řízení.

## K čemu slouží

ICI bylo vytvořeno, aby vyřešilo kritickou potřebu standardizované, bezpečné a spolehlivé metody konfigurace zákonného odposlechu napříč složitými, více-dodavatelskými sítěmi 3GPP. S digitalizací a rozvojem mobilní telekomunikace potřebovaly orgány činné v trestním řízení technicky robustní prostředek k provádění příkazů k zákonnému odposlechu. Před standardizací byly mechanismy odposlechu často proprietární, specifické pro danou zemi a nekonzistentní, což operátorům ztěžovalo efektivní plnění zákonných požadavků a orgánům práci s daty z různých sítí.

Primární problém, který ICI řeší, je překlad právního příkazu (lidsky čitelného dokumentu) do přesné sady technických instrukcí, kterým automatizované síťové zařízení rozumí a může je provést. Definuje společný jazyk mezi právním a síťovým světem. Tato standardizace zajišťuje, že žádost o odposlech znamená totéž ve Švédsku i v Jižní Koreji, za předpokladu, že obě země dodržují specifikace 3GPP. Zabraňuje nejednoznačnosti při definování cíle, rozsahu odposlechu a způsobu doručení.

K jeho vytvoření vedly právní požadavky na odposlech telekomunikací v mnoha jurisdikcích spolu s globalizací síťového vybavení. Standardizované ICI umožňuje síťovým dodavatelům zabudovat schopnosti LI do svých produktů tak, aby fungovaly kdekoli, snižuje náklady a složitost pro operátory při plnění místních zákonů a poskytuje orgánům činným v trestním řízení předvídatelné a bezpečné rozhraní. Vyvažuje potřebu efektivního vymáhání práva se zásadami soukromí a minimalizace dat tím, že vyžaduje explicitní konfiguraci pro každou akci odposlechu.

## Klíčové vlastnosti

- Jednoznačně identifikuje cíl odposlechu pomocí identifikátorů účastníka nebo služby (např. IMSI, MSISDN)
- Definuje přesný rozsah odposlechu (např. pouze hovory, všechna paketová data, SMS)
- Specifikuje akci: aktivaci, deaktivaci nebo změnu příkazu k odposlechu
- Obsahuje doručovací adresu (IP/port) pro monitorovací zařízení orgánů činných v trestním řízení (LEMF)
- Poskytuje standardizovaný, strojově čitelný formát pro příkazy k odposlechu
- Zajišťuje, že se konfigurace bezpečně a přesně distribuuje všem relevantním síťovým prvkům (ICE)

## Související pojmy

- [ADMF – Administration Function](/mobilnisite/slovnik/admf/)
- [IRI – Intercept Related Information](/mobilnisite/slovnik/iri/)
- [CC – Component Carrier](/mobilnisite/slovnik/cc/)
- [LEMF – Law Enforcement Monitoring Facility](/mobilnisite/slovnik/lemf/)
- [ICE – Interactivity Connectivity Establishment](/mobilnisite/slovnik/ice/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 31.102** (Rel-19) — USIM Application Specification
- **TS 33.108** (Rel-19) — LI Handover Interface Specification
- **TR 38.808** (Rel-17) — Study on NR above 52.6 GHz to 71 GHz
- **TS 38.811** (Rel-15) — Study on NR Support for Non-Terrestrial Networks
- **TR 45.914** (Rel-19) — MUROS Feasibility Study for Voice Capacity

---

📖 **Anglický originál a plná specifikace:** [ICI na 3GPP Explorer](https://3gpp-explorer.com/glossary/ici/)
