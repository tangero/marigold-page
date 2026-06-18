---
slug: "t-csi"
url: "/mobilnisite/slovnik/t-csi/"
type: "slovnik"
title: "T-CSI – Terminating CAMEL Subscription Information"
date: 2025-01-01
abbr: "T-CSI"
fullName: "Terminating CAMEL Subscription Information"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/t-csi/"
summary: "Soubor dat o účastníkovi uložený v HLR, který definuje logiku služeb CAMEL pro ukončované (příchozí) hovory. Je odeslán GMSC, aby jej instruoval, které služby má vyvolat a kde najít platformu pro říze"
---

T-CSI je soubor dat o účastníkovi uložený v HLR, který definuje logiku služeb CAMEL pro příchozí hovory a instruuje GMSC, které služby má vyvolat.

## Popis

Terminating [CAMEL](/mobilnisite/slovnik/camel/) Subscription Information (T-CSI) je klíčový datový profil přidružený k mobilnímu účastníkovi v registru domovské lokace ([HLR](/mobilnisite/slovnik/hlr/)). Obsahuje parametry nezbytné pro síť, aby mohla vyvolat inteligentní síťové služby založené na CAMEL pro hovory ukončované (tj. příchozí) k tomuto účastníkovi. Když je hovor směrován k účastníkovi, bránový mobilní ústřednový uzel ([GMSC](/mobilnisite/slovnik/gmsc/)) dotazuje HLR, aby získal směrovací informace a data o účastníkovi. Součástí tohoto přenosu dat je i T-CSI, pokud má účastník aktivované služby CAMEL pro ukončované hovory. T-CSI je přenášeno do GMSC prostřednictvím protokolu [MAP](/mobilnisite/slovnik/map/) (Mobile Application Part).

Profil T-CSI zahrnuje několik klíčových polí: adresu prostředí služeb CAMEL ([CSE](/mobilnisite/slovnik/cse/)) nebo bodu řízení služeb ([SCP](/mobilnisite/slovnik/scp/)), který hostuje logiku služby (adresa gsmSCF), seznam spouštěcích detekčních bodů z [T-BCSM](/mobilnisite/slovnik/t-bcsm/), kde je vyžadována interakce, služební klíč identifikující konkrétní služební program k provedení a různé příznaky a parametry pro službu (jako například výchozí zacházení s hovorem). Po přijetí T-CSI podle toho nakonfiguruje GMSC svou logiku zpracování hovoru. Jak příchozí hovor postupuje modelem základního stavu ukončovaného hovoru (T-BCSM), GMSC v určených detekčních bodech pozastaví zpracování a zahájí dialog s gsmSCF pomocí protokolu [CAP](/mobilnisite/slovnik/cap/). gsmSCF následně provede personalizovanou logiku služby účastníka, což může zahrnovat úpravu hovoru, aplikaci účtování nebo implementaci funkcí, jako je přesměrování hovoru nebo jeho filtrování.

T-CSI umožňuje personalizaci služeb na úrovni jednotlivého účastníka. Jeho přítomnost v HLR umožňuje centrální správu služeb a jejich konzistentní aplikaci bez ohledu na to, kde se účastník nachází (roaming) nebo která MSC hovor obsluhuje. Tyto informace jsou klíčové pro zajištění výnosů u předplacených služeb, protože mohou spustit kontrolu kreditu v reálném čase pro příchozí hovory. Podporuje také pokročilé služby dokončování hovorů, jako je inteligentní překlad čísel nebo směrování závislé na čase. Struktura a kódování T-CSI jsou standardizovány napříč vydáními, což zajišťuje zpětnou i dopřednou kompatibilitu, jak se schopnosti CAMEL vyvíjely od fáze 1 do 4.

## K čemu slouží

T-CSI bylo zavedeno, aby umožnilo účastnicky specifické řízení inteligentních služeb pro příchozí hovory v rámci architektury CAMEL. Před CAMEL bylo zavádění vlastního chování pro příchozí hovory (jako personalizované přesměrování hovoru) typicky konfigurací na úrovni celé sítě nebo ústředny a nebylo snadno přizpůsobitelné jednotlivým uživatelům. Cílem CAMEL bylo přinést flexibilitu inteligentní sítě (IN) do GSM. T-CSI poskytuje mechanismus, jak uživatele k těmto službám 'přihlásit'.

Řeší problém, jak informovat navštívenou ústřednu (GMSC) o tom, které služby má vyvolat pro konkrétní příchozí hovor a kde najít logiku těchto služeb. Uložením těchto informací v HLR – centrální databázi účastníků – zajišťuje, že služební profil je vždy dostupný během sestavování hovoru, dokonce i pro účastníky v roamingu. Toto byl klíčový pokrok oproti dřívějším pokusům o přizpůsobení služeb, který operátorům umožnil nabízet diferencované, přidané služby, které mohly být nabízeny jednotlivě, jako je blokování příchozích hovorů pro předplacené uživatele nebo prémiové funkce dokončování hovorů.

## Klíčové vlastnosti

- Uloženo v HLR jako součást profilu účastníka
- Obsahuje adresu funkce řízení služeb (gsmSCF)
- Určuje, které detekční body v T-BCSM mají spustit událost
- Zahrnuje služební klíč pro identifikaci konkrétní služební logiky
- Přenášeno do GMSC přes MAP během sestavování hovoru
- Umožňuje personalizované služby CAMEL pro ukončované hovory

## Související pojmy

- [CAMEL – Customised Applications for Mobile network Enhanced Logic](/mobilnisite/slovnik/camel/)
- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)
- [T-BCSM – Terminating Basic Call State Model](/mobilnisite/slovnik/t-bcsm/)
- [MAP – Mobile Application Protocol](/mobilnisite/slovnik/map/)

## Definující specifikace

- **TR 21.978** (Rel-4) — CAMEL Control of VoIP Services Feasibility Study
- **TS 23.031** (Rel-19) — Fraud Information Gathering System (FIGS) - Stage 2
- **TS 23.035** (Rel-19) — Immediate Service Termination (IST) Stage 2
- **TS 23.078** (Rel-19) — CAMEL Phase 4 Stage 2 Specification
- **TS 32.250** (Rel-19) — Circuit Switched Offline Charging
- **TS 32.272** (Rel-19) — Charging for Push-to-Talk over Cellular (PoC)
- **TS 32.293** (Rel-19) — Proxy Function in Domestic Service Provider

---

📖 **Anglický originál a plná specifikace:** [T-CSI na 3GPP Explorer](https://3gpp-explorer.com/glossary/t-csi/)
