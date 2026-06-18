---
slug: "vcf"
url: "/mobilnisite/slovnik/vcf/"
type: "slovnik"
title: "VCF – V2X Control Function"
date: 2025-01-01
abbr: "VCF"
fullName: "V2X Control Function"
category: "Services"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/vcf/"
summary: "V2X Control Function je základní síťová entita specifikovaná pro služby Cellular Vehicle-to-Everything (C-V2X). Spravuje autorizaci komunikace V2X, řízení politik a poskytování služeb pro připojená vo"
---

VCF je základní síťová entita, která spravuje autorizaci, řízení politik a poskytování služeb pro zabezpečenou a spolehlivou komunikaci Cellular Vehicle-to-Everything (C-V2X).

## Popis

[V2X](/mobilnisite/slovnik/v2x/) Control Function (VCF) je logická funkce definovaná v architektuře 3GPP pro podporu autorizace a řízení politik pro komunikaci V2X přes síť 3GPP. Funguje jako součást servisní vrstvy pro V2X a komunikuje s dalšími funkcemi základní sítě, jako je Policy Control Function ([PCF](/mobilnisite/slovnik/pcf/)) a Unified Data Management ([UDM](/mobilnisite/slovnik/udm/)). VCF je zodpovědná za určení, zda je uživatelské zařízení (UE), například palubní jednotka ve vozidle, oprávněno používat služby V2X. Ověřuje předplatné UE a požadované specifické parametry služby V2X, jako je typ komunikace V2X (např. Vehicle-to-Vehicle, Vehicle-to-Infrastructure) a přidružené geografické oblasti, kde je komunikace povolena.

Architektonicky je VCF specifikována pro podporu V2X založeného na LTE (zavedeno ve vydání 14) i V2X založeného na 5G NR (vylepšeno v následujících vydáních). Rozhraní s PCF slouží k získání rozhodnutí o politikách specifických pro V2X, která mohou zahrnovat parametry kvality služby (QoS), směrování dat a výběr síťového řezu pro provoz V2X. VCF také komunikuje s UDM za účelem získání dat předplatného souvisejících se službami V2X. Ve scénářích zahrnujících roaming může VCF ve navštívené veřejné pozemní mobilní síti ([VPLMN](/mobilnisite/slovnik/vplmn/)) komunikovat s VCF v domovské [PLMN](/mobilnisite/slovnik/plmn/) ([HPLMN](/mobilnisite/slovnik/hplmn/)) za účelem ověření autorizace, což zajišťuje konzistentní poskytování služeb přes hranice sítí.

Role VCF je klíčová pro zabezpečení a správu ekosystémů V2X. Zabrání neautorizovaným vozidlům účastnit se komunikací kritických z hlediska bezpečnosti, což by mohlo vést k nebezpečným situacím nebo zahlcení sítě. Centralizací autorizační logiky umožňuje VCF síťovým operátorům vynucovat politiky, spravovat zdroje a podporovat pokročilé aplikace V2X, jako je kooperativní povědomí, dynamické aktualizace map a jízda v koloně. Její specifikace v 3GPP TS 33.185 a TS 33.885 se zaměřují na bezpečnostní aspekty a podrobně popisují postupy pro správu přihlašovacích údajů, autorizaci a ochranu signalizačních zpráv V2X.

## K čemu slouží

[V2X](/mobilnisite/slovnik/v2x/) Control Function byla vytvořena, aby řešila specifické požadavky na zabezpečení a správu politik pro komunikaci Vehicle-to-Everything založenou na buněčných sítích. Tradiční mechanismy autorizace v buněčných sítích byly navrženy pro služby zaměřené na člověka, jako je hlas a prohlížení internetu, a postrádaly podrobnost a požadavky na nízkou latenci potřebné pro komunikaci V2X typu stroj-stroj, která je kritická z hlediska bezpečnosti. VCF poskytuje specializovanou funkci pro autorizaci komunikace V2X, která zajišťuje, že pouze legitimní a řádně vybavená vozidla mohou odesílat a přijímat bezpečnostní zprávy, což je prvořadé pro bezpečnost silničního provozu a prevenci škodlivých útoků na systém V2X.

Její vývoj byl motivován snahou automobilového průmyslu směrem k připojeným a autonomním vozidlům, která jsou závislá na spolehlivé, bezpečné a okamžité výměně dat. Bez standardizované řídicí funkce, jako je VCF, by mohl každý operátor nebo výrobce automobilů implementovat proprietární autorizační systémy, což by vedlo k fragmentaci a problémům s interoperabilitou, zejména pro vozidla roamující v různých zemích a mezi různými síťovými operátory. VCF, standardizovaná organizací 3GPP, poskytuje jednotný rámec, který umožňuje škálovatelné, bezpečné a interoperabilní služby V2X v globálním měřítku, a usnadňuje tak nasazení pokročilých systémů asistovaného řízení a funkcí autonomní jízdy.

## Klíčové vlastnosti

- Autorizuje UE pro komunikaci V2X na základě předplatného a parametrů služby
- Poskytuje řízení politik specifických pro V2X ve spolupráci s PCF
- Podporuje autorizaci pro režimy komunikace LTE-V2X i NR-V2X
- Umožňuje roamingové scénáře prostřednictvím interakce s instancemi VCF v HPLMN a VPLMN
- Spravuje bezpečnostní přihlašovací údaje a parametry pro ochranu zpráv V2X
- Usnadňuje poskytování služeb pro různé typy aplikací V2X (např. bezpečnost, efektivita provozu)

## Související pojmy

- [V2X – Vehicle-to-Everything Application Server](/mobilnisite/slovnik/v2x/)
- [PCF – Positioning Calculation Function](/mobilnisite/slovnik/pcf/)
- [UDM – Unified Data Management](/mobilnisite/slovnik/udm/)

## Definující specifikace

- **TS 33.185** (Rel-19) — V2X Security in LTE
- **TS 33.885** (Rel-14) — Security Study for V2X Services

---

📖 **Anglický originál a plná specifikace:** [VCF na 3GPP Explorer](https://3gpp-explorer.com/glossary/vcf/)
