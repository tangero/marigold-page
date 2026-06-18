---
slug: "lp-wur"
url: "/mobilnisite/slovnik/lp-wur/"
type: "slovnik"
title: "LP-WUR – Low Power Wake Up Receiver"
date: 2025-01-01
abbr: "LP-WUR"
fullName: "Low Power Wake Up Receiver"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/lp-wur/"
summary: "Sekundární obvod přijímače s ultranízkou spotřebou v UE, zavedený ve specifikaci 3GPP Release 18. Naslouchá signálům pro probuzení (jako je LP-WUS), zatímco hlavní transceiver spí, což drasticky snižu"
---

LP-WUR je sekundární obvod přijímače s ultranízkou spotřebou v zařízení, který naslouchá signálům pro probuzení zatímco hlavní transceiver spí, což drasticky snižuje spotřebu energie.

## Popis

Low Power Wake Up Receiver (LP-WUR) je hardwarová a protokolová komponenta definovaná ve specifikaci 3GPP Release 18 pro uživatelská zařízení (UE) New Radio (NR), navržená k minimalizaci spotřeby energie oddělením funkce probouzení od hlavního rádiového transceiveru. Jedná se o sekundární přijímací obvod, který pracuje nezávisle a spotřebovává mikrowatty energie ve srovnání s miliwatty pro hlavní přijímač. LP-WUR kontinuálně nebo periodicky monitoruje rádiový kanál pro specifické signály probuzení, jako je Low Power Wake Up Signal ([LP-WUS](/mobilnisite/slovnik/lp-wus/)), zatímco hlavní komunikační moduly UE (např. modem, procesor základního pásma) zůstávají v hlubokém spánku. Po detekci platného signálu probuzení LP-WUR spustí aktivaci hlavního přijímače a vyšších protokolových vrstev pro zpracování příchozích dat nebo provedení síťových procedur, čímž optimalizuje celkovou spotřebu energie.

Architektonicky je LP-WUR integrován do subsystémů vysokofrekvenčního ([RF](/mobilnisite/slovnik/rf/)) a základního pásma UE, jak je specifikováno v 3GPP TS 38.101 pro rádiové požadavky a TS 38.331 pro protokoly [RRC](/mobilnisite/slovnik/rrc/). Skládá se z jednoduchého analogového front-endu, detektoru s nízkou složitostí a řídicí logiky, která komunikuje s jednotkou pro správu napájení UE. Přijímač je navržen k detekci signálů s minimálním zpracováním, často využívá klíčování zapnuto/vypnuto nebo podobné modulační schéma s nízkou složitostí. Klíčové komponenty zahrnují šumově nízký zesilovač, detektor obálky a korelátor pro rozpoznání signálu. V síti gNB koordinuje provoz LP-WUR konfigurací parametrů, jako jsou vzory signálu probuzení a intervaly naslouchání prostřednictvím signalizace RRC nebo systémových informací, čímž zajišťuje soulad se síťovým plánováním a politikami úspory energie.

V provozu LP-WUR umožňuje dvoustupňový proces probuzení: když je UE nečinná nebo v režimu úspory energie, LP-WUR zůstává aktivní a vyhledává předem nakonfigurované signály probuzení od gNB. Pokud není detekován žádný signál, hlavní přijímač zůstává vypnutý, čímž šetří energii. Po detekci LP-WUR odešle přerušení řadiči UE, který zapne hlavní transceiver pro úkoly jako příjem pagingu, přenos dat nebo synchronizaci. Tento mechanismus snižuje pracovní cyklus komponent s vysokou spotřebou a významně prodlužuje životnost baterie. LP-WUR je specifikován v řadě dokumentů 3GPP, včetně TS 38.774 a 38.869, které detailně popisují jeho výkonnostní požadavky a integraci s dalšími funkcemi pro nízkou spotřebu, jako je [LP-SS](/mobilnisite/slovnik/lp-ss/) a LP-WUS, což z něj činí základní kámen energeticky efektivních NR zařízení.

## K čemu slouží

LP-WUR byl vyvinut k řešení kritických problémů spotřeby energie v 5G NR, zejména pro zařízení Internetu věcí (IoT) a zařízení se sníženou schopností (RedCap), která vyžadují ultradlouhou životnost baterie, často přesahující 10 let. Před Release 18 NR UE spoléhala na cykly nespojitého příjmu ([DRX](/mobilnisite/slovnik/drx/)), při kterých se hlavní přijímač periodicky probouzel ke kontrole pagingu nebo řídicích signálů, což stále spotřebovávalo značnou energii kvůli složitosti moderních NR přijímačů. Tento přístup byl nedostatečný pro masivní nasazení IoT, kde zařízení tráví většinu času v nečinnosti, což vedlo k časté výměně baterií a zvýšeným provozním nákladům.

Vytvoření LP-WUR bylo motivováno úspěchem podobných technologií v [IEEE](/mobilnisite/slovnik/ieee/) 802.11 (Wi-Fi) a proprietárních IoT systémech, které prokázaly, že vyhrazený přijímač probuzení s nízkou spotřebou může drasticky snížit spotřebu energie. V rámci 3GPP řeší problém režie 'přijímač stále zapnutý' zavedením minimalistického přijímače, který zvládá úlohu naslouchání s téměř nulovou spotřebou. To umožňuje aplikacím, jako jsou chytré měřiče, environmentální senzory a nositelná zařízení, fungovat po desetiletí na malých bateriích, přičemž jsou stále dosažitelné ze sítě na požádání. LP-WUR je v souladu s cíli 3GPP pro udržitelné sítě a podporuje expanzi NR do odvětví s nízkou spotřebou, čímž překlenuje propast mezi vysokovýkonným 5G a případy použití s omezenými energetickými zdroji.

## Klíčové vlastnosti

- Sekundární přijímací obvod s ultranízkou spotřebou
- Nezávislý provoz od hlavního transceiveru UE
- Detekuje signály probuzení (např. LP-WUS) s minimální spotřebou energie
- Po detekci signálu spouští aktivaci hlavního přijímače
- Konfigurovatelný prostřednictvím signalizace RRC pro síťové řízení
- Prodlužuje životnost baterie UE pro IoT a RedCap zařízení

## Související pojmy

- [LP-WUS – Low Power Wake Up Signal](/mobilnisite/slovnik/lp-wus/)
- [LP-SS – Low Power Synchronization Signal](/mobilnisite/slovnik/lp-ss/)

## Definující specifikace

- **TS 38.101** (Rel-19) — NR User Equipment Radio Transmissions
- **TS 38.331** (Rel-19) — NR Radio Resource Control (RRC) Protocol Specification
- **TS 38.774** (Rel-19) — Rel-19 LP-WUS/WUR RF Requirements TR
- **TR 38.869** (Rel-18) — Study on low-power wake up signal and receiver for NR

---

📖 **Anglický originál a plná specifikace:** [LP-WUR na 3GPP Explorer](https://3gpp-explorer.com/glossary/lp-wur/)
