---
slug: "bdp"
url: "/mobilnisite/slovnik/bdp/"
type: "slovnik"
title: "BDP – Bandwidth Delay Product"
date: 2018-01-01
abbr: "BDP"
fullName: "Bandwidth Delay Product"
category: "Other"
segment: "Testing"
canonical: "https://3gpp-explorer.com/glossary/bdp/"
summary: "Bandwidth Delay Product (BDP) je základní metrika výkonnosti sítě, která představuje maximální množství dat, které může být přenášeno v síťové cestě v libovolném daném okamžiku. Vypočítá se jako souči"
---

BDP (Bandwidth Delay Product) je maximální množství dat, které může být přenášeno v síťové cestě v daném okamžiku; vypočítá se jako součin přenosové kapacity (šířky pásma) spoje a jeho doby oběhu (RTT).

## Popis

Bandwidth Delay Product (BDP) je klíčový koncept v síťových technologiích, který kvantifikuje přenosovou kapacitu komunikačního kanálu, měřenou v bitech nebo bajtech. Matematicky je BDP = Šířka pásma × Doba oběhu ([RTT](/mobilnisite/slovnik/rtt/)), kde se šířka pásma obvykle vyjadřuje v bitech za sekundu (bps) a RTT v sekundách. Tento součin udává maximální množství nepotvrzených dat, která mohou být současně na cestě mezi odesílatelem a příjemcem. Prakticky BDP představuje „velikost potrubí“ síťového spojení – objem dat, který zaplní přenosovou cestu od konce ke konci.

Z architektonického hlediska BDP ovlivňuje několik klíčových rozhodnutí při návrhu sítě. Pro komunikace založené na TCP musí být velikost TCP okna alespoň tak velká jako BDP, aby bylo dosaženo maximální propustnosti. Pokud je velikost okna menší než BDP, odesílatel přestane vysílat a bude čekat na potvrzení dříve, než je „potrubí“ plné, což vede k nevyužitému přenosovému pásmu. Tento vztah je dán vzorcem: Maximální propustnost = Velikost okna / RTT. Optimální výkon TCP tedy vyžaduje nastavení velikosti oken, která odpovídají nebo překračují BDP síťové cesty.

V sítích 3GPP jsou úvahy o BDP obzvláště důležité kvůli proměnlivým charakteristikám bezdrátových spojů. Mobilní sítě vykazují kolísavou šířku pásma (vlivem rádiových podmínek, mobility a zahlcení) a proměnlivou latenci (ovlivněnou zpracováním, plánováním a charakteristikami přenosové sítě). Tyto dynamické změny znamenají, že BDP není statický, ale mění se v čase a za různých síťových podmínek. Síťové prvky se těmto změnám musí přizpůsobovat – například implementací adaptivního škálování TCP oken, inteligentní správy vyrovnávacích pamětí v základnových stanicích a bránách jádra sítě a algoritmů pro řízení zahlcení, které berou v úvahu efektivní BDP.

BDP také přímo ovlivňuje dimenzování vyrovnávacích pamětí v síťových zařízeních. Aby se předešlo ztrátě paketů a maximalizovala propustnost, měly by se vyrovnávací paměti v routerech, přepínačích a základnových stanicích dimenzovat podle BDP spojů, které obsluhují. Nedostatečné vyrovnávací paměti vedou při zahlcení ke ztrátě paketů, zatímco příliš velké paměti mohou způsobit „bufferbloat“ – zvýšenou latenci a kolísání zpoždění. V architekturách 3GPP to ovlivňuje návrh vyrovnávacích pamětí v eNodeB/gNB (radiové přístupové síti), [SGW/PGW](/mobilnisite/slovnik/sgw-pgw/)/[UPF](/mobilnisite/slovnik/upf/) (jádru sítě) a přenosových síťových prvcích. Správné dimenzování vyrovnávacích pamětí na základě odhadů BDP pomáhá udržovat kvalitu služeb (QoS) a minimalizovat latenci pro aplikace v reálném čase.

Role BDP se rozšiřuje na optimalizaci výkonu od konce ke konci v celém systému 3GPP. Je klíčovým parametrem při testování výkonu, plánování kapacity a odstraňování problémů. Porozuměním BDP síťových cest mohou operátoři správně dimenzovat své sítě, konfigurovat parametry protokolů a diagnostikovat problémy s výkonem. V pokročilých nasazeních mohou mechanismy zohledňující BDP dynamicky upravovat přenosové parametry v reakci na měnící se síťové podmínky, čímž zajišťují efektivní využití rádiových i přenosových zdrojů při splnění požadavků na služby.

## K čemu slouží

Bandwidth Delay Product (BDP) existuje jako základní metrika pro charakterizaci a optimalizaci přenosu dat po sítích s nenulovou latencí. Řeší kritický problém nevyužité síťové kapacity, který nastává, když jsou parametry protokolů (zejména velikosti TCP oken) nevyvážené vůči inherentním charakteristikám zpoždění a šířky pásma sítě. Před širším pochopením BDP často sítě trpěly suboptimální propustností, protože odesílatelé vyčerpali svá přenosová okna dříve, než obdrželi potvrzení, což je nutilo pozastavit přenos, i když síťová cesta mohla pojmout více dat.

Vznik konceptu BDP byl motivován potřebou maximalizace propustnosti v dálkových a vysokokapacitních sítích. V raných sítích s nižší šířkou pásma a kratšími vzdálenostmi bylo [RTT](/mobilnisite/slovnik/rtt/) relativně malé, což činilo BDP méně kritickým. S rostoucími síťovými rychlostmi (od kilobitů po gigabity za sekundu) a geografickým rozsahem (včetně transkontinentálních a satelitních spojů) však součin šířky pásma a zpoždění podstatně vzrostl. To učinilo tradiční pevné velikosti oken nedostatečnými a vyžadovalo metriku pro správné dimenzování přenosových parametrů. Standardizace BDP v 3GPP Release 11 odráží jeho důležitost v mobilních sítích, kde se šířka pásma i latence významně mění v důsledku bezdrátových podmínek.

BDP řeší problém neefektivního využití přenosového pásma tím, že poskytuje kvantitativní základ pro konfiguraci parametrů protokolů a síťových zařízení. Umožňuje systémům dosáhnout propustnosti na úrovni linkové rychlosti bez ohledu na vzdálenost, za předpokladu dostatečné vyrovnávací paměti a vhodných velikostí oken. V sítích 3GPP je to obzvláště cenné, protože mobilní spojení kombinují vysokou potenciální šířku pásma s proměnlivou latencí ovlivněnou rádiovými podmínkami, přechody mezi buňkami a zpracováním v jádru sítě. Zohledněním BDP mohou mobilní sítě optimalizovat výkon TCP pro různé služby – od přenosů velkých objemů dat po aplikace citlivé na latenci – a zajistit tak efektivní využití vzácných rádiových zdrojů při zachování dobrého uživatelského zážitku.

## Klíčové vlastnosti

- Kvantifikuje maximální přenosovou kapacitu dat na cestě v síťových trasách
- Určuje optimální velikost TCP okna pro maximální propustnost
- Napomáhá dimenzování vyrovnávacích pamětí v síťových zařízeních, aby se předešlo ztrátám nebo bufferbloatu
- Umožňuje adaptivní ladění přenosových parametrů za proměnlivých podmínek
- Slouží jako klíčová metrika pro plánování a dimenzování síťové kapacity
- Usnadňuje optimalizaci výkonu od konce ke konci v heterogenních sítích

## Definující specifikace

- **TR 37.901** (Rel-15) — UE Application Layer Data Throughput Performance

---

📖 **Anglický originál a plná specifikace:** [BDP na 3GPP Explorer](https://3gpp-explorer.com/glossary/bdp/)
