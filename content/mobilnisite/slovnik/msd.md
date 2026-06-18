---
slug: "msd"
url: "/mobilnisite/slovnik/msd/"
type: "slovnik"
title: "MSD – Minimum Set of emergency related Data"
date: 2025-01-01
abbr: "MSD"
fullName: "Minimum Set of emergency related Data"
category: "Services"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/msd/"
summary: "Standardizovaná minimální sada dat, kterou musí být síť schopna získat a poskytnout pro tísňové služby, a to i při selhání běžného ověření účastníka a kontrol předplatného. Zajišťuje dostupnost základ"
---

MSD je standardizovaná minimální sada dat, kterou musí síť získat a poskytnout pro tísňové služby, aby zajistila základní sestavení hovoru a informace o poloze, a to i při selhání běžného ověření.

## Popis

Minimální sada dat souvisejících s tísňovým voláním (MSD) je klíčový koncept 3GPP navržený tak, aby zaručil dostupnost nezbytných informací pro podporu tísňových služeb (např. volání na 112, 911). Je definována jako naprosto minimální soubor dat, který musí být síť schopna získat a využít k založení tísňové relace a poskytnutí pomoci, zejména pro uživatele, kteří nejsou ověřeni, nemají platné předplatné nebo se nacházejí v roamingu mimo domovskou síť. MSD zajišťuje, že regulatorní požadavky na tísňové služby mohou být splněny za prakticky všech okolností.

Z architektonického hlediska se na MSD podílí více síťových entit. Když uživatelské zařízení (UE) zahájí tísňový požadavek, obsluhující síť (navštívená veřejná pozemní mobilní síť - [VPLMN](/mobilnisite/slovnik/vplmn/)) se musí pokusit MSD získat. Tato data mohou být uložena v samotném UE, pokud je to možné, načtena z domovské sítě UE ([HPLMN](/mobilnisite/slovnik/hplmn/)) nebo odvozena z vlastního kontextu sítě. Mezi klíčové zapojené komponenty patří UE, rádiová přístupová síť (RAN), entita správy mobility ([MME](/mobilnisite/slovnik/mme/)) v LTE nebo funkce správy přístupu a mobility ([AMF](/mobilnisite/slovnik/amf/)) v 5GC, centrum polohové brány ([GMLC](/mobilnisite/slovnik/gmlc/)) a tísňové centrum. MSD typicky zahrnuje, ale není omezena na, polohu UE (nebo informace k jejímu určení), zpětné telefonní číslo a identitu obsluhující buňky.

Proces funguje následovně: Po detekci požadavku na tísňovou službu síť obejde běžné kontroly ověření a předplatného. Poté aktivuje procedury ke shromáždění MSD. UE může poskytnout některá data (např. svůj poslední známý odhad polohy, pokud má polohovací schopnosti). Síť použije identifikátor buňky (Cell-ID) nebo pokročilejší metody k určení polohy. Je zřízeno dočasné identifikační číslo nebo síťově přiřazené zpětné telefonní číslo. Tato MSD je následně zpřístupněna místu příjmu tísňových volání ([PSAP](/mobilnisite/slovnik/psap/)) nebo tísňovému centru. Úlohou MSD je naplnit základní princip, že tísňové služby musí být dostupné komukoli a kdykoli. Její specifikace napříč četnými technickými dokumenty (od protokolů jádra sítě po specifikace výkonu rádiové části) zajišťuje interoperabilitu a definuje záložní mechanismy pro situace, kdy nejsou k dispozici úplná data o účastníkovi.

## K čemu slouží

MSD existuje, aby vyřešila zásadní život zachraňující problém: zajistit, aby tísňové služby mohly přijmout hovor a lokalizovat volajícího, i když mobilní systém postrádá běžné přihlašovací údaje účastníka. Před jejím formalizováním mohly sítě odmítat pokusy o tísňové volání od nepředplatitelů nebo nezajistit klíčová data o poloze, což mohlo mít fatální následky. Vznik MSD byl motivován regulatorními a etickými požadavky na univerzální přístup k tísňovým službám.

Řeší omezení tradičního fungování mobilních sítí, které je z velké části založeno na ověřených účastnících se známými profily. V situacích, jako je uživatel bez [SIM](/mobilnisite/slovnik/sim/) karty, s neplatným předplatným nebo roamující uživatel, jehož domovská síť není dosažitelná, má síť stále zákonnou povinnost spojit tísňový hovor. MSD poskytuje standardizovaný záložní rámec. Historický kontext zahrnuje vývoj požadavků na tísňové služby od základní hlasové konektivity (např. GSM fáze 1) k rozšířeným požadavkům na lokalizaci volajícího (E911 v USA, eCall v Evropě), což si vyžádalo robustní, standardizovanou sadu dat.

Vytvoření MSD zajišťuje technologickou shodu s těmito předpisy ve všech sítích založených na 3GPP. Definuje jasný smluvní bod mezi síťovými operátory a úřady o tom, jaké minimální informace budou poskytnuty. Tím se řeší problémy interoperability mezi různými síťovými dodavateli a přes hranice států, což zajišťuje, že telefon od jakéhokoli výrobce na jakékoli kompatibilní síti může poskytnout základní úroveň podpory pro tísňové situace. Je to základní kámen bezpečnosti občanů v mobilních komunikacích.

## Klíčové vlastnosti

- Zajišťuje sestavení tísňového hovoru bez ověření/předplatného
- Zahrnuje minimální požadované informace o poloze volajícího
- Poskytuje zpětné telefonní číslo nebo identifikátor pro tísňové služby
- Standardizována napříč specifikacemi jádra sítě a přístupové sítě
- Podporuje regulatorní požadavky (např. E911, eCall)
- Zahrnuje záložní procedury, když nejsou k dispozici data z domovské sítě

## Související pojmy

- [PSAP – Public Safety Answering Point](/mobilnisite/slovnik/psap/)
- [GMLC – Gateway Mobile Location Center](/mobilnisite/slovnik/gmlc/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 22.967** (Rel-19) — eCall Emergency Data Transmission
- **TS 23.167** (Rel-19) — IMS Emergency Sessions
- **TS 23.216** (Rel-19) — SRVCC Architecture Enhancements
- **TS 23.237** (Rel-19) — IMS Service Continuity (ISC) Stage 2
- **TS 24.008** (Rel-19) — 3GPP TS 24008: Core Network Protocols
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 26.267** (Rel-19) — eCall In-band Modem Specification
- **TS 26.268** (Rel-19) — eCall In-band Modem ANSI-C Code
- **TS 26.269** (Rel-19) — eCall In-band Modem Conformance Testing
- **TR 26.967** (Rel-19) — eCall via CTM Suitability Analysis
- **TR 26.969** (Rel-19) — eCall In-band Modem Performance Characterization
- **TS 29.165** (Rel-19) — Inter-IMS Network to Network Interface (NNI)
- **TS 36.101** (Rel-19) — LTE UE Radio Transmission & Reception Requirements
- **TS 36.833** — 3GPP TR 36.833
- … a dalších 40 specifikací

---

📖 **Anglický originál a plná specifikace:** [MSD na 3GPP Explorer](https://3gpp-explorer.com/glossary/msd/)
