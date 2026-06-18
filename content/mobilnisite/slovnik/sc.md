---
slug: "sc"
url: "/mobilnisite/slovnik/sc/"
type: "slovnik"
title: "SC – Super-Charger"
date: 2025-01-01
abbr: "SC"
fullName: "Super-Charger"
category: "Services"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/sc/"
summary: "Super-Charger (SC) je služební funkce 3GPP navržená ke zlepšení výkonu a uživatelského zážitku z datových služeb, zejména pro provoz založený na HTTP. Optimalizuje doručování obsahu pomocí technik jak"
---

SC je služební funkce 3GPP navržená ke zlepšení výkonu datových služeb pro HTTP provoz optimalizací doručování obsahu pomocí technik jako detekce provozu, vynucování politik a případné ukládání do mezipaměti nebo komprese.

## Popis

Super-Charger (SC), jak je definováno ve specifikacích 3GPP, například v TS 23.116, je síťová funkce optimalizace služeb. Funguje jako vylepšení uvnitř mobilní jádrové sítě, konkrétně interaguje s architekturou Policy and Charging Control ([PCC](/mobilnisite/slovnik/pcc/)) a často zahrnuje Traffic Detection Function ([TDF](/mobilnisite/slovnik/tdf/)). Základní koncept SC spočívá v identifikaci specifických typů uživatelského datového provozu – primárně webového ([HTTP](/mobilnisite/slovnik/http/)/[HTTPS](/mobilnisite/slovnik/https/)) a streamovacího video provozu – a aplikaci optimalizací ke zlepšení kvality uživatelského zážitku ([QoE](/mobilnisite/slovnik/qoe/)) a efektivity využití síťových zdrojů. Nejde o samostatný síťový uzel, ale o soubor schopností, které lze integrovat do stávajících síťových prvků nebo nasadit jako vyhrazenou službu.

Z architektonického hlediska funkce SC typicky zahrnuje několik klíčových komponent. Traffic Detection Function (TDF) je klíčová pro hlubokou kontrolu paketů (DPI) za účelem identifikace toků provozu, na které se SC vztahuje, na základě typu aplikace, cíle nebo obsahu. TDF komunikuje s Policy and Charging Rules Function ([PCRF](/mobilnisite/slovnik/pcrf/)) přes referenční bod Sd. Na základě hlášení o detekci provozu a politik definovaných operátorem může PCRF následně nainstalovat nová pravidla do Policy and Charging Enforcement Function ([PCEF](/mobilnisite/slovnik/pcef/)), která sídlí v bráně (např. [PGW](/mobilnisite/slovnik/pgw/)/UPF). Tato pravidla určují, jak je identifikovaný provoz zpracováván. Samotná optimalizace může být provedena samotnou PCEF, vyhrazeným optimalizačním uzlem (jako je transparentní proxy nebo mezipaměť) nebo přesměrováním provozu na Service Capability Exposure Function (SCEF)/Network Exposure Function (NEF) pro interakci se serverem aplikace třetí strany.

Fungování SC zahrnuje dynamický cyklus politik. Když uživatel zahájí datovou relaci, PCEF vyžádá pravidla od PCRF. Pokud je SC povoleno, PCRF může pro tuto relaci aktivovat detekci provozu. Jak pakety procházejí bránou, TDF (která může být umístěna společně s PCEF) je kontroluje. Po detekci provozu odpovídajícího politice Super-Charger (např. video od konkrétního poskytovatele) TDF informuje PCRF. PCRF pak rozhodne o akci, například o aplikaci vyhrazeného nosiče se zaručenou přenosovou rychlostí (GBR) pro tento video tok, o instrukcích PCEF k aplikaci komprese hlaviček nebo o přesměrování toku přes optimalizační engine obsahu, který může provádět ukládání do mezipaměti, překódování nebo kompresi. Celý tento proces probíhá dynamicky a pro každý tok zvlášť, což umožňuje podrobnou diferenciaci služeb.

Role SC v síti je překlenout propast mezi jednoduchým přístupem k internetu s nejlepším úsilím a sofistikovanou sítí s povědomím o aplikacích. Umožňuje mobilním síťovým operátorům aktivně spravovat a vylepšovat oblíbené datové služby. Díky prioritizaci, tvarování nebo optimalizaci specifického provozu může SC snížit buffering videa, urychlit načítání webových stránek a snížit celkovou latenci. To vede k vyšší spokojenosti zákazníků. Z pohledu sítě může SC zlepšit spektrální efektivitu snížením objemu redundantních dat (prostřednictvím ukládání do mezipaměti) a zajištěním, že kritický provoz získá potřebné zdroje, čímž vyhladí špičky v provozu a zlepší celkovou kapacitu a výkon sítě pro všechny uživatele.

## K čemu slouží

Super-Charger byl vytvořen, aby řešil výzvy způsobené explozivním růstem internetového provozu, zejména náročných na šířku pásma a citlivých na latenci aplikací, jako je streamování videa a prohlížení webu, v mobilních sítích. Klasický model IP s nejlepším úsilím v mobilních jádrech byl nedostatečný pro zaručení dobré kvality uživatelského zážitku u těchto služeb, což vedlo k frustraci uživatelů z bufferingu a pomalého načítání. Účelem SC je to vyřešit tím, že umožní síti inteligentně identifikovat a optimalizovat specifické datové toky, čímž urychlí doručování služeb a efektivněji využije omezené rádiové a transportní zdroje.

Historický kontext SC spočívá ve vývoji od jednoduchých sítí zaměřených na hlas ke komplexním platformám služeb zaměřeným na data. S nasazením 3G a 4G (LTE) operátoři hledali způsoby, jak monetizovat datové služby nad rámec jednoduchého objemového účtování. Potřebovali nástroje pro diferenciaci svých nabídek – například poskytnutí úrovně služby 'premium video'. SC poskytlo technický rámec, jak toho dosáhnout. Odstranilo omezení předchozích, statičtějších přístupů k QoS, které se často spoléhaly na filtrování podle Access Point Name (APN) nebo statické IP adresy, zavedením dynamického, na aplikaci zaměřeného řízení politik. To umožnilo reakci v reálném čase na aktivitu uživatele.

Dále bylo SC motivováno potřebou efektivity sítě. Nezávislé přenášení stejného oblíbeného video obsahu tisícům uživatelů plýtvá backhaulovými a rádiovými zdroji. Integrací schopností ukládání do mezipaměti a komprese si SC klade za cíl snížit redundantní přenos dat. Také umožňuje operátorům efektivněji spravovat špičky v provozu tím, že zajišťuje stabilitu vysoce prioritních služeb během přetížení. V podstatě SC existuje proto, aby transformovalo mobilní síť z pasivní 'bitové trubky' na aktivní platformu s povědomím o službách, která může zlepšit výkon, vytvořit nové úrovně služeb a zlepšit ekonomickou efektivitu poskytování datových služeb.

## Klíčové vlastnosti

- Detekce provozu s povědomím o aplikaci pomocí hluboké kontroly paketů (DPI)
- Dynamické vynucování politik integrované s architekturou PCC
- Schopnost aktivovat vyhrazené nosiče pro optimalizované datové toky
- Podpora technik optimalizace obsahu (např. ukládání do mezipaměti, komprese)
- Sledování a hlášení kvality uživatelského zážitku (QoE)
- Umožňuje diferenciaci služeb a vrstvené datové nabídky

## Související pojmy

- [PCC – Performance-oriented Congestion Control](/mobilnisite/slovnik/pcc/)
- [PCRF – Policy and Charging Rules Function](/mobilnisite/slovnik/pcrf/)
- [PCEF – Policy and Charging Enforcement Function](/mobilnisite/slovnik/pcef/)
- [TDF – Traffic Detection Function](/mobilnisite/slovnik/tdf/)
- [QoS – Quality of Service](/mobilnisite/slovnik/qos/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 22.944** (Rel-19) — UE Functionality Split Scenarios and Requirements
- **TR 22.950** (Rel-19) — Feasibility Study on Priority Service
- **TR 22.978** (Rel-19) — Feasibility of All-IP Network (AIPN) in 3GPP
- **TS 23.016** (Rel-19) — Subscriber Data Management Stage 2
- **TS 23.039** (Rel-5) — SMSC to SME Interface Protocols
- **TS 23.237** (Rel-19) — IMS Service Continuity (ISC) Stage 2
- **TS 23.875** (Rel-5) — Feasibility Study for Push Services Architecture
- **TS 23.889** (Rel-10) — Local Call Local Switch Core Network Impact Study
- **TS 24.216** (Rel-19) — Communication Continuity Management Object
- **TS 24.237** (Rel-19) — IMS Service Continuity Protocol Details
- **TS 24.337** (Rel-19) — IMS Inter-UE Transfer Protocol Specification
- **TS 25.141** (Rel-19) — UTRA FDD Base Station RF Conformance Testing
- **TS 25.142** (Rel-19) — UTRA TDD Base Station RF Test Methods
- **TS 25.707** (Rel-14) — Multi-Carrier Enhancements for UMTS Study
- … a dalších 22 specifikací

---

📖 **Anglický originál a plná specifikace:** [SC na 3GPP Explorer](https://3gpp-explorer.com/glossary/sc/)
