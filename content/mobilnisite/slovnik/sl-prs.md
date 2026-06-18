---
slug: "sl-prs"
url: "/mobilnisite/slovnik/sl-prs/"
type: "slovnik"
title: "SL-PRS – Sidelink Positioning Reference Signals"
date: 2025-01-01
abbr: "SL-PRS"
fullName: "Sidelink Positioning Reference Signals"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/sl-prs/"
summary: "Referenční signály speciálně navržené pro sidelinkovou komunikaci, které umožňují přesná pozicování měření mezi zařízeními. Usnadňují měření doby příchodu (TOA), úhlu příchodu (AOA) a další metriky pr"
---

SL-PRS je soubor referenčních signálů navržených pro sidelinkovou komunikaci, který umožňuje přesná pozicování měření mezi zařízeními pro určení polohy v aplikacích ProSe a V2X.

## Popis

SL-PRS (Sidelink Positioning Reference Signals) jsou specializované referenční signály definované ve standardech 3GPP pro sidelinkovou komunikaci, jejichž cílem je umožnit přesná pozicování měření mezi uživatelskými zařízeními (UE) bez nutnosti spoléhat se na síťovou infrastrukturu. Tyto signály jsou přenášeny přes rozhraní PC5, což je přímá komunikace mezi zařízeními, a slouží k odhadu parametrů, jako je doba příchodu ([TOA](/mobilnisite/slovnik/toa/)), úhel příchodu ([AOA](/mobilnisite/slovnik/aoa/)) a časový rozdíl referenčních signálů ([RSTD](/mobilnisite/slovnik/rstd/)). Analýzou těchto měření mohou UE vypočítat svou relativní nebo absolutní polohu, což je klíčové pro aplikace jako komunikace mezi vozidlem a okolím ([V2X](/mobilnisite/slovnik/v2x/)), služby založené na blízkosti ([ProSe](/mobilnisite/slovnik/prose/)) a operace veřejné bezpečnosti. Specifikace pokrývající SL-PRS zahrnují 37.571 pro testování, 38.300 pro celkový popis NR, 38.305 pro služby určování polohy fáze 2, 38.331 pro řízení rádiových zdrojů ([RRC](/mobilnisite/slovnik/rrc/)) a 38.355 pro protokoly sidelinkového určování polohy, což zajišťuje komplexní rámec pro implementaci.

Architektura SL-PRS zahrnuje generování, vysílání a příjem těchto signálů ve fyzické vrstvě sidelinku. SL-PRS jsou typicky vloženy do sidelinkového zdrojového rastru, podobně jako referenční signály pro určování polohy v downlinku nebo uplinku v celulárních sítích, ale jsou optimalizovány pro charakteristiky komunikace přes PC5. Jsou navrženy se specifickými sekvencemi a vzory, aby minimalizovaly interferenci a maximalizovaly přesnost v různých prostředích, jako jsou scénáře s vysokou mobilitou ve V2X. Mezi klíčové komponenty patří vysílající UE, které vysílá SL-PRS podle nakonfigurovaných parametrů, jako je šířka pásma, periodicita a výkon; přijímající UE, které měří signály pomocí svých přijímacích řetězců; a pozicovací algoritmy, které tato měření zpracovávají a odvozují odhady polohy. Signály mohou být vysílány všesměrově pro více UE nebo jednosměrně pro cílené určování polohy, což podporuje flexibilní případy použití.

SL-PRS fungují tak, že využívají ortogonalitu a předvídatelnost svých sekvencí k umožnění přesného měření vlastností signálu. Když UE vysílá SL-PRS, sousední UE tyto signály přijímají a měří čas jejich přícholu vzhledem ke svým vnitřním hodinám. Kombinací měření z více vysílačů lze použít techniky jako multilaterace nebo triangulace k určení polohy. Například ve scénáři V2X si vozidla vyměňují SL-PRS k odhadu vzdáleností mezi sebou, což umožňuje systémy pro zabránění kolizím. Signály jsou konfigurovány prostřednictvím protokolů vyšších vrstev, jako jsou zprávy RRC (Radio Resource Control) definované v 38.331, které nastavují parametry jako přidělení zdrojů a vzory utlumení pro snížení interference. SL-PRS mohou být navíc integrovány s jinými metodami určování polohy, jako je [GNSS](/mobilnisite/slovnik/gnss/) nebo celulární určování polohy, aby se zvýšila přesnost prostřednictvím hybridních přístupů. Jejich role v síti je klíčová pro umožnění autonomních sidelinkových lokalizačních služeb, což snižuje závislost na externích systémech, jako je [GPS](/mobilnisite/slovnik/gps/), která nemusí být dostupná v městských kaňonech nebo vnitřních prostorech.

Návrh SL-PRS zohledňuje výzvy, jako je Dopplerův posun v prostředích s vysokou rychlostí a vícecestné šíření, a zahrnuje funkce jako delší sekvence nebo přeskakování kmitočtů pro zmírnění těchto účinků. Měření odvozená ze SL-PRS jsou hlášena pozicovacím entitám, což mohou být samotná UE nebo centralizované servery, pro další zpracování. To umožňuje aplikace od jednoduchého relativního určování polohy pro sociální sítě v ProSe až po vysoce přesné absolutní určování polohy pro autonomní řízení. Standardizací SL-PRS zajišťuje 3GPP, že zařízení od různých výrobců mohou bezproblémově spolupracovat, což podporuje široké přijetí v nově vznikajících technologiích.

## K čemu slouží

SL-PRS byly vytvořeny, aby řešily nedostatek standardizovaných referenčních signálů pro určování polohy v sidelinkové komunikaci, což se stalo úzkým hrdlem, protože aplikace V2X a ProSe vyžadovaly přesné povědomí o poloze. Před jejich zavedením se sidelinkové určování polohy spoléhalo na ad-hoc metody nebo opětovně používalo celulární signály, což vedlo k podoptimální přesnosti a problémům s interoperabilitou. V bezpečnostně kritických scénářích, jako je autonomní řízení nebo zásahy v nouzových situacích, je přesné určení polohy nezbytné pro zabránění kolizím a koordinaci, ale stávající řešení, jako je GPS, často trpí omezeními, jako je blokování signálu nebo latence. SL-PRS poskytují vyhrazený, optimalizovaný prostředek pro zařízení, aby přímo měřila své relativní polohy, čímž zvyšují spolehlivost a výkon v přímých komunikačních sítích.

Historicky se určování polohy v sítích 3GPP zaměřovalo na referenční signály v downlinku a uplinku, jako je PRS v LTE nebo TRS v NR, které závisí na infrastruktuře základnových stanic. S rozšířením sidelinkových schopností od Rel-14 rostla potřeba podobných signálů přizpůsobených pro komunikaci mezi zařízeními. SL-PRS se objevily v Rel-18, aby tuto mezeru zaplnily, přičemž motivací byly požadavky automobilového průmyslu na přesnost na úrovni centimetrů ve V2X systémech. Umožňují vozidlům vnímat své okolí bez neustálé asistence sítě, což podporuje pokročilé asistenty řidiče (ADAS) a jízdu v koloně. Tento vývoj odráží posun směrem k decentralizované inteligenci, kde zařízení spolupracují na dosažení složitých úkolů nezávisle.

Vývoj SL-PRS také podporuje regulatorní a komerční hnací síly, jako je soulad s bezpečnostními standardy pro připojená vozidla a umožnění nových lokalizačních služeb v IoT. Poskytnutím standardizované struktury signálu snižují složitost implementace a podporují růst ekosystému, čímž řeší fragmentaci pozorovanou u proprietárních sidelinkových řešení. To je v souladu s cílem 3GPP vytvořit jednotný rámec pro 5G a další generace, kde se sidelinkové určování polohy stane nedílnou součástí celkového portfolia lokalizačních služeb, což zvýší schopnosti jak pro operace pokryté sítí, tak pro samostatné operace.

## Klíčové vlastnosti

- Vyhrazené referenční signály pro sidelinkové určování polohy přes rozhraní PC5
- Podporuje měření, jako je doba příchodu (TOA) a úhel příchodu (AOA), pro přesný odhad polohy
- Konfigurovatelné parametry prostřednictvím RRC pro šířku pásma, periodicitu a přidělení zdrojů
- Navrženo pro prostředí s vysokou mobilitou s odolností vůči Dopplerovým a vícecestným jevům
- Umožňuje jak relativní, tak absolutní určování polohy v aplikacích ProSe a V2X
- Integruje se s hybridními metodami určování polohy kombinujícími sidelink, celulární síť a GNSS

## Související pojmy

- [PRS – Positioning Reference Signal](/mobilnisite/slovnik/prs/)
- [SL-MO-LR – Sidelink Mobile Originating Location Request](/mobilnisite/slovnik/sl-mo-lr/)
- [SL-MT-LR – Sidelink Mobile Terminating Location Request](/mobilnisite/slovnik/sl-mt-lr/)
- [V2X – Vehicle-to-Everything Application Server](/mobilnisite/slovnik/v2x/)

## Definující specifikace

- **TS 37.571** (Rel-19) — UE Conformance for Positioning
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TS 38.305** (Rel-19) — NG-RAN UE Positioning Stage 2
- **TS 38.331** (Rel-19) — NR Radio Resource Control (RRC) Protocol Specification
- **TS 38.355** (Rel-19) — Sidelink Positioning Protocol (SLPP)

---

📖 **Anglický originál a plná specifikace:** [SL-PRS na 3GPP Explorer](https://3gpp-explorer.com/glossary/sl-prs/)
