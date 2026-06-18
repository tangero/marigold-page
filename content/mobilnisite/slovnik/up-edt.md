---
slug: "up-edt"
url: "/mobilnisite/slovnik/up-edt/"
type: "slovnik"
title: "UP-EDT – User Plane Early Data Transmission"
date: 2025-01-01
abbr: "UP-EDT"
fullName: "User Plane Early Data Transmission"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/up-edt/"
summary: "UP-EDT je mechanismus v LTE a 5G NR, který umožňuje přenos malých datových paketů během procedury náhodného přístupu (RACH), a to ještě před plným navázáním RRC spojení. Výrazně snižuje signalizační r"
---

UP-EDT je mechanismus v LTE a 5G NR, který přenáší malé datové pakety během náhodného přístupu před plným navázáním RRC spojení, čímž snižuje signalizační zátěž a latenci pro efektivní přenosy IoT dat.

## Popis

User Plane Early Data Transmission (UP-EDT) je optimalizační technika definovaná pro technologie LTE-M a NB-IoT v rámci standardů 3GPP. Umožňuje zařízení odeslat omezené množství uživatelských dat vestavěných do zprávy 3 (Msg3) procedury náhodného přístupu ([RACH](/mobilnisite/slovnik/rach/)), konkrétně během žádosti o obnovení [RRC](/mobilnisite/slovnik/rrc/) spojení (RRC Connection Resume Request). Tradičně vyžaduje přenos dat dokončení celé procedury navázání nebo obnovení RRC spojení, což zahrnuje výměnu více zpráv. UP-EDT tento proces zkracuje tím, že umožňuje přenést uplink data společně s počáteční signalizační zprávou, a síť může odpovědět downlink daty v následující zprávě 4 (Msg4), čímž se celá transakce dokončí ve vysoce kompaktní výměně.

Z architektonického hlediska UP-EDT využívá stávající stavy a procedury protokolu RRC, ale zavádí nové zpracování v [eNB](/mobilnisite/slovnik/enb/)/gNB a v UE. UE indikuje svou schopnost a záměr použít UP-EDT pomocí specifické příčinové hodnoty (cause value) v žádosti o obnovení RRC spojení. eNB/gNB po přijetí této žádosti s uplink daty může data zpracovat a okamžitě odpovědět zprávou RRC Connection Release, která může rovněž obsahovat downlink data pro UE. Celá tato transakce proběhne bez přechodu UE do stavu připojení (RRC_CONNECTED), takže zařízení zůstává po většinu času v energeticky úsporném stavu idle nebo inactive. Datové pakety jsou zpracovány běžným zásobníkem uživatelské roviny ([PDCP](/mobilnisite/slovnik/pdcp/), [RLC](/mobilnisite/slovnik/rlc/)), ale v kontextu této zkrácené signalizační výměny.

Klíčovými komponentami jsou vrstva RRC v UE, která sestavuje Msg3 s daty, a síťové koncové body RRC a uživatelské roviny v základnové stanici. UP-EDT funguje ve spojení s optimalizací Control Plane CIoT EPS ([CP-EDT](/mobilnisite/slovnik/cp-edt/) je protějšek pro data řídicí roviny), ale je specificky určen pro efektivnější přenos dat uživatelské roviny. Jeho úlohou je minimalizovat signalizační rádiové nosiče, snížit latenci pro malé datové záblesky (typické pro IoT senzory) a snížit spotřebu energie zařízení zkrácením doby zapnutého rádiového rozhraní. Jde o klíčovou funkci pro hromadnou komunikaci mezi stroji (mMTC) v celulárním IoT, která umožňuje škálovatelnou podporu pro miliony nízkopříkonových zařízení s občasným přenosem dat.

## K čemu slouží

UP-EDT byl vytvořen, aby vyřešil zásadní neefektivitu používání tradičních celulárních procedur navazování spojení pro IoT zařízení, která přenášejí velmi malá a občasná data. Před zavedením [EDT](/mobilnisite/slovnik/edt/) spouštělo IoT zařízení odesílající několik bajtů dat dlouhé navázání/obnovení [RRC](/mobilnisite/slovnik/rrc/) spojení zahrnující několik signalizačních zpráv, z nichž každá vyžadovala zpracování, energii a rádiové zdroje. Tato režie byla často řádově větší než samotný užitečný přenos, což plýtvalo kapacitou sítě a rychle vybíjelo baterii zařízení, což je kritické pro zařízení navržená na provoz po mnoho let na jedno nabití.

Tato technologie byla motivována specifickými charakteristikami provozu služeb mMTC, jako jsou chytré měřiče, sledovače majetku a environmentální senzory. Tato zařízení generují sporadické, malé datové reporty, u kterých signalizační náklady dominovaly celkovým nákladům transakce. UP-EDT tento problém řeší přizpůsobením stávajících signalizačních zpráv náhodného přístupu a obnovení spojení tak, aby přenášely uživatelská data, čímž efektivně slučuje fázi přenosu dat s fází navazování spojení. Tím se snižuje počet potřebných výměn zpráv z několika na v podstatě dvě (Msg3 a Msg4), což drasticky snižuje latenci a spotřebu energie.

Zaveden v Release 15 jako součást širších vylepšení LTE-M/NB-IoT, UP-EDT navázal na dřívější IoT optimalizace jako PSM a eDRX. Přímo řešil omezení počátečních optimalizací CIoT EPS, které nabízely CP-EDT, ale pouze pro řídicí rovinu. UP-EDT rozšířil tento přínos na uživatelskou rovinu, což je nezbytné pro IP nebo non-IP doručování dat přes cestu uživatelské roviny. Jeho vznik byl hnán požadavky operátorů na vyšší efektivitu sítě a cíli výrobců umožnit skutečně nízkopříkonový IoT v široké oblasti, čímž se stala celulární technologie konkurenceschopnou vůči alternativám v nelicencovaném pásmu, jako je LoRaWAN.

## Klíčové vlastnosti

- Přenáší data uživatelské roviny uvnitř RACH Msg3 (žádost o obnovení RRC spojení)
- Umožňuje síti odpovědět downlink daty ve zprávě RRC Connection Release (Msg4)
- Vyhýbá se plnému přechodu do stavu RRC_CONNECTED, čímž šetří energii zařízení
- Významně snižuje signalizační režii pro přenos malých dat
- Aplikovatelné pro kategorie zařízení LTE-M a NB-IoT
- Síťově řízená alokace zdrojů pro uplink data v Msg3

## Související pojmy

- [CP-EDT – Control Plane Early Data Transmission](/mobilnisite/slovnik/cp-edt/)

## Definující specifikace

- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [UP-EDT na 3GPP Explorer](https://3gpp-explorer.com/glossary/up-edt/)
