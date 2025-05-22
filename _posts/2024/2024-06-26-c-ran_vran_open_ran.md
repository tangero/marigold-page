---
categories:
- Mobilní sítě
- 5G
- 5G Advanced
- 4G
excerpt: Technologie pro radiové přístupové sítě se vyvíjejí. Pojďme se podívat na
  nejmodernější koncepty, které se dostávají do sítí 5G, [5G Advanced](/5g-advanced/) a také do 6G.
layout: post
post_date: 2024-09-26 13:48:16
summary_points:
- C-RAN centralizuje zpracování signálu v jádru sítě pomocí cloudových serverů.
- D-RAN sítě decentralizovaly zpracování signálu na tisících základnových stanicích.
- C-RAN snižuje náklady na hardware, elektřinu a zjednodušuje správu sítě.
- Open RAN otevírá rozhraní mezi komponentami RAN pro interoperabilitu různých výrobců.
thumbnail: https://www.marigold.cz/assets/dran-cran.png
title: Způsoby zlepšení radiové sítě v 5G čili C-RAN, vRAN a Open RAN
---

Problematika C-RAN patří mezi na první pohled obtížně pochopitelné změny v architektuře sítí 5G a tak se u ní speciálně zastavíme. Je totiž symbolem pokroku v rádiové přístupové síti, tedy ve způsobu, jakým se mobilní telefon připojuje do mobilní sítě.

Malá vsuvka: C-RAN bývá dávána za příklad toho, že i Čína je schopna na intelektuálním poli rozvoje mobilních technologií nějak přispět, nikoliv pouze kopírovat. S návrhem C-RAN totiž přišel v roce 2010 China Mobile Research Institut. Kritikové přípomínají, že patenty na tuto technologii ovšem o nějakých deset let dříve podala americká firma, respektive Steve Shattil, takže zase takový čínský průlom to nebyl. Na jednu stranu nazrála doba (a technologie), na druhou je dobré, že se tento přístup podařilo čínskému CMRI dotáhnout do konce.

C-RAN je zkratka znamenající Cloud RAN nebo Centralized RAN. V tom je to zmatení. Cloudovou technologii si většinou nezaměňujeme s centralizovanou technologií, jenže v případě C-RAN tomu tak je. Pokusím se vysvětlit.

V sítích předchozích generací byla rádiová přístupová síť (RAN - Radio Access Network) striktně decentralizována - proto ji nově také označujeme jako D-RAN. Aby existovalo plošné pokrytí, bylo potřeba tisíce základnových stanic provozovaných operátorem, které se staraly o zpracování signálu v základním pásmu a spojení dále do sítě. Tzn. byly decentralizované.

Jenže aby sítě 5G mohly odbavit ještě o řády vyšší provoz než starší generace sítí, není tento přístup možný. Nároky na handovery a další obsluhu signálu základnovými stanicemi jsou příliš vysoké a potřebné hustoty základnových stanic by bylo těžké dosáhnout, protože klasické základnové stanice jsou pořád relativně rozměrné kabinety.

Cloud RAN předpokládá, že signál v základním pásmu se vůbec na základnové stanici nezpracovává, ale posouvá se (po rychlých, typicky optických linkách) do jádra sítě, kde je zpracován serverovým cloudem, již postaveným na komerčních serverech, nikoliv na specializovaném telekomunikačním hardware. Tím je možné se v základnových stanicicích zbavit jednotek zpracovávajících základní signál, BBU (BaseBand Unit) a jejich činnost vysunout do jádra sítě na virtualizované BBU, které sdílejí kapacitu i náklady. Z toho důvodu se o C-RAN hovoří zároveň jako o cloudovém řešení: kvůli virtualizovaným, cloudově uspořádaným BBU v jádře sítě, tak jako o centralizovaném řešení, kdy se BBU vyjmou ze základnových stanic a centralizují se v jádře sítě.

Fakticky by tak bylo možné, aby se o obsluhu mobilky staral třeba přístupový bod s WiFi. Mobilka by se připojila na přístupový bod přes WiFi, přístupový bod by data bez meškání předal do cloudu, kde by se mobilka autorizovala a podle toho se na přístupový bod posílala odpověď, kterou by zase přístupový bod bez prodlení posunul přes WiFi na mobilku.

Je dobré povšimnout si přínosů, které užitím C-RAN nastanou. Mimo zrychlení sítě a snížení ceny hardware základnové stanice, který nyní nemusí obsahovat BBU, se také sníží nároky na elektřinu, protože BBU je sdílené více základnovými stanicemi v cloudu a nemusí běžet bez užitku v nevytížených částech sítě.

Komunikace mezi rádiovou jednotkou a basebandovým serverem probíhá přes Common Public Radio Interface (CPRI) - to je náchylné na kvalitu linky, jsou tedy nutné optické spoje nebo mikrovlná rádia, což už ale dnes není problém. I proto čas na tuto technologii nastává až dnes. Tady je ale potřeba mít na paměti, že starší levná pojítka už spojení mezi základnovou stanicí a jádrem sítě neobslouží, typicky budou na základnu potřeba gigabitové rychlosti s velmi nízkým zpožděním, tedy kvalitní optické spojení (třísektorová základnová stanice obsluhující TD-LTE si vyžádá až 30 Gb/s propojení na BBU!). A to není dnes běžně dostupné. Z toho důvodu se počítá pro C-RAN hlavně s metropolitními oblastmi, kde hustota pokrytí je požadována vysoká a vysoká je i dostupnost FTTH. Druhým důvodem je výpočetní kapacita serverů v centrálním cloudu. Dříve by nebylo ekonomické používat menší množství výkonných serverů, bylo lepší zpracování provádět v místě základnové stanice.

Mezi hlavní podporovatele a výzkumníky na poli C-RAN figuruje China Mobile Research Institut, IBM, Alcatel - Lucent, Huawei, ZTE, Nokia Siemens Network, Intel a Texas Instruments, určitou formu kooperace na tom najdeme i jinde, protože se každému dodavateli hardware líbí, co by C-RAN obnášel (obměny dohledového software, řadu prodaného hardware atd). Často i proto, že koncept C-RAN velmi podporuje nějaký jiný jejich koncept jako CoMP nebo eICIC, se kterými je C-RAN velmi komplementární tím, jak výrazně likviduje zpoždění a zvyšuje spektrální efektivitu.

Tady je dlužno dodat, že až doposud základnové stanice při každém upgrade na novou rádiovou technologii musely podstoupit ugprade BBU, která se rozšířila (či vyměnila) tak, aby podporovala zpracování nových rádiových standardů. C-RAN je tak spíš zajímavý pro sítě 5G, ve kterých se přenosy z předchozích sítí zpracovávají virtualizovaným jádrem sítě, “dolátáním" stávající síťové technologie do nového jádra sítě. Ale to je vize, v praxi se samozřejmě budou existující 3G/4G sítě spojovat dohromady se sítí 5G, poběží ve vrstvách vedle sebe a bude s tím hromada problémů.

## Jak se tedy s ohledem na C-RAN změní základnová stanice?

Dnešní základnové stanice obsahují dvě hlavní elektronické části, BBU a RFU. Nově se v Release 10 a pozdějších setkáváme s návrhem na rozdělení na BBU zpracovávající základní signál a RRH (Remote Radio Head), což je jednotka propojená koaxiálním a později optickým kabelem s anténním systémem a BBU a stará se o konverzi základního digitálního signálu do analogového na antény a opačně. V tomto případě jde ale o menší základnové stanice určené pro pokrytí poloměru několika málo kilometrů, což na druhou stranu v zatížených oblastech bude typický poloměr obsluhy základnové stanice. Zatímco modul RRH je umístěn u anténního systému, moduly BBU jsou v dosahu rychlého připojení, typicky v místě, ale i ve vzdálenosti 20-40 kilometrů tam, kde mohou být pro provozovatele sítě pohodlně dostupné.

![Posun od D-RAN k C-RAN](/assets/dran-[cran](/mobilnisite/epc-evolved-packet-core-lte/).png)

Podstatnou změnou je vysunutí BBU z kontajneru základnové stanice do cloudu v jádru sítě.

Na této změně je podstatné si uvědomit několik změn:

1.  Operátor nadále nepotřebuje provozovat kontajner základnové stanice, tedy pronajímat si na něj zvláštní místno (mistnost). Veškerá technika v místě základnové stanice je umístěna v RRH na anténním stožáru, tedy v outdoorovém provedení venku.
 2.  Snižuje to výdaje za elektřinu
3.  Zjednodušuje to správu a zvyšuje možnost loadbalancingu a reakce na nestandardní zatížení sítě, které se stává stále standardnějším (=nejistota je nová jistota)
4.  Zrychluje to datové služby snížením zpoždění a zvýšením kapacity, propustnosti.
5.  Zvyšuje to potřebu propojovat základnové stanice optickým vláknem s jádrem sítě (což byl dodneška hlavní problém)
6.  Klade to nároky na standardizaci interface mezi RRH a BBU a [[EPC](/mobilnisite/epc-evolved-packet-core-lte/)](/mobilnisite/epc-evolved-packet-core-lte/), což se snaží řešít interface OBSAI a ORI a dále dnes používané CPRI.
    

Předpokladem je, že C-RAN bude v prvé fázi nasazován v lokacích, kde jsou vysoké nároky na přenosové rychlosti a pokrytí, tedy zejména pro metropolitní oblasti. Teoreticky by bylo možné pro C-RAN transparentně použít i jiné přístupové technologie, než LTE frekvence, třeba WiFi, návrhy toto zatím nijak neupravují a obnášelo by to podporu na mobilním zařízení. C-RAN je vhodný jak pro makro-buňky, tak pro malé buňky včetně těch uvnitř budov.

Očekává se, že v první fázi nebude plošně nasazován C-RAN, ale že jedna BBU bude schopna obsluhovat více okolních RRH připojených optickým kabelem. Již dnes BBU podporují šest RRH, ovšem na jedné základně, do budoucna by měly být schopny obsluhovat i více RRH v rozdílných základnových stanicích.

## V-RAN a [[[Open RAN](/mobilnisite/epc-evolved-packet-core-lte/)](/mobilnisite/epc-evolved-packet-core-lte/)](/mobilnisite/epc-evolved-packet-core-lte/)

Vývoj architektury rádiové přístupové sítě ale šel rychle dále. Dalším posunem měla být širší propojitelnost. Tu výrazně posunul přechod Baseband Unit (BBU) z propriteráního hardware na běžné servery, které se nazývají COTS (zkratka pro Komerční produkty). Tím se zlevňuje výstavba sítě, protože lze použít jakýkoliv COTS, který provozovatel sítě uváží. Lze lépe škálovat, provoz sítě může být flexibilnější.  Software, který běží na BBU, je virtualizován tak, aby mohl běžet na jakémkoli serveru COTS. Proprietární rozhraní mezi rádii a jednotkou BBU založenou na COTS však zůstávají zachována. Ačkoli jsou tedy funkce RAN virtualizovány na serveru COTS (odtud též označení vRAN), rozhraní mezi BBU a RRU/RRH není otevřené, takže software jakéhokoli dodavatele nemůže s RRU/RRH pracovat, pokud se rozhraní nestanou otevřenými. V případě vRAN je tedy nutné použít stejného dodavatele pro rádio i pro software běžícího na COTS BBU. Provozovatel nemůže na stejnou COTS BBU umístit software jiného dodavatele, pokud rozhraní k rádiu není otevřené. VRAN tedy stále umožňuje vendor lock-in. Což je přesně to, co má postihnout další vývojový krok nazvaný Open RAN, tedy otevřená rádiová přístupová síť.

Open RAN rozdělí tradiční BBU na tři hlavní komponenty: Radio Units (RUs), Distributed Units (DUs), a Centralized Units (CUs). Každá komponenta může pocházet od jiného výrobce a je spojena přes otevřená rozhraní. Klíčovým faktorem u Open RAN je, že rozhraní mezi BBU a RRU/RRH je standardizované, takže software _jakéhokoli_ výrobce může fungovat na _jakémkoli_ otevřeném RRU/RRH. To u C-RAN nebo vRAN **není možné**.

Open RAN totiž otevřel rozhraní fronthaul a zavedl dva nové řadiče, Non-Real-Time RIC a Near-Real-Time RIC, ve vrstvě řízení a RAN a přidal rozhraní A1, E2, O1, O2 a další. Open RAN tak definuje specifická rozhraní, jako jsou Open Fronthaul Interface (mezi RUs a DUs) a Open Midhaul Interface (mezi DUs a CUs).

Na obrázku vidíme konkrétně, jak ty rozdíly mezi C-RAN, vRAN a Open RAN vypadají.

![rozdíly mezi C-RAN, vRAN a Open RAN vypadají](/assets/ran-overview.jpeg)

A to je již výsledek. Pokud se použije Open RAN, lze kombinovat jak řídící software, tak rádiový software i hardware různých výrobců mezi sebou. Je ale zřejmé, že s tím bude ještě dosta práce a z toho plyne, že technologie ještě není standardně nasazována. Zatím se dělají pilotní testy, velkým propagátorem je japonský operátor Rakuten a samozřejmě čínští výrobci, kteří v tom vidí potenciál dalších prodejů. V Evropě se očekává zahájení nasazování Open RAN spíše v roce 2025 a dále.

Tato tabulka shrnuje klíčové rozdíly mezi těmito třemi přístupy k architektuře RAN. C-RAN představuje základní centralizaci, V-RAN přidává virtualizaci, zatímco Open RAN přináší plnou otevřenost, standardizaci a pokročilou inteligenci.



| Vlastnost               | C-RAN                        | V-RAN                         | Open RAN                          |
|-------------------------|------------------------------|-------------------------------|-----------------------------------|
| Centralizace            | Ano                          | Ne (ale BBUs mohou být centralizovány) | Ne nutně                         |
| Virtualizace            | Ne                           | Ano                           | Ano                               |
| Otevřenost              | Ne                           | Ne                            | Ano                               |
| Architektura            | Centralizované BBUs, RRHs    | Virtualizované BBUs           | Otevřené komponenty RAN           |
| Výhody                  | Efektivita, snížení latence, náklady | Flexibilita, škálování, komoditní servery | Interoperabilita, konkurence, náklady |
| Nevýhody                | Vyžaduje vysokokapacitní síť | Investice do IT infrastruktury | Integrace a správa komponent     |


## Jak je to se specifikacemi a standardizací?

V 3GPP Release 14 jsou zahájeny práce na rozdělení funkcí RAN, příprava na nové architektury včetně C-RAN. V Release 15 pak přistupuje  formální specifikace CU/DU, dokončuje se rozdělení pro [[NG-RAN](/mobilnisite/epc-evolved-packet-core-lte/)](/ng-ran/) a je tu první implementace virtualizovaných funkcí. V Release 16 je pak plná podpora vRAN. S ohledem na to, že Open RAN je vlastně otevřená a interoperabilní vRAN, je to s její specifikací trochu jinak.

Open RAN (O-RAN) není přímo specifikován v žádné konkrétní verzi 3GPP Release. Místo toho je O-RAN standardizován a vyvíjen prostřednictvím O-RAN Alliance, která definuje specifikace pro otevřená rozhraní mezi různými komponentami Radio Access Network (RAN). O-RAN Alliance spolupracuje s 3GPP na zajištění interoperability mezi otevřenými rozhraními a existujícími 3GPP specifikacemi.

Open RAN vypadá jako dobrý přístup a uvidíme, nakolik se ve výstavbě sítí chytne.