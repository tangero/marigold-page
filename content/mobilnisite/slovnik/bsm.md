---
slug: "bsm"
url: "/mobilnisite/slovnik/bsm/"
type: "slovnik"
title: "BSM – Basic Safety Message"
date: 2026-01-01
abbr: "BSM"
fullName: "Basic Safety Message"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/bsm/"
summary: "Základní bezpečnostní zpráva (Basic Safety Message – BSM) je standardizovaný formát zprávy V2X definovaný 3GPP pro přímou komunikaci vozidlo-vozidlo a vozidlo-infrastruktura. Poskytuje základní inform"
---

BSM je standardizovaný formát zprávy V2X pro přímou komunikaci mezi vozidly, který poskytuje základní údaje o stavu vozidla v reálném čase a umožňuje klíčové bezpečnostní aplikace v rámci služeb Cellular-V2X (C-V2X).

## Popis

Základní bezpečnostní zpráva (Basic Safety Message – BSM) je základní zpráva aplikační vrstvy definovaná v rámci architektury 3GPP pro komunikační služby Vehicle-to-Everything ([V2X](/mobilnisite/slovnik/v2x/)). Funguje jako standardizovaná datová struktura, kterou vozidla a vozovými jednotky ([RSU](/mobilnisite/slovnik/rsu/)) periodicky vysílají nebo generují na základě události, aby sdělily svůj dynamický stav dalším entitám v okolí. Zpráva je navržena pro přenos s nízkou latencí a vysokou spolehlivostí přes rozhraní postranního spoje PC5, což je přímý komunikační spoj mezi uživatelskými zařízeními (UE) určenými pro V2X, nezávislý na infrastruktuře mobilní sítě (rozhraní Uu). To umožňuje komunikaci i v oblastech bez pokrytí sítě, což je zásadní pro aplikace na ochranu života.

Z architektonického hlediska BSM generuje aplikační vrstva V2X v UE, kterou může být palubní jednotka (OBU) ve vozidle nebo modul v RSU. Tato aplikační vrstva komunikuje s protokolovými zásobníky Přístupové vrstvy (Access Stratum – [AS](/mobilnisite/slovnik/as/)) a Vrstvy nezávislé na přístupu (Non-Access Stratum – [NAS](/mobilnisite/slovnik/nas/)) standardu 3GPP za účelem přenosu. Pro přenos přes rozhraní PC5 je zpráva zpracována vrstvami [PDCP](/mobilnisite/slovnik/pdcp/) (Packet Data Convergence Protocol), [RLC](/mobilnisite/slovnik/rlc/) (Radio Link Control) a [MAC](/mobilnisite/slovnik/mac/) (Medium Access Control), než je odeslána přes fyzickou vrstvu pomocí specifických zdrojových fondů vyhrazených pro komunikaci V2X přes postranní spoj. Specifikace 3GPP definují požadavky na službu a potřebné parametry kvality služby (QoS) pro přenos BSM, ale konkrétní kódování zprávy (např. použití ASN.1 dle standardů [SAE](/mobilnisite/slovnik/sae/) J2735 nebo ETSI ITS-G5) typicky odkazuje na externí organizace jako SAE nebo ETSI, přičemž 3GPP zajišťuje, aby transportní síť dokázala podporovat její přísné požadavky.

Mezi klíčové součásti informací v BSM patří základní datové prvky, jako je zeměpisná šířka, délka a nadmořská výška vozidla (poloha); rychlost a směr; zrychlení (včetně podélného, příčného a vertikálního); rozměry a typ vozidla; stav brzdového systému; a úhel natočení volantu. Zpráva může také obsahovat dočasné ID vozidla pro anonymitu. Zpráva je vysílána vysokou frekvencí (typicky 10 Hz), aby měli ostatní přijímače téměř reálný přehled o stavu vysílajícího. Role BSM v síti 3GPP není role síťového protokolu, ale primárního užitečného zatížení pro bezpečnostní služby V2X. Role sítě, definovaná např. ve specifikacích 23.700 a 37.985, spočívá v poskytování spolehlivého transportního mechanismu s definovanými QoS toky, správě přidělování zdrojů pro postranní spoj (buď naplánované sítí – režim 3, nebo autonomní – režim 4) a podpoře autorizace služeb a řízení politik pro šíření BSM.

## K čemu slouží

Základní bezpečnostní zpráva existuje za účelem umožnění základní sady aplikací pro kooperativní povědomí a základní bezpečnost v automobilovém ekosystému, které nebyly možné pouze s tradičními palubními senzory, jako je radar a kamery. Předchozí bezpečnostní systémy vozidel byly omezeny na přímou viditelnost a dosah senzorů jednotlivých vozidel, což vytvářelo mrtvé úhly a prodlužovalo reakční dobu na skrytá nebezpečí. BSM jako součást rámce V2X tento problém řeší vytvořením 360stupňového povědomí o okolním provozním prostředí bez nutnosti přímé viditelnosti tím, že umožňuje vozidlům elektronicky přímo 'vidět' stav ostatních. Tím se řeší kritické bezpečnostní mezery, které vedou ke kolizím na křižovatkách, nárazům zezadu za podmínek snížené viditelnosti a nehodám se zranitelnými účastníky provozu.

Motivace pro její vytvoření a standardizaci v rámci 3GPP vycházela z tlaku automobilového průmyslu na technologie propojených vozidel a z potřeby globálně harmonizovaného řešení založeného na mobilních sítích. Zatímco komunikace s vyhrazeným krátkým dosahem (DSRC) založená na IEEE 802.11p definovala podobné zprávy, vstup 3GPP s LTE-V2X a později NR-V2X poskytl migrační cestu využívající všudypřítomnou mobilní technologii, lepší spektrální účinnost a jasnější cestu k vývoji směrem k 5G. Standardizace požadavků na službu pro přenos BSM v 3GPP Release 16 zajistila, že síťové a protokolové mechanismy mobilních zařízení mohou být optimalizovány tak, aby splňovaly požadavky na ultra-spolehlivou komunikaci s nízkou latencí (URLLC) pro tyto zprávy kritické pro bezpečnost života, což bylo omezením dřívějších mobilních datových služeb, které nebyly navrženy pro přímou bezpečnostní komunikaci mezi zařízeními.

## Klíčové vlastnosti

- Standardizovaná struktura zprávy pro výměnu údajů o stavu vozidla
- Podpora periodického vysílání i generování na základě události
- Optimalizováno pro přenos přes rozhraní postranního spoje PC5 definované 3GPP (LTE-V2X a NR-V2X)
- Definuje přísné požadavky QoS na latenci (např. <100 ms) a spolehlivost
- Umožňuje kooperativní povědomí bez nutnosti přímé viditelnosti pro účastníky provozu
- Základ pro pokročilé aplikace V2X, jako je předcházení srážkám a varování před nebezpečím

## Související pojmy

- [V2X – Vehicle-to-Everything Application Server](/mobilnisite/slovnik/v2x/)
- [URLLC – Ultra Reliable Low Latency Communication](/mobilnisite/slovnik/urllc/)

## Definující specifikace

- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TR 37.985** (Rel-19) — Overview of V2X features in LTE and NR

---

📖 **Anglický originál a plná specifikace:** [BSM na 3GPP Explorer](https://3gpp-explorer.com/glossary/bsm/)
