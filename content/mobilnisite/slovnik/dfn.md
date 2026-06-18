---
slug: "dfn"
url: "/mobilnisite/slovnik/dfn/"
type: "slovnik"
title: "DFN – Direct Frame Number"
date: 2025-01-01
abbr: "DFN"
fullName: "Direct Frame Number"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/dfn/"
summary: "DFN je číslovací mechanismus rámců používaný v LTE a 5G NR pro přímou komunikaci mezi zařízeními v operacích přímého spojení (sidelink). Poskytuje společnou časovou referenci pro komunikaci typu zaříz"
---

DFN je číslovací mechanismus rámců používaný v LTE a 5G NR přímém spojení (sidelink) k poskytnutí společné časové reference pro komunikaci typu zařízení-zařízení (Device-to-Device) a vozidlo-vše (Vehicle-to-Everything), umožňující synchronizaci bez nepřetržitého pokrytí sítí.

## Popis

Direct Frame Number (DFN) je klíčový mechanismus časové reference specifikovaný ve standardech 3GPP pro komunikaci přímým spojením (sidelink), primárně dokumentovaný v TS 36.331 (LTE) a TS 38.331/38.355 (5G NR). DFN funguje jako nezávislý systém číslování rámců, který poskytuje společnou časovou referenci pro zařízení komunikující přímo mimo tradiční rámec uplink/downlink. Na rozdíl od System Frame Number ([SFN](/mobilnisite/slovnik/sfn/)) používaného v celulární komunikaci mezi základnovými stanicemi a UE je DFN speciálně navržen pro scénáře komunikace zařízení-zařízení ([D2D](/mobilnisite/slovnik/d2d/)), kde si zařízení musí koordinovat přímo mezi sebou.

Architektura DFN funguje v rámci rozhraní přímého spoje (sidelink), což je přímé rádiové spojení mezi uživatelskými zařízeními bez průchodu síťovou infrastrukturou. Každé zařízení udržuje vlastní čítač DFN, který se zvyšuje s každým rádiovým rámcem, typicky o délce 10 milisekund. Hodnota DFN se pohybuje od 0 do 1023 v LTE a je rozšířena v 5G NR pro zvládnutí složitějších scénářů synchronizace. Zařízení synchronizují své čítače DFN prostřednictvím synchronizačních signálů vysílaných referenčními zdroji synchronizace, kterými mohou být [eNB](/mobilnisite/slovnik/enb/)/gNB, časování globálního navigačního satelitního systému ([GNSS](/mobilnisite/slovnik/gnss/)) nebo jiná UE fungující jako synchronizační zdroje.

Klíčové komponenty systému DFN zahrnují samotný čítač DFN, bloky synchronizačních signálů (SSB) pro distribuci časové reference a mechanismy alokace prostředků, které používají DFN jako časovou kotvu. V provozu zařízení využívají DFN k určení, kdy vysílat a přijímat kanály přímého spoje včetně fyzického řídicího kanálu přímého spoje ([PSCCH](/mobilnisite/slovnik/pscch/)), fyzického sdíleného kanálu přímého spoje ([PSSCH](/mobilnisite/slovnik/pssch/)) a fyzického vysílacího kanálu přímého spoje ([PSBCH](/mobilnisite/slovnik/psbch/)). Hodnota DFN pomáhá zařízením identifikovat konkrétní podrámce či sloty alokované pro komunikaci přímým spojem v rámci celkové struktury rámce.

DFN hraje klíčovou roli v alokaci prostředků pro komunikaci přímým spojem prostřednictvím mechanismů, jako je alokace prostředků režimu 2 v LTE a NR sidelink. Zařízení používají časování založené na DFN k implementaci procedur snímání (sensing), kdy monitorují prostředky v průběhu více cyklů DFN k identifikaci dostupných přenosových příležitostí. DFN poskytuje časový rámec pro intervaly rezervace prostředků, kde si zařízení mohou rezervovat prostředky pro budoucí přenosy uvedením odsazení (offset) DFN mezi rezervací a skutečným přenosem. To umožňuje efektivní využití prostředků a minimalizuje kolize v prostředích s distribuovaným plánováním.

V pokročilých implementacích, zejména pro 5G NR [V2X](/mobilnisite/slovnik/v2x/), DFN podporuje vylepšené požadavky na přesnost synchronizace pro komunikaci vysokorychlostních vozidel. Systém zahrnuje mechanismy pro úpravu a udržování DFN během scénářů mobility, včetně předávání služeb (handover) mezi různými synchronizačními zdroji. DFN také spolupracuje s protokoly vyšších vrstev pro služby objevování (discovery), komunikace a vysílání (broadcast) přímým spojem, čímž poskytuje základní časový základ, který umožňuje spolehlivou přímou komunikaci mezi zařízeními ve scénářích s pokrytím i bez pokrytí sítí.

## K čemu slouží

DFN byl vytvořen, aby řešil základní výzvu vytvoření společné časové reference pro přímou komunikaci mezi zařízeními v sítích LTE a 5G. Před implementací DFN se celulární systémy spoléhaly výhradně na časování základnových stanic (SFN) pro veškerou komunikaci, což znemožňovalo spolehlivou přímou komunikaci mezi zařízeními bez nepřetržitého pokrytí sítí. Toto omezení bylo zvláště problematické pro scénáře veřejné bezpečnosti, kde si první respondenti potřebují komunikovat přímo během výpadků sítě nebo v odlehlých oblastech bez celulární infrastruktury.

Vývoj DFN motivovala rostoucí potřeba služeb založených na blízkosti (proximity-based services) a vznik požadavků komunikace V2X. Tradiční celulární časovací mechanismy byly pro operace přímého spoje nedostatečné, protože vyžadovaly, aby zařízení udržovala synchronizaci s potenciálně vzdálenými základnovými stanicemi, což bylo pro přímou komunikaci mezi blízkými zařízeními nepraktické. DFN poskytl nezávislý časovací rámec, který mohl být udržován prostřednictvím různých synchronizačních zdrojů, včetně GNSS, jiných UE nebo zbytkového síťového časování, což umožnilo robustní přímou komunikaci i v náročných prostředích.

DFN řeší několik kritických problémů v moderních bezdrátových systémech: umožňuje efektivní alokaci prostředků pro komunikaci přímým spojem tím, že poskytuje společnou časovou referenci pro distribuované plánovací algoritmy; podporuje synchronizaci ve scénářích bez pokrytí sítí, kde tradiční celulární časování není dostupné; a usnadňuje pokročilé aplikace V2X vyžadující přesnou časovou koordinaci mezi vysokorychlostními vozidly. Oddělením časování přímého spoje od časování celulární sítě umožňuje DFN koexistenci tradiční celulární komunikace a přímé komunikace mezi zařízeními v rámci stejného spektra, čímž maximalizuje spektrální efektivitu a zároveň podporuje různorodé komunikační paradigmy.

## Klíčové vlastnosti

- Poskytuje nezávislé číslování rámců pro komunikaci přímým spojením (sidelink) oddělené od celulárního SFN
- Podporuje synchronizaci z více zdrojů včetně GNSS, eNB/gNB a dalších UE
- Umožňuje alokaci prostředků a plánování pro komunikaci D2D a V2X
- Usnadňuje provoz ve scénářích s pokrytím i bez pokrytí sítí
- Podporuje distribuované plánovací mechanismy prostřednictvím rezervace prostředků založené na DFN
- Poskytuje časový základ pro pokročilé služby přímého spoje včetně objevování (discovery) a vysílání (broadcast)

## Definující specifikace

- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification
- **TS 38.331** (Rel-19) — NR Radio Resource Control (RRC) Protocol Specification
- **TS 38.355** (Rel-19) — Sidelink Positioning Protocol (SLPP)

---

📖 **Anglický originál a plná specifikace:** [DFN na 3GPP Explorer](https://3gpp-explorer.com/glossary/dfn/)
