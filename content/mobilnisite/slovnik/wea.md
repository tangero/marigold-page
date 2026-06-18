---
slug: "wea"
url: "/mobilnisite/slovnik/wea/"
type: "slovnik"
title: "WEA – Wireless Emergency Alert"
date: 2026-01-01
abbr: "WEA"
fullName: "Wireless Emergency Alert"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/wea/"
summary: "Wireless Emergency Alert (WEA) je systém veřejné bezpečnosti, který doručuje kritické nouzové zprávy na mobilní zařízení v konkrétní geografické oblasti. Umožňuje vládním orgánům varovat veřejnost pře"
---

WEA je systém veřejné bezpečnosti, který doručuje kritické nouzové zprávy na mobilní zařízení v konkrétní geografické oblasti.

## Popis

Wireless Emergency Alert (WEA) je standardizovaná služba v rámci sítí 3GPP navržená pro vysílání kritických, neinteraktivních nouzových zpráv všem kompatibilním mobilním zařízením v cílové geografické oblasti, známé jako oblast pro vysílání buňkami (cell broadcast area). Systém funguje nezávisle na běžných kanálech pro uživatelský provoz a využívá mechanismus služby vysílání buňkami (Cell Broadcast Service, [CBS](/mobilnisite/slovnik/cbs/)) definovaný v jádru sítě. Využívá entitu Centrum pro vysílání buňkami (Cell Broadcast Centre, [CBC](/mobilnisite/slovnik/cbc/)), která se rozhraní připojuje k systémům veřejného varování (jako jsou vládní varovné orgány) pro příjem výstražných zpráv. CBC následně tyto zprávy předává příslušným řadičům základnových stanic (Base Station Controller, [BSC](/mobilnisite/slovnik/bsc/)) pro 2G/3G nebo entitám správy mobility (Mobility Management Entity, [MME](/mobilnisite/slovnik/mme/)) pro 4G, které následně instruují základnové stanice (NodeB nebo eNodeB), aby vysílaly výstrahu přes rozhraní vzduch pomocí vyhrazených kanálů pro vysílání buňkami.

Z architektonického hlediska se WEA integruje do stávající infrastruktury mobilní sítě bez nutnosti uživatelského předplatného nebo registrace zařízení, čímž zajišťuje, že se varování dostanou ke každému schopnému zařízení v zóně, včetně uživatelů v roamingu. Zpráva obsahuje parametry jako identifikátor zprávy, sériové číslo, geografický rozsah (definovaný sadou buněk nebo varovnou oblastí), obsah zprávy a typ výstrahy (např. Extrémní, Závažná, AMBER). Firmware modemu uživatelského zařízení (UE) je zodpovědný za sledování vyhrazeného vysílacího kanálu, dekódování zpráv určených pro jeho aktuální polohu a jejich prezentaci uživateli pomocí odlišného audiovizuálního signálu, který potlačí tichý režim.

Účinnost služby závisí na přesném geografickém cílení, kterého je dosaženo mapováním cílové oblasti výstrahy na seznam identifikátorů buněk (cell IDs) nebo oblastí sledování (tracking areas) v síti. To vyžaduje koordinaci mezi síťovými operátory a varovnými orgány pro udržování přesných geografických dat. Zprávy WEA jsou krátké, typicky 90 nebo 360 znaků v závislosti na vydání (release), a mohou obsahovat jedinečný výstražný tón a vibrační vzor pro zajištění pozornosti. Jsou zahrnuta bezpečnostní opatření, jako je autentizace zpráv, aby se zabránilo podvržení. Role WEA je klíčová pro veřejné varování a doplňuje další systémy, jako je systém varování před zemětřesením a tsunami (Earthquake and Tsunami Warning System, ETWS) a systém komerčních mobilních výstrah (Commercial Mobile Alert System, [CMAS](/mobilnisite/slovnik/cmas/)), a poskytuje spolehlivý, síťově efektivní vysílací mechanismus pro hromadné oznamování.

## K čemu slouží

WEA byla vytvořena, aby řešila kritickou potřebu rychlého, spolehlivého a geograficky cíleného systému veřejného varování využívajícího infrastrukturu mobilní telekomunikace. Před její standardizací byly nouzové výstrahy šířeny primárně prostřednictvím televize, rádia nebo sirén, které měly omezení v dosahu, bezprostřednosti a mobilitě. Tsunami v Indickém oceánu v roce 2004 a další katastrofy zdůraznily nutnost schopnosti přímého varování osob, které by mohlo varovat jednotlivce bez ohledu na jejich činnost nebo polohu, což vedlo k celosvětovým iniciativám pro varovné systémy založené na mobilních sítích.

3GPP standardizovalo WEA, aby poskytlo jednotný technický rámec umožňující interoperabilitu mezi různými síťovými operátory, výrobci zařízení a národními varovnými orgány. Řeší problém se zpožděním výstrah a mezerami v pokrytí tím, že využívá všudypřítomnou mobilní síť, a zajišťuje doručení výstrah během sekund na všechna zařízení v ohrožené oblasti bez přetížení sítě individuálním [SMS](/mobilnisite/slovnik/sms/) provozem. Systém je navržen tak, aby fungoval i při přetížených síťových podmínkách, protože vysílané zprávy nevyžadují individuální signalizační spojení. Jeho vytvoření bylo motivováno regulatorními požadavky v různých zemích (např. americký [CMAS](/mobilnisite/slovnik/cmas/), evropský systém veřejného varování), které nařizují mobilním operátorům podporu nouzových výstrah, což vedlo 3GPP k začlenění těchto schopností od vydání (Release) 9 dále, přičemž WEA byla konkrétně upřesňována v pozdějších vydáních.

## Klíčové vlastnosti

- Geograficky cílené vysílání do specifických oblastí buněk (cell areas) nebo oblastí sledování (tracking areas)
- Doručení nezávislé na uživatelském předplatném, registraci nebo stavu roamingu
- Odlišné výstrahy s potlačením režimů s jedinečnými tóny a vibracemi, i v tichém režimu
- Podpora více kategorií výstrah (např. Extrémní, Závažná, AMBER, Prezidentská)
- Síťově efektivní vysílací mechanismus, který se vyhýbá signalizačnímu přetížení
- Autentizace zpráv a ochrana integrity pro prevenci podvržení

## Definující specifikace

- **TS 22.268** (Rel-20) — Public Warning System (PWS) Requirements
- **TS 23.041** (Rel-19) — Cell Broadcast Service and Public Warning System

---

📖 **Anglický originál a plná specifikace:** [WEA na 3GPP Explorer](https://3gpp-explorer.com/glossary/wea/)
