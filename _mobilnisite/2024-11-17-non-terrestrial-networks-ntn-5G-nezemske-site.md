---
categories:
- 5G
- Mobilní sítě
date: 2024-11-17
layout: post
thumbnail: https://cdn.everythingrf.com/live/1681111338034_638167081392088941.png
title: Non-Terrestrial Networks -  integrace nezemských sítí do sítí 5G/6G
---

__Co konkrétně se v tomto článku dozvíte?__ 
* Obsah
{:toc}

[Non-Terrestrial Networks](/mobilnisite/non-terrestrial-networks-ntn-5G-nezemske-site/) ([NTN](/mobilnisite/non-terrestrial-networks-ntn-5G-nezemske-site/)) představují další významný krok v evoluci mobilních sítí, který spojuje konvenční pozemní infrastrukturu s vesmírnou komponentou. S příchodem 5G standardů, konkrétně od Release 17, se NTN stávají integrální součástí mobilních sítí, což otevírá zcela nové možnosti v oblasti globální konektivity.

Základní komponenty NTN zahrnují:
- Satelitní systémy (LEO, MEO, GEO)
- High-Altitude Platform Systems (HAPS)
- Unmanned Aerial Vehicles (UAV)
- Pozemní gateway stanice
- Uživatelské terminály s podporou NTN

![Non-Terrestrial Networks: Komplexní pohled](/assets/Non-Terrestrial-Network.png)

## Architektura NTN

### Satelitní komponenty

NTN architektura je primárně založena na třech typech satelitních orbit, jejichž charakteristiky jsou shrnuty v následující tabulce:

| Parametr | Low Earth Orbit (LEO) | Medium Earth Orbit (MEO) | Geostationary Orbit (GEO) |
|----------|----------------------|-------------------------|--------------------------|
| Výška | 300-1500 km | 7000-25000 km | 35786 km |
| Latence | 30-50 ms | 125-325 ms | 600-800 ms |
| Velikost buňky | 100-1000 km | 100-1000 km | 200-3500 km |
| Handover četnost | Vysoká (3-10 min) | Střední | Minimální |
| Path loss | Nejnižší | Střední | Nejvyšší |
| Doppleruv efekt | Významný | Střední | Minimální |
| Výhody | - Nízká latence<br>- Menší path loss<br>- Nižší vysílací výkon | - Dobrý kompromis mezi latencí a pokrytím<br>- Střední komplexita systému | - Stabilní pokrytí<br>- Jednoduchá síťová architektura<br>- Minimální handover |
| Nevýhody | - Častý handover<br>- Komplexní konstelace<br>- Vysoká komplexita systému | - Vyšší latence než LEO<br>- Nutnost více satelitů než GEO | - Vysoká latence<br>- Významný path loss<br>- Vyšší požadavky na vysílací výkon |

### Payload architektury

Payload architektura v kontextu satelitních komunikačních systémů definuje způsob, jakým satelit zpracovává a přeposílá signály mezi pozemními stanicemi a uživatelskými terminály. V Release 17 standardizace 3GPP jsou definovány dva základní typy payload architektury:

1. **Transparentní payload**
   - Funguje jako "bent pipe" repeater - přijímá signál v uplink frekvenci, provádí frekvenční konverzi, zesiluje signál a vysílá v downlink frekvenci
   - Jednoduchá frekvence konverze a zesílení
   - Standardizováno v Release 17

2. **Regenerativní payload**
   - Plná demodulace/modulace na satelitu
   - Možnost implementace gNB funkcionalit
   - Plánováno pro Release 18


![Payload v architektuře NTN](/assets/NTN_payload.jpg)

Payload architektura představuje kritický aspekt NTN systémů, který významně ovlivňuje jejich výkon, flexibilitu a použitelnost. Volba mezi transparentním a regenerativním payloadem, případně jejich hybridní kombinací, závisí na konkrétních požadavcích mise, dostupných technologiích a ekonomických faktorech. S postupným vývojem technologií lze očekávat rostoucí adopci pokročilých regenerativních payloadů, které umožní plnou integraci satelitních systémů do budoucích 6G sítí.

## Integrace s pozemními sítěmi

Integrace NTN s existující 5G infrastrukturou představuje komplexní technickou výzvu, která vyžaduje řešení několika klíčových aspektů:

### Synchronizace a timing

**Kompenzace vysoké latence** v NTN představuje jeden z fundamentálních problémů, který výrazně ovlivňuje fungování celého systému. V případě GEO satelitů může latence dosahovat až 600-800 ms, což je řádově více než u pozemních sítí (typicky jednotky milisekund). Tato vysoká latence má přímý dopad na mnoho síťových mechanismů, například na TCP protokol, který může chybně interpretovat zpoždění jako ztrátu paketu. Proto musí být implementovány speciální mechanismy jako Performance Enhancing Proxies (PEP) a modifikované TCP varianty, které jsou optimalizované pro satelitní přenosy.

**Dopplerův efekt** v NTN systémech dosahuje výrazně vyšších hodnot než v pozemních sítích, především kvůli vysokým relativním rychlostem satelitů vůči pozemním stanicím. V případě LEO satelitů může frekvenční posun dosahovat až desítek kHz, což představuje významnou výzvu pro synchronizaci a demodulaci signálu. Systém musí implementovat sofistikované algoritmy pro predikci a kompenzaci Dopplerova posunu, které berou v úvahu přesnou znalost orbitální mechaniky satelitů a pozice uživatelského zařízení. Tyto algoritmy musí být schopny rychle a přesně upravovat parametry modulace a demodulace v reálném čase.

**Timing advance přizpůsobení** je kritické pro zajištění správného časování uplink přenosů v NTN. Na rozdíl od pozemních sítí, kde se vzdálenost mezi základnovou stanicí a uživatelským zařízením mění relativně pomalu a v omezeném rozsahu, v satelitních systémech dochází k rapidním změnám vzdáleností v řádu stovek až tisíců kilometrů. UE musí tyto změny aktivně kompenzovat pomocí dynamického timing advance mechanismu, který zohledňuje aktuální pozici satelitu a predikuje budoucí změny vzdálenosti. Pro efektivní implementaci tohoto mechanismu je klíčová přesná znalost pozice jak satelitu, tak UE, typicky zajištěná pomocí GNSS.

**Synchronizace HARQ (Hybrid Automatic Repeat Request) procedur** vyžaduje v NTN kontextu specifické úpravy. Standardní HARQ mechanismy používané v pozemních sítích předpokládají relativně krátké round-trip time (RTT), typicky v řádu milisekund. V satelitních systémech je však RTT výrazně vyšší, což může vést k neefektivnímu využití síťových zdrojů, pokud by byly použity konvenční HARQ procedury. Proto 3GPP Release 17 zavádí modifikované HARQ procedury pro NTN, které jsou optimalizované pro vysoké latence. Tyto úpravy zahrnují například zvýšení počtu paralelních HARQ procesů a implementaci adaptivních časovačů, které se přizpůsobují aktuální RTT.

Celý synchronizační systém v NTN musí navíc řešit problém s různými referenčními časovými základnami. Zatímco pozemní komponenty systému typicky využívají GPS čas nebo jiné pozemní časové reference, satelity mohou mít vlastní časové reference ovlivněné relativistickými efekty. Systém proto musí implementovat robustní mechanismy pro převod mezi různými časovými doménami a zajistit konzistentní časovou synchronizaci napříč celou sítí. Tento aspekt je kritický zejména pro služby vyžadující přesnou časovou synchronizaci, jako jsou průmyslové aplikace nebo přesné určování polohy.

### Mobility Management

Management mobility v kontextu NTN představuje zásadní výzvu pro současné mobilní sítě, především kvůli dynamické povaze satelitních systémů. Na rozdíl od tradičních terrestrických sítí, kde jsou buňky statické a pohybují se pouze uživatelé, v NTN se pohybují jak uživatelé, tak i samotné satelity (v případě non-GEO konstelací). Tato dvojitá dynamika vytváří zcela nové scénáře pro správu mobility, které vyžadují inovativní přístupy k jejich řešení.

Klíčovým konceptem v NTN je zavedení tzv. "Earth-fixed tracking areas" (pevných sledovacích oblastí vztažených k Zemi). Tento přístup představuje fundamentální změnu oproti konvenčnímu pojetí buněk v mobilních sítích. Zatímco satelity se pohybují po svých orbitách, tracking areas zůstávají fixní vzhledem k zemskému povrchu. To znamená, že satelity musí dynamicky měnit své vysílané identifikátory tracking areas podle své aktuální pozice. Tento koncept významně redukuje signalizační zátěž způsobenou častými tracking area updates, které by jinak byly nutné při pohybu satelitů.

Handover management v NTN musí řešit několik specifických scénářů. První je inter-satellite handover, ke kterému dochází, když se satelit pohybuje mimo dosah uživatele a spojení musí být předáno jinému satelitu. Tento typ handoveru je unikátní tím, že je předvídatelný díky známým orbitálním drahám satelitů. V případě LEO konstelací může k takovému handoveru docházet každých 3-10 minut, což klade vysoké nároky na rychlost a efektivitu procesu. Další scénář představuje satellite-to-ground handover, kdy dochází k přepínání mezi satelitní a pozemní sítí. Tento typ handoveru musí zohledňovat značné rozdíly v latenci a charakteristikách přenosového kanálu mezi oběma typy sítí.

3GPP Release 17 zavádí několik mechanismů pro optimalizaci těchto procesů. Jedním z nich je využití GNSS (Global Navigation Satellite System) v uživatelských zařízeních pro přesnou lokalizaci a predikci handoverů. UE může díky znalosti své pozice a efemerid satelitů předvídat potřebu handoveru a optimalizovat timing těchto procedur. Systém také implementuje koncepty jako "soft handover" v případě překrývajícího se pokrytí více satelitů a "make-before-break" přístup, který minimalizuje přerušení služby během handoveru.

Významnou roli v managementu mobility hraje také beam management. Satelity typicky využívají množství úzkých paprsků pro pokrytí své servisní oblasti. Tyto paprsky musí být dynamicky směrovány a jejich výkon musí být řízen tak, aby optimálně pokrývaly cílové oblasti na zemském povrchu. V případě LEO satelitů je tento proces ještě komplexnější, protože paprsky musí neustále sledovat pohybující se servisní oblasti. Tento proces vyžaduje sofistikované algoritmy pro predikci pohybu a optimalizaci výkonu jednotlivých paprsků.

Pro efektivní fungování těchto mechanismů je klíčová přesná časová synchronizace mezi všemi komponenty systému. NTN proto implementuje speciální timing advance mechanismy, které kompenzují variabilní propagační zpoždění způsobené pohybem satelitů. Tyto mechanismy musí být dostatečně robustní, aby zvládly rychlé změny vzdáleností a relativních rychlostí, ke kterým v satelitních systémech dochází.

### QoS Management

V kontextu NTN je QoS management kritický vzhledem k:
- Variabilní latenci
- Různým typům orbit
- Proměnlivému path loss
- Atmosférickým vlivům

![Architektura NTN](/assets/ntn-architektura.png)

## Klíčové technické výzvy

### 1. Latence a její kompenzace

Hlavní výzvy v oblasti latence zahrnují:
- Propagační zpoždění způsobené vzdáleností satelitů
- Procesní zpoždění v síťových uzlech
- Queueing zpoždění v síťových frontách
- Handover latence při přepínání mezi satelity

**Propagační zpoždění** představuje v NTN systémech fundamentální výzvu danou fyzikálními zákony. U GEO satelitů dosahuje jednosměrné zpoždění přibližně 120 ms, což znamená RTT kolem 240 ms bez započtení dalších zpoždění. Toto zpoždění je neodstranitelné a síťové protokoly musí být navrženy tak, aby s ním dokázaly efektivně pracovat. V LEO konstelacích je situace příznivější s propagačním zpožděním v řádu 10-20 ms, ale i to je výrazně více než u pozemních sítí.

**Procesní zpoždění** vzniká při zpracování signálů v různých bodech systému - v satelitu, pozemních stanicích a síťových uzlech. V případě transparentního payloadu je toto zpoždění minimální, ale u regenerativního payloadu může být významné kvůli demodulaci, zpracování a opětovné modulaci signálu. Moderní satelitní systémy implementují vysoce optimalizované signálové procesory pro minimalizaci tohoto zpoždění.

**Queueing zpoždění** vzniká v síťových frontách při čekání paketů na zpracování. V NTN je toto zpoždění obzvláště kritické kvůli omezeným síťovým zdrojům a vysoké agregaci provozu v satelitních spojích. Systémy proto implementují sofistikované QoS mechanismy a traffic shaping algoritmy pro minimalizaci front a zajištění spravedlivého přístupu k síťovým zdrojům.

**Handover latence** představuje specifický typ zpoždění vznikající při přepínání spojení mezi satelity nebo mezi satelitní a pozemní sítí. Toto zpoždění je kritické zejména v LEO konstelacích, kde dochází k častým handoverům. Systémy implementují prediktivní handover algoritmy a make-before-break přístupy pro minimalizaci tohoto zpoždění.

### 2. Frekvenční management

Klíčové aspekty frekvenčního managementu:
- Dopplerovský frekvenční posun
- Koordinace frekvencí mezi systémy
- Interferenční management
- Adaptivní modulace a kódování

**Dopplerovský frekvenční posun** dosahuje v NTN systémech extrémních hodnot kvůli vysokým relativním rychlostem satelitů. V případě LEO satelitů může tento posun dosahovat až ±50 kHz, což vyžaduje implementaci pokročilých kompenzačních mechanismů. Systémy využívají kombinaci prediktivní kompenzace založené na známých orbitálních parametrech a adaptivní kompenzace založené na měření aktuálního posunu.

**Koordinace frekvencí** mezi různými satelitními systémy a pozemními sítěmi představuje komplexní regulační a technický problém. Satelitní systémy musí respektovat mezinárodní frekvenční alokace a implementovat mechanismy pro sdílení spektra s jinými službami. To zahrnuje dynamickou správu frekvencí, koordinaci mezi operátory a implementaci ochranných pásem.

**Interferenční management** je kritický pro zajištění kvalitního spojení v prostředí s mnoha potenciálními zdroji rušení. Systémy implementují adaptivní interferenční potlačení, beam forming techniky a frekvenční plánování pro minimalizaci vzájemného rušení mezi různými službami a systémy. Zvláštní pozornost je věnována ko-existenci s pozemními sítěmi ve sdílených frekvenčních pásmech.

**Spektrální efektivita** musí být maximalizována vzhledem k omezeným frekvenčním zdrojům. Systémy implementují adaptivní modulaci a kódování (ACM), které dynamicky přizpůsobují přenosové parametry aktuálním podmínkám kanálu. To zahrnuje změny modulačních schémat, kódových poměrů a výkonových úrovní v reálném čase.

### 3. Beam Management

Kritické aspekty správy paprsků:
- Dynamická optimalizace vyzařovacích charakteristik
- Tracking pohybujících se uživatelů
- Koordinace mezi překrývajícími se paprsky
- Výkonová optimalizace

**Dynamická optimalizace** vyzařovacích charakteristik představuje kontinuální proces přizpůsobování parametrů anténních paprsků aktuální situaci. V případě LEO satelitů musí systém neustále upravovat směrování paprsků tak, aby sledovaly požadované oblasti na zemském povrchu. To vyžaduje precizní řízení fázovaných anténních polí a implementaci pokročilých beam forming algoritmů.

**Tracking pohybujících se uživatelů** vyžaduje sofistikované algoritmy pro predikci pohybu a optimální alokaci síťových zdrojů. Systém musí být schopen efektivně sledovat jak pomalu se pohybující pozemní uživatele, tak rychle se pohybující objekty jako letadla. To zahrnuje implementaci adaptivních tracking algoritmů a prediktivních handover mechanismů.

**Koordinace mezi překrývajícími se paprsky** je kritická pro minimalizaci interference a optimální využití síťových zdrojů. Systém musí implementovat mechanismy pro koordinaci mezi sousedními paprsky stejného satelitu i mezi paprsky různých satelitů. To zahrnuje dynamické přidělování frekvencí, výkonovou koordinaci a časovou synchronizaci.

**Výkonová optimalizace** je klíčová pro maximalizaci pokrytí při minimální spotřebě energie. Systém musí dynamicky upravovat vysílací výkony jednotlivých paprsků v závislosti na aktuálních podmínkách propagace, požadavcích na služby a energetických omezeních satelitu. To zahrnuje implementaci pokročilých algoritmů pro power control a energy-aware beam management.

## Standardizace a implementace

### 3GPP aktivity

Release 17 přináší:
- Základní NTN funkcionalitu
- Transparentní payload podporu
- IoT over NTN specifikace
- Základní QoS framework

Release 18 plánuje:
- Regenerativní payload podporu
- Pokročilý mobility management
- Inter-satellite link standardizaci
- Rozšířené IoT případy užití

# Klíčové prvky Release 18 pro Non-Terrestrial Networks

## Regenerativní Payload Podpora

Regenerativní payload představuje jeden z nejvýznamnějších pokroků v Release 18, který fundamentálně mění způsob, jakým satelitní systémy zpracovávají komunikační signály. Na rozdíl od transparentního payloadu, který funguje jako jednoduchý "bent-pipe" repeater, regenerativní payload umožňuje plnohodnotné zpracování signálu přímo na satelitu.

Implementace regenerativního payloadu v Release 18 přináší tři hlavní architektonické varianty. První varianta zahrnuje implementaci plného gNB (gNodeB) přímo na satelitu. Tento přístup minimalizuje latenci pro user-plane komunikaci, ale klade vysoké nároky na výpočetní kapacity satelitu a spotřebu energie. Druhá varianta využívá split architekturu, kde je gNB rozděleno mezi satelit a pozemní segment - gNB-CU (Centralized Unit) zůstává na zemi, zatímco gNB-DU (Distributed Unit) je implementováno na satelitu. Třetí varianta představuje Low Layer Split (LLS), kde je na satelitu implementována pouze Radio Unit (RU), což snižuje hardwarové nároky, ale vyžaduje vyšší kapacitu feeder linků.

Regenerativní payload přináší několik klíčových výhod. Umožňuje optimalizaci signálu přímo na satelitu, včetně opravy chyb, adaptivní modulace a kódování, a inteligentního směrování provozu. Tato funkcionalita je zvláště důležitá pro redukci latence v komplexních satelitních konstelacích a pro podporu pokročilých síťových služeb. Release 18 definuje standardizované rozhraní pro management regenerativního payloadu, včetně mechanismů pro aktualizace software a rekonfiguraci síťových funkcí.

## Pokročilý Mobility Management

Mobility management v Release 18 představuje komplexní řešení pro správu mobility v multi-orbit satelitních systémech. Základním kamenem je implementace prediktivních handover mechanismů, které využívají znalost orbitální mechaniky pro optimalizaci přepínání mezi satelity a paprsky.

Release 18 zavádí koncept "Multi-Layer Mobility Management", který koordinuje handovery napříč různými orbitálními výškami - od LEO přes MEO až po GEO satelity. Systém využívá sofistikované algoritmy pro výběr optimální cesty signálu, přičemž zohledňuje faktory jako latence, dostupná kapacita, QoS požadavky a energetická efektivita.

Významnou inovací je implementace AI/ML algoritmů pro predikci mobility a optimalizaci handoverů. Tyto algoritmy analyzují historické vzory pohybu uživatelů, aktuální síťové podmínky a dostupné síťové zdroje pro minimalizaci přerušení služby během handoveru. Release 18 také standardizuje rozhraní pro sdílení informací o mobilitě mezi různými satelitními systémy a pozemními sítěmi.

## Inter-Satellite Link Standardizace

Standardizace Inter-Satellite Links (ISL) v Release 18 představuje klíčový krok k vytvoření plně propojeného satelitního systému. ISL umožňují přímou komunikaci mezi satelity bez nutnosti pozemního zprostředkování, což významně redukuje latenci a zvyšuje flexibilitu sítě.

Release 18 definuje dva základní typy ISL - rádiové (RF) a optické spoje. RF ISL typicky operují v Ka a V pásmech a poskytují robustní spojení s nižší přenosovou rychlostí. Optické ISL naproti tomu nabízejí výrazně vyšší přenosové rychlosti (>10 Gbps), ale jsou citlivější na atmosférické podmínky a vyžadují přesnější pointing systémy.

Standardizace zahrnuje komplexní routing protokoly optimalizované pro dynamickou topologii satelitních konstelací. Tyto protokoly musí zohledňovat neustále se měnící pozice satelitů, různé propagační zpoždění a dostupnost spojů. Release 18 také definuje mechanismy pro QoS management v ISL, včetně prioritizace provozu a řízení zahlcení.

## Rozšířené IoT Případy Užití

Release 18 významně rozšiřuje možnosti podpory IoT služeb v satelitních sítích. Klíčovou inovací je implementace nových tříd IoT zařízení optimalizovaných pro satelitní komunikaci, včetně kategorií pro ultra-low power zařízení a high-precision aplikace.

Standardizace zavádí nové přístupové mechanismy optimalizované pro masivní IoT komunikaci přes satelit. Tyto mechanismy zahrnují group-based přístup pro efektivní správu velkého počtu zařízení, energy-efficient random access procedury a prioritizační schémata pro kritické IoT aplikace.

Release 18 také definuje framework pro IoT služby s vysokou přesností lokalizace, který kombinuje satelitní poziční systémy s komunikačními službami. Tento framework je zvláště důležitý pro aplikace jako asset tracking, environmentální monitoring a precision agriculture.

Bezpečnostní aspekty IoT komunikace jsou adresovány prostřednictvím nových lightweight kryptografických mechanismů optimalizovaných pro omezené výpočetní zdroje IoT zařízení. Release 18 také standardizuje mechanismy pro bezpečné skupinové operace, jako jsou hromadné aktualizace firmware a group authentication.

Součástí standardizace je také definice nových QoS tříd specificky navržených pro různé typy IoT aplikací, od kritických senzorů vyžadujících nízkou latenci až po bulk sensors optimalizované pro energetickou efektivitu. Release 18 také zavádí mechanismy pro adaptivní přizpůsobení síťových parametrů různým typům IoT provozu.

### Implementační aspekty

Klíčové oblasti pro úspěšnou implementaci:

1. **Hardwarové požadavky**
   - Modifikované UE s NTN podporou
   - Vylepšené gateway stanice
   - Specializovaný satellite payload

2. **Software/Protokol Stack**
   - Modifikované RRC procedury
   - Adaptované MAC vrstva
   - Optimalizované higher layer protokoly

## Případy užití a business modely

### Primární use cases

1. **Globální pokrytí**
   - Námořní komunikace
   - Letecká konektivita
   - Pokrytí odlehlých oblastí

2. **IoT aplikace**
   - Globální asset tracking
   - Environmentální monitoring
   - Agricultural IoT

3. **Emergency komunikace**
   - Disaster recovery
   - První responder sítě
   - Backup konektivita

## Budoucí perspektivy

### Technologický vývoj

Očekávané trendy:
- Integrace AI/ML pro optimalizaci
- Pokročilé inter-satellite komunikace
- Quantum-secure komunikace
- Optické satelitní spoje

### Role Non-Terrestrial Networks v 6G systémech

NTN jako integrální součást 6G:
- 3D network architektura
- Space-air-ground integrace
- Terahertz komunikace
- Holistický přístup k síťové architektuře


#### 3D Network Architektura a NTN

V kontextu 6G hrají Non-Terrestrial Networks klíčovou roli v realizaci skutečně trojrozměrné síťové architektury. NTN komponenty - zejména satelity v různých orbitálních výškách, HAPS (High Altitude Platform Stations) a UAV platformy - tvoří vertikální vrstvy této architektury. Na rozdíl od současných 5G NTN systémů, kde satelity fungují primárně jako doplněk pozemní infrastruktury, v 6G se NTN stávají integrální součástí architektury s plnou podporou multi-layer komunikace.

NTN v 3D architektuře zavádí nový koncept "vertical handover", který umožňuje plynulé přepínání mezi různými výškovými vrstvami NTN. Například uživatel může být seamless přepínán mezi pozemní stanicí, LEO satelitem a HAPS platformou v závislosti na aktuálních podmínkách a požadavcích na službu. Toto vyžaduje implementaci sofistikovaných 3D beam forming technik specificky navržených pro NTN komponenty, které musí zohledňovat rychlý pohyb satelitů a dynamickou povahu konstelací.

NTN komponenty v 3D architektuře také přinášejí nové možnosti pro prostorový multiplexing. Různé orbitální vrstvy (LEO, MEO, GEO) mohou současně využívat stejná frekvenční pásma díky jejich přirozené prostorové separaci, což významně zvyšuje celkovou kapacitu systému.

#### Space-Air-Ground Integrace prostřednictvím NTN

NTN představují klíčový element v realizaci plně integrovaného space-air-ground systému. V 6G se NTN komponenty stávají aktivními síťovými uzly s plnou podporou mesh topologie a dynamického směrování. Toto je zásadní posun oproti současným NTN v 5G, kde satelity často fungují pouze jako "bent pipe" repeatery.

Integrace je realizována prostřednictvím nových typů NTN rozhraní:
1. Space-Space rozhraní: Inter-Satellite Links mezi různými orbitálními vrstvami
2. Space-Air rozhraní: Spoje mezi satelity a HAPS/UAV platformami
3. Space-Ground rozhraní: Vylepšené feeder linky a uživatelské spoje

NTN v této integraci implementují adaptivní routing algoritmy, které dynamicky optimalizují cesty skrz vesmírný, vzdušný a pozemní segment. Například data z pozemní stanice mohou být směrována přes LEO satelit na HAPS platformu a následně na cílového uživatele, pokud tato cesta poskytuje optimální QoS parametry.

#### Terahertzová komunikace v NTN

Terahertzová komunikace představuje revoluci především pro NTN komponenty, kde otevírá nové možnosti pro vysokorychlostní inter-satelitní komunikaci a feeder linky. V kontextu NTN se terahertz technologie uplatňuje ve třech hlavních oblastech:

1. Inter-Satellite Links:
   - Ultra-vysokorychlostní spoje mezi satelity v konstelaci
   - Terabitové přenosové rychlosti pro backbone konektivitu
   - Minimální interference díky vysoké směrovosti

2. Feeder Links:
   - Vysokorychlostní spojení mezi satelity a pozemními stanicemi
   - Využití atmosférických oken v THz pásmu
   - Adaptivní modulace pro kompenzaci atmosférických vlivů

3. User Links:
   - Selektivní využití THz pásma pro stacionární uživatele
   - Hybrid RF/THz systémy pro optimální pokrytí
   - Beam forming pro vysoký zisk a směrovost

NTN komponenty v THz pásmu implementují speciální techniky pro kompenzaci Dopplerova posunu, který je zvláště významný u LEO satelitů. Systémy také využívají adaptivní pointing mechanismy s extrémně vysokou přesností, nezbytnou pro THz komunikaci.

#### Holistický přístup k síťové architektuře s NTN

V 6G se NTN stávají plnohodnotnou součástí holistické síťové architektury, kde každá NTN komponenta aktivně přispívá k celkové inteligenci systému. Toto je realizováno prostřednictvím:

1. Distribuované AI/ML v NTN:
   - On-board AI procesory v satelitech
   - Distribuované učení napříč konstelací
   - Real-time optimalizace síťových parametrů
   - Prediktivní maintenance satelitních systémů

2. Quantum-secure NTN komunikace:
   - Quantum key distribution přes satelitní spoje
   - Post-quantum kryptografie pro NTN komponenty
   - Secure multi-party computation v distribuovaném prostředí

3. Edge Computing v NTN:
   - Satelity jako edge computing uzly
   - Distribuované výpočetní kapacity v kosmu
   - On-board processing pro kritické aplikace
   - Dynamic workload distribution

4. [Network Slicing](/mobilnisite/network-slicing-5g/) pro NTN:
   - End-to-end slicing zahrnující vesmírný segment
   - Dedikované satelitní slice pro specifické služby
   - Cross-layer optimalizace pro NTN slice



## Závěr

Role NTN v 6G systémech se fundamentálně mění z doplňkové technologie na integrální součást síťové architektury. NTN komponenty přinášejí unikátní možnosti pro realizaci true 3D sítí, implementaci terahertz komunikace a vytvoření plně integrovaného space-air-ground systému. Holistický přístup k síťovému designu pak umožňuje plné využití potenciálu NTN v kombinaci s pokročilými technologiemi jako AI/ML, quantum computing a edge processing.

Non-Terrestrial Networks představují postupné a přitom do budoucna podstatné rozšíření možností mobilních sítí. Jejich úspěšná implementace vyžaduje překonání významných technických výzev, ale potenciální přínosy jsou enormní. S pokračující standardizací a technologickým vývojem se NTN stanou klíčovou součástí budoucí globální komunikační infrastruktury.