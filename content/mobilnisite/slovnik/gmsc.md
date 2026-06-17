---
slug: "gmsc"
url: "/mobilnisite/slovnik/gmsc/"
type: "slovnik"
title: "GMSC – Gateway Mobile Services Switching Centre"
date: 2025-01-01
abbr: "GMSC"
fullName: "Gateway Mobile Services Switching Centre"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/gmsc/"
summary: "Ústředna v jádru sítě v okruhově přepínaných (CS) mobilních sítích, která slouží jako brána mezi mobilní sítí a externími pevnými nebo mobilními sítěmi (jako PSTN). Směruje příchozí hovory na správnou"
---

GMSC je ústředna v jádru sítě v okruhově přepínaných mobilních sítích, která slouží jako brána k externím sítím a směruje příchozí hovory dotazem na HLR pro zjištění polohy účastníka.

## Popis

Gateway Mobile Services Switching Centre (GMSC) je klíčový funkční uzel v okruhově přepínané ([CS](/mobilnisite/slovnik/cs/)) doméně sítí 2G (GSM) a 3G (UMTS). V podstatě se jedná o Mobile Switching Centre ([MSC](/mobilnisite/slovnik/msc/)) se specifickou dodatečnou rolí rozhraní mezi veřejnou pozemní mobilní sítí (PLMN) a externími sítěmi. Tyto externí sítě zahrnují jiné PLMN, veřejnou komutovanou telefonní síť (PSTN) a síť [ISDN](/mobilnisite/slovnik/isdn/). Primární technickou funkcí GMSC je určit aktuálně obsluhující MSC (navštívenou MSC nebo VMSC) volaného mobilního účastníka, pokud hovor pochází z mimo domovské sítě účastníka.

Z architektonického hlediska obsahuje GMSC plné schopnosti přepojování hovorů a signalizace standardní MSC. Jejím klíčovým rozlišovacím znakem je interakce s Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)). Když je hovor směrován na GMSC (typicky proto, že volané číslo je [MSISDN](/mobilnisite/slovnik/msisdn/)), GMSC zpočátku neví, které MSC aktuálně obsluhuje cílového účastníka. Proto odešle signalizační zprávu, konkrétně požadavek Send Routing Information (SRI) přes protokol Mobile Application Part ([MAP](/mobilnisite/slovnik/map/)), do HLR účastníka. HLR, které spravuje profil účastníka a aktuální oblast polohy, dotazuje příslušný Visitor Location Register (VLR), aby získalo dočasné směrovací číslo nazývané Mobile Station Roaming Number ([MSRN](/mobilnisite/slovnik/msrn/)).

HLR toto MSRN vrátí GMSC. MSRN je dočasné, síťově interní číslo, které odkazuje na aktuální VMSC. Vyzbrojeno MSRN může GMSC následně směrovat příchozí hovor přes CS jádro sítě na správnou VMSC. VMSC po přijetí žádosti o sestavení hovoru s MSRN ji přiřadí ke skutečné [IMSI](/mobilnisite/slovnik/imsi/) volané strany a dokončí sestavení hovoru k mobilní stanici. Tento proces, známý jako směrování a dotazování hovorů, je volající straně transparentní a umožňuje plynulou mobilitu. V mnoha síťových implementacích mohou mít všechny MSC funkci GMSC, nebo mohou být nasazeny vyhrazené uzly jako brány.

## K čemu slouží

GMSC bylo vytvořeno, aby vyřešilo základní problém směrování hovorů k mobilnímu účastníkovi, jehož poloha není pevná a je neznámá externí, pevné telefonní síti. V předcelulární éře telefonní ústředny směrovaly hovory na základě pevné geografické asociace telefonního čísla. Tento model se u mobilních uživatelů zcela rozpadá. GMSC ve spojení se systémem databází HLR/VLR zavedlo inteligenci potřebnou k oddělení identity účastníka (MSISDN) od jeho fyzického síťového připojovacího bodu.

Jeho vývoj byl základním kamenem architektury GSM, která umožnila skutečnou mobilitu terminálu napříč širokými geografickými oblastmi. Před touto architekturou byly mobilní systémy často omezeny na místní nebo regionální provoz bez efektivního volání mezi sítěmi. Model GMSC poskytl škálovatelnou, standardizovanou metodu, aby jakákoli externí ústředna (v PSTN nebo mobilní síti jiné země) mohla směrovat hovor na jedinou, známou bránu (GMSC) domovské sítě účastníka. GMSC domovské sítě pak přebírá odpovědnost za nalezení účastníka kdekoli se nachází, pomocí svých interních databází polohy. Toto oddělení externího směrování (do domovské sítě) a interního, dynamického směrování (na navštívenou lokalitu) je tím, co učinilo globální mobilní roaming komerčně a technicky proveditelným.

## Klíčové vlastnosti

- Funkce brány mezi mobilní PLMN a externími okruhově přepínanými sítěmi (PSTN, ISDN, jiné PLMN)
- Provádí proceduru dotazování HLR přes MAP signalizaci za účelem získání směrovacích informací (MSRN)
- Směruje příchozí hovory na aktuální navštívenou MSC (VMSC) volaného účastníka
- Zahrnuje plné schopnosti MSC pro přepojování hovorů a signalizaci
- Zpracovává sestavování a ukončování hovorů a základní doplňkové služby pro bránové hovory
- Klíčový uzel pro implementaci směrování hovorů a roamingu založeného na mobilitě

## Související pojmy

- [MSC – Mobile Services Switching Centre](/mobilnisite/slovnik/msc/)
- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)
- [MSRN – Mobile Subscriber Roaming Number](/mobilnisite/slovnik/msrn/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.044** (Rel-4) — GSM Teletex Service Support
- **TS 23.066** (Rel-19) — Mobile Number Portability Technical Realization
- **TS 23.078** (Rel-19) — CAMEL Phase 4 Stage 2 Specification
- **TS 23.226** (Rel-19) — Global Text Telephony (GTT) Stage 2
- **TS 23.806** (Rel-7) — Voice Call Continuity between CS and IMS
- **TS 24.206** (Rel-7) — Voice Call Continuity Between CS and IMS
- **TS 24.259** (Rel-19) — Personal Network Management (PNM) Protocol Details
- **TS 28.702** (Rel-19) — Core Network NRM IRP Information Service
- **TS 32.102** (Rel-19) — Telecom Management Physical Architecture Framework
- **TS 32.240** (Rel-19) — Charging Management Architecture & Principles
- **TS 32.250** (Rel-19) — Circuit Switched Offline Charging
- **TS 32.272** (Rel-19) — Charging for Push-to-Talk over Cellular (PoC)
- **TS 32.276** (Rel-19) — VCS Online Charging from Proxy Function
- **TS 32.293** (Rel-19) — Proxy Function in Domestic Service Provider
- … a dalších 5 specifikací

---

📖 **Anglický originál a plná specifikace:** [GMSC na 3GPP Explorer](https://3gpp-explorer.com/glossary/gmsc/)
