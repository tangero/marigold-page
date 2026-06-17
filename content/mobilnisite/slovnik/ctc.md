---
slug: "ctc"
url: "/mobilnisite/slovnik/ctc/"
type: "slovnik"
title: "CTC – Circuit Transport Channel"
date: 2025-01-01
abbr: "CTC"
fullName: "Circuit Transport Channel"
category: "Radio Access Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ctc/"
summary: "Circuit Transport Channel (CTC) je transportní mechanismus v GSM/EDGE Radio Access Network (GERAN), který přenáší okruhově přepínaná uživatelská data a signalizaci přes rozhraní Abis mezi Base Transce"
---

CTC je transportní mechanismus v GERAN, který přenáší okruhově přepínaná uživatelská data a signalizaci přes rozhraní Abis mezi BTS a BSC.

## Popis

Circuit Transport Channel (CTC) je základní transportní mechanismus definovaný v architektuře GSM/[EDGE](/mobilnisite/slovnik/edge/) Radio Access Network ([GERAN](/mobilnisite/slovnik/geran/)), který funguje přes rozhraní Abis spojující Base Transceiver Station ([BTS](/mobilnisite/slovnik/bts/)) s Base Station Controller ([BSC](/mobilnisite/slovnik/bsc/)). Jako okruhově přepínaný transportní kanál je CTC navržen pro přenos dat uživatelské roviny (primárně hlasového provozu ve formátech Full Rate, Half Rate nebo Enhanced Full Rate) a signalizačních informací řídicí roviny mezi těmito dvěma síťovými prvky. Kanál pracuje s vyhrazenou alokací šířky pásma a poskytuje předvídatelnou latenci a garantovanou kvalitu služby pro tradiční mobilní služby.

Z architektonického hlediska funguje CTC ve vrstvovém protokolovém zásobníku rozhraní Abis, nachází se nad fyzickou přenosovou vrstvou (typicky linky E1/T1 nebo pozdější paketové přenosy) a pod funkcemi správy rádiových zdrojů a mobility. Kanál využívá principy časového multiplexu, kdy jsou specifické časové úseky v přenosovém rámci trvale přiděleny jednotlivým instancím CTC. Každý CTC odpovídá jedné okruhově přepínané spojení a přenáší buď Traffic Channels (TCH) pro hlas/data, nebo Standalone Dedicated Control Channels (SDCCH) pro signalizaci během sestavování hovorů, aktualizace polohy a dalších řídicích procedur.

Z provozní perspektivy CTC funguje vytvářením pevných přenosových kanálů s fixní šířkou pásma mezi BTS a BSC, které zůstávají alokovány po dobu trvání okruhově přepínaného hovoru nebo signalizační transakce. Když mobilní stanice zahájí hlasový hovor, BSC přidělí specifický CTC na rozhraní Abis spolu s odpovídajícími rádiovými zdroji na rádiovém rozhraní. BTS pak transparentně přeposílá zakódované hlasové rámce mezi mobilní stanicí a přiděleným CTC, přičemž BSC zajišťuje další směrování do Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)) jádra sítě. Pro účely signalizace přenášejí CTC s informacemi SDCCH zprávy třetí vrstvy mezi mobilní stanicí a BSC, což umožňuje funkce jako autentizace, šifrování a příprava předávání spojení.

Role CTC v síti je klíčová pro zachování zpětné kompatibility se staršími okruhově přepínanými službami a zároveň pro efektivní využití zdrojů. V tradičních GSM sítích představuje CTC primární transportní mechanismus pro hlasové služby, zajišťuje přenos hlasu s kvalitou veřejné telefonní sítě a minimálním zpožděním a chvěním. I když se sítě vyvíjely směrem k paketově přepínaným architekturám, CTC zůstal nezbytný pro podporu starších mobilních zařízení a poskytování záložních možností. Deterministická povaha kanálu zjednodušuje plánování a dimenzování sítě, protože inženýring provozu může být založen na Erlangových výpočtech namísto předpokladů statistického multiplexování.

## K čemu slouží

CTC byl vytvořen k řešení základního požadavku na spolehlivý transport s nízkou latencí pro okruhově přepínané služby v sítích GSM. Před rozšířením paketově přepínaných technologií jako IP mobilní sítě spoléhaly výhradně na okruhově přepínané architektury pro hlasové i datové služby. Rozhraní Abis mezi [BTS](/mobilnisite/slovnik/bts/) a [BSC](/mobilnisite/slovnik/bsc/) potřebovalo transportní mechanismus, který by mohl garantovat kvalitu služby pro hlasovou komunikaci v reálném čase a zároveň efektivně využívat omezenou šířku pásma dostupnou na backhaul spojích (typicky linky E1/T1 s kapacitou 2,048/1,544 Mbps).

Historicky CTC vyřešil problém, jak rozšířit okruhově přepínané paradigma z jádra sítě přes rádiovou přístupovou síť k rádiovému rozhraní. Dřívější pevné telefonní sítě používaly vyhrazené okruhy od konce ke konci, ale mobilní sítě přinesly složitost sdílení rádiových zdrojů a správy mobility. CTC vytvořil chybějící článek vytvořením virtuálních okruhů přes rozhraní Abis, které odpovídaly okruhově přepínaným spojením zřízeným v jádru sítě. Tento přístup zajistil hladkou integraci se stávající telefonní infrastrukturou a zároveň vzal v úvahu jedinečné charakteristiky bezdrátové komunikace.

Technologie řešila několik konkrétních omezení alternativních přístupů. Čistě paketový transport (který se objevil později) přinášel proměnlivé zpoždění a chvění nepřijatelné pro hlasovou kvalitu veřejné telefonní sítě bez sofistikovaných mechanismů kvality služby. Přístupy se sdílenými kanály nemohly garantovat konzistentní nízkou latenci potřebnou pro komunikaci v reálném čase. Okruhově přepínaná povaha CTC poskytla deterministický výkon, který zjednodušil návrh a provoz sítě, což bylo zvláště důležité během počátečního nasazení GSM, kdy měli operátoři rozsáhlé zkušenosti s okruhově přepínanými sítěmi, ale omezenou odbornost s paketovými technologiemi.

## Klíčové vlastnosti

- Vyhrazené přidělení šířky pásma pro každé spojení
- Transport s nízkou latencí vhodný pro hlasové služby v reálném čase
- Podpora jak pro traffic kanály (TCH), tak pro signalizační kanály (SDCCH)
- Časový multiplex přes fyzická rozhraní E1/T1
- Funkce transparentního přeposílání mezi rádiovým rozhraním a rozhraním Abis
- Zpětná kompatibilita se starší okruhově přepínanou infrastrukturou

## Související pojmy

- [GERAN – GSM EDGE Radio Access Network](/mobilnisite/slovnik/geran/)

## Definující specifikace

- **TR 26.928** (Rel-19) — Study on eXtended Reality (XR) in 5G
- **TR 26.955** (Rel-19) — Video Codec Analysis for 5G Services
- **TS 44.318** (Rel-19) — Generic Access Network (GAN) Interface Procedures

---

📖 **Anglický originál a plná specifikace:** [CTC na 3GPP Explorer](https://3gpp-explorer.com/glossary/ctc/)
