---
slug: "etftu"
url: "/mobilnisite/slovnik/etftu/"
type: "slovnik"
title: "ETFTU – Extended Traffic Flow Template Support User Equipment"
date: 2025-01-01
abbr: "ETFTU"
fullName: "Extended Traffic Flow Template Support User Equipment"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/etftu/"
summary: "Schopnost uživatelského zařízení (UE) indikující podporu rozšířené sady paketových filtrů v šabloně toku provozu (TFT). Umožňuje složitější a podrobnější správu toků provozu pro IP toky, což podporuje"
---

ETFTU je schopnost uživatelského zařízení (UE) indikující podporu rozšířené sady paketových filtrů v šabloně toku provozu (Traffic Flow Template), což umožňuje složitější správu toků provozu a pokročilou QoS v EPS a 5GS.

## Popis

Extended Traffic Flow Template Support User Equipment (ETFTU) je indikátor schopnosti uvnitř uživatelského zařízení (UE), který signalizuje síti, že UE dokáže zpracovat rozšířený počet a složitost paketových filtrů v rámci šablony toku provozu ([TFT](/mobilnisite/slovnik/tft/)). TFT je základní konstrukcí v 3GPP paketových jádrových sítích ([GPRS](/mobilnisite/slovnik/gprs/), EPS, 5GS) používanou k asociaci IP toků provozu s konkrétními přenašeči (bearers), což umožňuje diferencovanou kvalitu služeb (QoS) a vynucování politik. TFT obsahuje sady paketových filtrů, které klasifikují uplink a downlink IP pakety na základě parametrů, jako jsou zdrojové/cílové IP adresy, čísla portů, typ protokolu (např. TCP/[UDP](/mobilnisite/slovnik/udp/)) a pole Type of Service ([TOS](/mobilnisite/slovnik/tos/)). Každý paketový filtr je v podstatě pravidlo, které odpovídá konkrétnímu IP provozu.

V architektuře jádrové sítě, konkrétně v Packet Data Network Gateway ([PGW](/mobilnisite/slovnik/pgw/)) v EPS nebo v User Plane Function ([UPF](/mobilnisite/slovnik/upf/)) v 5GC, se TFT používají k mapování klasifikovaných IP toků na příslušný Evolved Packet System (EPS) bearer nebo QoS Flow. Síť pro provoz odpovídající TFT filtrům zřizuje vyhrazené přenašeče se specifickými charakteristikami QoS (jako je garantovaná přenosová rychlost, priorita). Standardní TFT má definované omezení počtu paketových filtrů, které může obsahovat. Schopnost ETFTU indikuje, že UE dokáže podporovat rozšířenou sadu překračující toto základní omezení, což umožňuje sofistikovanější diferenciaci provozu.

Schopnost ETFTU se vyměňuje během procedur přenosu schopností UE, jako jsou procedury připojení (Attach) nebo aktualizace oblasti sledování (Tracking Area Update). Síť (např. Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)) nebo Access and Mobility Management Function ([AMF](/mobilnisite/slovnik/amf/))) se o této schopnosti UE dozví. Když funkce Policy and Charging Rules Function (PCRF) nebo Policy Control Function (PCF) určí pravidla politiky vyžadující složité filtrování provozu, síť může tuto rozšířenou schopnost využít. Umožňuje funkci správy relace (Session Management) konfigurovat na straně UE TFT s větším počtem filtrů pro klasifikaci uplink provozu a na straně sítě pro vynucení downlink provozu. To je klíčové pro služby vyžadující více souběžných toků s odlišnou QoS, jako jsou podnikové VPN s více aplikacemi, pokročilé služby IP Multimedia Subsystem (IMS) nebo scénáře se simultánními toky s garantovanou a negarantovanou přenosovou rychlostí.

## K čemu slouží

ETFTU bylo zavedeno, aby řešilo omezení kapacity standardní šablony toku provozu (TFT) pro paketové filtry. Jak se mobilní služby vyvíjely, aplikace začaly generovat více souběžných IP toků s různorodými požadavky. Standardní VoIP hovor přes IMS může například vyžadovat samostatné toky pro hlas, video a signalizaci (SIP), z nichž každý potřebuje jinou QoS. Podnikové scénáře mohou zahrnovat desítky odlišných aplikačních toků. Původní specifikace TFT představovala omezení v tom, kolik takových toků může být individuálně identifikováno a namapováno na vyhrazené přenašeče.

Hlavním problémem, který ETFTU řeší, je umožnění jemnějšího řízení provozu a diferenciace QoS. Bez podpory rozšířeného TFT by síť mohla být nucena agregovat odlišný provoz na jediný přenašeč, což by ohrozilo schopnost poskytovat optimální QoS pro každý tok, nebo by nemusela být schopna zřídit všechny potřebné vyhrazené přenašeče. To by mohlo vést k suboptimálnímu uživatelskému zážitku, zejména pro aplikace citlivé na latenci nebo s vysokou prioritou smíchané s provozem typu best-effort. ETFTU poskytuje základní schopnost v UE pro podporu pokročilého vynucování politik sítí, což umožňuje přesnější směrování provozu a alokaci zdrojů podle definice politických rámců, jako je Policy and Charging Control (PCC).

Jeho vytvoření bylo motivováno přechodem průmyslu na plně IP sítě a rostoucí poptávkou po bohatých komunikačních službách. Budoucí vývoj sady schopností UE tím byl zabezpečen, aby se při rostoucí sofistikovanosti síťových politik UE nestala úzkým hrdlem. Je to klíčový faktor pro architekturu řízenou QoS a politikami, která je ústřední pro 4G EPS i 5G 5GS, a zajišťuje konzistentní uživatelský zážitek napříč různými přístupovými technologiemi.

## Klíčové vlastnosti

- Signalizuje podporu UE pro rozšířený počet paketových filtrů na jednu TFT
- Umožňuje vytváření složitějších pravidel klasifikace provozu na UE
- Umožňuje pokročilé mapování QoS pro větší počet souběžných IP toků
- Funguje ve spojení s architekturou PCC pro dynamické vynucování politik
- Aplikovatelné pro vyhrazené přenašeče EPS i QoS Flows v 5GS
- Zpětně kompatibilní; sítě mohou pracovat s UE podporujícími ETFTU i bez nich

## Definující specifikace

- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2

---

📖 **Anglický originál a plná specifikace:** [ETFTU na 3GPP Explorer](https://3gpp-explorer.com/glossary/etftu/)
