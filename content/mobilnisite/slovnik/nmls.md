---
slug: "nmls"
url: "/mobilnisite/slovnik/nmls/"
type: "slovnik"
title: "NMLS – Network Management Layer Service"
date: 2025-01-01
abbr: "NMLS"
fullName: "Network Management Layer Service"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/nmls/"
summary: "Standardizovaná servisní vrstva v rámci architektury správy sítí (NM) 3GPP. Poskytuje společnou sadu služeb a rozhraní pro provoz, správu a údržbu (OAM) telekomunikačních sítí, což umožňuje konzistent"
---

NMLS je standardizovaná servisní vrstva v rámci architektury správy sítí 3GPP, která poskytuje společné služby a rozhraní OAM pro konzistentní a efektivní správu telekomunikačních sítí napříč různými doménami.

## Popis

Služba vrstvy správy sítě (NMLS) je základní architektonická komponenta definovaná v rámci architektury telekomunikační správy ([TM](/mobilnisite/slovnik/tm/)) 3GPP, konkrétně ve vrstvě správy sítě ([NM](/mobilnisite/slovnik/nm/)). Funguje jako mezilehlá servisní vrstva mezi vyšší vrstvou obchodní správy (BML) a nižší vrstvou správy prvků ([EML](/mobilnisite/slovnik/eml/)). NMLS poskytuje standardizovanou sadu služeb, funkcí a severovýchodních rozhraní (NBI), která abstrahují složitost správy jednotlivých síťových prvků a specifických technologických domén.

Architektonicky je NMLS navržena tak, aby nabízela sadu schopností nezávislých na doméně a technologii. Poskytuje společné služby správy, jako je správa poruch, správa výkonnosti, správa konfigurace a správa životního cyklu. Tyto služby jsou zpřístupněny prostřednictvím standardizovaných rozhraní, často založených na protokolech jako [CORBA](/mobilnisite/slovnik/corba/) nebo modernějších webových službách ([SOAP](/mobilnisite/slovnik/soap/)/[XML](/mobilnisite/slovnik/xml/)), což umožňuje externím systémům podpory provozu ([OSS](/mobilnisite/slovnik/oss/)) a systémům podpory obchodu ([BSS](/mobilnisite/slovnik/bss/)) komunikovat se sítí jednotným způsobem. NMLS funguje jako integrační bod, který agreguje a koreluje data z více systémů správy prvků (EMS) nebo síťových funkcí (NF) spravovaných prostřednictvím EML.

V praxi implementace NMLS přijímá a zpracovává informace o správě od podřízených síťových prvků prostřednictvím jižních rozhraní k EML. Provádí funkce jako korelace alarmů (k filtrování a konsolidaci více souvisejících alarmů do jedné smysluplné události), agregace dat o výkonnosti a monitorování úrovně služeb. Tím, že poskytuje jednotný pohled a řídicí rovinu pro síť, zjednodušuje úkoly síťových operátorů. Její role je klíčová pro dosažení správy služeb od konce ke konci, což operátorům umožňuje spravovat sítě s více dodavateli a technologiemi (např. koexistující 2G, 3G, 4G a 5G) prostřednictvím jediné, koherentní vrstvy správy, čímž se snižuje provozní složitost a náklady.

## K čemu slouží

NMLS byla zavedena, aby řešila rostoucí složitost a heterogenitu mobilních sítí, zejména s příchodem 3G a pozdějších technologií. Před její standardizací byla správa sítí často specifická pro dodavatele a doménu, což vedlo k provozním izolacím. Správa sítě, která zahrnovala zařízení od více dodavatelů, vyžadovala samostatné systémy správy pro každého z nich, což zvyšovalo kapitálové a provozní výdaje a komplikovalo poskytování služeb od konce ke konci a izolaci poruch.

Hlavní motivací pro NMLS bylo definovat jasnou, standardizovanou vrstvu v rámci pyramidového modelu TMN (Telecommunications Management Network) přijatého 3GPP. Tato standardizace měla za cíl oddělit obchodní a servisní logiku (v BML) od detailů správy prvků specifických pro technologii (v EML). Poskytnutím společné servisní vrstvy umožňuje vývoj aplikací OSS, které jsou znovupoužitelné napříč různými síťovými technologiemi a implementacemi dodavatelů. Řeší problém integrace a umožňuje operátorům vytvořit flexibilnější a budoucím změnám odolnější ekosystém správy.

Historicky, jak se sítě vyvíjely od technologií s jedním RAN přes multi-RAN až po cloud-nativní 5G Core se síťovými řezy, potřeba robustní, abstrahované vrstvy správy se stala ještě kritičtější. NMLS poskytuje základ pro správu těchto pokročilých konceptů tím, že nabízí služby, které lze jednotně aplikovat napříč fyzickými a virtuálními síťovými funkcemi, a podporuje tak požadavky na automatizaci a orchestraci moderních softwarově definovaných sítí.

## Klíčové vlastnosti

- Standardizovaná severovýchodní rozhraní (NBI) pro integraci s OSS/BSS
- Společné definice služeb správy pro poruchy, konfiguraci, výkonnost a zabezpečení (FCAPS)
- Schopnosti korelace alarmů a analýzy hlavní příčiny
- Agregace dat o výkonnosti a monitorování úrovně služeb
- Vrstva abstrakce technologie a dodavatele
- Podpora správy sítí s více doménami a technologiemi

## Související pojmy

- [OSS – Operations and Supervisory System](/mobilnisite/slovnik/oss/)

## Definující specifikace

- **TS 28.301** (Rel-19) — LSA Controller IRP Requirements
- **TS 28.667** (Rel-19) — RPTA IRP Requirements
- **TS 32.101** (Rel-19) — Management principles and high-level requirements
- **TS 32.855** (Rel-14) — Study on OAM Support for Licensed Shared Access

---

📖 **Anglický originál a plná specifikace:** [NMLS na 3GPP Explorer](https://3gpp-explorer.com/glossary/nmls/)
