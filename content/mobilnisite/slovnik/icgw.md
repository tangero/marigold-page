---
slug: "icgw"
url: "/mobilnisite/slovnik/icgw/"
type: "slovnik"
title: "ICGW – Incoming Call Gateway"
date: 2025-01-01
abbr: "ICGW"
fullName: "Incoming Call Gateway"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/icgw/"
summary: "Incoming Call Gateway (ICGW) je funkční entita v architektuře sítě 3GPP odpovědná za zpracování a směrování příchozích hovorů k mobilním účastníkům. Působí jako brána mezi externími sítěmi (jako PSTN"
---

ICGW je funkční entita v síti 3GPP, která funguje jako brána z externích sítí do mobilního jádra, zpracovává a směruje příchozí hovory k mobilním účastníkům.

## Popis

Incoming Call Gateway (ICGW) je prvek jádrové sítě definovaný v architektuře 3GPP, konkrétně pro služby přepojovaných okruhů ([CS](/mobilnisite/slovnik/cs/)) pro hlas. Slouží jako primární vstupní bod pro hovory určené účastníkům v doméně operátora mobilní sítě. Když hovor pochází z externí sítě, jako je veřejná telefonní komutovaná síť (PSTN) nebo jiná veřejná pozemní mobilní síť (PLMN), je nejprve směrován na ICGW. ICGW provádí potřebnou signalizaci a převody protokolů, aby přeložil externí signalizaci (např. [ISUP](/mobilnisite/slovnik/isup/)) do vnitřního signalizačního protokolu mobilní sítě, především Mobile Application Part ([MAP](/mobilnisite/slovnik/map/)) nebo jiných relevantních protokolů používaných pro řízení hovoru.

Architektonicky je ICGW často integrován nebo úzce spojen s funkcí Gateway [MSC](/mobilnisite/slovnik/msc/) ([GMSC](/mobilnisite/slovnik/gmsc/)). GMSC je MSC, které dotazuje Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)), aby získalo směrovací informace pro volaného mobilního účastníka. ICGW lze chápat jako fyzickou nebo logickou funkci brány, která rozhraní s externí sítí. Zpracovává úvodní signalizaci pro navázání hovoru, včetně analýzy adresy, překladu čísel a potenciálně funkcí spojených s účtováním. Její provoz zahrnuje přijetí zprávy Initial Address Message ([IAM](/mobilnisite/slovnik/iam/)) z externí sítě, určení správného HLR k dotazování a následné předání hovoru příslušnému Visited MSC (VMSC), kde se účastník aktuálně nachází.

Role ICGW přesahuje prosté směrování. Je kritickým bodem pro implementaci regulatorních a servisních funkcí, jako je oprávněný odposlech, kontroly blokování hovorů a specifické směrovací politiky pro příchozí hovory. Zajišťuje, že navázání hovoru je v souladu s politikami sítě a servisním profilem účastníka, než je hovor rozšířen do mobilní sítě. V moderních sítích, zejména s přechodem na Voice over LTE (VoLTE) a IP Multimedia Subsystem (IMS), byla tradiční funkce ICGW založená na CS vyvinuta nebo nahrazena entitami založenými na IMS, jako je Interrogating Call Session Control Function ([I-CSCF](/mobilnisite/slovnik/i-cscf/)) a Media Gateway Control Function (MGCF), pro zpracování příchozích hovorů z legacy CS sítí.

## K čemu slouží

ICGW byl vytvořen, aby řešil základní potřebu vzájemného propojení mezi mobilními sítěmi a externími pevnými nebo jinými mobilními sítěmi. V počátcích GSM a UMTS byly mobilní sítě izolované ostrovy, které potřebovaly připojení ke globální PSTN a jiným PLMN, aby zajistily univerzální konektivitu. Bez vyhrazené bránové funkce by příchozí hovory z těchto externích sítí neměly definovaný vstupní bod ani standardizovaný postup pro směrování v rámci mobilní sítě.

Před standardizovanými branami, jako je ICGW, byla mezisíťová komunikace často ad-hoc, proprietární a neefektivní. ICGW poskytl standardizované, škálovatelné a spolehlivé rozhraní. Řešil problémy s překladem adres (konverze čísel E.164 na směrovací adresy mobilní sítě), převodem signalizačních protokolů (např. z ISUP na MAP) a centralizovaným bodem kontroly příchozího provozu. To umožnilo efektivní doručování hovorů, zjednodušenou správu sítě a implementaci konzistentních funkcí, jako je řešení přenositelnosti čísel a bezpečnostní filtrování na hranici sítě.

Jeho vytvoření bylo motivováno komerční nutností plné integrace mobilních sítí do globálního telekomunikačního ekosystému. Umožnil splnit slib mobilní telefonie o konektivitě 'kdekoli a kdykoli' tím, že zajistil, aby hovory z jakékoli sítě na světě mohly úspěšně dosáhnout mobilního účastníka. ICGW se stal základním kamenem pro účtování, oprávněný odposlech a servisní diferenciaci příchozích hovorů a vytvořil kritickou část infrastruktury pro výnosy a provoz mobilních operátorů.

## Klíčové vlastnosti

- Působí jako standardizovaný vstupní bod pro mobilní ukončené hovory z externích sítí
- Provádí převod signalizačních protokolů mezi externími (např. ISUP) a interními (např. MAP) protokoly
- Dotazuje HLR, aby získalo směrovací informace pro volaného účastníka
- Poskytuje centrální bod pro implementaci politik filtrování, blokování a směrování hovorů
- Podporuje účtovací funkce pro zpracování příchozích hovorů
- Usnadňuje funkce pro dodržování regulatorních požadavků, jako je oprávněný odposlech na hraně sítě

## Související pojmy

- [GMSC – Gateway Mobile Services Switching Centre](/mobilnisite/slovnik/gmsc/)
- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)
- [MSC – Mobile Services Switching Centre](/mobilnisite/slovnik/msc/)
- [MAP – Mobile Application Protocol](/mobilnisite/slovnik/map/)
- [ISUP – MIME ISDN User Part Multi-purpose Internet Mail Extension](/mobilnisite/slovnik/isup/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [ICGW na 3GPP Explorer](https://3gpp-explorer.com/glossary/icgw/)
