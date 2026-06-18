---
slug: "ipdl"
url: "/mobilnisite/slovnik/ipdl/"
type: "slovnik"
title: "IPDL – Idle Period Downlink"
date: 2025-01-01
abbr: "IPDL"
fullName: "Idle Period Downlink"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ipdl/"
summary: "Metoda určování polohy s podporou sítě pro UMTS (WCDMA), při které základnová stanice (Node B) vytváří ve svém downlinkovém přenosu tiché periody. To umožňuje uživatelskému zařízení (UE) přesněji měři"
---

IPDL je metoda určování polohy v UMTS, při které základnová stanice vytváří tiché periody na downlinku, aby umožnila uživatelskému zařízení přesněji měřit signály sousedních buněk pro odhad polohy.

## Popis

Idle Period Downlink (IPDL) je technika určování polohy standardizovaná v 3GPP pro sítě UMTS/[WCDMA](/mobilnisite/slovnik/wcdma/). Funguje v rámci rádiové přístupové sítě (RAN) a konkrétně vylepšuje metodu Observed Time Difference of Arrival ([OTDOA](/mobilnisite/slovnik/otdoa/)). Základní princip spočívá v tom, že obsluhující Node B (základnová stanice) dočasně přeruší svůj downlinkový přenos během předdefinovaných, velmi krátkých tichých period. Tyto koordinované a řídce se vyskytující tiché mezery umožňují uživatelskému zařízení (UE) detekovat a měřit Primary Synchronization Channel (P-Sch) ze sousedních Node B s výrazně vyšší přesností. Bez IPDL může být přijímač v UE desenzibilizován silným signálem z vlastní obsluhující buňky (problém blízko-daleko), což ztěžuje nebo znemožňuje detekci slabších synchronizačních signálů ze vzdálených buněk potřebných pro OTDOA výpočty.

Architektura podporující IPDL zahrnuje Radio Network Controller ([RNC](/mobilnisite/slovnik/rnc/)) a Node B. RNC spravuje relaci určování polohy, typně iniciovanou Serving Mobile Location Centre ([SMLC](/mobilnisite/slovnik/smlc/)) v core síti přes rozhraní Iupc. RNC nakonfiguruje parametry IPDL pro obsluhující Node B, jako je délka a vzor tichých period. Tyto parametry jsou pak signalizovány UE prostřednictvím zpráv Radio Resource Control ([RRC](/mobilnisite/slovnik/rrc/)), takže UE ví, kdy má očekávat a provádět mezibuněčná měření. UE využívá tyto příležitosti k měření k zachycení času příchodu signálů z více sousedních buněk, které jsou následně nahlášeny zpět do sítě pro výpočet polohy.

Klíčové komponenty zahrnují generátor vzoru IPDL v Node B, měřicí procedury ve fyzické vrstvě UE a koordinační protokoly mezi RNC a Node B (přes rozhraní Iub). Tato technika je obzvláště klíčová pro OTDOA v synchronních WCDMA sítích (kde základnové stanice nejsou časově synchronizovány přes [GPS](/mobilnisite/slovnik/gps/)), protože poskytuje nezbytnou slyšitelnost sousedních buněk. Tiché periody jsou navrženy tak, aby byly dostatečně krátké, aby významně neovlivnily downlinkový provoz nebo kvalitu služby, ale zároveň dostatečné pro to, aby přijímač v UE zachytil synchronizační sekvence z jiných buněk.

Úloha IPDL spočívá v umožnění síťového, uživatelským zařízením asistovaného určování polohy ve scénářích, kde satelitní metody jako GPS nejsou dostupné nebo jsou nepřesné (např. uvnitř budov). Zlepšuje spolehlivost a přesnost architektury určování polohy UMTS definované v TS 25.305. Řešením problému slyšitelnosti přeměňuje OTDOA z teoretického konceptu na praktickou metodu určování polohy pro komerční sítě a vytváří základní schopnost, která se později vyvinula v rámci rámců pro určování polohy LTE a 5G NR.

## K čemu slouží

IPDL byl vytvořen, aby vyřešil zásadní omezení při implementaci určování polohy metodou Observed Time Difference of Arrival ([OTDOA](/mobilnisite/slovnik/otdoa/)) v sítích [WCDMA](/mobilnisite/slovnik/wcdma/) (UMTS). OTDOA vyžaduje, aby UE změřilo časový rozdíl příchodu signálů z alespoň tří geograficky rozptýlených základnových stanic. V CDMA systému je však UE typicky připojeno k jedné silné obsluhující buňce. Výkon tohoto blízkého signálu může přehlušit přijímač UE, což znemožňuje detekci mnohem slabších pilotních signálů ze vzdálených sousedních buněk – klasický problém blízko-daleko. Tento problém „slyšitelnosti“ činil základní OTDOA v mnoha reálných nasazeních nefunkční.

Před zavedením IPDL se síťové určování polohy v UMTS spoléhalo hlavně na metody Cell-ID, které nabízely špatnou přesnost (stovky metrů až kilometry), nebo vyžadovaly, aby mělo UE integrovaný GPS, což nebylo univerzální a v interiérech fungovalo špatně. Průmysl potřeboval standardizovanou, sítí asistovanou metodu, která by mohla poskytnout lepší přesnost bez nutnosti specifického hardwaru v UE. IPDL vyřešil problém slyšitelnosti tím, že nechal obsluhující buňku na okamžik „ustoupit stranou“ a vytvořil tak čisté okno pro naslouchání. Tato inovace umožnila OTDOA fungovat v asynchronních WCDMA sítích a poskytovat přesnost v řádu desítek až stovek metrů, což byl významný pokrok pro služby založené na poloze, lokalizaci nouzových volání (E911) a optimalizaci sítě.

Motivace byla hnána regulačními požadavky pro nouzové služby (např. E112 v Evropě) a rostoucí komerční poptávkou po službách založených na poloze. Díky zavedení ve verzi Release 99 vytvořil IPDL již na počátku nasazení 3G klíčovou schopnost určování polohy. Ukázal, že síťové asistované metody mohou doplňovat a někdy nahrazovat satelitní určování polohy, což je princip, který se dále vyvíjel prostřednictvím OTDOA v LTE a funkcí určování polohy v 5G NR, kde koncept utlumení referenčních signálů pro lepší slyšitelnost zůstává základní technikou.

## Klíčové vlastnosti

- Vytváří řízené tiché periody v downlinkovém přenosu obsluhující buňky
- Umožňuje UE detekovat synchronizační signály ze vzdálených sousedních buněk
- Řeší problém blízko-daleko pro OTDOA v sítích WCDMA
- Parametry řízené sítí (délka tiché periody, vzor) signalizované přes RRC
- Minimalizuje dopad na downlinkový provoz a QoS obsluhující buňky
- Základní pro určování polohy metodou OTDOA v asynchronních nasazeních UMTS

## Související pojmy

- [OTDOA – Observed Time Difference Of Arrival](/mobilnisite/slovnik/otdoa/)
- [SMLC – Standalone Mobile Location Center](/mobilnisite/slovnik/smlc/)

## Definující specifikace

- **TS 23.171** (Rel-4) — LCS Stage 2 Specification for UMTS
- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TS 25.305** (Rel-19) — UTRAN UE Positioning Stage 2
- **TS 25.306** (Rel-19) — UE Radio Access Capabilities Specification
- **TS 25.423** (Rel-19) — UTRAN RNSAP Specification
- **TS 25.433** (Rel-19) — Node B Application Part (NBAP) Protocol

---

📖 **Anglický originál a plná specifikace:** [IPDL na 3GPP Explorer](https://3gpp-explorer.com/glossary/ipdl/)
