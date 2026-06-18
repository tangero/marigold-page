---
slug: "cfra"
url: "/mobilnisite/slovnik/cfra/"
type: "slovnik"
title: "CFRA – Contention Free Random Access"
date: 2025-01-01
abbr: "CFRA"
fullName: "Contention Free Random Access"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/cfra/"
summary: "CFRA je procedura náhodného přístupu v 5G NR, při které gNB předem přidělí vyhrazené prostředky preambule konkrétnímu UE, čímž eliminuje kolizi. Tím se snižuje latence a zvyšuje spolehlivost časově kr"
---

CFRA je procedura náhodného přístupu v 5G, při které síť předem přidělí vyhrazený preambuli konkrétnímu UE, aby se eliminovala kolize, čímž se snižuje latence pro kritické operace, jako je předávání spojení (handover).

## Popis

Contention Free Random Access (CFRA) je specializovaná procedura náhodného přístupu definovaná ve standardech 3GPP 5G New Radio (NR). Na rozdíl od procedury Contention Based Random Access ([CBRA](/mobilnisite/slovnik/cbra/)), při které může více uživatelských zařízení (UE) přistupovat k síti pomocí stejné sady preambulí, což vede k možným kolizím, CFRA přiřadí konkrétnímu UE vyhrazenou, na kolizi nezávislou preambuli. Tuto vyhrazenou preambuli přiděluje gNodeB (gNB) prostřednictvím signalizace Radio Resource Control ([RRC](/mobilnisite/slovnik/rrc/)), typicky ve zprávách jako RRCReconfiguration, nebo prostřednictvím [PDCCH](/mobilnisite/slovnik/pdcch/) příkazu v downlinku. Procedura je zahájena pro konkrétní, naplánované události, kde jsou prvořadé nízká latence a vysoká spolehlivost, například při provedení povelu k předání spojení (handover) nebo v reakci na žádost o obnovu po selhání beamu.

Architektura procedury CFRA je integrována v celkových protokolech vrstvy 2 a vrstvy 3 NR. Klíčovými součástmi jsou Medium Access Control ([MAC](/mobilnisite/slovnik/mac/)) entita na straně UE a plánovač MAC na straně gNB. Když gNB rozhodne, že UE musí provést CFRA – například při předání spojení do cílové buňky – poskytne UE sadu vyhrazených prostředků pro náhodný přístup. Tyto prostředky zahrnují konkrétní index preambule (ze sady 64 preambulí dostupných v buňce) a konkrétní příležitost (časový/frekvenční zdroj) na Physical Random Access Channel ([PRACH](/mobilnisite/slovnik/prach/)). UE následně vysílá tuto vyhrazenou preambuli na přiřazené PRACH příležitosti. Protože je tato preambule pro danou událost jedinečně přiřazena, žádné jiné UE ji nepoužívá, což zaručuje, že ji gNB přijme bez kolize.

Po detekci vyhrazené preambule odešle gNB zprávu Random Access Response ([RAR](/mobilnisite/slovnik/rar/)) na Physical Downlink Shared Channel ([PDSCH](/mobilnisite/slovnik/pdsch/)), adresovanou pomocí dočasného identifikátoru sítě pro náhodný přístup ([RA-RNTI](/mobilnisite/slovnik/ra-rnti/)) vypočteného z PRACH příležitosti. RAR obsahuje povel pro časový předstih (timing advance) a uplink grant pro následnou zprávu UE (Msg3), kterou je v případě CFRA typicky RRCReconfigurationComplete nebo C-RNTI MAC Control Element. Absence kolize odstraňuje potřebu kroku řešení koliz (Msg4), který je v CBRA povinný. Toto snížení počtu kroků přímo vede k nižší přístupové latenci, která je často klíčová pro udržení plynulého spojení během mobility vysokou rychlostí nebo pro obnovení komunikace po selhání beamu.

CFRA hraje klíčovou roli v rádiové přístupové síti 5G NR tím, že umožňuje rychlou a deterministickou počáteční synchronizaci v uplinku. Jejími primárními operačními rolemi jsou provedení předání spojení, kdy se UE musí rychle přistoupit k cílové buňce; obnova po selhání beamu, kdy UE potřebuje rychle nahlásit nový kandidátní beam gNB; a navázání synchronizace v uplinku pro prostředky žádosti o plánování (SR), pokud žádné nejsou dostupné. Poskytnutím cesty bez koliz CFRA zvyšuje spolehlivost a snižuje latenci těchto procedur řídicí roviny, což je základním předpokladem pro splnění přísných požadavků 5G na rozšířené mobilní širokopásmové připojení (eMBB), hromadnou komunikaci mezi stroji (mMTC) a zejména komunikace s ultra spolehlivou nízkou latencí (URLLC).

## K čemu slouží

CFRA byla zavedena, aby řešila inherentní omezení tradiční procedury Contention Based Random Access (CBRA) ve scénářích, kde jsou přístupové zpoždění a spolehlivost kritické. V LTE a starších mobilních systémech byla CBRA dostačující pro počáteční přístup k síti. Zahrnuje však čtyřfázový handshake s pravděpodobnostním krokem řešení koliz, což zavádí proměnlivou a potenciálně vysokou latenci. Pro pokročilé případy užití 5G, jako je automatizace továren, autonomní vozidla a plynulá předání spojení při vysoké mobilitě, je toto nepředvídatelné zpoždění nepřijatelné. CFRA byla vytvořena, aby poskytla deterministický mechanismus přístupu s nízkou latencí pro naplánované, časově kritické události.

Historický kontext vychází z vývoje požadavků na mobilitu a spolehlivost. V LTE byla již definována forma náhodného přístupu bez koliz pro předání spojení, ale 5G NR tento mechanismus formalizovala a vylepšila, aby byl integrálnější a flexibilnější, zejména pro podporu operací zaměřených na beamy. Omezení CBRA spočívá v její statistické povaze: s rostoucím zatížením sítě roste pravděpodobnost kolize preambulí, což vede k neúspěšným přístupům, retransmisím a zvýšené latenci. U procedur, jako je předání spojení, kdy UE přechází mezi buňkami, může jakékoli zpoždění nebo selhání vést k selhání rádiového spoje (RLF) a ztrátě hovoru. CFRA to řeší předběžným přidělením prostředků, což zaručuje úspěšný přenos preambule na první pokus.

Dále bylo vytvoření CFRA motivováno potřebou podporovat pokročilé anténní systémy a beamforming v 5G. V síti využívající beamforming je spojení UE udržováno prostřednictvím specifických směrových beamů. Pokud beam selže, musí to UE rychle nahlásit gNB, aby přešlo na nový beam – proces známý jako obnova po selhání beamu (BFR). Použití CBRA pro BFR by bylo příliš pomalé a nespolehlivé. CFRA poskytuje rychlou cestu pro UE k odeslání žádosti BFR pomocí vyhrazené preambule, což umožňuje rychlou obnovu beamu a udržení vysokokvalitního spoje vyžadovaného pro frekvence milimetrových vln (mmWave) a služby URLLC. CFRA je tedy základním prvkem umožňujícím splnění výkonnostních cílů 5G.

## Klíčové vlastnosti

- Eliminuje kolizi preambulí použitím vyhrazených preambulí přidělených gNB
- Snižuje latenci náhodného přístupu vynecháním kroku řešení koliz
- Je spuštěna prostřednictvím signalizace RRC (např. povel k předání spojení) nebo PDCCH příkazu
- Primárně se používá pro předání spojení, obnovu po selhání beamu a navázání synchronizace v uplinku
- Zvyšuje spolehlivost časově kritických řídicích procedur
- Je nedílnou součástí podpory URLLC a efektivní mobility v 5G NR

## Související pojmy

- [CBRA – Contention Based Random Access](/mobilnisite/slovnik/cbra/)
- [PRACH – Physical Random Access Channel](/mobilnisite/slovnik/prach/)

## Definující specifikace

- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TS 38.523** (Rel-19) — 5G NR UE Conformance Testing: Idle/Inactive

---

📖 **Anglický originál a plná specifikace:** [CFRA na 3GPP Explorer](https://3gpp-explorer.com/glossary/cfra/)
