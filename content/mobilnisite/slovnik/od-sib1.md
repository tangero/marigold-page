---
slug: "od-sib1"
url: "/mobilnisite/slovnik/od-sib1/"
type: "slovnik"
title: "OD-SIB1 – On-Demand System Information Block 1"
date: 2025-01-01
abbr: "OD-SIB1"
fullName: "On-Demand System Information Block 1"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/od-sib1/"
summary: "Funkce 5G NR, kde síť vysílá SIB1, obsahující základní informace pro počáteční přístup k buňce, pouze na výslovnou žádost od UE. Tím se snižuje neustálá režie vysílání, šetří se energie a spektrální z"
---

OD-SIB1 je funkce 5G NR, kde síť vysílá základní systémový informační blok 1 (SIB1) pouze na žádost UE, čímž se snižuje neustálá režie vysílání.

## Popis

On-Demand SIB1 (OD-SIB1) je funkce 5G New Radio (NR) zavedená ve specifikaci 3GPP Release 19, definovaná napříč protokolovou sadou RAN (TS 38.300, 38.331 atd.). Systémový informační blok 1 (SIB1) je nejkritičtější systémový informační blok, obsahující parametry nezbytné pro to, aby uživatelské zařízení (UE) mohlo určit, zda má povolen přístup k buňce (stav blokování buňky, rezervace buňky), a plánovací informace pro ostatní SIBy. Tradičně gNB vysílá SIB1 periodicky, což nepřetržitě spotřebovává zdroje rádiového rozhraní na downlinku.

OD-SIB1 tento model mění. V tomto režimu gNB ve výchozím stavu SIB1 nevysílá. Místo toho vysílá minimální systémovou informaci (SI), zahrnující hlavní informační blok ([MIB](/mobilnisite/slovnik/mib/)) a případně plánovací informaci pro SIB1, což signalizuje, že SIB1 je k dispozici na vyžádání. UE, které potřebuje SIB1 – například během počátečního výběru buňky po zapnutí nebo při vstupu do nové sledovací oblasti – jej musí výslovně požádat. Tato žádost se provádí prostřednictvím procedury náhodného přístupu (RACH). UE odešle preambuli na fyzickém kanálu pro náhodný přístup (PRACH) a v následné zprávě 2 (Random Access Response, RAR) gNB zahrne povolení pro uplink. UE pak použije toto povolení k odeslání vyhrazené [RRC](/mobilnisite/slovnik/rrc/) zprávy (např. RRCSystemInfoRequest) k vyžádání SIB1. Po přijetí této platné žádosti gNB následně vysílá SIB1 po nakonfigurovanou dobu, což umožní této UE i jakýmkoli dalším UE v oblasti si jej získat.

Architektura zahrnuje koordinaci napříč vrstvami PHY, [MAC](/mobilnisite/slovnik/mac/) a RRC. MIB, vysílaný přes fyzický vysílací kanál (PBCH), nese příznak (např. si-BroadcastStatus), který UE informuje o stavu dostupnosti na vyžádání. RRC vrstva v UE řídí logiku pro spuštění žádosti na základě své potřeby SIB1. MAC vrstva gNB naplánuje RAR s povolením pro UL a jeho RRC vrstva spustí následné vysílání SIB1. Tento mechanismus významně snižuje průměrnou režii vysílání systémových informací, zejména v malých buňkách, indoorových buňkách nebo buňkách obsluhujících převážně UE v připojeném stavu, kde jsou události počátečního přístupu vzácné. Je klíčovým prvkem pro energeticky efektivní provoz sítě, v souladu s cíli 5G v oblasti udržitelnosti a podpory masivního IoT.

## K čemu slouží

OD-SIB1 byl vytvořen, aby řešil neefektivitu neustálého vysílání systémových informací v 5G sítích, zejména pro scénáře nasazení, kde je nepřetržité vysílání plýtváním. V tradičních sítích se SIB1 vysílá každých 80 ms bez ohledu na to, zda jej nějaké UE potřebuje. V scénářích s nízkým provozem – jako je malá buňka v noci, neutrální hostitelská síť v budově po pracovní době nebo síťový výsek věnovaný řídce rozmístěným IoT senzorům – to představuje neustálou zátěž pro spotřebu energie gNB a trvalé využívání zdrojů rádiového rozhraní na downlinku (energie a spektrum) s malým nebo žádným přínosem.

Motivace vychází z pilířů návrhu 5G: rozšířeného mobilního širokopásmového připojení, masivního IoT a ultra-spolehlivé komunikace s nízkou latencí, které všechny vyžadují efektivnější využití zdrojů. Zaměření Release 19 na 'Úsporu energie sítě' poskytlo přímý kontext. OD-SIB1 přímo snižuje spotřebu energie gNB tím, že umožňuje vysílači vypnout kanál pro vysílání SIB1, když není potřeba. Také uvolňuje bloky fyzických zdrojů (PRB) pro přenos uživatelských dat nebo jiné účely. Tím se řeší omezení modelu 'vždy zapnutého' vysílání, což byl odkaz z předchozích generací, kde primárními omezeními byla složitost UE a výdrž baterie, nikoli energetická účinnost sítě. Díky tomu, že získání SIB1 je spouštěný proces na vyžádání, mohou sítě dosáhnout významných úspor provozních nákladů a sníženého dopadu na životní prostředí, zejména s tím, jak se nasazení 5G stává hustší.

## Klíčové vlastnosti

- Vysílání SIB1 je spuštěno pouze výslovnou žádostí UE přes RACH.
- Snižuje neustálou režii vysílání na downlinku, šetří energii gNB a spektrální zdroje.
- Mechanismus žádosti UE využívá vyhrazené RRC signalizace přes proceduru náhodného přístupu s možností kolize.
- MIB indikuje UE stav dostupnosti SIB1 na vyžádání.
- gNB vysílá SIB1 po omezenou dobu po přijetí platné žádosti.
- Zvláště výhodné pro buňky s nízkým provozem, indoorová nasazení a síťové stavy pro úsporu energie.

## Související pojmy

- [MIB – Management Information Base](/mobilnisite/slovnik/mib/)

## Definující specifikace

- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TS 38.304** (Rel-19) — UE RRC_IDLE and RRC_INACTIVE Procedures
- **TS 38.331** (Rel-19) — NR Radio Resource Control (RRC) Protocol Specification
- **TS 38.401** (Rel-19) — NG-RAN Architecture Specification
- **TS 38.423** (Rel-19) — Xn Application Protocol (XnAP) specification
- **TS 38.473** (Rel-19) — 5G F1 Application Protocol (F1AP)

---

📖 **Anglický originál a plná specifikace:** [OD-SIB1 na 3GPP Explorer](https://3gpp-explorer.com/glossary/od-sib1/)
