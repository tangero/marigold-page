---
slug: "ruci"
url: "/mobilnisite/slovnik/ruci/"
type: "slovnik"
title: "RUCI – RAN User Plane Congestion Information"
date: 2025-01-01
abbr: "RUCI"
fullName: "RAN User Plane Congestion Information"
category: "Management"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/ruci/"
summary: "RUCI je mechanismus, který umožňuje RAN hlásit stav zahlcení uživatelské roviny do jádra sítě a tím umožnit dynamické řízení politik. Pomáhá optimalizovat využití zdrojů a udržovat QoS tím, že informu"
---

RUCI je mechanismus RAN pro hlášení stavu zahlcení uživatelské roviny do jádra sítě, který umožňuje dynamické řízení politik a úpravu provozu ze strany PCRF/PGW.

## Popis

RAN User Plane Congestion Information (RUCI) je standardizovaný mechanismus v sítích 3GPP, který umožňuje přístupové rádiové síti (RAN) komunikovat stav zahlcení v uživatelské rovině v reálném čase s prvky jádra sítě, především s funkcí Policy and Charging Rules Function ([PCRF](/mobilnisite/slovnik/pcrf/)) a Packet Data Network Gateway ([PGW](/mobilnisite/slovnik/pgw/)). Tato výměna informací umožňuje síti zavádět proaktivní a reaktivní opatření pro správu provozu během období vysokého zatížení nebo nedostatku zdrojů. RUCI funguje definováním specifických signalizačních procedur a informačních prvků, které přenášejí indikátory zahlcení, jako jsou úrovně zahlcení (např. nízká, střední, vysoká), zasažené oblasti (např. na úrovni buňky nebo uzlu RAN) a časová razítka. Tyto informace jsou přenášeny z uzlů RAN, jako jsou eNodeB v LTE nebo gNB v 5G, do jádra sítě přes standardizovaná rozhraní.

Architektonicky RUCI využívá stávající rozhraní, jako je rozhraní S1 v LTE (mezi eNodeB a [MME](/mobilnisite/slovnik/mme/)/[SGW](/mobilnisite/slovnik/sgw/)) nebo rozhraní [N2](/mobilnisite/slovnik/n2/) v 5G (mezi gNB a [AMF](/mobilnisite/slovnik/amf/)), s rozšířeními pro podporu hlášení zahlcení. V jádře sítě PCRF tyto informace využívá k dynamickému přizpůsobování rozhodnutí o politikách, což může spustit akce jako omezení datových rychlostí, zvýšení priority určitých služeb nebo přesměrování provozu. Mezi klíčové komponenty patří funkce detekce zahlcení v RAN, která sleduje metriky jako využití rádiových zdrojů nebo obsazenost vyrovnávací paměti, a funkce hlášení zahlcení, která formátuje a odesílá zprávy RUCI. Proces zahrnuje detekci, hlášení, vynucování politik a případné zpětnovazební smyčky pro zmírnění zahlcení.

Role RUCI je nedílnou součástí správy kvality služeb (QoS) od konce ke konci a optimalizace sítě. Poskytnutím přehledu o podmínkách v RAN umožňuje inteligentnější směrování provozu a přidělování zdrojů, což je v souladu s koncepty jako síťové segmenty (network slicing) a provoz citlivý na služby. Například během zahlcení může RUCI pomoci zajistit, že kritické služby, jako jsou nouzová komunikace, si zachovají výkon, zatímco nepodstatný provoz je odsunut na nižší prioritu. Jeho implementace podporuje systémy LTE i 5G, zvyšuje přizpůsobivost v heterogenních sítích a přispívá k efektivnímu využití spektra a lepší uživatelské zkušenosti.

## K čemu slouží

RUCI byl vyvinut, aby řešil problém neefektivního řízení zdrojů během zahlcení uživatelské roviny v mobilních sítích, kde tradiční metody postrádaly koordinaci v reálném čase mezi politikami RAN a jádra sítě. Před zavedením RUCI bylo zvládání zahlcení často lokalizováno pouze na RAN, s omezenou možností ovlivnit toky provozu na trase od konce ke konci nebo aplikovat úpravy specifické pro služby z jádra sítě. To mohlo vést k podoptimální QoS, plýtvání zdroji a špatné uživatelské zkušenosti během špiček.

Zaveden v 3GPP Release 13, byl RUCI motivován rostoucími požadavky na datový provoz a potřebou dynamičtějšího, holistického řízení zahlcení. Tyto problémy řeší vytvořením standardizovaného zpětnovazebního mechanismu, který umožňuje jádru sítě reagovat na podmínky v RAN s detailními kontrolami politik. To umožňuje lepší podporu různorodých služeb, včetně těch pro kritické mise a aplikace citlivé na latenci, a je v souladu s trendy směřujícími k softwarově definovaným sítím a automatizované optimalizaci provozu v rozvíjejících se nasazeních 4G a 5G.

## Klíčové vlastnosti

- Hlásí stav zahlcení RAN jádru sítě v reálném čase
- Umožňuje dynamické úpravy politik ze strany PCRF/PGW
- Podporuje úrovně zahlcení a indikátory geografické oblasti
- Funguje přes rozhraní LTE S1 a 5G N2
- Umožňuje správu provozu citlivou na služby během přetížení
- Zvyšuje kvalitu služeb (QoS) a efektivitu využití zdrojů na trase od konce ke konci

## Související pojmy

- [PCRF – Policy and Charging Rules Function](/mobilnisite/slovnik/pcrf/)
- [QoS – Quality of Service](/mobilnisite/slovnik/qos/)
- [RAN – Radio Access Network](/mobilnisite/slovnik/ran/)

## Definující specifikace

- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 23.203** (Rel-19) — Policy and charging control architecture
- **TS 23.401** (Rel-19) — Evolved Packet System (EPS) Stage 2 Description
- **TS 29.212** (Rel-19) — Gx/Gxx/Sd/St Diameter Protocol
- **TS 29.213** (Rel-19) — PCC Signalling Flows and QoS Mapping
- **TS 29.217** (Rel-19) — Policy and Charging Control (PCC) for Np Interface

---

📖 **Anglický originál a plná specifikace:** [RUCI na 3GPP Explorer](https://3gpp-explorer.com/glossary/ruci/)
