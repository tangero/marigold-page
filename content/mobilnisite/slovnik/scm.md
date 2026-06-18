---
slug: "scm"
url: "/mobilnisite/slovnik/scm/"
type: "slovnik"
title: "SCM – Single-Connection Mode"
date: 2025-01-01
abbr: "SCM"
fullName: "Single-Connection Mode"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/scm/"
summary: "Provozní režim uživatelského zařízení (UE), ve kterém si udržuje jediné, současné připojení nebo asociaci k síti Packet Data Network (PDN) prostřednictvím jedné sítě (3GPP nebo ne-3GPP). Je to základn"
---

SCM je provozní režim, ve kterém si uživatelské zařízení (UE) udržuje jediné, současné připojení k síti PDN prostřednictvím sítě 3GPP nebo ne-3GPP pro základní správu mobility zajišťovanou sítí.

## Popis

Režim jediného připojení (SCM) je klíčový koncept pro správu mobility zajišťovanou sítí 3GPP, formálně definovaný v dokumentu TS 23.402 pro architekturu System Architecture Evolution ([SAE](/mobilnisite/slovnik/sae/)). Popisuje stav uživatelského zařízení (UE), když je současně připojeno k jádru sítě přes právě jednu přístupovou síť. Toto jediné připojení představuje aktivní bod připojení pro IP provoz uživatelského zařízení. V kontextu Evolved Packet Core (EPC) to typicky znamená, že uživatelské zařízení má jedno aktivní připojení k síti [PDN](/mobilnisite/slovnik/pdn/) zřízené přes jedinou bránu Packet Data Network Gateway ([PGW](/mobilnisite/slovnik/pgw/)). Přístupovou sítí pro toto připojení může být 3GPP přístup jako [E-UTRAN](/mobilnisite/slovnik/e-utran/), [UTRAN](/mobilnisite/slovnik/utran/) nebo [GERAN](/mobilnisite/slovnik/geran/), nebo důvěryhodný/nedůvěryhodný ne-3GPP přístup jako Wi-Fi.

Technické fungování SCM je řízeno protokoly pro správu mobility. Pro uživatelské zařízení v režimu SCM veškerý jeho IP provoz protéká touto jedinou přenosovou cestou. Entita pro správu mobility (např. [MME](/mobilnisite/slovnik/mme/) pro 3GPP, ePDG pro nedůvěryhodný ne-3GPP přístup) sleduje polohu uživatelského zařízení a spravuje procedury předávání pro toto jediné připojení. IP adresa(y) uživatelského zařízení jsou ukotveny v jediné bráně PGW obsluhující toto připojení k síti PDN. Klíčové procedury jako Připojení (Attach), Zřízení připojení k síti PDN a Správa přenosových kanálů jsou prováděny s vědomím, že uživatelské zařízení je v tomto jedinečném stavu konektivity. Síťová pravidla pro politiky a účtování ([PCRF](/mobilnisite/slovnik/pcrf/)) jsou aplikována na tuto jedinou datovou cestu.

SCM se často porovnává s funkcionalitami Multi-Access PDN Connectivity (MAPCON) nebo IP Flow Mobility (IFOM), kde může uživatelské zařízení udržovat více současných připojení k síti PDN přes různé přístupy. V režimu SCM síť řeší události mobility (např. předání z LTE na Wi-Fi) přenosem celého připojení k síti PDN a s ním asociovaných přenosových kanálů z jednoho přístupu na druhý, což může zahrnovat proceduru předávání mezi přístupy. Tento koncept je zásadní pro pochopení toho, jak se uživatelské zařízení registruje, připojuje a je spravováno ve svém nejzákladnějším a nejběžnějším provozním stavu v rámci architektur EPS a 5GS, kde je vyžadována jednoduchost a směrování po jediné cestě.

## K čemu slouží

SCM byl definován za účelem stanovení jasného a základního výchozího stavu pro chování konektivity uživatelského zařízení v rámci nového, na přístupu nezávislého Evolved Packet System (EPS) zavedeného ve 3GPP Rel-8. Před EPS byla konektivita více izolovaná (např. připojení GPRS pro 2G/3G). EPS měl za cíl poskytnout bezproblémovou mobilitu a kontinuitu služeb napříč heterogenními přístupovými technologiemi (LTE, 3G, 2G, Wi-Fi) pod jednotným jádrem sítě. Formální definice stavu, kdy uživatelské zařízení používá v daný okamžik pouze jeden z těchto přístupů, byla nezbytná pro specifikaci standardních procedur.

Řeší problém nejednoznačnosti ve specifikacích pro správu mobility. Definováním SCM jako výchozího a nejjednoduššího režimu mohlo 3GPP přesně specifikovat procedury připojení, odpojení, předávání a správy přenosových kanálů pro tento případ. Tím byl vytvořen stabilní referenční model. Pokročilejší funkce, jako je současná konektivita přes více přístupů (např. MAPCON), byly následně definovány jako rozšíření nebo odchylky od tohoto základního chování SCM. Tento koncept je klíčový pro síťové implementace, aby správně zvládaly alokaci zdrojů, směrování, účtování a vynucování politik pro drtivou většinu uživatelských zařízení, která nepoužívají pokročilé funkce více konektivity, a zajišťovaly tak předvídatelný a efektivní provoz sítě.

## Klíčové vlastnosti

- Definuje stav uživatelského zařízení s jedním současným připojením k síti PDN/jedním přístupem.
- Základní pro správu mobility zajišťovanou sítí v EPS/5GS.
- Zjednodušuje směrování, přičemž veškerý IP provoz je ukotven v jedné bráně PGW/UPF.
- Slouží jako základní provozní režim pro většinu uživatelských zařízení.
- Umožňuje jasnou specifikaci procedur předávání mezi přístupy.
- Stojí v protikladu k funkcím s více připojeními, jako jsou MAPCON a IFOM.

## Související pojmy

- [EPC – Evolved Packet Core Network](/mobilnisite/slovnik/epc/)
- [MAPCON – Multi Access PDN Connectivity](/mobilnisite/slovnik/mapcon/)
- [IFOM – IP Flow Mobility](/mobilnisite/slovnik/ifom/)
- [PGW – PDN Gateway](/mobilnisite/slovnik/pgw/)

## Definující specifikace

- **TS 23.161** (Rel-19) — Network-based IP Flow Mobility (NBIFOM)
- **TS 23.861** (Rel-13) — Network-Based IP Flow Mobility (NBIFOM)
- **TS 24.161** (Rel-19) — Network-Based IP Flow Mobility (NBIFOM)
- **TS 24.302** (Rel-19) — Access to EPC via non-3GPP networks; Stage 3
- **TR 25.996** (Rel-19) — 3GPP-3GPP2 Spatial Channel Model Specification
- **TR 26.955** (Rel-19) — Video Codec Analysis for 5G Services
- **TS 29.826** (Rel-13) — P-CSCF Restoration Enhancements for WLAN
- **TS 36.840** (Rel-12) — LTE 450 MHz Band Technical Requirements for Brazil
- **TR 37.976** (Rel-19) — MIMO OTA Test Methodology Study
- **TR 37.977** (Rel-19) — MIMO OTA Test Methodology
- **TR 38.900** (Rel-15) — Channel Model Study for >6 GHz
- **TR 38.901** (Rel-19) — Channel Model for 0.5-100 GHz

---

📖 **Anglický originál a plná specifikace:** [SCM na 3GPP Explorer](https://3gpp-explorer.com/glossary/scm/)
