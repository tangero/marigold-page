---
slug: "ism"
url: "/mobilnisite/slovnik/ism/"
type: "slovnik"
title: "ISM – Industrial, Scientific and Medical Band"
date: 2025-01-01
abbr: "ISM"
fullName: "Industrial, Scientific and Medical Band"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ism/"
summary: "Pásmo pro průmysl, vědu a lékařství (Industrial, Scientific and Medical - ISM) označuje rádiové frekvenční spektrum mezinárodně vyhrazené pro netelekomunikační využití, jako je průmyslové ohřev, lékař"
---

ISM je rádiové frekvenční pásmo mezinárodně vyhrazené pro netelekomunikační využití, které mohou technologie 3GPP, jako je LTE-LAA a NR-U, využívat pro provoz bez licence.

## Popis

Pásma pro průmysl, vědu a lékařství (Industrial, Scientific and Medical - ISM) jsou části rádiového frekvenčního spektra mezinárodně vyhrazené v Předpisech pro rádiovou komunikaci [ITU](/mobilnisite/slovnik/itu/) pro použití zařízeními, která generují rádiovou energii pro nekomunikační účely. Mezi běžné aplikace patří mikrovlnné trouby (2,45 GHz), průmyslové ohřevy, lékařské diatermické přístroje a rádiová identifikace ([RFID](/mobilnisite/slovnik/rfid/)). Klíčové je, že tato pásma jsou často dostupná pro provoz bez licence (nes licencovaný) za určitých regulací, jako jsou nízké výkonové limity a dodržování protokolů etikety, jako je Naslouchej-před-vysíláním (Listen-Before-Talk - [LBT](/mobilnisite/slovnik/lbt/)).

V rámci ekosystému 3GPP mají pásma ISM, zejména rozsahy 2,4 GHz a 5 GHz, obrovský význam pro umožnění provozu celulárních technologií v nelicencovaném spektru. Toho je dosaženo prostřednictvím standardů, jako je Přístup s licenční podporou (License Assisted Access - [LAA](/mobilnisite/slovnik/laa/)), LTE v nelicencovaném spektru (LTE-U), MulteFire a NR v nelicencovaném spektru ([NR-U](/mobilnisite/slovnik/nr-u/)). Tyto technologie umožňují základnovým stanicím a uživatelským zařízením LTE a 5G NR vysílat a přijímat data v pásmech ISM, typicky ve spojení s kotvícím nosičem v licencovaném spektru (pro LAA) nebo v samostatném režimu (pro MulteFire/NR-U).

Provoz v pásmech ISM vyžaduje specifické adaptace fyzické vrstvy a řízení přístupu k médiu pro spravedlivé koexistenci se zavedenými systémy, jako je Wi-Fi. Specifikace 3GPP definují podrobné mechanismy pro přístup ke kanálu, primárně založené na LBT, kde zařízení před vysíláním detekuje energii od jiných uživatelů na kanálu. To je vyžadováno v regionech, jako je Evropa a Japonsko. Rámování fyzické vrstvy a referenční signály jsou také navrženy tak, aby byly robustní ve sdíleném a potenciálně šumivém prostředí ISM. Klíčové specifikace, jako jsou 36.331, 38.805 a 38.807, podrobně popisují procedury řízení rádiových zdrojů a fyzické vrstvy pro provoz v těchto pásmech, což zajišťuje, že přístup 3GPP bez licence dobře koexistuje s jinými technologiemi a splňuje regionální regulační požadavky.

## K čemu slouží

Primárním účelem využití pásem ISM v rámci 3GPP je získat přístup k velkému množství dalšího rádiového spektra bez nákladů a administrativní zátěže spojené s licenčními aukcemi. Licencované spektrum je vzácný a drahý zdroj, zatímco pásma ISM nabízejí široké šířky pásma (zejména kolem 5 GHz), které lze využít ke zvýšení kapacity, zvláště pro hustá městská nasazení a vnitřní pokrytí. Tím se řeší neustále rostoucí poptávka po kapacitě mobilních dat.

Historicky dominoval nelicencovanému prostoru Wi-Fi. Vstup 3GPP do pásem ISM, který vážně začal s LTE-U a [LAA](/mobilnisite/slovnik/laa/) v Rel-13, byl motivován snahou přinést do nelicencovaného spektra vynikající mobilitu, zabezpečení a bezproblémovou integraci celulárních sítí. Řešil problém odlehčování provozu z přetížených licencovaných nosičů a cílil poskytnout koordinovanější a efektivnější využití nelicencovaného spektra ve srovnání s distribuovanou koordinací Wi-Fi. Dále pro nové vertikály, jako je Průmysl 4.0 a privátní sítě, nabízejí technologie jako [NR-U](/mobilnisite/slovnik/nr-u/) provozující se v pásmech ISM kvalitu služeb na úrovni licencovaného spektra v lokálně kontrolovaném spektru, což bylo omezení čistě Wi-Fi založených průmyslových sítí.

## Klíčové vlastnosti

- Umožňuje provoz technologií 3GPP bez licence (LAA, NR-U, MulteFire)
- Poskytuje přístup k dalšímu širokopásmovému spektru (např. pásmo 5 GHz) pro zvýšení kapacity
- Ukládá mechanismy koexistence, jako je Naslouchej-před-vysíláním (LBT), pro spravedlivé sdílení spektra
- Podporuje jak doplňkový downlink, tak i agregaci nosičů pro uplink/downlink s licencovanými kotvami
- Umožňuje samostatný celulární provoz v nelicencovaném spektru pro privátní sítě
- Podléhá regionálním regulačním limitům výkonu a emisí

## Definující specifikace

- **TS 26.253** (Rel-19) — IVAS Codec Algorithmic Description
- **TS 26.254** (Rel-19) — IVAS Rendering Functions Specification
- **TS 26.258** (Rel-19) — IVAS Codec Floating-Point C Code Specification
- **TS 26.260** (Rel-19) — Immersive Audio Objective Test Methods
- **TS 26.261** (Rel-19) — Electro-acoustic specs for immersive terminals
- **TR 26.865** (Rel-18) — Technical Report
- **TR 26.996** (Rel-19) — ISAR Split Rendering Audio Characterization
- **TR 26.997** (Rel-19) — IVAS Codec Specification
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification
- **TR 36.791** (Rel-16) — E-UTRA 2.4 GHz TDD Band for US
- **TS 37.718** — 3GPP TR 37.718
- **TS 37.719** (Rel-19) — 3GPP TR 37.719: Dual Connectivity Band Combinations
- **TS 37.863** — 3GPP TR 37.863
- **TR 38.805** (Rel-14) — Study on New Radio Access Technology; 60 GHz unlicensed spectrum
- … a dalších 2 specifikací

---

📖 **Anglický originál a plná specifikace:** [ISM na 3GPP Explorer](https://3gpp-explorer.com/glossary/ism/)
