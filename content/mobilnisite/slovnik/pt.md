---
slug: "pt"
url: "/mobilnisite/slovnik/pt/"
type: "slovnik"
title: "PT – Protocol Type"
date: 2025-01-01
abbr: "PT"
fullName: "Protocol Type"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/pt/"
summary: "Pole v hlavičce GTP' (GPRS Tunnelling Protocol prime) používané k rozlišení mezi různými typy přenášených protokolů užitečného zatížení. Je nezbytné pro fakturační systémy (Charging Data Function) pro"
---

PT je pole v hlavičce GTP' používané k rozlišení mezi různými typy přenášených protokolů užitečného zatížení, což je zásadní pro fakturační systémy pro správné zpracování záznamů o účtování.

## Popis

Protocol Type (PT) je jednooktetové pole umístěné v hlavičce zprávy [GTP](/mobilnisite/slovnik/gtp/)' ([GPRS](/mobilnisite/slovnik/gprs/) Tunnelling Protocol prime). GTP' je varianta GTP používaná specificky na referenčních bodech Ga a Gz mezi síťovými elementy, jako jsou GGSN, [SGSN](/mobilnisite/slovnik/sgsn/) nebo [P-GW](/mobilnisite/slovnik/p-gw/), a funkcí Charging Data Function ([CDF](/mobilnisite/slovnik/cdf/)) nebo Charging Gateway Function ([CGF](/mobilnisite/slovnik/cgf/)). Jeho jediným účelem je přenos Charging Data Records ([CDR](/mobilnisite/slovnik/cdr/)) nebo informací o účtování založeném na událostech. Pole PT je v tomto transportním mechanismu klíčovým rozlišovačem. Udává povahu protokolu zapouzdřeného v poli 'Data' zprávy GTP', což umožňuje přijímající účtovací entitě záznam správně analyzovat.

Technicky pole PT zabírá bity 5 až 8 prvního oktetu v hlavičce GTP' (následující za bity Version, P a E). Jeho hodnota je definována v 3GPP TS 29.060 a souvisejících specifikacích pro účtování. Mezi běžné hodnoty patří: 0 (Rezervováno), 1 (GTP'), 2 (GTP), 16 ([TPKT](/mobilnisite/slovnik/tpkt/), používaný pro transport OSI TP0) a 17 (UDP). Nejčastěji používanou hodnotou v účtovacích scénářích je 1, což značí, že užitečné zatížení samo je PDU (Protocol Data Unit) GTP' – tedy že zpráva obsahuje data CDR formátovaná podle účtovacích procedur GTP'. Jiné hodnoty mohou být použity ve specifických legacy scénářích pro interoperabilitu nebo pro testovací účely. Přijímající CGF nebo fakturační systém toto pole nejprve prozkoumá, aby určil příslušný dekodér nebo handler pro příchozí datový paket.

Role pole PT je architektonická a zajišťuje rozšiřitelnost a správnou funkci transportní vrstvy pro offline účtovací data. Protože rozhraní Ga/Gz může v průběhu času potřebovat přenášet různé typy datových jednotek (např. různé verze formátů CDR nebo dokonce jiné protokoly pro interoperabilitu), statický formát užitečného zatížení je nedostatečný. Pole PT poskytuje jednoduchý mechanismus značkování s nízkou režií. To je analogické poli 'Protocol' v IP hlavičce, které udává, zda je užitečné zatížení TCP, UDP nebo ICMP. Ve flow účtovacích dat, poté co síťový element vygeneruje CDR, je tento zapouzdřen do zprávy GTP' s příslušnou hodnotou PT a odeslán do CGF. CGF použije pole PT k nasměrování záznamu ke správné zpracovatelské logice před jeho předáním do fakturační domény. Toto jasné oddělení transportu (GTP') a typu užitečného zatížení umožňuje robustní a budoucím vývoji odolnou architekturu účtování.

## K čemu slouží

Pole Protocol Type bylo zavedeno, aby řešilo konkrétní problém v transportu účtovacích dat: jednoznačnou identifikaci užitečného zatížení. Již na počátku standardizace účtování v GPRS bylo rozpoznáno, že rozhraní mezi sítí generující záznamy o využití (GGSN/SGSN) a fakturačním systémem bude potřebovat přenášet strukturovaná data. GTP bylo již používáno pro tunelování uživatelské roviny (GTP-U) a řídicí signalizaci (GTP-C), takže pro účtování byla vytvořena jeho odvozenina, GTP'. Bylo však předvídáno, že užitečné zatížení na tomto rozhraní nemusí být vždy CDR ve formátu GTP'; mohlo by potenciálně jít o surový CDR v jiném formátu nebo být zapouzdřeno mezilehlým transportním protokolem pro průchod sítí.

Pole PT poskytuje potřebnou flexibilitu a dopřednou kompatibilitu. Umožňuje jedinému transportnímu mechanismu GTP' přenášet více typů užitečného zatížení bez nutnosti změny základní struktury hlavičky GTP' nebo zřizování samostatných fyzických rozhraní pro různé typy užitečného zatížení. To zjednodušuje síťový design a provoz pro operátory. Jeho vytvoření bylo motivováno potřebou spolehlivého, standardizovaného a rozšiřitelného transportního protokolu pro účtovací data, který by se mohl vyvíjet spolu s jádrovou sítí a pojmout nové služby a účtovací modely bez nutnosti přepracování transportní vrstvy. Řeší tak omezení plynoucí z pevného, implicitního typu užitečného zatížení, což by učinilo systém křehkým a obtížně aktualizovatelným.

## Klíčové vlastnosti

- Jednooktetové pole v hlavičce zprávy GTP'
- Definuje protokol zapouzdřených dat užitečného zatížení
- Klíčové hodnoty: 1 pro GTP' (účtovací data), 2 pro GTP, 16 pro TPKT
- Umožňuje přijímacímu systému vybrat správný parser/dekodér
- Poskytuje rozšiřitelnost pro budoucí typy užitečného zatížení
- Nezbytné pro správné zpracování Charging Data Records (CDR)

## Související pojmy

- [CDR – Call Detail Record](/mobilnisite/slovnik/cdr/)
- [GPRS – CSI GPRS CAMEL Subscription Information](/mobilnisite/slovnik/gprs/)

## Definující specifikace

- **TR 23.977** (Rel-19) — Bandwidth/Resource Savings & Speech Quality Requirements
- **TS 25.424** (Rel-19) — UTRAN Iur Interface Data Transport & Signalling
- **TS 25.426** (Rel-19) — UTRAN Iur/Iub Transport Bearers
- **TS 25.434** (Rel-19) — UTRAN Iub Interface Data Transport and Signalling
- **TS 29.332** (Rel-19) — MGCF-IM-MGW Interface Protocol (Mn)
- **TS 29.333** (Rel-19) — MRFC-MRFP Mp Interface Protocol
- **TS 29.424** (Rel-8) — H.248 Profile for Trunking Media Gateways
- **TS 32.272** (Rel-19) — Charging for Push-to-Talk over Cellular (PoC)
- **TS 32.273** (Rel-19) — MBMS Charging Management
- **TS 32.295** (Rel-19) — 3GPP Charging: CDR Transfer via GTP' Protocol

---

📖 **Anglický originál a plná specifikace:** [PT na 3GPP Explorer](https://3gpp-explorer.com/glossary/pt/)
