---
slug: "mmss"
url: "/mobilnisite/slovnik/mmss/"
type: "slovnik"
title: "MMSS – Maritime Mobile Satellite Service"
date: 2025-01-01
abbr: "MMSS"
fullName: "Maritime Mobile Satellite Service"
category: "Services"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/mmss/"
summary: "Maritime Mobile Satellite Service (MMSS) označuje satelitní komunikační služby poskytující konektivitu lodím a jiným plavidlům na moři. V rámci 3GPP zahrnuje integraci satelitního přístupu s pozemními"
---

MMSS je satelitní komunikační služba, která poskytuje konektivitu lodím na moři prostřednictvím integrace satelitního přístupu s pozemními mobilními sítěmi pro plynulé pokrytí námořních oblastí.

## Popis

Maritime Mobile Satellite Service (MMSS) zahrnuje komunikační služby poskytované prostřednictvím satelitů mobilním stanicím umístěným na lodích a jiných námořních plavidlech. V rámci 3GPP je MMSS studována a standardizována, aby umožnila využití technologií definovaných 3GPP přes satelitní spoje pro námořní uživatele. To zahrnuje rozšíření pokrytí pozemní mobilní sítě do námořních oblastí prostřednictvím satelitních přístupových sítí, což umožňuje uživatelskému zařízení (UE) na lodích se připojit, jako by se nacházelo v oblasti pokryté pozemní buňkou. Specifikace 3GPP, zejména od Release 15 v kontextu 5G, zkoumají, jak mohou satelity fungovat jako nepozemské sítě ([NTN](/mobilnisite/slovnik/ntn/)) pro zajištění pokrytí pro námořní mobilitu.

Architektura pro integraci MMSS typicky zahrnuje satelit (např. na geostacionární oběžné dráze - [GEO](/mobilnisite/slovnik/geo/) nebo na nízké oběžné dráze - [LEO](/mobilnisite/slovnik/leo/)), který komunikuje s satelitním rádiovým rozhraním na plavidle. Satelitní spoj je napojen na pozemní bránovou stanici (Gateway Earth Station), která následně propojuje s jádrovou sítí 3GPP (např. 5GC nebo EPC). Z pohledu jádrové sítě je satelitní přístup považován za další typ rádiového přístupu, podobně jako pozemní gNB nebo [eNB](/mobilnisite/slovnik/enb/), i když s určitými úpravami pro dlouhá zpoždění a proměnlivé podmínky spoje. Mezi klíčové technické výzvy, které se řeší, patří zpracování dlouhých prodlev šíření (zejména u satelitů GEO), Dopplerova jevu způsobeného pohybem satelitu a plavidla a přerušované konektivity.

Klíčové komponenty zahrnují námořní UE (které může být specializovaným terminálem nebo standardním UE se satelitní schopností), satelitní užitečné zatížení (payload), bránu (Gateway) a jádrovou síť 3GPP s podporou pro MMSS. Služba umožňuje řadu typů komunikace: kritické bezpečnostní služby (např. tísňové signalizace prostřednictvím integrace s GMDSS), provozní komunikaci pro správu lodí a služby pro cestující jako hlasové služby a širokopásmová data. Práce v 3GPP zahrnuje definici nových rádiových protokolů, procedur správy mobility pro přesun mezi satelitními paprsky a pozemními buňkami a mechanismů QoS vhodných pro námořní satelitní kanál.

## K čemu slouží

Standardizace Maritime Mobile Satellite Service (MMSS) v rámci 3GPP je motivována potřebou poskytovat spolehlivou globální komunikaci pro námořní průmysl, který operuje mimo dosah pozemních mobilních sítí. Historicky námořní komunikace spoléhala na specializované proprietární satelitní systémy (např. Inmarsat, Iridium), které byly často drahé a nabízely omezenou šířku pásma nebo interoperabilitu s pozemními mobilními službami. Integrace satelitního přístupu do ekosystému 3GPP si klade za cíl vytvořit jednotný, nákladově efektivní a plynulý komunikační rámec pro plavidla.

MMSS řeší kritické problémy bezpečnosti života na moři, vyžadující spolehlivou tísňovou a bezpečnostní komunikaci podle požadavků Mezinárodní námořní organizace (IMO) a Globálního námořního systému tísňového a bezpečnostního spojení (GMDSS). Dále podporuje rostoucí poptávku po provozní efektivitě (např. správa flotily, navigační data) a konektivitě pro cestující (např. přístup k internetu pro posádku a cestující) na komerčních a rekreačních plavidlech. Využitím standardů 3GPP umožňuje MMSS dosáhnout úspor z rozsahu použitím komerčně dostupných komponent, podporuje inovace prostřednictvím konkurenčního ekosystému a připravuje cestu pro konvergenci pozemských a nepozemských sítí v éře 5G a dalších generací.

## Klíčové vlastnosti

- Poskytuje mobilní komunikační pokrytí pro lodě a námořní plavidla mimo přímou viditelnost prostřednictvím satelitních spojů
- Integruje se s jádrovými sítěmi 3GPP (5GC/EPC) za účelem zajištění plynulé kontinuity služeb mezi pozemním a satelitním přístupem
- Podporuje kritické námořní bezpečnostní služby, včetně požadavků na integraci s GMDSS
- Přizpůsobuje rádiové protokoly 3GPP pro zvládání dlouhých prodlev šíření, Dopplerova jevu a přerušované konektivity charakteristické pro satelitní kanály
- Umožňuje škálu služeb od IoT monitorování s nízkou šířkou pásma po vysokokapacitní širokopásmové služby pro cestující
- Definuje správu mobility pro plavidla pohybující se mezi satelitními paprsky a potenciálními pozemními pobřežními buňkami

## Definující specifikace

- **TS 31.102** (Rel-19) — USIM Application Specification
- **TR 38.820** (Rel-16) — NR; 7-24 GHz Frequency Range Study

---

📖 **Anglický originál a plná specifikace:** [MMSS na 3GPP Explorer](https://3gpp-explorer.com/glossary/mmss/)
