---
slug: "tadv"
url: "/mobilnisite/slovnik/tadv/"
type: "slovnik"
title: "TADV – Timing Advance"
date: 2025-01-01
abbr: "TADV"
fullName: "Timing Advance"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/tadv/"
summary: "Timing Advance (TADV) je klíčový mechanismus v mobilních sítích, který kompenzuje zpoždění šíření mezi uživatelským zařízením (UE) a základnovou stanicí. Zajišťuje, aby uplinkové přenosy od více uživa"
---

TADV je mechanismus, který kompenzuje rádiové zpoždění šíření, aby synchronizoval uplinkové přenosy od více uživatelských zařízení (UE) na základnové stanici, a zabránil tak interferenci.

## Popis

Timing Advance (TADV) je základní synchronizační mechanismus v rádiové přístupové síti (RAN) systémů 3GPP, zvláště důležitý pro technologie využívající Time Division Duplex ([TDD](/mobilnisite/slovnik/tdd/)) a Orthogonal Frequency-Division [Multiple Access](/mobilnisite/slovnik/multiple-access/) ([OFDMA](/mobilnisite/slovnik/ofdma/)), jako jsou LTE a NR. Jeho primární funkcí je sladit časování uplinkových přenosů od všech uživatelských zařízení (UE) v rámci buňky tak, aby dorazily na základnovou stanici (eNodeB v LTE, gNB v NR) v rámci určeného přijímacího okna. Toto sladění je klíčové, protože rádiové signály se šíří konečnou rychlostí, což způsobuje zpoždění šíření úměrné vzdálenosti mezi UE a základnovou stanicí. Bez kompenzace by přenosy od vzdálenějších UE dorazily později než od blízkých UE, což by vedlo k nesouososti symbolů, mezi-symbolové interferenci ([ISI](/mobilnisite/slovnik/isi/)) a ztrátě ortogonality mezi subnosnými, což by vážně snížilo výkon sítě.

Mechanismus TADV funguje dynamicky v uzavřené smyčce. Základnová stanice kontinuálně měří časování přijímaných uplinkových signálů od každého UE, typicky pomocí známých referenčních signálů, jako je Sounding Reference Signal ([SRS](/mobilnisite/slovnik/srs/)) nebo preambule Physical Random Access Channel ([PRACH](/mobilnisite/slovnik/prach/)) během počátečního přístupu. Na základě naměřené časové odchylky (rozdílu mezi očekávaným a skutečným časem příjmu) základnová stanice vypočítá potřebný příkaz Timing Advance. Tento příkaz je hodnota, často vyjádřená v jednotkách základního kroku časového předstihu (např. 16 Ts nebo 64 Ts, kde Ts je základní časová jednotka), která uživatelskému zařízení instruuje, o kolik má posunout časování svého přenosu. Příkaz je přenášen k uživatelskému zařízení prostřednictvím downlinkového řídicího signalizování, jako je Medium Access Control ([MAC](/mobilnisite/slovnik/mac/)) Control Element nebo zpráva Random Access Response ([RAR](/mobilnisite/slovnik/rar/)).

Po přijetí příkazu TADV uživatelské zařízení podle něj upraví své vnitřní časování přenosu. Tato úprava se aplikuje na všechny následující uplinkové přenosy, včetně dat na Physical Uplink Shared Channel (PUSCH) a řídicích informací na Physical Uplink Control Channel (PUCCH). Proces je kontinuální; jak se uživatelské zařízení pohybuje nebo se mění podmínky kanálu, základnová stanice vydává aktualizované příkazy TADV, aby udržela synchronizaci. Samotná hodnota TADV má definovaný rozsah, který omezuje maximální podporovaný poloměr buňky. Například v LTE maximální TADV odpovídá poloměru buňky přibližně 100 km. V NR vylepšení podporují ještě větší buňky a přesnější časování pro pokročilé případy užití. Mechanismus TADV je klíčovým kamenem pro umožnění efektivního uplinkového přístupu více uživatelů, minimalizaci interference a zajištění spolehlivé demodulace signálů, což přímo ovlivňuje kapacitu sítě a uživatelský zážitek.

## K čemu slouží

Účelem Timing Advance je řešit základní problém uplinkové synchronizace v mobilní síti, kde jsou uživatelská zařízení (UE) v různých vzdálenostech od základnové stanice. V synchronizovaném systému, jako je OFDMA, je ortogonalita mezi subnosnými, která zabraňuje interferenci uvnitř buňky, zachována pouze tehdy, jsou-li všechny přijímané signály časově sladěny v rámci trvání cyklické předpony. Bez TADV by přirozené zpoždění šíření způsobilo nesouosost, která by tuto ortogonalitu zničila a vedla k vážnému snížení výkonu známému jako mezi-nosná interference (ICI). Tento problém je obzvláště akutní v systémech TDD, kde uplink a downlink sdílejí stejný frekvenční kanál v různých časových slotech, což vyžaduje striktní časování, aby se zabránilo interferenci mezi uplinkovými a downlinkovými přenosy.

Historicky používaly dřívější mobilní systémy, jako GSM, také koncept časového předstihu, ale byl jednodušší kvůli použití Frequency Division Multiple Access (FDMA) a Time Division Multiple Access (TDMA). Motivace pro TADV v 3GPP LTE a NR vychází z adopce OFDMA v uplinku (SC-FDMA v LTE, OFDMA v NR), která je vysoce citlivá na časovou nesouosost. Vytvoření dynamického mechanismu úpravy časování řízeného sítí bylo nezbytné k uvolnění plné spektrální efektivity a možností více uživatelů těchto pokročilých rozhraní. Řeší omezení statického časování nebo odhadu v otevřené smyčce, které se nedokáží přizpůsobit pohyblivosti uživatelských zařízení a měnícím se rádiovým podmínkám. Zajištěním přesné uplinkové synchronizace umožňuje TADV síti podporovat vysoké přenosové rychlosti, nízkou latenci a velký počet současně připojených zařízení, což jsou klíčové požadavky pro moderní mobilní broadband a služby IoT.

## Klíčové vlastnosti

- Uzavřená smyčka synchronizace řízená sítí (základnovou stanicí)
- Dynamické přizpůsobování založené na kontinuálním měření časování uplinkového signálu
- Kompenzuje rádiové zpoždění šíření, aby sladil přenosy uživatelských zařízení (UE) na přijímači
- Zásadní pro udržení ortogonality OFDMA/SC-FDMA a prevenci mezi-symbolové interference
- Podporuje velikost buněk až do definovaného maximálního poloměru (např. ~100 km v LTE)
- Signalizováno prostřednictvím MAC Control Elements nebo zpráv Random Access Response

## Definující specifikace

- **TS 36.305** (Rel-19) — UE Positioning in E-UTRAN Stage 2
- **TS 38.305** (Rel-19) — NG-RAN UE Positioning Stage 2

---

📖 **Anglický originál a plná specifikace:** [TADV na 3GPP Explorer](https://3gpp-explorer.com/glossary/tadv/)
