---
slug: "naics"
url: "/mobilnisite/slovnik/naics/"
type: "slovnik"
title: "NAICS – Network-Assisted Interference Cancellation and Suppression"
date: 2025-01-01
abbr: "NAICS"
fullName: "Network-Assisted Interference Cancellation and Suppression"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/naics/"
summary: "Síťově koordinovaná technika potlačení interference pro LTE a 5G NR. Síť signalizuje charakteristiky interference uživatelským zařízením (UE), což umožňuje pokročilé zpracování v přijímači pro zrušení"
---

NAICS je síťově koordinovaná technika potlačení interference pro LTE a 5G NR, při které síť signalizuje uživatelským zařízením (UE) charakteristiky interference, aby umožnila pokročilé zpracování v přijímači za účelem zrušení nebo potlačení dominantních rušičů.

## Popis

Network-Assisted Interference Cancellation and Suppression (NAICS) je sofistikovaný rámec pro správu interference standardizovaný v 3GPP, primárně pro sítě LTE-Advanced a 5G New Radio (NR). Funguje na principu, že síť (eNodeB nebo gNodeB) disponuje nadřazenými znalostmi o interferenčním prostředí, včetně parametrů přenosů sousedních buněk, které může signalizovat uživatelskému zařízení (UE). Tato asistence umožňuje UE používat pokročilé přijímací algoritmy, jako je Interference Rejection Combining ([IRC](/mobilnisite/slovnik/irc/)), Symbol-Level Interference Cancellation (SLIC) nebo Codeword-Level Interference Cancellation (CWIC), které přesahují možnosti tradičních lineárních přijímačů. Síť vysílá pomocné informace NAICS, které mohou zahrnovat podrobnosti jako počet interferenčních vrstev, modulační řád, informace o předkódování a přidělení zdrojů dominantního rušiče, což umožňuje UE rekonstruovat a odečíst interferenční signál z přijatého složeného signálu.

Architektura NAICS zahrnuje vylepšení jak v rádiové přístupové síti, tak v přijímači UE. Na straně sítě je klíčová koordinace mezi základnovými stanicemi (přes rozhraní jako [X2](/mobilnisite/slovnik/x2/) v LTE) za účelem shromáždění a sdílení potřebných interferenčních parametrů. Obsluhující buňka pak tyto informace zakóduje v rámci signalizace na downlinku, například na Physical Downlink Control Channel ([PDCCH](/mobilnisite/slovnik/pdcch/)) nebo prostřednictvím signalizace vyšší vrstvy Radio Resource Control ([RRC](/mobilnisite/slovnik/rrc/)). Na straně UE musí být přijímač schopen tyto pomocné informace zpracovat a provést odpovídající pokročilé algoritmy pro zrušení interference. To vyžaduje zvýšenou výpočetní složitost na straně UE, ale vede k podstatnému zisku v poměru signálu k interferenci a šumu ([SINR](/mobilnisite/slovnik/sinr/)), zejména pro uživatele na okraji buňky, kde je interference limitujícím faktorem.

NAICS hraje klíčovou roli ve zlepšování výkonu hustých, heterogenních sítí (HetNets) a scénářů s agresivní frekvenční reutilizací. Tím, že efektivně promění silného rušiče na známý signál, který lze zrušit, přeměňuje NAICS klíčovou výzvu moderních celulárních sítí – mezibuněčnou interferenci – na příležitost pro zvýšení kapacity. Jeho implementace je klíčovým krokem k využití plného potenciálu víceanténních ([MIMO](/mobilnisite/slovnik/mimo/)) systémů a síťové koordinace, posunem za jednoduché řízení výkonu nebo dělení zdrojů směrem k inteligentnímu, na přijímači založenému řízení interference. Specifikace detailně popisují přesné signalizační parametry, schopnosti přijímače a požadavky na výkon, aby byla zajištěna interoperabilita a předvídatelná zlepšení výkonu sítě.

## K čemu slouží

NAICS byl vytvořen, aby řešil základní kapacitní omezení v celulárních sítích: mezibuněčnou interferenci, která se stává závažnou v sítích s malými buňkami a univerzální frekvenční reutilizací (např. reuse-1). Tradiční techniky potlačení interference, jako je Inter-Cell Interference Coordination ([ICIC](/mobilnisite/slovnik/icic/)) nebo enhanced ICIC (eICIC), spoléhají na koordinaci na síťové straně, aby se interferenci vyhnuly v časové, frekvenční nebo výkonové doméně, což může být neefektivní a snižovat celkové spektrální zdroje. NAICS byl motivován potřebou spektrálně účinnějšího řešení, které by mohlo aktivně využívat, a ne pouze se vyhýbat, interferenci.

Historický kontext představuje evoluce směrem k LTE-Advanced a hustým nasazením sítí, kde uživatelé na okraji buňky trpí nízkou propustností kvůli silným signálům ze sousedních buněk. Předchozí přijímače UE, primárně lineární přijímače s minimální střední kvadratickou chybou ([LMMSE](/mobilnisite/slovnik/lmmse/)), mohly potlačit šum, ale proti strukturované, silné interferenci byly suboptimální. NAICS to řeší využitím znalostí sítě k posílení přijímače UE. Řeší omezení, že UE samo o sobě nemůže slepě a spolehlivě odhadnout všechny parametry komplexního interferenčního signálu, zejména pokud používá pokročilé přenosové režimy. Poskytnutím těchto informací prostřednictvím signalizace umožňuje NAICS deterministické a efektivní zrušení interference, přímo řeší problém výkonu na okraji buňky a zlepšuje celkovou kapacitu sítě a spravedlnost uživatelského zážitku.

## Klíčové vlastnosti

- Signalizace interferenčních parametrů poskytovaná sítí (např. modulační řád, počet vrstev)
- Podpora pokročilých přijímacích algoritmů v UE, jako je CWIC a SLIC
- Zlepšení propustnosti uživatelů na okraji buňky a spektrální účinnosti
- Použitelnost v homogenních i heterogenních nasazeních sítí
- Zpětná kompatibilita s UE nepodporujícími NAICS
- Koordinace mezi základnovými stanicemi za účelem shromáždění informací o interferenci

## Související pojmy

- [MIMO – Multiple Input Multiple Output](/mobilnisite/slovnik/mimo/)

## Definující specifikace

- **TS 25.423** (Rel-19) — UTRAN RNSAP Specification
- **TS 25.433** (Rel-19) — Node B Application Part (NBAP) Protocol
- **TS 25.766** (Rel-13) — Network-Assisted Interference Cancellation for UMTS
- **TS 36.306** (Rel-19) — E-UTRA UE Radio Access Capability Parameters
- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification
- **TS 36.423** (Rel-19) — X2 Application Protocol (X2AP) Specification
- **TS 36.825** (Rel-13) — Study on Additional LTE TDD Configurations

---

📖 **Anglický originál a plná specifikace:** [NAICS na 3GPP Explorer](https://3gpp-explorer.com/glossary/naics/)
