---
slug: "eif"
url: "/mobilnisite/slovnik/eif/"
type: "slovnik"
title: "EIF – Energy Information Function"
date: 2026-01-01
abbr: "EIF"
fullName: "Energy Information Function"
category: "Management"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/eif/"
summary: "Funkce pro energetické informace (EIF) je síťová funkce 3GPP zavedená ve Release 19 pro správu energetické účinnosti. Shromažďuje, zpracovává a poskytuje energeticky relevantní data ze síťových prvků"
---

EIF je síťová funkce 3GPP Release 19, která shromažďuje, zpracovává a poskytuje energeticky relevantní data ze síťových prvků za účelem podpory analytiky pro monitorování a snižování energetické spotřeby sítě.

## Popis

Funkce pro energetické informace (EIF) je řídicí funkce definovaná v rámci standardů 3GPP, která je specificky navržena pro řešení rostoucí potřeby energetické účinnosti v mobilních sítích. Funguje jako centralizovaná nebo distribuovaná entita, která komunikuje s různými síťovými funkcemi ([NF](/mobilnisite/slovnik/nf/)) a síťovými prvky ([NE](/mobilnisite/slovnik/ne/)) napříč rádiovým přístupovým sítí (RAN) a jádrem sítě (CN). Jejím hlavním úkolem je shromažďovat nezpracované metriky energetické spotřeby, jako je například využití energie ze základnových stanic (gNB, [eNB](/mobilnisite/slovnik/enb/)), serverů jádra sítě a dalších komponent infrastruktury. EIF tato data zpracovává, což může zahrnovat časové vzorce, korelace se zátěží a faktory prostředí, za účelem generování strukturovaných reportů o energetických informacích.

EIF funguje tak, že zpřístupňuje standardizovaná rozhraní založená na službách ([SBI](/mobilnisite/slovnik/sbi/)), jak jsou definována ve specifikacích 3GPP jako 29.508 a 29.566, což umožňuje ostatním autorizovaným síťovým funkcím, jako je Funkce pro analýzu síťových dat ([NWDAF](/mobilnisite/slovnik/nwdaf/)) nebo systémy pro provoz, správu a údržbu ([OAM](/mobilnisite/slovnik/oam/)), vyžádat si energetická data. Může shromažďovat data pomocí push nebo pull mechanismů, často agreguje informace od agentů pro správu energie nižší úrovně vestavěných v síťovém zařízení. Mezi klíčové vnitřní komponenty patří moduly pro sběr dat, zpracovatelské jednotky pro normalizaci a korelaci, úložiště pro historická data a body pro vynucování politik, které zajišťují ochranu soukromí dat a řízení přístupu podle specifikace 33.766.

V celkové síťové architektuře hraje EIF klíčovou roli v udržitelnosti a strategiích operátorů pro snižování provozních nákladů ([OPEX](/mobilnisite/slovnik/opex/)). Poskytováním detailních, reálných a historických energetických přehledů podporuje pokročilou analytiku pro predikci energetické poptávky, identifikaci neefektivit a automatizaci úsporných opatření. Například může zásobovat daty modely [AI/ML](/mobilnisite/slovnik/ai-ml/), které optimalizují topologii sítě nebo režimy spánku buněk na základě provozní zátěže. Její integrace s řídicími systémy umožňuje automatizaci v uzavřené smyčce, kde jsou energetické politiky dynamicky upravovány, což přímo přispívá ke snížení uhlíkové stopy sítě a plnění ekologických regulačních požadavků.

## K čemu slouží

EIF byla vytvořena pro řešení rostoucích nákladů na energii a dopadů na životní prostředí rychle se rozšiřujících sítí 5G a budoucích sítí 6G. Před její standardizací bylo řízení energie často proprietární, fragmentované a postrádalo jednotný rámec pro sběr a výměnu energetických dat napříč nasazeními sítí s více dodavateli. To ztěžovalo holistickou optimalizaci energie a omezovalo schopnost implementovat automatizované, síťově široké politiky úspory energie. Telekomunikační průmysl čelil rostoucímu tlaku regulátorů a společnosti na snížení emisí skleníkových plynů, což si vyžádalo standardizovaný přístup k měření a řízení energetické spotřeby.

Historicky byly funkce energetické účinnosti, jako jsou režimy spánku základnových stanic nebo vypínání nosných, spravovány odděleně v rámci domény RAN bez komplexní viditelnosti napříč doménami. EIF to řeší tím, že poskytuje centralizovanou, standardizovanou funkci, která propojuje energetické informace z domén RAN i jádra sítě. Její vznik byl motivován potřebou podporovat vznikající případy užití, jako je síťové dělení energie (network energy slicing), kde lze přidělovat energetické rozpočty na jednotlivé služební řezy, a umožnit pokročilou analytiku pro prediktivní správu energie. Nabídkou společného datového modelu a rozhraní EIF usnadňuje interoperabilitu, což operátorům umožňuje nasazovat nejlepší dostupná řešení pro správu energie a integrovat se s externími energetickými sítěmi nebo obnovitelnými zdroji energie pro chytřejší využití energie.

## Klíčové vlastnosti

- Standardizovaný sběr dat o energetické spotřebě od síťových prvků RAN a jádra sítě od více dodavatelů
- Rozhraní založená na službách (např. Nnrf, Nnef) pro zabezpečené zpřístupnění energetických dat konzumentům (NF) a systémům OAM
- Podpora agregace, zpracování a reportování reálných a historických energetických dat
- Řízení přístupu založené na politikách a bezpečnostní mechanismy pro energetické informace podle specifikace 33.766
- Integrace s analytickými funkcemi (např. NWDAF) pro umožnění optimalizace energie řízené AI/ML
- Schopnost podporovat klíčové ukazatele výkonnosti (KPI) energetické účinnosti a reportování udržitelnosti

## Související pojmy

- [NWDAF – Network Data Analytics Function](/mobilnisite/slovnik/nwdaf/)
- [OAM – Operations, Administration, and Maintenance](/mobilnisite/slovnik/oam/)
- [SBI – Service Based Interfaces](/mobilnisite/slovnik/sbi/)

## Definující specifikace

- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TR 26.942** (Rel-19) — Study on Media Energy Consumption Exposure & Evaluation
- **TS 29.508** (Rel-19) — 5G Session Management Event Exposure Service
- **TS 29.566** (Rel-19) — Neif SBI for Energy Information Function in 5G
- **TS 33.766** (Rel-19) — Security Study for 5G Energy Savings

---

📖 **Anglický originál a plná specifikace:** [EIF na 3GPP Explorer](https://3gpp-explorer.com/glossary/eif/)
