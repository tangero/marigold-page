---
slug: "fta"
url: "/mobilnisite/slovnik/fta/"
type: "slovnik"
title: "FTA – Fine Time Assistance"
date: 2025-01-01
abbr: "FTA"
fullName: "Fine Time Assistance"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/fta/"
summary: "Metoda určování polohy, při níž server polohových služeb poskytuje uživatelskému zařízení (UE) přesné časové informace týkající se buněčných základnových stanic, aby zvýšil přesnost jeho vlastního výp"
---

FTA je metoda síťově asistovaného určování polohy, při níž server polohových služeb poskytuje uživatelskému zařízení (UE) přesné časové informace základnových stanic za účelem zvýšení přesnosti vlastního výpočtu polohy založeného na OTDOA.

## Popis

Fine Time Assistance (FTA) je síťově asistovaná funkce pro určování polohy definovaná v rámci protokolu 3GPP LTE Positioning Protocol ([LPP](/mobilnisite/slovnik/lpp/)) a NR Positioning Protocol (NRPP). Jejím hlavním účelem je doručit závěři přesné časové informace z sítě k uživatelskému zařízení (UE) za účelem korekce chyb v jeho lokálním časovém referenčním signálu, čímž se významně zvyšuje přesnost metod určování polohy založených na downlinku, především metody [OTDOA](/mobilnisite/slovnik/otdoa/) (Observed Time Difference of Arrival). Při OTDOA měří uživatelské zařízení časový rozdíl příchodu polohových referenčních signálů ([PRS](/mobilnisite/slovnik/prs/)) z více sousedních buněk. Jakákoli chyba ve vnitřních hodinách uživatelského zařízení se přímo promítne do chyby těchto změřených časových rozdílů a následně i do vypočítané polohy.

Z architektonického hlediska se FTA týká funkce Location Management Function ([LMF](/mobilnisite/slovnik/lmf/)) v 5G core síti nebo Evolved Serving Mobile Location Center ([E-SMLC](/mobilnisite/slovnik/e-smlc/)) v LTE. Tyto servery mají přístup k přesným časovým informacím týkajícím se okamžiků vysílání PRS ze všech základnových stanic (gNB nebo [eNB](/mobilnisite/slovnik/enb/)) v síti, které jsou často synchronizovány pomocí [GPS](/mobilnisite/slovnik/gps/) nebo protokolu [IEEE](/mobilnisite/slovnik/ieee/) 1588 Precision Time Protocol (PTP). Server zabalí tyto časové informace – jako je absolutní časování konkrétní PRS příležitosti nebo relativní časování mezi různými buňkami – do pomocné zprávy LPP/NRPP zaslané uživatelskému zařízení. Uživatelské zařízení použije tyto data 'fine time assistance' ke kalibraci svých měření, čímž efektivně sladí své okno pozorování s hlavní časovou referencí sítě.

Technický princip spočívá v tom, že uživatelské zařízení přijme data FTA, která typicky zahrnují referenční čas (např. číslo systémového rámce a posunutí podrámce) pro konkrétní buňku spolu s očekávaným rozdílem reálného času (RTD) mezi touto referenční buňkou a dalšími sousedními buňkami. Uživatelské zařízení porovná svůj vlastní změřený čas příchodu (TOA) pro PRS z referenční buňky s referenčním časem poskytnutým sítí. Rozdíl představuje časovou chybu uživatelského zařízení. Tento odhad chyby je následně použit jako korekce pro měření TOA ze všech ostatních sousedních buněk před výpočtem hodnot rozdílu času příchodu (TDOA). Tento proces zmírňuje chyby způsobené driftem a nepřesnostmi hodin uživatelského zařízení, které jsou hlavním zdrojem chyb u hodin uživatelských zařízení spotřebitelské třídy. FTA je obzvláště užitečné pro určování polohy v interiéru nebo v prostředí se slabou geometrií (např. tam, kde jsou buňky téměř kolineární), kde i malé časové chyby mohou způsobit velké chyby v určení polohy.

## K čemu slouží

Fine Time Assistance bylo vyvinuto, aby překonalo základní omezení uživatelským zařízením založeného a asistovaného určování polohy OTDOA: nízkou kvalitu a nestabilitu vnitřních hodin typického uživatelského zařízení. Spotřebitelská zařízení používají levné oscilátory náchylné k driftu, které nejsou synchronizovány s časováním mobilní sítě. Tato chyba hodin zavádí společný bias do všech měření downlinkových signálů, což vážně snižuje přesnost určování polohy, často na úroveň nepřijatelnou pro mnoho komerčních služeb a služeb tísňového volání (E911).

Vytvoření FTA bylo motivováno potřebou přesnějších služeb založených na poloze bez nutnosti vybavit každé uživatelské zařízení drahými hodinami s vysokou přesností. Představuje posun složitosti ze zařízení do sítě a využívá inherentně přesné a synchronizované časové infrastruktury sítě. FTA řeší omezení základního OTDOA, které mohlo poskytovat přesnost pouze v řádu desítek až stovek metrů. Poskytnutím síťově kalibrované časové asistence uživatelskému zařízení umožňuje FTA dosáhnout metodě OTDOA přesnosti srovnatelné s GPS nebo ji doplňující, zejména v náročném prostředí, jako jsou městské kaňony nebo hluboké interiéry, kde nejsou dostupné signály satelitů. Tím jsou splněny regulační požadavky na lokalizaci tísňových volání a umožněna nová generace komerčních aplikací, jako je navigace v interiéru, sledování aktiv a analytika založená na poloze.

## Klíčové vlastnosti

- Poskytuje uživatelskému zařízení přesné časové informace odvozené ze sítě prostřednictvím LPP/NRPP
- Opravuje chyby lokálních hodin uživatelského zařízení pro měření downlinkových signálů
- Významně zvyšuje přesnost určování polohy metodou OTDOA
- Umožňuje přesnost určování polohy pod 10 metrů za příznivých podmínek
- Využívá synchronizované časování sítě z GNSS nebo PTP
- Definováno pro architektury určování polohy jak LTE (LPP), tak 5G NR (NRPP)

## Související pojmy

- [OTDOA – Observed Time Difference Of Arrival](/mobilnisite/slovnik/otdoa/)
- [LPP – LTE Positioning Protocol](/mobilnisite/slovnik/lpp/)
- [PRS – Positioning Reference Signal](/mobilnisite/slovnik/prs/)
- [LMF – Location Management Function](/mobilnisite/slovnik/lmf/)

## Definující specifikace

- **TR 22.816** (Rel-14) — 3GPP TV Service Enhancement Technical Report
- **TS 36.355** (Rel-19) — LTE Positioning Protocol (LPP)
- **TS 37.355** (Rel-19) — LTE Positioning Protocol (LPP)

---

📖 **Anglický originál a plná specifikace:** [FTA na 3GPP Explorer](https://3gpp-explorer.com/glossary/fta/)
