---
slug: "speechsc"
url: "/mobilnisite/slovnik/speechsc/"
type: "slovnik"
title: "SPEECHSC – Speech service Control"
date: 2025-01-01
abbr: "SPEECHSC"
fullName: "Speech service Control"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/speechsc/"
summary: "Mechanismus řízení služeb definovaný v 3GPP pro správu doplňkových služeb v telefonii s přepojováním okruhů, jako je přesměrování nebo zákaz hovorů. Poskytuje standardizované postupy a protokoly pro s"
---

SPEECHSC je mechanismus řízení služeb podle 3GPP pro správu doplňkových služeb přepojování okruhů v telefonii, jako je například přesměrování hovorů, prostřednictvím standardizovaných síťových procedur.

## Popis

Speech service Control (SPEECHSC) označuje soubor protokolů, procedur a funkčních entit v architektuře 3GPP odpovědných za řízení doplňkových služeb v mobilní síti s přepojováním okruhů. Funguje nad základními postupy pro zřízení a ukončení hovoru a zajišťuje aktivaci, deaktivaci, registraci, vyvolání a dotazování na služby jako Bezpodmínečné přesměrování hovoru ([CFU](/mobilnisite/slovnik/cfu/)), Zákaz hovoru ([CB](/mobilnisite/slovnik/cb/)) nebo Čekání na hovor ([CW](/mobilnisite/slovnik/cw/)). Řídicí logika je rozdělena mezi mobilní stanici ([MS](/mobilnisite/slovnik/ms/)) a síť, primárně v rámci ústředny pro mobilní služby ([MSC](/mobilnisite/slovnik/msc/)) a domovského registru polohy ([HLR](/mobilnisite/slovnik/hlr/)).

Jeho fungování zahrnuje řadu standardizovaných dialogů mezi uživatelským zařízením a sítí. Uživatel typicky aktivuje službu, jako je přesměrování hovoru, odesláním specifické číselné sekvence (např. **21*[DN](/mobilnisite/slovnik/dn/)#) nebo prostřednictvím menu v telefonu. To vyvolá zprávu FACILITY z MS do MSC, která obsahuje požadavek na doplňkovou službu. MSC, často ve spolupráci s HLR (který ukládá profil služeb účastníka), ověří požadavek, zkontroluje konflikty s jinými aktivními službami a aplikuje příslušnou servisní logiku. Výsledek (úspěch nebo selhání) je sdělen zpět do MS. Při vyvolání služby (např. při přesměrování příchozího hovoru) funkce řízení služeb v MSC automaticky provede logiku na základě profilu účastníka a aktuálního stavu sítě.

Klíčovými komponentami v architektuře SPEECHSC jsou entita Řízení hovoru ([CC](/mobilnisite/slovnik/cc/)), entita Doplňkové služby (SS) v MS a síti a protokol MAP (Mobile Application Part) pro komunikaci mezi MSC a HLR. Jeho úlohou je oddělit komplexní servisní logiku od základních přepojovacích funkcí, což umožňuje flexibilní zavádění a správu četných telefonních funkcí. Tento strukturovaný řídicí mechanismus zajišťuje konzistentní chování doplňkových služeb napříč různými síťovými operátory a výrobci telefonů, což je klíčové pro uživatelský zážitek a interoperabilitu.

## K čemu slouží

SPEECHSC byl vytvořen, aby poskytl standardizovaný rámec pro nabízení přidaných funkcí nad rámec prostých bod-bod hlasových hovorů v GSM a následných systémech s přepojováním okruhů. Vyřešil problém proprietární a neinteroperabilní povahy raných implementací doplňkových služeb, která by bránila roamingu a nasazení sítí od více dodavatelů. Vytvořil společný 'jazyk' a postup pro řízení služeb.

Historický kontext je zakořeněn v konceptech inteligentní sítě (IN) ze světa pevné telefonie. 3GPP tyto principy přizpůsobilo pro mobilní prostředí, kde mobilita účastníka přidávala složitost. Specifikace SPEECHSC (jako 3GPP TS 22.977) definují požadavky fáze 1 (popis služby), což motivovalo vytvoření podrobných protokolů fáze 2 a fáze 3. Jeho vznik byl motivován komerčními potřebami: operátoři potřebovali diferencované služby (jako přesměrování hovoru na hlasovou schránku) pro zvýšení příjmů a loajality zákazníků, a standardizovaný přístup snížil náklady na vývoj a čas uvedení na trh jak pro síťové dodavatele, tak pro výrobce telefonů.

Řešil omezení pevného zakódování servisní logiky přímo do softwaru ústředny, což bylo nepružné a ztěžovalo zavádění nových služeb. Definováním řídicí vrstvy SPEECHSC umožnil dynamičtější poskytování a správu služeb. I když jeho relevance poklesla s nástupem IP telefonie založené na IMS, tvořil základní kámen telefonních služeb pro generace 2G a 3G.

## Klíčové vlastnosti

- Standardizované řídicí postupy pro doplňkové služby s přepojováním okruhů
- Podpora služeb jako přesměrování hovoru, zákaz hovoru, čekání na hovor a CLIP/CLIR
- Definuje interakce mezi mobilní stanicí (MS), MSC a HLR
- Pro správu služeb využívá zprávy FACILITY přes rozhraní rádiového přístupu
- Odděluje servisní logiku od základního řízení hovoru pro flexibilitu
- Zajišťuje interoperabilitu služeb pro roamující účastníky

## Definující specifikace

- **TR 22.977** (Rel-19) — Speech Enabled Services and Multimodal Framework

---

📖 **Anglický originál a plná specifikace:** [SPEECHSC na 3GPP Explorer](https://3gpp-explorer.com/glossary/speechsc/)
