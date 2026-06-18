---
slug: "bm-iwf"
url: "/mobilnisite/slovnik/bm-iwf/"
type: "slovnik"
title: "BM-IWF – Broadcast Multicast Interworking Function"
date: 2025-01-01
abbr: "BM-IWF"
fullName: "Broadcast Multicast Interworking Function"
category: "Core Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/bm-iwf/"
summary: "Funkce pro propojení vysílání a multicastu (Broadcast Multicast Interworking Function, BM-IWF) je prvek jádra sítě, který umožňuje efektivní doručování vysílacích a multicastových služeb v sítích UMTS"
---

BM-IWF je prvek jádra sítě, který zprostředkovává rozhraní mezi centrem vysílacích/multicastových služeb a UTRANem, aby umožnil efektivní doručování vysílacího a multicastového obsahu v sítích UMTS.

## Popis

Funkce pro propojení vysílání a multicastu (Broadcast Multicast Interworking Function, BM-IWF) je klíčová architektonická komponenta v jádru sítě UMTS, která se specificky zabývá doručováním vysílacích a multicastových služeb. Umístěna mezi centrem vysílacích/multicastových služeb (Broadcast Multicast Service Center, [BM-SC](/mobilnisite/slovnik/bm-sc/)) a pozemní rádiovou přístupovou sítí UMTS ([UTRAN](/mobilnisite/slovnik/utran/)) slouží BM-IWF jako hlavní bod rozhraní pro převod vysílacích/multicastových protokolů na úrovni služeb na transportní mechanismy na úrovni sítě. Jejím hlavním účelem je umožnit efektivní distribuci dat typu point-to-multipoint napříč infrastrukturou UMTS, což dovoluje více uživatelům přijímat identický obsah současně bez nutnosti individuálních unicastových spojení pro každého účastníka.

Z architektonického hlediska se BM-IWF nachází v doméně jádra sítě a komunikuje s více síťovými prvky. Na straně služeb se připojuje k BM-SC pomocí protokolů založených na IP a přijímá proudy obsahu a řídicí informace služeb. Na síťové straně komunikuje s podpůrným uzlem [GPRS](/mobilnisite/slovnik/gprs/) (Serving GPRS Support Node, [SGSN](/mobilnisite/slovnik/sgsn/)) a bránovým podpůrným uzlem GPRS (Gateway GPRS Support Node, GGSN) za účelem vytvoření vhodných přenosových cest pro vysílací/multicastový provoz. BM-IWF provádí převod protokolů mezi protokoly aplikační vrstvy používanými BM-SC a transportními protokoly vyžadovanými sítí UMTS, čímž zajišťuje bezproblémové doručování obsahu při zachování kvality služby a efektivity sítě.

Funkčně BM-IWF zvládá několik klíčových operací včetně zpracování oznámení služby, správy členství, distribuce bezpečnostních klíčů a synchronizace obsahu. Když je vysílací nebo multicastová služba zahájena, BM-IWF přijímá parametry služby od BM-SC a vytváří potřebné vysílací/multicastové přenosové cesty v síti UMTS. Spravuje definice oblastí služby a určuje, které buňky by měly obsah vysílat na základě distribuce účastníků a topologie sítě. BM-IWF také hraje klíčovou roli v řízení mobility, neboť zajišťuje, aby uživatelé pohybující se mezi buňkami pokračovali v nepřerušeném příjmu vysílacích/multicastových služeb díky správným procedurám předávání.

Z pohledu protokolů implementuje BM-IWF specifická rozhraní definovaná ve specifikacích 3GPP. Rozhraní Gmb ji spojuje s BM-SC a přenáší řídicí informace služeb a proudy obsahu. BM-IWF komunikuje s prvky SGSN/GGSN pomocí standardních rozhraní UMTS upravených pro vysílací/multicastové operace. Komponenta zvládá mapování kvality služby (QoS), převádějící požadavky na QoS na úrovni služeb na odpovídající charakteristiky síťových přenosových cest. Také spravuje sběr účtovacích dat pro vysílací/multicastové služby a generuje záznamy o využití, které mohou být zpracovány účtovacími systémy.

Implementace BM-IWF se liší v závislosti na síťové architektuře a požadavcích služeb. V některých nasazeních může být integrována s jinými funkcemi jádra sítě, zatímco v jiných funguje jako samostatný síťový prvek. Bez ohledu na implementaci musí BM-IWF udržovat synchronizaci s časováním rádiové sítě, aby zajistila správnou koordinaci doručování obsahu napříč více buňkami. Také zvládá procedury obnovy po chybě, detekuje a reaguje na síťové poruchy, které by mohly ovlivnit kontinuitu vysílací/multicastové služby.

## K čemu slouží

BM-IWF byla vytvořena, aby řešila základní výzvu efektivního doručování identického obsahu více uživatelům v mobilních sítích. Před jejím zavedením se sítě primárně spoléhaly na spojení point-to-point (unicast) pro všechny služby, což se ukázalo jako vysoce neefektivní pro vysílací aplikace, jako je mobilní televize, zpravodajské kanály nebo aktualizace softwaru. Každé unicastové spojení spotřebovávalo vyhrazené rádiové a síťové zdroje jádra bez ohledu na to, kolik uživatelů chtělo stejný obsah, což vedlo k zahlcení sítě a špatné škálovatelnosti pro oblíbené služby.

3GPP uznala, že tradiční buněčné architektury potřebují vylepšení pro podporu efektivních vysílacích a multicastových schopností. BM-IWF se objevila jako řešení pro překlenutí mezery mezi platformami vysílacích služeb a sítěmi UMTS. Umožnila operátorům využít inherentní efektivitu přenosu point-to-multipoint při zachování kompatibility se stávajícími unicastovými službami a síťovou infrastrukturou. Tento přístup umožnil mobilním operátorům nabízet nové služby generující příjmy bez nutnosti kompletní přestavby sítě.

Vytvoření BM-IWF bylo zvláště motivováno rostoucí poptávkou po multimediálních vysílacích službách na počátku roku 2000. Mobilní televize se objevovala jako slibná aplikace, ale doručování televizního obsahu prostřednictvím individuálních unicastových proudů by zahltilo kapacitu sítě. BM-IWF poskytla potřebnou architektonickou komponentu, aby byly vysílací služby technicky proveditelné a ekonomicky životaschopné. Řešila klíčové problémy včetně objevování služeb, efektivního využití zdrojů, podpory mobility pro vysílací služby a integrace se stávajícími účtovacími a bezpečnostními systémy.

## Klíčové vlastnosti

- Převod protokolů mezi aplikační vrstvou BM-SC a transportní vrstvou UMTS
- Efektivní vytváření a správa přenosových cest typu point-to-multipoint
- Definice oblasti služby a koordinace vysílání v buňkách
- Podpora mobility pro kontinuitu vysílacích/multicastových služeb
- Mapování QoS mezi požadavky služeb a možnostmi sítě
- Sběr účtovacích dat pro vysílací/multicastové služby

## Související pojmy

- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)
- [UTRAN – Universal Terrestrial Radio Access Network](/mobilnisite/slovnik/utran/)
- [SGSN – Serving GPRS Support Node](/mobilnisite/slovnik/sgsn/)

## Definující specifikace

- **TS 25.401** (Rel-19) — UTRAN Overall Architecture

---

📖 **Anglický originál a plná specifikace:** [BM-IWF na 3GPP Explorer](https://3gpp-explorer.com/glossary/bm-iwf/)
