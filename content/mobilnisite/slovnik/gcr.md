---
slug: "gcr"
url: "/mobilnisite/slovnik/gcr/"
type: "slovnik"
title: "GCR – Global Call Reference"
date: 2025-01-01
abbr: "GCR"
fullName: "Global Call Reference"
category: "Identifier"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/gcr/"
summary: "Global Call Reference (GCR) je jedinečný identifikátor přiřazený hovoru nebo relaci napříč více síťovými doménami a administrativními hranicemi. Umožňuje end-to-end korelaci záznamů o účtování, dat sp"
---

GCR je jedinečný identifikátor přiřazený hovoru nebo relaci napříč více síťovými doménami, který umožňuje end-to-end korelaci dat pro účtování, správu chyb a dohled podle zákona.

## Popis

Global Call Reference (GCR) je globálně jedinečný identifikátor používaný v sítích 3GPP k označení konkrétní instance komunikační služby, jako je hlasový hovor, videoschůzka nebo datová relace. Jeho hlavní úlohou je poskytnout korelační klíč, který lze použít k propojení všech záznamů a událostí spojených s touto jedinou komunikační instancí, jak prochází různými síťovými elementy, různými sítěmi operátorů a různými administrativními doménami (např. navštívená a domácí síť). GCR je generován při zřízení hovoru/relace, typicky síťovým elementem, který pro tuto relaci iniciuje proces účtování nebo řízení.

Technicky je GCR strukturován tak, aby zajišťoval globální jedinečnost. Často zahrnuje prvky jako identifikátor síťového operátora (např. PLMN ID), časové razítko a lokálně jedinečné pořadové číslo generované vytvářejícím uzlem. Tento strukturovaný přístup zabraňuje kolizím. GCR je následně šířen v signalizačních zprávách (např. v rámci protokolů Diameter nebo [MAP](/mobilnisite/slovnik/map/)) do všech relevantních síťových funkcí zapojených do hovoru, včetně Call Session Control Functions (CSCFs), Media Gateway Control Functions (MGCFs), účtovacích systémů ([OCS](/mobilnisite/slovnik/ocs/), [OFCS](/mobilnisite/slovnik/ofcs/)) a bran pro dohled podle zákona.

Když jakýkoli síťový uzel pro daný hovor vygeneruje záznam o účtovacích datech ([CDR](/mobilnisite/slovnik/cdr/)) nebo zprávu s informacemi souvisejícími s dohledem ([IRI](/mobilnisite/slovnik/iri/)), je do ní GCR zahrnut. To umožňuje fakturačnímu systému nebo zařízení pro monitorování orgánů činných v trestním řízení sloučit všechny dílčí záznamy z různých uzlů – jako jsou S-CSCF, [MGW](/mobilnisite/slovnik/mgw/) a breakout gateway – do jediného souvislého pohledu na celý hovor. Podobně při správě chyb lze výstrahy nebo měření výkonu z různých segmentů cesty hovoru korelovat pomocí GCR k diagnostice problémů s kvalitou služby end-to-end.

## K čemu slouží

GCR byl vytvořen k řešení problému korelace informací pro jednotlivý hovor, který pokrývá více, potenciálně heterogenních, síťových segmentů a administrativních domén. V raných mobilních sítích a zejména ve scénářích s více operátory / mezi PLMN sítěmi bylo účtování, odstraňování závad a dohled podle zákona obtížné, protože každý síťový element generoval své vlastní lokální záznamy s lokálními identifikátory. Neexistoval standardizovaný způsob, jak tyto záznamy definitivně spojit zpět s toutéž instancí hovoru.

Tento nedostatek korelace vedl k několika problémům: fakturačním sporům mezi operátory ohledně roamingu, obtížím při sestavování úplných záznamů detailů hovoru pro zákaznické faktury, neefektivitě při izolaci chyb přes síťové hranice a složitostem při plnění požadavků na dohled podle zákona, které vyžadují úplný, korelovaný záznam o komunikaci cíle. GCR, zavedený jako standardizovaný koncept, poskytuje společný klíč, který všechny strany souhlasí používat a šířit. Řeší tato omezení tím, že umožňuje jednoznačné přiřazení. Jeho vytvoření bylo motivováno potřebou robustního vypořádání mezi operátory, přesného zajištění služeb end-to-end a dodržování regulačních nařízení pro dohled, čímž se stal základním prvkem pro správu služeb v globálně propojeném mobilním ekosystému.

## Klíčové vlastnosti

- Globálně jedinečný identifikátor pro instanci hovoru/relace
- Používá se jako korelační klíč napříč síťovými doménami
- Obsahuje prvky zajišťující jedinečnost (např. PLMN ID, časové razítko)
- Šířen v signalizačních zprávách řídicí roviny
- Zahrnut v Charging Data Records (CDR) a zprávách pro dohled podle zákona
- Umožňuje end-to-end účtování, odstraňování závad a dodržování předpisů

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.284** (Rel-19) — Local Call Local Switch Stage 2
- **TS 23.796** (Rel-16) — FRMCS Architectural Analysis
- **TS 23.889** (Rel-10) — Local Call Local Switch Core Network Impact Study
- **TS 29.205** (Rel-19) — BICC Protocols for Bearer-Independent CS Core Network
- **TS 32.102** (Rel-19) — Telecom Management Physical Architecture Framework
- **TS 43.020** (Rel-19) — Security Procedures for GSM
- **TS 43.068** (Rel-19) — Voice Group Call Service (VGCS) Stage 2
- **TS 43.069** (Rel-19) — Voice Broadcast Service (VBS) Stage 2
- **TS 48.008** (Rel-19) — BSS-MSC Interface Layer 3 Procedures

---

📖 **Anglický originál a plná specifikace:** [GCR na 3GPP Explorer](https://3gpp-explorer.com/glossary/gcr/)
