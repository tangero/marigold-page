---
slug: "mag"
url: "/mobilnisite/slovnik/mag/"
type: "slovnik"
title: "MAG – Mobility Access Gateway"
date: 2025-01-01
abbr: "MAG"
fullName: "Mobility Access Gateway"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/mag/"
summary: "Síťová entita definovaná v Evolved Packet Core (EPC), která spravuje mobilitu pro ne-3GPP přístupové sítě, jako je Wi-Fi. Funguje jako brána, která umožňuje plynulé přechody a zabezpečené připojení me"
---

MAG je síťová entita v Evolved Packet Core, která spravuje mobilitu a funguje jako brána pro zabezpečené připojení a přechody mezi sítěmi 3GPP a ne-3GPP, jako je Wi-Fi.

## Popis

Mobility Access Gateway (MAG) je klíčová funkční entita v architektuře 3GPP Evolved Packet Core (EPC), specificky definovaná pro spolupráci s ne-3GPP přístupovými sítěmi, jako jsou Wi-Fi, CDMA2000 nebo pevné širokopásmové připojení. Funguje jako brána, která usnadňuje IP připojení a správu mobility pro uživatelské zařízení (UE) připojující se prostřednictvím těchto ne-3GPP přístupů. Hlavní úlohou MAG je implementace Proxy Mobile IPv6 (PMIPv6) jako mobilního protokolu směrem k Packet Data Network Gateway ([PGW](/mobilnisite/slovnik/pgw/)) nebo Local Packet Data Network Gateway (L-PGW) v jádru sítě. Když se UE připojí prostřednictvím důvěryhodného nebo nedůvěryhodného ne-3GPP přístupu, MAG vytvoří s PGW, která slouží jako Local Mobility Anchor ([LMA](/mobilnisite/slovnik/lma/)), tunel PMIPv6 (obousměrný tunel). Tento tunel přenáší veškerý datový provoz UE a zajišťuje, že UE zachová stejnou IP adresu a nepřetržité spojení i při pohybu mezi různými přístupovými body nebo technologiemi. Pro nedůvěryhodný přístup MAG často integruje s evolved Packet Data Gateway (ePDG) k vytvoření tunelu [IPsec](/mobilnisite/slovnik/ipsec/) pro zabezpečení provozu přes nedůvěryhodnou síť. MAG komunikuje s infrastrukturou Authentication, Authorization, and Accounting ([AAA](/mobilnisite/slovnik/aaa/)) pro autentizaci účastníka a vynucování pravidel. Jeho architektura zahrnuje rozhraní jako S2a (pro důvěryhodný ne-3GPP přístup) a S2b (pro nedůvěryhodný ne-3GPP přístup přes ePDG) směrem k PGW a může také komunikovat s Policy and Charging Rules Function ([PCRF](/mobilnisite/slovnik/pcrf/)) pro dynamické řízení pravidel. Správou těchto tunelů a vazeb mobility MAG umožňuje plynulé přechody, kontinuitu relace a integrované vynucování pravidel napříč heterogenními přístupovými sítěmi.

## K čemu slouží

MAG byl zaveden, aby řešil rostoucí potřebu plynulé mobility a integrovaného poskytování služeb napříč heterogenními síťovými prostředími, zejména když se Wi-Fi a další ne-3GPP technologie staly všudypřítomnými. Před jeho standardizací byla integrace ne-3GPP přístupů s jádrovými sítěmi 3GPP často proprietární, což vedlo k roztříštěným uživatelským zkušenostem a složité správě sítě. Vývoj architektury EPC ve 3GPP Release 8 si kladl za cíl vytvořit jednotné, plně IP jádro sítě, které by podporovalo více přístupových technologií. MAG jako součást této vize řeší problém poskytování plynulé IP mobility a konzistentního vynucování pravidel pro zařízení připojující se prostřednictvím ne-3GPP přístupů. Umožňuje operátorům přesměrovávat datový provoz na Wi-Fi sítě při zachování kontroly jádrové sítě nad autentizací, účtováním a kvalitou služeb. To bylo motivováno posunem průmyslu směrem ke konvergenci pevných a mobilních sítí a snahou využít nákladově efektivní přístupové technologie bez kompromisů v zabezpečení nebo kontinuitu služeb. MAG standardizuje funkci brány, čímž zajišťuje interoperabilitu a zjednodušuje nasazení vícepřístupových sítí.

## Klíčové vlastnosti

- Implementuje Proxy Mobile IPv6 (PMIPv6) pro správu mobility
- Funguje jako brána pro důvěryhodné a nedůvěryhodné ne-3GPP přístupové sítě
- Vytváří IP tunely s Packet Data Network Gateway (PGW)
- Podporuje plynulý přechod a kontinuitu relace napříč typy přístupu
- Integruje se s AAA pro autentizaci a autorizaci účastníka
- Umožňuje vynucování pravidel a účtování pro ne-3GPP přístup

## Související pojmy

- [EPC – Evolved Packet Core Network](/mobilnisite/slovnik/epc/)
- [PMIP – Proxy Mobile Internet Protocol version 6](/mobilnisite/slovnik/pmip/)
- [PGW – PDN Gateway](/mobilnisite/slovnik/pgw/)
- [EPDG – Evolved Packet Data Gateway](/mobilnisite/slovnik/epdg/)

## Definující specifikace

- **TS 23.402** (Rel-19) — EPC for Non-3GPP Access (PMIP)
- **TS 29.273** (Rel-19) — AAA Protocols for Non-3GPP Access in EPS & 5GS NSWO
- **TS 29.275** (Rel-19) — PMIPv6 Mobility & Tunnelling Protocols Stage 3
- **TS 33.402** (Rel-19) — Security for non-3GPP access to EPS

---

📖 **Anglický originál a plná specifikace:** [MAG na 3GPP Explorer](https://3gpp-explorer.com/glossary/mag/)
