---
slug: "lsa"
url: "/mobilnisite/slovnik/lsa/"
type: "slovnik"
title: "LSA – Localised Service Area Identity"
date: 2025-01-01
abbr: "LSA"
fullName: "Localised Service Area Identity"
category: "Identifier"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/lsa/"
summary: "Jedinečný identifikátor pro lokalizovanou oblast služeb (LSA), což je definovaná geografická zóna v rámci PLMN, kde jsou uplatňovány specifické služby nebo politiky. Umožňuje síťovým operátorům nabíze"
---

LSA je jedinečný identifikátor pro definovanou geografickou zónu v rámci PLMN, kde jsou na základě polohy uživatele uplatňovány specifické služby nebo politiky, jako jsou speciální tarify nebo přístupová omezení.

## Popis

Identita lokalizované oblasti služeb (LSA) je základním identifikátorem v rámci specifikací 3GPP, který definuje konkrétní geografickou oblast ve veřejné pozemní mobilní síti ([PLMN](/mobilnisite/slovnik/plmn/)). LSA není pouze buňka nebo skupina buněk; jedná se o logickou konstrukci, která může zahrnovat jednu či více buněk, sektorů nebo dokonce uživatelem definovaný polygon, což umožňuje detailní diferenciaci služeb. Identita LSA je uložena v databázích účastníků sítě a je spojena se specifickými profily služeb a politikami. Když uživatelské zařízení (UE) vstoupí nebo se nachází v rámci LSA, může síť na základě LSA-ID spustit specifické akce, jako je povolení přístupu k uzavřené skupině účastníků, aplikace lokalizovaného tarifu nebo omezení určitých služeb.

Fungování LSA závisí na schopnosti sítě přesně určit polohu UE a tuto polohu namapovat na předdefinovanou LSA. To vyžaduje koordinaci mezi rádiovou přístupovou sítí (RAN), která poskytuje informace o poloze na úrovni buňky nebo přesnější, a jádrem sítě (CN), které uchovává data o předplatném LSA a servisní politiky účastníka. Serving [GPRS](/mobilnisite/slovnik/gprs/) Support Node ([SGSN](/mobilnisite/slovnik/sgsn/)) nebo Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)) hraje klíčovou roli při vyhodnocování polohy UE vůči jeho předplaceným LSA. Koncept LSA je nedílnou součástí funkcí, jako je přístup pouze v LSA (LSA-only access), kde je UE povoleno kempovat a přijímat služby pouze ve své určené LSA, a preferovaný přístup k LSA (LSA-preferred access), kde síť upřednostňuje buňky LSA, ale umožňuje přechod na širší PLMN.

Z architektonického pohledu je LSA-ID odkazováno v mnoha síťových prvcích a rozhraních. Je součástí profilu účastníka v Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) nebo Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)). Je signalizací komunikováno k RAN, aby pomohlo při rozhodování o výběru/převýběru buňky a předání. Identita je také používána v účtovacích systémech pro aplikaci tarifů závislých na poloze. Definice a správa LSA jsou typicky řešeny Operations Support System ([OSS](/mobilnisite/slovnik/oss/)) operátora sítě, který konfiguruje geografické hranice a přidruženou servisní logiku. To činí z LSA mocný nástroj pro vytváření virtuálních síťových oddílů a implementaci sofistikovaných služeb bez nutnosti fyzických síťových překryvů.

## K čemu slouží

Identita lokalizované oblasti služeb byla zavedena, aby řešila rostoucí potřebu síťových operátorů nabízet diferencované a lokalizačně založené služby nad rámec jednoduchých celostátních nebo regionálních tarifů. Před její standardizací měli operátoři omezené mechanismy pro aplikaci služeb nebo politik na velmi specifické oblasti, jako je univerzitní kampus, firemní park nebo nákupní centrum. Primární motivací bylo umožnit nové obchodní modely, včetně lokalizovaných servisních balíčků, uzavřených uživatelských skupin pro podniky a optimalizované využití síťových zdrojů v zónách s vysokou poptávkou.

Historicky bylo diferenciace služeb často dosahováno prostřednictvím oddělené síťové infrastruktury nebo složitých řešení, která byla nákladná a neefektivní. Koncept LSA poskytl standardizovanou, softwarově definovanou metodu pro vytváření logických servisních zón v rámci jedné [PLMN](/mobilnisite/slovnik/plmn/). Tím vyřešil problém rigidních servisních hranic a umožnil vytváření 'virtuálních' privátních sítí nebo specializovaných servisních oblastí. Také usnadnil regulatorní soulad pro služby specifické podle polohy a umožnil operátorům konkurovat lokalizovaným bezdrátovým nabídkám, jako jsou Wi-Fi hotspoty, tím, že poskytli bezproblémové, operátorem spravované alternativy s integrovanou mobilitou a účtováním.

## Klíčové vlastnosti

- Jedinečný identifikátor pro definovanou geografickou servisní zónu v rámci PLMN
- Umožňuje aktivaci služeb a vynucování politik na základě polohy
- Podporuje jak režim přístupu pouze v LSA (LSA-only), tak preferovaný přístup k LSA (LSA-preferred) pro UE
- Integruje se s profily účastníků v HSS/HLR pro správu předplatného
- Používá se RAN pro řízení výběru, převýběru buňky a předání
- Usnadňuje účtování a fakturaci závislé na poloze v síti

## Související pojmy

- [PLMN – Public Land Mobile Network](/mobilnisite/slovnik/plmn/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.043** (Rel-4) — Localised Service Area Support
- **TS 22.830** (Rel-16) — Business Role Models for Network Slicing
- **TS 23.073** (Rel-5) — Localised Service Area (SoLSA) Stage 2 Description
- **TS 23.078** (Rel-19) — CAMEL Phase 4 Stage 2 Specification
- **TS 25.304** (Rel-19) — UTRA Idle Mode Procedures Specification
- **TS 28.301** (Rel-19) — LSA Controller IRP Requirements
- **TS 31.102** (Rel-19) — USIM Application Specification
- **TS 32.101** (Rel-19) — Management principles and high-level requirements
- **TS 32.808** (Rel-8) — Common User Profile Storage Framework
- **TS 32.855** (Rel-14) — Study on OAM Support for Licensed Shared Access
- **TS 42.043** (Rel-19) — Support of Localised Service Area (SoLSA)
- **TS 43.073** (Rel-19) — SoLSA (Support of Localised Service Area) - Stage 2

---

📖 **Anglický originál a plná specifikace:** [LSA na 3GPP Explorer](https://3gpp-explorer.com/glossary/lsa/)
