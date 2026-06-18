---
slug: "si-rnti"
url: "/mobilnisite/slovnik/si-rnti/"
type: "slovnik"
title: "SI-RNTI – System Information Radio Network Temporary Identifier"
date: 2025-01-01
abbr: "SI-RNTI"
fullName: "System Information Radio Network Temporary Identifier"
category: "Identifier"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/si-rnti/"
summary: "Specifický RNTI používaný v LTE a NR pro zakódování a identifikaci přenosů PDCCH, které plánují bloky systémových informací (SIBs). Zajišťuje, aby všechna UE v buňce mohla správně přijmout a dekódovat"
---

SI-RNTI je specifický Radio Network Temporary Identifier používaný v LTE a NR pro zakódování a identifikaci přenosů PDCCH, které plánují vysílání bloků systémových informací (System Information Blocks) pro všechna UE v buňce.

## Popis

System Information [RNTI](/mobilnisite/slovnik/rnti/) (SI-RNTI) je pevný, předdefinovaný Radio Network Temporary Identifier používaný v downlinkovém řídicím kanálu přístupových technologií LTE ([E-UTRA](/mobilnisite/slovnik/e-utra/)) a NR (New Radio). Jeho primární funkcí je zakódovat bity cyklického redundantního součtu ([CRC](/mobilnisite/slovnik/crc/)) zpráv downlink control information ([DCI](/mobilnisite/slovnik/dci/)) přenášených na Physical Downlink Control Channel ([PDCCH](/mobilnisite/slovnik/pdcch/)). Tyto specifické zprávy DCI plánují prostředky Physical Downlink Shared Channel ([PDSCH](/mobilnisite/slovnik/pdsch/)), které nesou bloky systémových informací (SIBs). Použitím pevné, všeobecně známé hodnoty (0xFFFF v hexadecimální soustavě pro LTE, 0xFFFF pro NR) umožňuje SI-RNTI každému uživatelskému zařízení (UE) v buňce, bez ohledu na jeho stav spojení (idle nebo connected), monitorovat PDCCH pro tyto příkazy plánující systémové informace.

Operačně, když základnová stanice (eNodeB v LTE, gNB v NR) potřebuje vysílat nebo aktualizovat [SIB](/mobilnisite/slovnik/sib/), odešle na PDCCH formát DCI 1A (v LTE) nebo formát DCI 1_0 s SI-RNTI (v NR). UE nepřetržitě monitoruje common search space PDCCH a pokouší se dekódovat zprávy DCI pomocí sady známých RNTI, včetně SI-RNTI. Když UE úspěšně dekóduje DCI použitím SI-RNTI k dekódování CRC, ví, že toto DCI obsahuje plánovací informace (např. alokaci resource blocks, modulation and coding scheme) pro přenos PDSCH. UE následně dekóduje indikovaný prostředek PDSCH, který obsahuje vlastní data SIB.

SI-RNTI je klíčový pro broadcast mechanismus. Na rozdíl od UE-specifických RNTI, jako je [C-RNTI](/mobilnisite/slovnik/c-rnti/), které jsou přiděleny během random access a používají se pro vyhrazený provoz, je SI-RNTI společný pro všechna UE. To zajišťuje, že kritické systémové informace – jako parametry přístupu k buňce, seznamy sousedních buněk a společné konfigurace rádiových prostředků – jsou dostupné jakémukoli UE, které se pokouší vybrat, připojit se k nebo přistupovat k buňce. Hodnota je standardizovaná, takže UE od jakéhokoli výrobce mohou okamžitě začít naslouchat systémovým informacím po zapnutí v nové síti.

V rámci celkových stavů radio resource control (RRC) je SI-RNTI obzvláště důležitý pro UE ve stavech RRC_IDLE a RRC_INACTIVE. Tato UE nemají vyhrazené spojení a spoléhají se zcela na broadcast kanály pro převýběr buňky a aktualizace přístupových parametrů. gNB může také použít SI-RNTI k plánování periodických přenosů SIB nebo k signalizaci změn systémových informací prostřednictvím paging mechanismu nebo přímé indikace (SystemInfoModification v NR). SI-RNTI je tedy ústředním prvkem broadcast služby buňky, který umožňuje efektivní a spolehlivé distribuce základních konfiguračních dat celé populaci UE v její pokryté oblasti.

## K čemu slouží

SI-RNTI byl zaveden s LTE (Rel-8) k vyřešení problému efektivního a spolehlivého vysílání základních systémových konfiguračních informací všem uživatelským zařízením v buňce. Předchozí buněčné systémy měly mechanismy pro vysílání systémových informací, ale integrace s dynamickým, paketově plánovaným sdíleným kanálem jako je PDSCH vyžadovala robustní metodu řídicí signalizace. Účelem bylo vytvořit standardizovaný, pevný identifikátor, který jednoznačně označuje zprávy řídicího kanálu určené pro plánování vysílaných systémových informací, a odlišuje je tak od zpráv určených pro konkrétní uživatele nebo jiné společné účely.

Řeší klíčovou výzvu počátečního přístupu k buňce a jejího objevení. Když se UE zapne nebo vstoupí do nové oblasti, nemá žádnou předchozí znalost o buňce ani přidělenou identitu. Potřebuje získat základní parametry jako šířku pásma, konfiguraci PHICH a přístupová omezení, aby vůbec mohla zahájit proceduru random access. SI-RNTI poskytuje UE prostředek k nalezení těchto informací. Neustálým monitorováním tohoto specifického RNTI může UE dekódovat plán pro SIBs bez nutnosti jakékoli předchozí konfigurace ze sítě, což by bylo začarovaným kruhem.

Dále SI-RNTI umožňuje síťovou efektivitu. Namísto nepřetržitého vysílání SIBs na pevném, rigidním plánu na broadcast kanálu může síť použít framework PDCCH/PDSCH k jejich dynamickému plánování. To umožňuje flexibilitu v alokaci prostředků – systémové informace mohou být přenášeny méně často v podmínkách nízkého provozu a robustněji (např. s větší redundancí), když je to potřeba. Pevná hodnota SI-RNTI zajišťuje, že tento zisk efektivity nepřichází na úkor interoperability; je to základní stavební kánek rozhraní LTE a NR, který garantuje, že všechna kompatibilní zařízení se chovají konzistentně při získávání systémových informací, což je předpoklad pro provoz sítě a mobilitu.

## Klíčové vlastnosti

- Pevná, standardizovaná hodnota (0xFFFF) známá všem UE a základnovým stanicím.
- Používá se k zakódování CRC zpráv DCI plánujících bloky systémových informací (SIBs).
- Monitorováno UE v common search space PDCCH/PDCCH.
- Nezbytné pro UE ve stavech RRC_IDLE, RRC_INACTIVE a během počátečního výběru buňky.
- Umožňuje dynamické plánování vysílaných systémových informací na sdíleném kanálu (PDSCH).
- Odlišuje plánování systémových informací od jiných společných a UE-specifických zpráv.

## Související pojmy

- [RNTI – Radio Network Temporary Identifier](/mobilnisite/slovnik/rnti/)
- [PDCCH – Physical Downlink Control Channel](/mobilnisite/slovnik/pdcch/)
- [DCI – Downlink Control Information](/mobilnisite/slovnik/dci/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.321** (Rel-19) — E-UTRA MAC Protocol Specification
- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification
- **TS 38.300** (Rel-19) — NG-RAN Overall Description

---

📖 **Anglický originál a plná specifikace:** [SI-RNTI na 3GPP Explorer](https://3gpp-explorer.com/glossary/si-rnti/)
