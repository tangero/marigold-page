---
slug: "dnic"
url: "/mobilnisite/slovnik/dnic/"
type: "slovnik"
title: "DNIC – Data Network Identifier"
date: 2025-01-01
abbr: "DNIC"
fullName: "Data Network Identifier"
category: "Identifier"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/dnic/"
summary: "Číselný kód používaný v raných systémech 3GPP k jednoznačné identifikaci paketové datové sítě (PDN), ke které se může uživatelské zařízení (UE) připojit, například internetu nebo operátorské služby. B"
---

DNIC je číselný kód používaný v raných systémech 3GPP k jednoznačné identifikaci paketové datové sítě, například internetu, jako součást Názvu přístupového bodu (APN) pro výběr sítě.

## Popis

Data Network Identifier (DNIC) je součástí Názvu přístupového bodu ([APN](/mobilnisite/slovnik/apn/)) používaného v paketově orientovaných jádrech sítí 3GPP, primárně v systémech [GPRS](/mobilnisite/slovnik/gprs/), UMTS a raných LTE. APN je plně kvalifikovaný doménový název ([FQDN](/mobilnisite/slovnik/fqdn/)), který identifikuje konkrétní paketovou datovou síť ([PDN](/mobilnisite/slovnik/pdn/)), ke které si uživatelské zařízení (UE) přeje připojit, například "internet.mnc012.mcc345.gprs". DNIC tvoří část této struktury. Konkrétně se APN skládá ze dvou částí: APN Network Identifier (který definuje externí PDN) a APN Operator Identifier (který definuje [PLMN](/mobilnisite/slovnik/plmn/), ve kterém se PDN nachází). DNIC je historický prvek související s tímto adresováním.

Technicky byl DNIC kód, který mohl být použit v kontextech síťového směrování. Jeho hlavní funkcí bylo napomáhat výběru správného uzlu Gateway GPRS Support Node (GGSN) nebo později brány Packet Data Network Gateway ([PGW](/mobilnisite/slovnik/pgw/)), která sloužila jako rozhraní k externí datové síti. Když uživatelské zařízení aktivovalo kontext Packet Data Protocol ([PDP](/mobilnisite/slovnik/pdp/)), poskytlo APN. Síť toto APN rozřešila a informace DNIC mohly být interně použity k nasměrování žádosti o zřízení relace na příslušný bránový uzel, který měl konektivitu k požadované externí síti.

Role DNIC byla výraznější v éře jádrových sítí GPRS a UMTS. Pomáhal v době, kdy byly síťové konfigurace a propojení mezi operátory méně standardizované než dnes. Poskytoval jasný, na kódu založený identifikátor pro sítě, který doplňoval systém doménových jmen. S vývojem směrem k plně IP sítím a zjednodušením architektur jádrových sítí v EPS a 5GS však explicitní použití a nutnost DNIC ustoupily ve prospěch flexibilnějšího rozřešování APN založeného na [DNS](/mobilnisite/slovnik/dns/) a přímých mechanismů výběru PGW.

## K čemu slouží

DNIC byl vytvořen k řešení základního problému identifikace a směrování datových relací do správné externí paketové datové sítě v raných systémech mobilních dat 2G a 3G. Před všudypřítomnou IP konektivitou potřebovali operátoři spolehlivou metodu k rozlišení různých služebních sítí (např. podnikové intranety, WAP brány, veřejný internet). DNIC jako součást konstrukce APN poskytoval pro tento účel standardizovaný, strojově vhodný identifikátor.

Řešil omezení spočívající pouze v používání potenciálně nejednoznačných textových názvů nebo IP adres pro výběr sítě. Formát číselného kódu umožňoval efektivní parsování a rozhodování o směrování v rámci uzlů jádrové sítě, jako jsou SGSN a GGSN. To bylo klíčové pro umožnění více PDN připojení a pro roaming mezi operátory, kdy navštěvovaná síť potřebovala pochopit, ke které PDN domovské sítě se předplatitel chce připojit.

Historicky koncept DNIC přebíral adresování X.121 používané v legacy paketových sítích X.25, což odráželo přechodnou povahu raných mobilních datových služeb. Jeho účelem bylo přinést strukturu a jednoznačnou identifikaci do rodícího se ekosystému mobilních dat. Jak se sítě vyvíjely směrem k IP Multimedia Subsystem (IMS) a plně IP architekturám v LTE, potřeba takového specifického číselného identifikátoru zeslábla. APN zůstal kritický, ale jeho rozřešování a proces výběru brány se více integrovaly s DNS a mechanismy založenými na politikách, což učinilo explicitní komponentu DNIC v moderních specifikacích 5G z velké části zastaralou.

## Klíčové vlastnosti

- Číselný identifikátor pro paketovou datovou síť (PDN)
- Součást konstrukce Názvu přístupového bodu (APN) v GPRS/UMTS/EPS
- Používán pro směrování žádostí o aktivaci kontextu PDP ke správnému GGSN/PGW
- Umožňoval identifikaci externích sítí, jako je internet nebo operátorské služby
- Podporoval roamingové scénáře identifikací PDN domovské sítě
- Poskytoval strukturovanou alternativu k čistě DNS založené síťové identifikaci

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [DNIC na 3GPP Explorer](https://3gpp-explorer.com/glossary/dnic/)
