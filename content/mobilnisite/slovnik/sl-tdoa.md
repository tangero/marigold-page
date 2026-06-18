---
slug: "sl-tdoa"
url: "/mobilnisite/slovnik/sl-tdoa/"
type: "slovnik"
title: "SL-TDOA – Sidelink Time Difference Of Arrival"
date: 2025-01-01
abbr: "SL-TDOA"
fullName: "Sidelink Time Difference Of Arrival"
category: "Radio Access Network"
segment: "Testing"
canonical: "https://3gpp-explorer.com/glossary/sl-tdoa/"
summary: "SL-TDOA je metoda určování polohy pro zařízení na postranním spoji (sidelink), která vypočítává polohu měřením časových rozdílů příchodu signálů z více referenčních vysílačů. Umožňuje přesné určování"
---

SL-TDOA je metoda určování polohy na postranním spoji (sidelink), která vypočítává polohu zařízení měřením časových rozdílů příchodu signálů z více referenčních vysílačů, a umožňuje tak přesné určování polohy mezi zařízeními pro služby jako V2X.

## Popis

Sidelink Time Difference Of Arrival (SL-TDOA) je technika určování polohy standardizovaná v 3GPP pro scénáře přímé komunikace mezi zařízeními ([D2D](/mobilnisite/slovnik/d2d/)), zejména v rámci rozhraní postranního spoje (sidelink) používaného pro komunikaci vozidlo-se-vším ([V2X](/mobilnisite/slovnik/v2x/)) a služby založené na blízkosti. Funguje tak, že cílové zařízení, například vozidlo nebo chodcovské UE, přijímá referenční signály pro určování polohy ([PRS](/mobilnisite/slovnik/prs/)) nebo jiné známé signály vysílané z více sousedních referenčních uzlů s podporou postranního spoje, což mohou být jiná vozidla, jednotky na okraji vozovky ([RSU](/mobilnisite/slovnik/rsu/)) nebo infrastruktura. Každý referenční uzel vysílá své signály s přesným časováním, často synchronizovaným prostřednictvím globálního navigačního satelitního systému ([GNSS](/mobilnisite/slovnik/gnss/)) nebo síťového časování. Cílové zařízení měří čas příchodu ([TOA](/mobilnisite/slovnik/toa/)) těchto signálů od každé reference. Protože přesné časy vysílání z referencí jsou známé nebo lze je odvodit (např. pomocí časových značek nebo společné synchronizace), zařízení vypočítá časový rozdíl příchodu (TDOA) mezi dvojicemi příchozích signálů. Tato měření TDOA odpovídají hyperbolickým polohovým čarám; průsečík více hyperbol, odvozených z hodnot TDOA mezi několika referenčními dvojicemi, určuje polohu cíle ve dvou nebo třech rozměrech. Metoda vyžaduje alespoň tři nebo čtyři referenční uzly pro 2D nebo 3D určování polohy, v závislosti na geometrii.

Architektura pro SL-TDOA zahrnuje několik klíčových komponent: cílové uživatelské zařízení (UE) provádějící měření, referenční UE nebo RSU vysílající polohové signály a případně funkci správy polohy ([LMF](/mobilnisite/slovnik/lmf/)) v síti pro poskytování pomocných dat a výpočet polohy, pokud se používá síťový výpočet. V postranním spoji může být určování polohy založeno na UE (kde cílové UE vypočítává svou vlastní polohu), asistováno UE (kde UE odesílá měření do sítě pro výpočet) nebo založeno na síti. Pro SL-TDOA mohou pomocná data zahrnovat polohy referenčních uzlů, konfigurace signálů a časové informace, poskytované prostřednictvím rozhraní Uu ze sítě nebo přímo přes postranní spoj. Použité signály fyzické vrstvy mohou být vyhrazené referenční signály pro určování polohy na postranním spoji (PRS), definované ve specifikacích jako 38.211, nebo přizpůsobené synchronizační signály nebo referenční signály pro informace o stavu kanálu ([CSI-RS](/mobilnisite/slovnik/csi-rs/)) nakonfigurované pro určování polohy. Měření jsou hlášena podle protokolů v 37.571 (shoda UE) a 38.355 (protokoly pro určování polohy).

Úlohou SL-TDOA je poskytovat přesné relativní nebo absolutní určování polohy ve scénářích, kde jsou signály GNSS slabé nebo nedostupné, jako jsou městské kaňony, tunely nebo vnitřní parkovací garáže, a to využitím hustého nasazení zařízení s postranním spojem. Zvyšuje spolehlivost aplikací V2X, jako je zabránění kolizím, kooperativní vnímání a automatizované řízení, tím, že zajišťuje, aby vozidla znala vzájemné polohy s vysokou přesností. Tato technika je nedílnou součástí rámce pro určování polohy na postranním spoji 3GPP, doplňuje další metody jako SL-TOA nebo určování polohy založené na úhlu a podporuje jak bezpečnostně kritické, tak komerční polohové služby v ekosystémech 5G NR a LTE-V2X.

## K čemu slouží

SL-TDOA byl zaveden, aby řešil rostoucí potřebu přesného a spolehlivého určování polohy v přímé komunikaci mezi zařízeními, zejména pro bezpečnostní aplikace V2X. Před jeho standardizací se určování polohy v celulárních sítích primárně spoléhalo na metody v uplinku nebo downlinku (např. UTDOA, OTDOA), které vyžadují infrastrukturní základnové stanice, jež mohou být v odlehlých oblastech nebo při katastrofách řídké nebo nedostupné. Určování polohy na postranním spoji, včetně SL-TDOA, umožňuje vozidlům a dalším zařízením určovat polohy nezávisle nebo s minimální síťovou asistencí, čímž zvyšuje robustnost. Motivace vychází z autonomního řízení a pokročilých služeb V2X, kde jsou přesnost na úrovni submětru a nízká latence kritické pro rozhodování v reálném čase, jako je asistence pohybu na křižovatkách nebo varování před nouzovým brzděním.

Historický kontext ukazuje, že dřívější verze 3GPP (Rel-14/15) se zaměřovaly na základní komunikaci na postranním spoji pro V2X, ale postrádaly standardizované techniky určování polohy. Jak se případy užití v Rel-16/17 vyvíjely směrem k pokročilé automatizaci, stalo se zřejmým omezení spoléhání se pouze na GNSS – signály GNSS jsou náchylné k blokování, mnohocestnému šíření a podvrhu. SL-TDOA poskytuje doplňkovou nebo alternativní metodu, která využívá samotná množící se zařízení s postranním spojem jako referenční body, čímž vytváří ad-hoc polohovou síť. Tím se řeší problém mezer v pokrytí a zlepšuje se přesnost v náročném prostředí, což v konečném důsledku podporuje vizi 3GPP o všudypřítomném určování polohy s vysokou integritou pro připojená vozidla a zařízení IoT.

## Klíčové vlastnosti

- Umožňuje určování polohy na základě měření časových rozdílů z více referenčních uzlů na postranním spoji
- Podporuje režimy určování polohy založené na UE, asistované UE a založené na síti pro flexibilitu
- Využívá referenční signály pro určování polohy (PRS) nebo jiné signály postranního spoje pro měření
- Funguje v prostředích bez GNSS využitím konektivity mezi zařízeními
- Poskytuje vysokou přesnost vhodnou pro bezpečnostně kritické aplikace V2X, jako je zabránění kolizím
- Integruje se s architekturou pro určování polohy 3GPP prostřednictvím protokolů definovaných v 38.355 a 37.571

## Související pojmy

- [SL-TOA – Sidelink Time Of Arrival](/mobilnisite/slovnik/sl-toa/)
- [SL-PRS – Sidelink Positioning Reference Signals](/mobilnisite/slovnik/sl-prs/)
- [V2X – Vehicle-to-Everything Application Server](/mobilnisite/slovnik/v2x/)

## Definující specifikace

- **TS 37.571** (Rel-19) — UE Conformance for Positioning
- **TS 38.355** (Rel-19) — Sidelink Positioning Protocol (SLPP)

---

📖 **Anglický originál a plná specifikace:** [SL-TDOA na 3GPP Explorer](https://3gpp-explorer.com/glossary/sl-tdoa/)
