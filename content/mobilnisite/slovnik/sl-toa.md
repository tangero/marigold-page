---
slug: "sl-toa"
url: "/mobilnisite/slovnik/sl-toa/"
type: "slovnik"
title: "SL-TOA – Sidelink Time Of Arrival"
date: 2025-01-01
abbr: "SL-TOA"
fullName: "Sidelink Time Of Arrival"
category: "Radio Access Network"
segment: "Testing"
canonical: "https://3gpp-explorer.com/glossary/sl-toa/"
summary: "SL-TOA je metoda určování polohy, při které zařízení měří absolutní čas příchodu signálu od referenčního vysílače přes sidelink. Používá se k výpočtu vzdáleností pro odhad polohy a podporuje bezpečnos"
---

SL-TOA je metoda sidelinkového určování polohy, při které zařízení měří absolutní čas příchodu referenčního signálu, aby vypočítalo vzdálenosti pro odhad polohy.

## Popis

Sidelink Time Of Arrival (SL-TOA) je základní technika určování polohy v sidelinkovém rámci 3GPP, při které cílové zařízení měří přesný čas příchodu polohovacího signálu od jediného referenčního vysílače přes sidelinkové rozhraní. Toto měření představuje dobu šíření signálu, která po vynásobení rychlostí světla udává vzdálenost mezi vysílačem a přijímačem za předpokladu přímé viditelnosti a přesné časové synchronizace. V praxi se SL-TOA často používá ve spojení s jinými měřeními nebo s více referenčními body pro určení polohy; například kombinace měření [TOA](/mobilnisite/slovnik/toa/) ze tří nebo více referencí umožňuje trilateraci pro určení 2D nebo 3D polohy. Referenčním vysílačem může být jiné vozidlo, dopravní zařízení ([RSU](/mobilnisite/slovnik/rsu/)) nebo jakékoli sidelinkové UE se známou polohou, které vysílá signály, jako jsou sidelinkové polohovací referenční signály ([SL-PRS](/mobilnisite/slovnik/sl-prs/)), synchronizační signály nebo demodulační referenční signály nakonfigurované pro určování polohy.

Technická implementace zahrnuje několik vrstev: na fyzické vrstvě cílové UE přijímá SL-PRS nebo ekvivalentní signál, který je navržen s dobrými autokorelačními vlastnostmi pro umožnění přesného časového odhadu. Přijímač UE provádí zpracování založené na korelaci pro detekci času příchodu, často s dosažením přesnosti na úrovni submikrosekund za ideálních podmínek. Naměřená hodnota TOA je následně korigována o hodinové odchylky; protože obě zařízení mohou mít nezávislé hodiny, je synchronizace klíčová. Synchronizace může být dosažena prostřednictvím [GNSS](/mobilnisite/slovnik/gnss/), síťového časování (např. od gNB) nebo prostřednictvím sidelinkových synchronizačních signálů ([SLSS](/mobilnisite/slovnik/slss/)) od synchronizační reference. V některých režimech reference zahrnuje svůj čas vysílání do datové části signálu, což cílovému zařízení umožňuje přímo vypočítat dobu letu. Měření jsou řízena protokolovým zásobníkem pro určování polohy v UE, jak je specifikováno v 38.355, a mohou být hlášena funkci Location Management Function ([LMF](/mobilnisite/slovnik/lmf/)) pro síťově asistované určování polohy nebo použita lokálně pro UE-bázované určování polohy.

SL-TOA hraje klíčovou roli v ekosystému sidelinkového určování polohy tím, že poskytuje surová data o vzdálenosti, která slouží jako vstup pro algoritmy vyšší úrovně. Je zvláště cenná pro relativní určování polohy mezi dvěma zařízeními, například pro stanovení vzdálenosti mezi dvěma vozidly pro posouzení rizika kolize. V architekturách, jako je UE-bázované určování polohy, cílové UE shromažďuje měření TOA z více referencí, zjišťuje jejich polohy (např. prostřednictvím sidelinkové komunikace nebo síťové asistence) a vypočítává svou vlastní polohu. Pro síťově-bázované určování polohy UE odesílá měření TOA do LMF, která je kombinuje s dalšími daty (např. od jiných UE nebo senzorů) pro výpočet polohy UE. SL-TOA je základem pokročilejších metod, jako je [SL-TDOA](/mobilnisite/slovnik/sl-tdoa/), která využívá rozdíly mezi TOA k eliminaci společných hodinových chyb. Její integrace do standardů 3GPP zajišťuje interoperabilitu a měření výkonu, s podrobnými požadavky na zkoušení shody uvedenými v 37.571.

## K čemu slouží

SL-TOA byl vyvinut, aby poskytl základní, avšak přesný, mechanismus měření vzdálenosti pro sidelinková zařízení, a řešil tak potřebu odhadu vzdálenosti pro služby založené na blízkosti a bezpečnost [V2X](/mobilnisite/slovnik/v2x/). Před jeho standardizací sidelinková komunikace v 3GPP (např. v Rel-14 pro LTE-V2X) podporovala základní vysílání bezpečnostních zpráv, ale postrádala standardizované možnosti určování polohy, což nutilo spoléhat se na GNSS pro povědomí o poloze. Toto omezení se stalo problematickým v prostředích, kde je GNSS nespolehlivé, jako jsou městské kaňony nebo tunely, a omezovalo tak účinnost aplikací, jako je varování před nouzovými vozidly nebo jízda v koloně. SL-TOA umožňuje zařízením měřit vzdálenosti přímo pomocí buněčných signálů, čímž zlepšuje situační povědomí bez závislosti na externích systémech.

Vytvoření SL-TOA bylo motivováno rozšířením V2X a komerčních D2D případů užití v 5G NR, které vyžadují určování polohy s nízkou latencí a vysokou spolehlivostí. Tradiční metody buněčného určování polohy (např. E-OTDOA v LTE) fungují na rozhraní Uu mezi UE a základnovou stanicí, což nemusí být pro scénáře zařízení-zařízení optimální kvůli problémům s latencí nebo pokrytím. SL-TOA využívá přímý sidelinkový kanál, umožňuje rychlejší výměnu měření a snížení zatížení sítě. Řeší problém relativního určování polohy mezi blízkými zařízeními, což je nezbytné pro aplikace jako detekce zranitelných účastníků silničního provozu nebo koordinace autonomního řízení, tím, že poskytuje standardizovanou, na signálu založenou techniku měření vzdálenosti, která doplňuje další senzory, jako je radar nebo lidar.

## Klíčové vlastnosti

- Měří absolutní čas příchodu sidelinkových polohovacích signálů pro výpočet vzdálenosti
- Podporuje použití s jednou nebo více referencemi pro určování polohy založené na trilateraci
- Závisí na přesné časové synchronizaci mezi vysílačem a přijímačem, často prostřednictvím GNSS nebo sítě
- Využívá vyhrazené sidelinkové polohovací referenční signály (SL-PRS) pro přesný časový odhad
- Umožňuje jak UE-bázované, tak síťově asistované režimy určování polohy
- Integruje se s protokoly pro určování polohy 3GPP pro hlášení měření a doručování pomocných dat

## Související pojmy

- [SL-TDOA – Sidelink Time Difference Of Arrival](/mobilnisite/slovnik/sl-tdoa/)
- [SL-PRS – Sidelink Positioning Reference Signals](/mobilnisite/slovnik/sl-prs/)

## Definující specifikace

- **TS 37.571** (Rel-19) — UE Conformance for Positioning
- **TS 38.355** (Rel-19) — Sidelink Positioning Protocol (SLPP)

---

📖 **Anglický originál a plná specifikace:** [SL-TOA na 3GPP Explorer](https://3gpp-explorer.com/glossary/sl-toa/)
