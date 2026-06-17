---
slug: "ine"
url: "/mobilnisite/slovnik/ine/"
type: "slovnik"
title: "INE – Interrogating Network Entity"
date: 2025-01-01
abbr: "INE"
fullName: "Interrogating Network Entity"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/ine/"
summary: "INE je funkční entita v CAMEL (Customised Applications for Mobile network Enhanced Logic), která se nachází ve navštívené síti. Dotazuje se domácí sítě účastníka, aby získala informace o CAMEL službác"
---

INE (Interrogating Network Entity) je dotazovací síťová entita v CAMEL, která dotazuje domácí síť roamujícího účastníka, aby získala informace o službách, což umožňuje operátorské specifické služby, jako je předplacené účtování.

## Popis

Interrogating Network Entity (INE) je klíčová funkční komponenta v architektuře 3GPP [CAMEL](/mobilnisite/slovnik/camel/) (Customised Applications for Mobile network Enhanced Logic), specifikovaná v TS 23.066. Funguje jako brána nebo dotazovací bod, který je typicky umístěn ve Visited Public Land Mobile Network (VPLMN). Jejím hlavním úkolem je komunikovat s Home Public Land Mobile Network ([HPLMN](/mobilnisite/slovnik/hplmn/)) účastníka, aby při roamingu získala potřebné CAMEL Subscription Information ([CSI](/mobilnisite/slovnik/csi/)). INE není nutně samostatný fyzický uzel; její funkčnost je často integrována do prvků jádra sítě, jako je Visited Mobile Switching Center (VMSC) nebo Visited Gateway [MSC](/mobilnisite/slovnik/msc/) (VGMSC) pro okruhově přepínané služby a Visited Serving [GPRS](/mobilnisite/slovnik/gprs/) Support Node (VSGSN) pro paketově přepínané služby.

Operačně INE funguje tak, že zahájí dialog s Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)) nebo Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) v domácí síti. Když roamující účastník zahájí nebo přijme hovor, nebo aktivuje paketovou datovou relaci, obslužný uzel navštívené sítě (např. VMSC) spustí funkci INE. INE odešle standardizovanou [MAP](/mobilnisite/slovnik/map/) (Mobile Application Part) zprávu, jako je SendRoutingInfoForSM nebo ProvideSubscriberInfo, do HLR. HLR odpoví s účastníkovým CSI, které obsahuje adresu CAMEL Service Environment (CSE) domácí sítě – gsmSCF (GSM Service Control Function). Toto CSI je pak předáno gsmSSF (GSM Service Switching Function) navštívené sítě, která naváže přímý CAP (CAMEL Application Part) dialog s gsmSCF.

Tato architektura umožňuje gsmSCF v domácí síti v reálném čase řídit zpracování hovoru nebo relace v navštívené síti. Například pro předplaceného roamujícího účastníka může domácí gsmSCF instruovat navštívený gsmSSF/INE, aby uplatnil limity délky hovoru nebo odečetl kredit. INE tak umožňuje navštívené síti „vědět“ o vlastních službách domácího operátora a provádět je, aniž by musela hostovat jejich servisní logiku sama. Je to základní kámen pro zajištění bezproblémových služeb inteligentní sítě přes mezinárodní hranice, což zajišťuje konzistentní uživatelský zážitek ze služeb bez ohledu na to, zda je účastník v domácí síti nebo roamuje.

## K čemu slouží

INE byla vytvořena, aby vyřešila zásadní výzvu v globálním mobilním roamingu: jak umožnit operátorovi domácí sítě nabízet své přidané, operátorsky specifické služby inteligentní sítě (jako předplacené účtování, virtuální privátní sítě nebo služby založené na poloze) svým účastníkům, když jsou mimo pokrytí domácí sítě. Před CAMEL a konceptem INE měl roamující účastník typicky přístup pouze k základním telefonním službám navštívené sítě a přicházel o všechna přizpůsobení domácí sítě. To bylo významné komerční a technické omezení, zejména pro předplacené služby, které byly hlavním hybatelem rozšíření mobilní komunikace.

Vývoj INE, počínaje Release 4, byl součástí širšího rozšíření CAMEL fáze 3 a 4. Řešil omezení dřívějších fází CAMEL, které měly více omezené roamingové schopnosti. INE formalizovala roli navštívené sítě jako dotazovatele a vykonavatele. Vyřešila problém definováním jasného, standardizovaného rozhraní (MAP) mezi navštívenou a domácí sítí za účelem získání instrukcí servisní logiky. To umožnilo, aby kontrola služby zůstala v domácí síti (u operátorova gsmSCF), což zachovává bezpečnost a kontrolu nad obchodní logikou, zatímco přepínání a spouštění služeb je delegováno na infrastrukturu navštívené sítě.

Tato architektura motivovala vytvoření skutečně globální platformy inteligentní sítě pro GSM a jeho následovníky. Umožnila prudký rozvoj trhu s předplaceným roamingem, dala operátorům konkurenční výhodu prostřednictvím konzistentní nabídky služeb a poskytla model pro distribuci síťových funkcí přes administrativní domény – koncept, který později ovlivnil návrh IP Multimedia Subsystem (IMS) a servisně orientovaných architektur v 5G.

## Klíčové vlastnosti

- Nachází se v navštívené síti (VPLMN) a funguje jako dotazovatel směrem k HPLMN
- Používá MAP protokoly k dotazování HLR/HSS na CAMEL Subscription Information (CSI)
- Umožňuje získání adresy domácího gsmSCF pro navázání CAP spojení
- Funkčně integrována do navštívených jádrových uzlů, jako jsou VMSC, VGMSC nebo VSGSN
- Nezbytná pro spouštění domácí sítí řízených služeb IN, jako je předplacené účtování v reálném čase během roamingu
- Poskytuje standardizovaný mechanismus pro interakci služeb mezi administrativně oddělenými sítěmi

## Související pojmy

- [CAMEL – Customised Applications for Mobile network Enhanced Logic](/mobilnisite/slovnik/camel/)
- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)

## Definující specifikace

- **TS 23.066** (Rel-19) — Mobile Number Portability Technical Realization

---

📖 **Anglický originál a plná specifikace:** [INE na 3GPP Explorer](https://3gpp-explorer.com/glossary/ine/)
