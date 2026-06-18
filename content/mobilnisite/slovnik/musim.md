---
slug: "musim"
url: "/mobilnisite/slovnik/musim/"
type: "slovnik"
title: "MUSIM – Multi-Universal Subscriber Identity Module"
date: 2025-01-01
abbr: "MUSIM"
fullName: "Multi-Universal Subscriber Identity Module"
category: "Services"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/musim/"
summary: "Služba umožňující jednomu zařízení podporovat více aktivních SIM profilů, což umožňuje současnou konektivitu a správu služeb napříč různými předplatnými nebo sítěmi. Je klíčová pro osobní i podnikové"
---

MUSIM je služba umožňující jednomu zařízení podporovat více aktivních SIM profilů pro současnou konektivitu a správu služeb napříč různými předplatnými nebo sítěmi.

## Popis

MUSIM (Multi-Universal Subscriber Identity Module) je služební funkce 3GPP, která umožňuje jednomu uživatelskému zařízení (UE) spravovat více aktivních profilů univerzálního modulu identity účastníka ([USIM](/mobilnisite/slovnik/usim/)) současně. Z architektonického hlediska zahrnuje vylepšení napříč UE, rádiovou přístupovou sítí (RAN) a jádrem sítě (CN) pro podporu nezávislého provozu a správy zdrojů pro každé předplatné. UE musí mít hardwarovou a softwarovou schopnost hostovat více USIM aplikací a udržovat samostatné protokolové zásobníky, včetně odlišných stavů řízení rádiových zdrojů ([RRC](/mobilnisite/slovnik/rrc/)) a kontextů nestupňové vrstvy přístupu ([NAS](/mobilnisite/slovnik/nas/)), pro každý aktivní profil. Síť, včetně gNB v 5G NR nebo [eNB](/mobilnisite/slovnik/enb/) v LTE, musí být schopna rozpoznat MUSIM kapacitu, aby mohla efektivně plánovat volání a spravovat stavy aktivity UE, protože zařízení může být dočasně nedostupné na jednom předplatném, zatímco aktivně komunikuje na druhém.

Z provozní perspektivy MUSIM umožňuje UE být současně registrováno v jedné nebo více veřejných pozemních mobilních sítích ([PLMN](/mobilnisite/slovnik/plmn/)) s využitím různých identit účastníka. Každý USIM profil má svou vlastní mezinárodní identitu mobilního účastníka ([IMSI](/mobilnisite/slovnik/imsi/)), bezpečnostní přihlašovací údaje a parametry předplatného. UE a síť koordinují prostřednictvím specifických procedur RRC a NAS, aby indikovaly MUSIM kapacitu a vyjednaly parametry, jako jsou cykly volání a konfigurace nespojitého příjmu ([DRX](/mobilnisite/slovnik/drx/)) přizpůsobené pro provoz s více [SIM](/mobilnisite/slovnik/sim/). Tato koordinace je zásadní pro prevenci narušení služeb, protože rádiový transceiver UE může typicky obsluhovat aktivní datovou relaci nebo hovor pouze pro jedno předplatné v daný čas, což vyžaduje mechanismy sdílení času nebo pozastavení.

Primární role MUSIM v síti je usnadnit pokročilé uživatelské služby bez nutnosti více fyzických zařízení. Ovlivňuje správu mobility, protože aktualizace polohy a správa oblastí sledování musí být zpracovány pro každé předplatné. Ovlivňuje také správu spojení, protože UE může potenciálně navazovat a udržovat více relací protokolové datové jednotky (PDU) nebo připojení k paketové datové síti (PDN) napříč svými profily. Pro jádro sítě je každé předplatné považováno za samostatného uživatele s vlastním ověřováním, správou relací a řízením politik, i když pocházejí ze stejného fyzického zařízení. Toto oddělení zajišťuje, že fakturace, zabezpečení a diferenciace služeb zůstávají neporušené pro každý profil, což činí MUSIM základním prvkem pro konvergované osobní a podnikové komunikační služby.

## K čemu slouží

MUSIM byl vytvořen, aby reagoval na rostoucí uživatelskou a tržní poptávku po tom, aby jedno mobilní zařízení bezproblémově podporovalo více aktivních síťových předplatných. Historicky zařízení s duální SIM často používala přístup 'Dual-SIM Dual-Standby' (DSDS), kde pouze jedna SIM mohla být aktivní v hovoru nebo datové relaci v daný čas, zatímco druhá byla nedostupná. Toto omezení bylo problematické pro uživatele, kteří potřebovali neustálou dostupnost na obou číslech, například pro oddělený osobní a pracovní život. Vývoj směrem k hardwaru 'Dual-SIM Dual-Active' (DSDA) přinesl nové výzvy pro efektivitu sítě a spotřebu energie UE, což si vyžádalo standardizovanou podporu sítě pro inteligentní správu konfliktů rádiových zdrojů a signalizační režie.

Technická motivace pro standardizaci MUSIM ve 3GPP Release 17 byla definovat jednotný rámec s podporou sítě, který jde nad rámec proprietárních implementací v koncových zařízeních. Předchozí nestandardizované implementace mohly vést k neefektivnímu chování sítě, jako jsou nadměrné pokusy o volání, když je UE zaneprázdněno na jiném předplatném, což plýtvalo rádiovými zdroji a životností baterie. Zavedením MUSIM umožňuje 3GPP UE explicitně informovat síť o své více-SIM kapacitě a vzorcích, což síti umožňuje optimalizovat strategie volání, procedury mobility a časovače uvolnění spojení. Tato spolupráce zlepšuje celkovou kapacitu systému, snižuje signalizační zahlcení a zlepšuje uživatelský zážitek poskytováním spolehlivější současné služby napříč předplatnými.

Dále MUSIM podporuje vznikající servisní paradigma, jako je síťové krájení (network slicing), kde různá předplatná mohou být asociována s různými síťovými řezy (např. jeden pro rozšířené mobilní širokopásmo a druhý pro vyhrazenou IoT službu). Také vyhovuje flexibilitě předplatného vyžadované pro IoT zařízení, která mohou potřebovat přepínat mezi profily operátorů z důvodu pokrytí nebo nákladů. Standardizací MUSIM poskytuje 3GPP budoucí základ pro zařízení, která musí zvládat více identit, ať už pro spotřebitelský komfort, správu podnikových zařízení nebo inovativní nasazení IoT, a zajišťuje interoperabilitu a efektivní provoz sítě napříč dodavateli a operátory.

## Klíčové vlastnosti

- Podpora více současně aktivních USIM aplikací v jednom UE
- Signalizace kapacity UE s podporou sítě pro optimalizovanou správu zdrojů
- Rozšířené procedury RRC a NAS pro zvládání stavů více předplatných
- Nezávislá správa mobility a spojení pro každý USIM profil
- Optimalizovaná koordinace volání a DRX pro zmírnění konfliktů mezi předplatnými
- Udržuje samostatné bezpečnostní kontexty a vynucování politik pro každé předplatné

## Související pojmy

- [USIM – Universal Subscriber Identity Module](/mobilnisite/slovnik/usim/)
- [RRC – Radio Resource Control](/mobilnisite/slovnik/rrc/)

## Definující specifikace

- **TR 22.834** (Rel-17) — Study on Support for Multi-USIM Devices
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification
- **TS 37.340** (Rel-19) — Multi-Connectivity Operation Overview
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TS 38.306** (Rel-19) — NR UE Radio Access Capability Parameters
- **TS 38.331** (Rel-19) — NR Radio Resource Control (RRC) Protocol Specification
- **TS 38.523** (Rel-19) — 5G NR UE Conformance Testing: Idle/Inactive

---

📖 **Anglický originál a plná specifikace:** [MUSIM na 3GPP Explorer](https://3gpp-explorer.com/glossary/musim/)
