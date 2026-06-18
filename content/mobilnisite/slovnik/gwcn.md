---
slug: "gwcn"
url: "/mobilnisite/slovnik/gwcn/"
type: "slovnik"
title: "GWCN – GateWay Core Network"
date: 2025-01-01
abbr: "GWCN"
fullName: "GateWay Core Network"
category: "Core Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/gwcn/"
summary: "Architektura sdílení sítě, kde více veřejných pozemních mobilních sítí (PLMN) sdílí společnou core síť, včetně klíčových uzlů, jako jsou MSC a SGSN. Umožňuje operátorům snížit náklady na nasazení a pr"
---

GWCN je architektura sdílení sítě, kde více PLMN sdílí společnou core síť za účelem snížení nákladů, přičemž si zachovávají samostatné rádiové přístupové sítě a identity účastníků.

## Popis

GWCN (GateWay Core Network) je specifický model sdílení sítě definovaný v 3GPP a podrobně popsaný v TS 23.251. V této architektuře dva nebo více spolupracujících operátorů (každý se svým vlastním [PLMN](/mobilnisite/slovnik/plmn/) ID) sdílí společnou sadu uzlů core sítě, které slouží jako brána pro všechny jejich příslušné rádiové přístupové sítě (RAN). Sdílená core síť typicky zahrnuje kritické uzly jako Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)), Serving [GPRS](/mobilnisite/slovnik/gprs/) Support Node ([SGSN](/mobilnisite/slovnik/sgsn/)) a případně Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)) nebo Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)). Každý operátor si zachovává vlastní nezávislou RAN, vysílající pod jeho jedinečnou PLMN identitou, ale veškerý provoz účastníků je směrován a zpracováván sdílenou infrastrukturou core sítě.

Operačně platí, že když se uživatel připojí k buňce vysílající PLMN Operátora A, spojení je navázáno prostřednictvím sdílené RAN a poté předáno společným uzlům GWCN. GWCN identifikuje domovského operátora uživatele na základě International Mobile Subscriber Identity ([IMSI](/mobilnisite/slovnik/imsi/)) a aplikuje příslušné politiky, služby a pravidla účtování pro daného operátora. MSC a SGSN v GWCN jsou nakonfigurovány tak, aby obsluhovaly účastníky všech partnerských sítí, což vyžaduje robustní správu dat účastníků a mechanismy oddělení politik. Klíčová rozhraní, jako je rozhraní Iu mezi [RNC](/mobilnisite/slovnik/rnc/) a core sítí, se připojují ke sdíleným uzlům.

Tato architektura je závislá na pečlivé konfiguraci, která zajišťuje logické oddělení provozu, účtování a provozních podpůrných systémů (OSS). Sdílené core uzly musí podporovat více PLMN kontextů a směrovat signalizaci a uživatelská data ke správným backendovým systémům specifickým pro daného operátora (jako jsou účtovací brány). Model GWCN je integrovanější než jiné modely sdílení, jako je Multi-Operator Core Network (MOCN), protože zahrnuje sdílení samotných bránových uzlů core sítě, což vede k vyšším úsporám nákladů, ale také k větší integrační složitosti a vzájemné závislosti mezi operátory.

## K čemu slouží

GWCN byl vyvinut primárně k řešení vysokých kapitálových výdajů (CAPEX) a provozních výdajů (OPEX) spojených s nasazením a údržbou nezávislých core sítí, zejména pro nové hráče na trhu nebo operátory ve venkovských oblastech. Před standardy pro sdílení sítě potřeboval každý operátor kompletní, duplicitní sadu síťové infrastruktury, což bylo ekonomicky neefektivní a zpomalovalo rozvoj sítě. Model GWCN poskytl standardizovaný způsob, jak mohou operátor spolupracovat a sdílet nejdražší části sítě – ústřední komutace a uzly pro směrování paketů – a přitom stále konkurovat v oblasti služeb a zachovat si svoji značku prostřednictvím vlastního rádiového spektra a PLMN.

Řešil problém nadbytečné infrastruktury a jejího nedostatečného využití. Sdílením MSC a SGSN mohli operátoři dosáhnout významných úspor nákladů na pronájem místa, hardware, energii a údržbu. To bylo zvláště motivující v období nasazování 3G/UMTS, kdy byly náklady vysoké. Model také usnadňoval rychlejší rozšíření pokrytí, protože operátoři mohli využít sdílenou core síť k obsluze oblastí, kde výstavba nezávislé core sítě nebyla životaschopná. Představoval strategický posun od čistě konkurenční infrastruktury ke spolupráci v oblasti infrastruktury v určitých geografických nebo ekonomických kontextech, formalizovaný standardy 3GPP za účelem zajištění interoperability a jasných provozních hranic.

## Klíčové vlastnosti

- Sdílené uzly core sítě (MSC, SGSN) mezi více operátory
- Nezávislá RAN a PLMN identita pro každého operátora
- Identifikace účastníka a oddělení politik založené na IMSI
- Snížení nákladů na nasazení a provoz core sítě
- Podpora jak okruhově, tak paketově orientovaných domén
- Standardizovaná architektura a rozhraní definovaná v 3GPP TS 23.251

## Související pojmy

- [MOCN – Multiple Operator Core Network](/mobilnisite/slovnik/mocn/)
- [PLMN – Public Land Mobile Network](/mobilnisite/slovnik/plmn/)
- [MSC – Mobile Services Switching Centre](/mobilnisite/slovnik/msc/)
- [SGSN – Serving GPRS Support Node](/mobilnisite/slovnik/sgsn/)

## Definující specifikace

- **TS 22.278** (Rel-19) — Evolved Packet System Service Requirements
- **TS 22.803** (Rel-12) — Proximity Services (ProSe) Study
- **TS 23.251** (Rel-19) — Network Sharing Stage 2 Specification
- **TS 23.851** (Rel-6) — Network Sharing Architecture for 3G Systems
- **TS 25.401** (Rel-19) — UTRAN Overall Architecture
- **TS 25.410** (Rel-19) — Iu Interface Introduction for UTRAN
- **TS 25.413** (Rel-19) — Radio Access Network Application Part (RANAP)
- **TS 25.423** (Rel-19) — UTRAN RNSAP Specification
- **TS 28.878** (Rel-19) — Study on Management of Network Sharing Phase3
- **TS 29.280** (Rel-19) — Sv Interface Specification for SRVCC
- **TS 32.130** (Rel-19) — Network Sharing OAM&P Requirements
- **TS 32.851** (Rel-12) — Network Sharing OAM Requirements
- **TR 33.969** (Rel-19) — Security for Public Warning System (PWS)
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.856** (Rel-12) — RAN Sharing Enhancements for LTE Study
- … a dalších 3 specifikací

---

📖 **Anglický originál a plná specifikace:** [GWCN na 3GPP Explorer](https://3gpp-explorer.com/glossary/gwcn/)
