---
slug: "imr"
url: "/mobilnisite/slovnik/imr/"
type: "slovnik"
title: "IMR – Interference Measurement Resource"
date: 2025-01-01
abbr: "IMR"
fullName: "Interference Measurement Resource"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/imr/"
summary: "Sada předdefinovaných časově-frekvenčních zdrojů v downlinku, kde uživatelské zařízení (UE) měří úrovně rušení, typicky přijímáním referenčního signálu. Tato měření jsou klíčová pro pokročilé funkce j"
---

IMR je sada předdefinovaných časově-frekvenčních zdrojů v downlinku, kde uživatelské zařízení (UE) měří úrovně rušení, typicky prostřednictvím referenčního signálu, aby umožnilo síťové optimalizační funkce jako CoMP a adaptaci přenosového spojení.

## Popis

Interference Measurement Resource (IMR, zdroj pro měření rušení) je koncept fyzické vrstvy v LTE-Advanced a NR, kde síť konfiguruje specifické zdrojové elementy (RE) v časově-frekvenční mřížce pro uživatelské zařízení (UE) za účelem provedení měření rušení. Tyto zdroje jsou typicky konfigurovány signalizací vyšší vrstvy ([RRC](/mobilnisite/slovnik/rrc/)) jako součást sady pro měření [CSI](/mobilnisite/slovnik/csi/) (informace o stavu kanálu). IMR se skládá ze zdrojů referenčních signálů pro informace o stavu kanálu ([CSI-RS](/mobilnisite/slovnik/csi-rs/)) s nulovým nebo nenulovým výkonem, na kterých UE předpokládá, že není vysílán žádný požadovaný signál z jeho obslužné buňky, což mu umožňuje měřit rušení plus šum od sousedních buněk nebo jiných zdrojů. UE měří přijímaný výkon na těchto konfigurovaných RE a toto měření se používá k výpočtu metrik jako poměr signálu k rušení plus šumu (SINR) nebo k odvození hlášení CSI, včetně indikátoru kvality kanálu ([CQI](/mobilnisite/slovnik/cqi/)), indikátoru předkodovací matice (PMI) a indikátoru pořadí (RI). Ve scénářích koordinovaného vícebodového přenosu (CoMP) může být poskytnuto více konfigurací IMR pro měření rušení od různých hypotetických přenosových bodů nebo hypotéz rušení. gNB (v NR) nebo [eNB](/mobilnisite/slovnik/enb/) (v LTE) používá tato hlášení o rušení k inteligentním rozhodnutím o plánování, výběru vhodných modulačních a kódovacích schémat ([MCS](/mobilnisite/slovnik/mcs/)) a aplikaci pokročilých víceanténních technik, jako je formování svazku a koordinace rušení. Konfigurace zahrnuje parametry jako mapování zdrojů, periodicitu, posun podrámce a identitu pro scramblování. IMR je klíčovým prvkem pro dynamické a přesné povědomí o rušení v hustých a heterogenních sítích.

## K čemu slouží

IMR byl zaveden, aby řešil rostoucí výzvu mezibuněčného rušení v sítích LTE-Advanced a 5G NR, která se stala závažnější s funkcemi jako nasazení heterogenních sítí (HetNet), zhušťování buněk a využívání sdíleného spektra. Tradiční měření rušení v celém pásmu byla nedostatečná pro pokročilé víceanténní a koordinační techniky, které vyžadují přesné znalosti o rušení specifické pro zdroj. IMR poskytuje standardizovaný, konfigurovatelný mechanismus, kterým síť může uživatelským zařízením (UE) instruovat, kde a jak měřit rušení, čímž řeší problém, jak získat přesné odhady rušení pro adaptaci spojení a CoMP. Jeho vytvoření bylo motivováno potřebou zlepšit spektrální účinnost a výkon uživatelů na okraji buňky ve scénářích omezených rušením. Umožněním přesného měření rušení IMR umožňuje síti implementovat sofistikované strategie pro zmírňování rušení, jako je dynamický výběr bodu, společný přenos a potlačování rušení, které byly klíčovými cíli LTE-Advanced od Release 11 a jsou zásadní pro výkonnostní cíle 5G.

## Klíčové vlastnosti

- Konfigurovatelná sada časově-frekvenčních zdrojů pro měření rušení uživatelským zařízením (UE)
- Typicky využívá zdroje referenčních signálů pro informace o stavu kanálu (CSI-RS) s nulovým nebo nenulovým výkonem
- Umožňuje přesné měření rušení plus šumu
- Nezbytný pro výpočet hlášení CSI (CQI, PMI, RI) s ohledem na rušení
- Podporuje více konfigurací pro pokročilé scénáře CoMP
- Konfigurován signalizací RRC s parametry pro periodicitu a mapování zdrojů

## Související pojmy

- [CSI-RS – Channel State Information Reference Signal](/mobilnisite/slovnik/csi-rs/)
- [CQI – Channel Quality Indicator](/mobilnisite/slovnik/cqi/)

## Definující specifikace

- **TS 33.838** (Rel-11) — Study on Protection against Unsolicited Communication for IMS
- **TS 38.522** (Rel-19) — UE Conformance Test Applicability Statement
- **TR 38.802** (Rel-14) — Study on New Radio Access Technology Physical Layer Aspects
- **TR 38.912** (Rel-19) — Study on New Radio Access Technology

---

📖 **Anglický originál a plná specifikace:** [IMR na 3GPP Explorer](https://3gpp-explorer.com/glossary/imr/)
