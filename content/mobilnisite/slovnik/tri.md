---
slug: "tri"
url: "/mobilnisite/slovnik/tri/"
type: "slovnik"
title: "TRI – Transmit Rank Indicator"
date: 2025-01-01
abbr: "TRI"
fullName: "Transmit Rank Indicator"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/tri/"
summary: "Zpětnovazební parametr v MIMO systémech udávající doporučený počet nezávislých datových proudů (vrstev), které může UE podporovat pro downlinkový přenos. Je klíčový pro optimalizaci zisku prostorového"
---

TRI je zpětnovazební parametr v MIMO systémech udávající doporučený počet nezávislých datových proudů, které může UE podporovat pro downlinkový přenos za účelem optimalizace prostorového multiplexu.

## Popis

Transmit Rank Indicator (TRI) je klíčovou součástí mechanismu zpětné vazby informace o stavu kanálu (Channel State Information, [CSI](/mobilnisite/slovnik/csi/)) v systémech 3GPP New Radio (NR) a vyvinutého LTE. Funguje v rámci technologie Multiple-Input Multiple-Output ([MIMO](/mobilnisite/slovnik/mimo/)), konkrétně pro downlinkové přenosy z gNB (nebo [eNB](/mobilnisite/slovnik/enb/)) k uživatelskému zařízení (UE). TRI je celočíselná hodnota hlášená UE síti, která doporučuje optimální vysílací rank – v podstatě počet prostorově multiplexovaných vrstev, které lze současně vysílat na stejném časově-frekvenčním zdroji. Toto doporučení vychází z odhadu podmínek downlinkového kanálu provedeného UE, včetně faktorů jako je hodnost kanálové matice, poměr signálu k šumu a interferenci ([SINR](/mobilnisite/slovnik/sinr/)) a schopnosti přijímače.

Generování TRI zahrnuje sofistikované postupy odhadu a měření kanálu na straně UE. UE periodicky nebo aperiodicky měří referenční signály, jako je Channel State Information Reference Signal ([CSI-RS](/mobilnisite/slovnik/csi-rs/)). Na základě těchto měření vypočítá kanálovou matici a provede singulární rozklad (SVD) nebo podobnou analýzu, aby určila počet dostupných silných vlastních módů (neboli prostorových kanálů). Toto číslo, omezené minimem z počtu vysílacích antén na gNB, přijímacích antén na UE a inherentní hodnosti kanálu, tvoří základ pro TRI. UE pak tuto hodnotu hlásí, často společně s dalšími parametry CSI, jako je Channel Quality Indicator ([CQI](/mobilnisite/slovnik/cqi/)) a Precoding Matrix Indicator ([PMI](/mobilnisite/slovnik/pmi/)), prostřednictvím uplinkových řídicích kanálů (např. [PUCCH](/mobilnisite/slovnik/pucch/)) nebo sdílených kanálů (např. PUSCH).

Po přijetí TRI plánovač gNB použije tuto informaci spolu s dalšími faktory, jako je vytížení přenosů a schopnosti UE, k rozhodnutí o skutečném vysílacím ranku pro následné downlinkové přenosy. Vyšší TRI (např. rank 4 nebo 8) umožňuje vyšší špičkové datové rychlosti díky prostorovému multiplexu, ale vyžaduje příznivé podmínky kanálu (např. bohaté rozptylové prostředí, vysoký SINR). Nižší TRI (např. rank 1 nebo 2) může být zvoleno za špatných podmínek pro zajištění robustnosti, často s přechodem na vysílací diverzitu nebo beamforming. TRI tedy umožňuje dynamickou adaptaci ranku, která je zásadní pro maximalizaci spektrální účinnosti a propustnosti v moderních bezdrátových systémech. Jeho přesnost přímo ovlivňuje výkon MIMO, což z něj činí klíčový prvek pro vysoké datové rychlosti slibované 5G NR a pokročilým 4G LTE.

## K čemu slouží

Transmit Rank Indicator byl zaveden, aby řešil výzvu efektivního využití prostorového rozměru v MIMO kanálech pro downlinkový přenos. Rané implementace MIMO často používaly pevné nebo polostatické konfigurace ranku, které se nedokázaly přizpůsobit rychle se měnícím rádiovým podmínkám. To vedlo buď k nedostatečnému využití kanálu (použití příliš nízkého ranku za dobrých podmínek), nebo k chybám přenosu (použití příliš vysokého ranku za špatných podmínek). TRI poskytuje dynamický mechanismus s asistencí UE, který informuje síť o okamžitě podporovatelném počtu prostorových vrstev, což umožňuje optimální prostorový multiplex.

Jeho vytvoření bylo motivováno potřebou sofistikovanější adaptace spoje přesahující pouhou úpravu výkonu a modulačně-kódového schématu (MCS). S nárůstem počtu antén u Massive MIMO a diverzifikací nasazení sítí (např. městské makrobuňky, vnitřní small cells) se prostorové charakteristiky kanálu staly velmi proměnlivými. TRI umožňuje systému přizpůsobit přenosovou strategii konkrétnímu prostředí šíření a schopnostem přijímače UE, čímž maximalizuje propustnost a spolehlivost. Je základním prvkem pro dosažení vysokých cílů spektrální účinnosti u 4G LTE-Advanced a 5G NR, kde je vícevrstvý přenos standardem.

Historicky se indikace ranku vyvinula z jednodušších schémat zpětné vazby MIMO. TRI, formalizovaný v 3GPP, poskytuje standardizovanou, kvantovanou metriku, která se hladce integruje s ostatními komponentami CSI. Řeší problém nesouladu prostorových předpokladů mezi vysílačem a přijímačem a zajišťuje, že gNB vysílá takový počet datových proudů, který je UE schopna úspěšně separovat a dekódovat, čímž minimalizuje retransmise a zvyšuje celkovou kapacitu systému.

## Klíčové vlastnosti

- Dynamické doporučení počtu prostorově multiplexovaných vrstev (vysílacího ranku) pro downlink.
- Integrální součást zpětné vazby informace o stavu kanálu (CSI) hlášené UE.
- Odvozeno z měření downlinkových referenčních signálů (např. CSI-RS) provedených UE.
- Umožňuje adaptivní přepínání mezi prostorovým multiplexem, vysílací diverzitou a beamformingem.
- Mezi omezující faktory patří hodnost kanálové matice, počet antén a schopnost přijímače UE.
- Hlášeno prostřednictvím uplinkových řídicích kanálů (PUCCH) nebo uplinkových sdílených kanálů (PUSCH).

## Související pojmy

- [CSI – Combined CS and IMS Services](/mobilnisite/slovnik/csi/)
- [MIMO – Multiple Input Multiple Output](/mobilnisite/slovnik/mimo/)
- [PMI – Precoding Matrix Indicator](/mobilnisite/slovnik/pmi/)
- [CQI – Channel Quality Indicator](/mobilnisite/slovnik/cqi/)

## Definující specifikace

- **TR 38.802** (Rel-14) — Study on New Radio Access Technology Physical Layer Aspects
- **TR 38.912** (Rel-19) — Study on New Radio Access Technology

---

📖 **Anglický originál a plná specifikace:** [TRI na 3GPP Explorer](https://3gpp-explorer.com/glossary/tri/)
