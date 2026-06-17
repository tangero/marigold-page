---
slug: "nch"
url: "/mobilnisite/slovnik/nch/"
type: "slovnik"
title: "NCH – Notification Channel"
date: 2025-01-01
abbr: "NCH"
fullName: "Notification Channel"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/nch/"
summary: "Vysílací kanál v sítích GSM používaný k upozornění mobilních stanic na příchozí hovory nebo zprávy, když jsou v klidovém režimu. Je základní součástí mechanismu pagingu, který umožňuje efektivní šetře"
---

NCH je vysílací kanál v sítích GSM, který v rámci mechanismu pagingu upozorňuje mobilní stanice v klidovém stavu na příchozí hovory nebo zprávy.

## Popis

Notification Channel (NCH) je specifický logický kanál v architektuře rozhraní GSM (Global System for Mobile Communications), definovaný v raných vydáních 3GPP. Funguje v rámci struktury časových slotů vysílacího řídicího kanálu ([BCCH](/mobilnisite/slovnik/bcch/)) a používá se výhradně pro paging a notifikace. Primární funkcí NCH je informovat mobilní stanice ([MS](/mobilnisite/slovnik/ms/)), označované v pozdější terminologii také jako uživatelské zařízení (UE), o síťových událostech iniciovaných sítí, zatímco je MS v klidovém režimu – tedy ve stavu, kdy je rádiový přijímač periodicky aktivní, ale není zapojen do hovoru nebo datové relace.

Technicky NCH funguje tak, že přenáší pagingové zprávy odesílané z řadiče základnových stanic ([BSC](/mobilnisite/slovnik/bsc/)) přes vysílač-přijímač základnové stanice ([BTS](/mobilnisite/slovnik/bts/)). Tyto zprávy se vysílají v rámci konkrétní buňky na předdefinovaných časových slotech a frekvencích. Každé MS je přiřazeno k pagingové skupině na základě své identity International Mobile Subscriber Identity ([IMSI](/mobilnisite/slovnik/imsi/)). Síť vypočítá, kdy a na kterých zdrojích NCH má dané MS naslouchat pagingovým zprávám. Tento skupinový přístup umožňuje MS zapínat přijímač pouze v konkrétních, naplánovaných intervalech namísto nepřetržitého naslouchání, což je klíčové pro šetření životnosti baterie – což byl hlavní konstrukční cíl u prvních mobilních telefonů.

Architektura zahrnuje několik klíčových komponent. Ústředna mobilní komunikace ([MSC](/mobilnisite/slovnik/msc/)) přijme příchozí hovor nebo SMS a určí oblast pokrytí, kde je cílové MS registrováno. Poté odešle pagingový požadavek k řadičům BSC obsluhujícím tuto oblast. BSC naformátuje pagingovou zprávu, která obsahuje identitu MS (jako IMSI nebo Temporary Mobile Subscriber Identity (TMSI)), a naplánuje její vysílání na NCH příslušných buněk BTS. MS, které je synchronizované se síťovým časováním a zná svou pagingovou skupinu, se probudí ve správný okamžik, dekóduje NCH a zkontroluje, zda je jeho identita přítomna v pagingové zprávě. Pokud ano, MS iniciuje žádost o kanál, aby přešlo do vyhrazeného režimu a mohlo reagovat na hovor nebo zprávu.

Jeho role v síti je klíčová pro procedury mobility a navazování hovorů. Umožňuje síti lokalizovat a kontaktovat MS v klidovém stavu, aniž by MS muselo nepřetržitě vysílat nebo naslouchat, čímž optimalizuje jak baterii UE, tak rádiové zdroje sítě. Efektivita pagingového mechanismu NCH přímo ovlivňuje kapacitu sítě GSM – kolik účastníků může podporovat – a vnímanou rychlost reakce pro uživatele přijímající hovory. Ačkoli pozdější generace (3G UMTS, 4G LTE, 5G NR) vyvinuly efektivnější pagingové mechanismy s různými názvy kanálů a strukturami, základní koncept vyhrazeného notifikačního nebo pagingového kanálu pochází právě z NCH v GSM.

## K čemu slouží

NCH byl vytvořen jako součást původních specifikací GSM, aby vyřešil základní problém spojení s mobilním zařízením, které není aktivně v hovoru. V rané mobilní telefonii byla možnost, aby síť mohla iniciovat komunikaci s zapnutým, ale neaktivním telefonem, klíčovým požadavkem. Bez vyhrazeného notifikačního mechanismu by telefony musely nepřetržitě naslouchat, což by rychle vybíjelo baterie, nebo by byly nedostupné pro příchozí hovory.

Historický kontext spočívá v návrhu GSM na konci 80. a začátku 90. let 20. století, kde digitální technologie umožnila sofistikované struktury kanálů s časovým dělením. NCH toho využil k vytvoření efektivního, naplánovaného vysílacího systému. Řešil tak omezení jednodušších analogových systémů, které měly méně efektivní způsoby signalizace mobilům. Skupinový paging na NCH dramaticky snížil spotřebu energie mobilních stanic ve srovnání s přístupem nepřetržitého naslouchání, což bylo zásadní pro spotřebitelské přijetí ručních telefonů.

Jeho vytvoření bylo motivováno potřebou efektivity sítě a dostupnosti účastníka. Seskupením uživatelů a plánováním pagingových zpráv mohla síť minimalizovat vysílací provoz potřebný pro paging, čímž uvolnila rádiové zdroje pro skutečné hovory. Také standardizoval metodu upozorňování uživatelů na SMS zprávy, které se staly klíčovou službou GSM. NCH vytvořil vzor pro všechny následující pagingové kanály v pozdějších systémech 3GPP, který se vyvinul v Paging Channel (PCH) v UMTS a v pagingovou proceduru na Physical Downlink Control Channel ([PDCCH](/mobilnisite/slovnik/pdcch/)) v LTE a NR, přičemž všechny zdědily základní princip efektivního, naplánovaného upozorňování zařízení v klidovém stavu.

## Klíčové vlastnosti

- Specifický logický kanál GSM používaný pro paging mobilních stanic v klidovém stavu
- Funguje v rámci struktury vysílacího řídicího kanálu (BCCH)
- Využívá pagingové skupiny založené na IMSI k plánování intervalů naslouchání MS
- Zásadní pro šetření baterie v klidovém režimu
- Přenáší zprávy pro příchozí hlasové hovory a notifikace SMS
- Umožňuje efektivní využití síťových zdrojů snížením potřeby nepřetržitého vysílání

## Související pojmy

- [BCCH – Broadcast Control Channel](/mobilnisite/slovnik/bcch/)
- [IMSI – International Mobile Subscriber Identity](/mobilnisite/slovnik/imsi/)
- [BSC – Base Station Controller](/mobilnisite/slovnik/bsc/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 43.068** (Rel-19) — Voice Group Call Service (VGCS) Stage 2
- **TS 43.069** (Rel-19) — Voice Broadcast Service (VBS) Stage 2

---

📖 **Anglický originál a plná specifikace:** [NCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/nch/)
