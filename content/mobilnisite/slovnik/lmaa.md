---
slug: "lmaa"
url: "/mobilnisite/slovnik/lmaa/"
type: "slovnik"
title: "LMAA – LMA Address"
date: 2025-01-01
abbr: "LMAA"
fullName: "LMA Address"
category: "Identifier"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/lmaa/"
summary: "LMA Address (LMAA) je IP adresa funkce Local Mobility Anchor (LMA), používaná jako koncový bod tunelu v signalizaci a přenosu dat Proxy Mobile IPv6 (PMIPv6). Je cílovou adresou pro zprávy Proxy Bindin"
---

LMAA je IP adresa Local Mobility Anchor (LMA), která slouží jako koncový bod tunelu pro signalizaci PMIPv6 a jako zdroj/cíl pro řídicí a uživatelskou přenosovou rovinu.

## Popis

[LMA](/mobilnisite/slovnik/lma/) Address (LMAA) je základní identifikátor sítě v architektuře 3GPP Proxy Mobile IPv6 (PMIPv6). Je definována jako IP adresa entity Local Mobility Anchor (LMA). Tato adresa plní několik klíčových rolí v provozu řídicí i uživatelské přenosové roviny síťového řízení mobility. V řídicí rovině je LMAA cílovou IP adresou, na kterou Mobility Access Gateway ([MAG](/mobilnisite/slovnik/mag/)) odesílá své zprávy Proxy Binding Update ([PBU](/mobilnisite/slovnik/pbu/)). Tyto zprávy slouží k registraci aktuálního bodu připojení UE (Proxy Care-of Address MAG) u LMA a k vyžádání IP prefixů pro UE. Naopak LMA odesílá zprávy Proxy Binding Acknowledgement ([PBA](/mobilnisite/slovnik/pba/)) z této LMAA zpět k MAG.

V uživatelské rovině LMAA funguje jako jeden koncový bod obousměrného tunelu zřízeného mezi LMA a MAG pro přenos datového provozu UE. Všechny downlink pakety určené pro Home Network Prefix UE jsou nejprve směrovány na LMA (konkrétně na LMAA). LMA tyto pakety následně zapouzdří, přičemž jako zdrojovou adresu vnější hlavičky použije LMAA, a tuneluje je na Proxy Care-of Address (Proxy-CoA) MAG. MAG pakety deenkapsuluje a přepošle je k UE. Pro uplink provoz MAG zapouzdřuje pakety pocházející od UE a odesílá je na LMAA, kde je LMA deenkapsuluje a směruje je směrem k externí paketové datové síti. LMAA je tedy klíčová pro směrování veškerého provozu pro UE připojená přes PMIPv6.

LMAA je typicky stabilní, dosažitelná IP adresa uvnitř jádrové sítě operátora. Může se jednat o adresu IPv6, IPv4 nebo obojí, v závislosti na IP schopnostech sítě a používaném tunelovacím protokolu (např. IPv6-in-IPv6, IPv4-in-IPv4 nebo IPv4-in-IPv6). Konkrétní LMAA, která má být použita pro relaci UE, je určena během procedury počátečního připojení, často je sdělena z infrastruktury [AAA](/mobilnisite/slovnik/aaa/) ([HSS](/mobilnisite/slovnik/hss/)/3GPP AAA Server) k MAG jako součást procesu autentizace a autorizace. MAG pak tuto adresu používá pro veškerou následnou signalizaci PMIPv6 a vytváření tunelů s danou instancí LMA. Koncept LMAA zajišťuje, že MAG má jednoznačný, směrovatelný cíl pro správu relace mobility.

## K čemu slouží

Účelem LMAA je poskytnout konkrétní, směrovatelný síťový lokátor pro funkci [LMA](/mobilnisite/slovnik/lma/), což je abstraktní logická entita. V jakékoli komunikaci založené na IP je pro navázání spojení a směrování paketů povinná cílová adresa. Protokol PMIPv6, na kterém je interakce LMA/[MAG](/mobilnisite/slovnik/mag/) postavena, je signalizační protokol založený na IP. Proto bylo pro interoperabilitu nutné standardizovat způsob identifikace a adresování LMA.

Před formální definicí parametru LMAA byla adresa LMA implementačním detailem, což ztěžovalo interoperabilitu mezi různými dodavateli. Její standardizace jako 'LMAA' v rámci specifikací 3GPP (zejména TS 29.275) zajišťuje, že všechny implementace MAG vědí, který parametr nese IP adresu LMA během zřizování relace (např. z atributů AAA). Tato jednoznačná identifikace řeší problém, jak MAG, který může být v jiné administrativní doméně nebo od jiného dodavatele, objeví a komunikuje se správnou LMA pro konkrétního účastníka. Je klíčovým prvkem pro dekomponovanou, interoperabilní architekturu přístupu založeného na EPC přes non-3GPP sítě, která zajišťuje spolehlivou signalizaci řídicí roviny a tunelování uživatelské roviny.

## Klíčové vlastnosti

- Slouží jako cílová IP adresa pro řídicí zprávy Proxy Binding Update (PBU) od MAG
- Funguje jako zdrojová IP adresa pro stranu LMA v tunelu uživatelské roviny k MAG
- Může být adresa IPv4, IPv6 nebo obojí (podpora dual-stack)
- Typicky je sdělena MAG prostřednictvím protokolů AAA během autentizace UE
- Nezbytná pro směrování downlink datových paketů uživatele ke správné instanci LMA
- Klíčový parametr v položce Binding Cache Entry (BCE), kterou spravuje LMA

## Definující specifikace

- **TS 29.275** (Rel-19) — PMIPv6 Mobility & Tunnelling Protocols Stage 3

---

📖 **Anglický originál a plná specifikace:** [LMAA na 3GPP Explorer](https://3gpp-explorer.com/glossary/lmaa/)
