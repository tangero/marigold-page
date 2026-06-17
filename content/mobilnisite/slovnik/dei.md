---
slug: "dei"
url: "/mobilnisite/slovnik/dei/"
type: "slovnik"
title: "DEI – Drop Eligible Indicator"
date: 2025-01-01
abbr: "DEI"
fullName: "Drop Eligible Indicator"
category: "QoS"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/dei/"
summary: "Jednobitové pole v hlavičkách paketů, které indikuje, zda lze paket při přetížení sítě zrušit. Umožňuje selektivní zahazování paketů pro udržení QoS kritického provozu a efektivní správu síťových zdro"
---

DEI (Drop Eligible Indicator) je jednobitové pole v hlavičce, které označuje paket jako vhodný ke zrušení při přetížení sítě, aby byla zachována kvalita služeb pro provoz s vyšší prioritou.

## Popis

Drop Eligible Indicator (DEI) je základní mechanismus kvality služeb (QoS) definovaný ve specifikacích 3GPP, který funguje na úrovni paketů pro správu přetížení sítě. Jedná se o jednobitové pole vložené do hlaviček různých protokolů, včetně ethernetových rámců (jako součást pole Priority Code Point ve VLAN tagu) a potenciálně i v rozšířeních protokolů jako [GTP-U](/mobilnisite/slovnik/gtp-u/) nebo jiných transportních protokolech používaných v 5G transportních sítích. Když síťový uzel (jako router, přepínač nebo User Plane Function) zaznamená přetížení, může zkontrolovat bit DEI frontovaných paketů. Pakety označené DEI=1 jsou považovány za 'vhodné ke zrušení' a mohou být selektivně zahazovány dříve než pakety označené DEI=0, které jsou považovány za vyšší prioritu a měly by být zachovány co nejdéle. Tento mechanismus je formou aktivní správy front (AQM).

Fungování DEI je úzce spojeno s klasifikací provozu a zásadami označování. Typicky síťové funkce jako Session Management Function ([SMF](/mobilnisite/slovnik/smf/)) nebo Policy Control Function ([PCF](/mobilnisite/slovnik/pcf/)) definují pravidla QoS, která mapují konkrétní datové toky (identifikované 5-ticí, identifikátorem QoS toku nebo aplikací) na profil QoS. Součástí tohoto profilu může být zásada označování, která specifikuje, zda mají být pakety z daného toku označeny jako vhodné ke zrušení (DEI=1) nebo ne (DEI=0) za určitých podmínek, například když tok překročí svou garantovanou přenosovou rychlost, ale zůstává v rámci maximální přenosové rychlosti. Označování obvykle provádí User Plane Function ([UPF](/mobilnisite/slovnik/upf/)) pro provoz ve směru downlink nebo User Equipment (UE) pro provoz ve směru uplink na základě těchto vynucených zásad.

Z architektonického hlediska DEI funguje v rámci širšího rámce QoS, který zahrnuje další značky, jako je Differentiated Services Code Point ([DSCP](/mobilnisite/slovnik/dscp/)) pro chování na každém hopu a 5G QoS Identifier ([5QI](/mobilnisite/slovnik/5qi/)) pro charakteristiky služby end-to-end. Zatímco DSCP/5QI definuje prioritu plánování a typ zdroje (např. Guaranteed Bit Rate, Delay Critical [GBR](/mobilnisite/slovnik/gbr/)), DEI poskytuje další, ortogonální dimenzi pro správu přetížení v rámci dané třídy priority. Například dva toky se stejným 5QI (a tedy podobnými požadavky na latenci a prioritu) lze během přetížení rozlišit: jeden může být označen jako vhodný ke zrušení, pokud jde o best-effort komponentu služby, zatímco druhý zůstane nevhodný ke zrušení, pokud přenáší zásadní řídicí informace.

V systému 5G je role DEI klíčová v segmentech transportní sítě (rozhraní N3, N6, N9), které přenášejí provoz uživatelské roviny. Umožňuje transportním uzlům implementovat jednoduché a efektivní akce při přetížení bez nutnosti hluboké kontroly paketů nebo porozumění specifickým parametrům QoS 3GPP. Toto oddělení umožňuje škálovatelný návrh sítě, kde jádrová síť řídí záměr (prostřednictvím zásad označování) a podkladová IP transportní infrastruktura provádí reakci na přetížení na základě standardního bitu DEI. Účinnost DEI závisí na správné konfiguraci algoritmů správy front (jako je Weighted Random Early Detection - WRED) na síťových zařízeních, aby byl bit DEI využit pro rozhodování o zrušení.

## K čemu slouží

DEI existuje, aby poskytl škálovatelnou a standardizovanou metodu pro správu přetížení sítě v paketově přepínaných sítích, zejména v transportních segmentech systémů 3GPP. Před takovými explicitními schématy označování sítě často spoléhaly na tail-drop při přetížení, kdy jsou pakety nerozlišně zahazovány po naplnění fronty, což vede k problémům s globální synchronizací, vysoké latenci a nízké spravedlnosti mezi datovými toky. DEI jako součást širší architektury Differentiated Services (DiffServ) umožňuje inteligentnější správu přetížení tím, že umožňuje selektivní zahazování paketů na základě zásad operátora.

Primární problém, který DEI řeší, je efektivní využití síťových zdrojů během období přetížení při současné ochraně výkonu provozu kritického pro misi nebo generujícího příjmy. V mobilních sítích, kde může být šířka pásma proměnlivá a drahá, je zásadní zajistit, aby služby s vysokou prioritou, jako jsou hlasové hovory, nouzová komunikace nebo příkazy pro průmyslový IoT s nízkou latencí, nebyly ovlivněny přetížením způsobeným méně kritickým provozem, jako jsou stahování souborů na pozadí nebo aktualizace softwaru. DEI poskytuje jednoduchý binární signál, který transportní zařízení mohou použít k okamžitému rozhodnutí o zrušení bez složitého zpracování, což odpovídá potřebě vysokorychlostního přeposílání v jádrových sítích.

Historicky, jak se sítě 3GPP vyvíjely z přepojování okruhů na plně IP architektury (počínaje 4G EPS a plně realizováno v 5GS), stala se potřeba mechanismů QoS kompatibilních s IP prvořadou. DEI, vypůjčený a adaptovaný ze standardů [IEEE](/mobilnisite/slovnik/ieee/) Ethernet a IETF DiffServ, byl integrován do rámce QoS 3GPP, aby překlenul propast mezi parametry QoS uvědomujícími si rádiové rozhraní (jako 5QI) a možnostmi QoS podkladové transportní infrastruktury. Řeší omezení spočívající v bohaté klasifikaci QoS uvnitř jádra 3GPP, ale bez efektivního způsobu, jak předat informace o přednosti zrušení do transportní sítě, která se často skládá z více dodavatelských IP routerů a přepínačů pracujících se standardními IP/ethernetovými hlavičkami.

## Klíčové vlastnosti

- Jednobitové pole v hlavičkách paketů pro jednoduchou signalizaci s nízkou režií
- Umožňuje selektivní zahazování paketů při přetížení sítě
- Funguje ve spojení s klasifikací QoS a zásadami označování
- Působí ortogonálně k indikátorům priority plánování (např. DSCP, 5QI)
- Standardizováno pro použití napříč transportními rozhraními 3GPP N3, N6 a N9
- Usnadňuje aktivní správu front (AQM) v transportních uzlech

## Související pojmy

- [5QI – 5G QoS Identifier](/mobilnisite/slovnik/5qi/)
- [UPF – User Plane Function](/mobilnisite/slovnik/upf/)

## Definující specifikace

- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 29.244** (Rel-19) — PFCP Specification for Control/User Plane Separation
- **TS 29.514** (Rel-19) — 5G System; Policy Authorization Service; Stage 3
- **TS 29.890** (Rel-16) — CT3 5G System Technical Report

---

📖 **Anglický originál a plná specifikace:** [DEI na 3GPP Explorer](https://3gpp-explorer.com/glossary/dei/)
