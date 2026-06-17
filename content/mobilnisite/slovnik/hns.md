---
slug: "hns"
url: "/mobilnisite/slovnik/hns/"
type: "slovnik"
title: "HNS – Home Node B Subsystem"
date: 2025-01-01
abbr: "HNS"
fullName: "Home Node B Subsystem"
category: "Radio Access Network"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/hns/"
summary: "Home Node B Subsystem (HNS) je kompletní architektonický rámec pro 3G femtobuňky, který zahrnuje Home Node B (HNB), HNB Gateway (HNB-GW) a Security Gateway (SeGW). Poskytuje zabezpečené, škálovatelné"
---

HNS je kompletní 3G femtobuňkový rámec zahrnující Home Node B, HNB Gateway a Security Gateway pro zajištění zabezpečeného, spravovaného pokrytí malými buňkami integrovaného s jádrem sítě UMTS.

## Popis

Home Node B Subsystem (HNS) je standardizovaná architektura 3GPP zavedená pro podporu rozsáhlého nasazení femtobuněk, známých jako Home Node B ([HNB](/mobilnisite/slovnik/hnb/)). Jedná se o podsystém UTRAN (UMTS Terrestrial Radio Access Network). Primárním účelem HNS je prezentovat standardní rozhraní Iu (Iu-cs a Iu-ps) směrem k jádru sítě ([MSC](/mobilnisite/slovnik/msc/) a SGSN), díky čemuž agregace potenciálně milionů HNB vypadá jako jediný, tradiční Radio Network Controller (RNC). Tato abstrakce umožňuje stávajícím prvkům jádra sítě fungovat bez úprav a zacházet s provozem z femtobuněk stejně jako s provozem z makrobuněk.

Architektura HNS se skládá ze tří klíčových logických uzlů. Home Node B (HNB) je femtobuňkový přístupový bod nasazený v prostorách zákazníka. Obsahuje funkce Node B (fyzická vrstva, [MAC](/mobilnisite/slovnik/mac/) atd.) a podmnožinu funkcí RNC pro řízení rádiových zdrojů připojených UE. HNB se připojuje k síti operátora přes širokopásmovou IP páteřní síť (např. [DSL](/mobilnisite/slovnik/dsl/), kabel). Security Gateway (SeGW) je prvním kontaktním bodem v síti operátora; navazuje vzájemně autentizované [IPsec](/mobilnisite/slovnik/ipsec/) tunely s HNB a zabezpečuje veškerý následný provoz. HNB Gateway ([HNB-GW](/mobilnisite/slovnik/hnb-gw/)) je centrální uzel pro agregaci a řízení. Ukončuje zabezpečené tunely od více HNB (přes rozhraní Iuh), provádí autentizaci a registraci HNB pomocí protokolu [HNBAP](/mobilnisite/slovnik/hnbap/), agreguje provoz v uživatelské rovině a prezentuje standardizované rozhraní Iu směrem k jádru sítě.

Princip fungování: Když je HNB zapnuta, objeví SeGW a naváže zabezpečený IPsec tunel. Prostřednictvím tohoto tunelu iniciuje procedury HNBAP s HNB-GW, aby se zaregistrovala, a poskytne svou identitu a polohu. HNB-GW autentizuje HNB vůči jádru sítě a [HSS](/mobilnisite/slovnik/hss/). Po registraci může HNB obsluhovat UE. Když se UE připojí, signalizační a uživatelský provoz z UE prochází zabezpečeným tunelem k HNB-GW. HNB-GW přeposílá signalizaci Iu k MSC/SGSN a přepíná data uživatelské roviny k příslušné bráně jádra sítě (MGW/GGSN). HNB-GW také zajišťuje kritické funkce, jako je paging, koordinaci předávání hovorů mezi HNB a makro sítí a řízení přístupu pro Closed Subscriber Group (CSG).

## K čemu slouží

HNS byla vytvořena za účelem ekonomického a škálovatelného řešení naléhavého problému špatného vnitřního pokrytí a kapacity mobilní sítě. Tradiční sítě makrobuněk mají potíže s pronikáním do budov, což vede k přerušeným hovorům a nízkým datovým rychlostem uvnitř. Výstavba dalších makrobuněk je drahá a pro hluboké vnitřní pokrytí neefektivní. Koncept HNS využil rozšíření domácího širokopásmového připojení k nasazení nízkopříkonových přístupových bodů (femtobuněk) v prostorech zákazníka.

Předchozí přístupy, jako jsou pikobuňky nebo systémy s distribuovanými anténami, vyžadovaly drahou infrastrukturu spravovanou operátorem a získávání lokalit. Architektura HNS tento problém vyřešila definicí zabezpečeného, samoinstalačního modelu nasazovaného zákazníkem. Mezi klíčové problémy, které řešila, patřily: Zabezpečení – zajištění, že nedůvěryhodné zařízení na veřejném internetu nemůže ohrozit jádro sítě operátora (řešeno pomocí SeGW a IPsec). Škálovatelnost – správa milionů uzlů vyžadovala agregační architekturu založenou na bráně (HNB-GW), aby nedocházelo k přetížení prvků jádra sítě. Rušení – HNB-GW poskytuje centralizované řízení pro konfiguraci rádiových parametrů HNB, čímž minimalizuje rušení s makrovrstvou. Motivace byla komerční: zlepšit spokojenost zákazníků, snížit odchod zákazníků, odlehčit provoz z makro sítě a vytvořit nové služby pro domácnosti a malé firmy, a to vše pomocí standardizované architektury umožňující interoperabilitu mezi více dodavateli.

## Klíčové vlastnosti

- Poskytuje standardizované rozhraní Iu ke stávajícímu jádru sítě UMTS (MSC, SGSN)
- Centralizuje řízení a agregaci milionů HNB prostřednictvím HNB Gateway (HNB-GW)
- Zajišťuje zabezpečení end-to-end pomocí IPsec tunelů ukončených na Security Gateway (SeGW)
- Podporuje Closed Subscriber Group (CSG) pro řízení přístupu s omezením
- Umožňuje konfiguraci a řízení rádiových zdrojů HNB pod kontrolou sítě
- Umožňuje mobilitu (předávání hovorů) mezi HNB a makro sítí UTRAN

## Související pojmy

- [HNB – Home Node B](/mobilnisite/slovnik/hnb/)
- [HNB-GW – Home Node B Gateway](/mobilnisite/slovnik/hnb-gw/)
- [CSG – Closed Subscriber Group](/mobilnisite/slovnik/csg/)

## Definující specifikace

- **TS 28.671** (Rel-19) — HNS Network Resource Model Requirements
- **TS 28.672** (Rel-19) — HNS NRM IRP Information Service
- **TS 28.673** (Rel-19) — HNS NRM IRP Solution Set Definitions
- **TS 32.572** (Rel-19) — HNB/HeNB Type 2 Interface Concepts & Requirements
- **TS 32.771** (Rel-11) — HNS Network Resource Model IRP Requirements
- **TS 32.772** (Rel-11) — HNS Network Resource Model (NRM) IRP
- **TS 32.773** (Rel-9) — HNS NRM IRP CORBA Solution Set

---

📖 **Anglický originál a plná specifikace:** [HNS na 3GPP Explorer](https://3gpp-explorer.com/glossary/hns/)
