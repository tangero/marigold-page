---
slug: "ctsarch"
url: "/mobilnisite/slovnik/ctsarch/"
type: "slovnik"
title: "CTSARCH – CTS Access Request CHannel"
date: 2025-01-01
abbr: "CTSARCH"
fullName: "CTS Access Request CHannel"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ctsarch/"
summary: "CTSARCH je vyhrazený uplink kanál v sítích GSM/EDGE, který mobilní stanice používají k vyžádání přístupu k síti pro služby s přepojováním okruhů. Umožňuje efektivní alokaci prostředků oddělením přístu"
---

CTSARCH je uplink kanál v sítích GSM/EDGE, který mobilní stanice používají k vyžádání přístupu k síti pro služby s přepojováním okruhů, jako jsou hlasová volání, čímž zvyšuje efektivitu a zkracuje dobu navazování hovoru.

## Popis

[CTS](/mobilnisite/slovnik/cts/) Access Request CHannel (CTSARCH) je specializovaný řídicí kanál definovaný v architektuře GSM/[EDGE](/mobilnisite/slovnik/edge/) Radio Access Network ([GERAN](/mobilnisite/slovnik/geran/)) dle specifikace 3GPP TS 43.052. Funguje jako součást struktury Common Control Channel ([CCCH](/mobilnisite/slovnik/ccch/)) a slouží jako primární mechanismus pro mobilní stanice ([MS](/mobilnisite/slovnik/ms/)) k iniciování požadavků na služby s přepojováním okruhů. Kanál je specificky navržen pro přístupové procedury související s hlasovými hovory, tísňovými voláními a dalšími službami s přepojováním okruhů, čímž se odlišuje od přístupových kanálů pro přepojování paketů.

Z architektonického hlediska je CTSARCH implementován jako vyhrazený uplink kanál s náhodným přístupem, který mobilní stanice používají k vysílání zpráv Channel Request. Tyto zprávy obsahují klíčové informace včetně identity mobilní stanice, požadovaného typu služby a důvodu navázání. Kanál funguje pomocí protokolu slotted Aloha se specifickými přístupovými parametry definovanými sítí, včetně maximálního počtu opakovaných pokusů, intervalů backoff a procedur power ramping. Subsystém základnové stanice ([BSS](/mobilnisite/slovnik/bss/)) monitoruje CTSARCH a odpovídá zprávami Immediate Assignment na odpovídajícím downlink řídicím kanálu.

Kanál funguje prostřednictvím dobře definované přístupové procedury: když mobilní stanice potřebuje navázat spojení s přepojováním okruhů, nejprve se synchronizuje s broadcast control channel ([BCCH](/mobilnisite/slovnik/bcch/)), aby získala systémové informace včetně parametrů CTSARCH. MS poté vybere vhodný timeslot a vysílá zprávu Channel Request obsahující náhodné referenční číslo a důvod navázání. BSS tento požadavek přijme, přidělí vyhrazený provozní kanál (TCH) nebo signalizační kanál (SDCCH) a odpoví zprávou Immediate Assignment obsahující stejné náhodné reference pro korelaci. Toto dvoukrokové handshake zajišťuje spolehlivou alokaci kanálu při minimalizaci kolizí.

Klíčové součásti systému CTSARCH zahrnují implementaci protokolu náhodného přístupu v mobilní stanici, konfiguraci přijímače základnové přenosové stanice ([BTS](/mobilnisite/slovnik/bts/)) pro detekci přístupových burstů a algoritmy alokace prostředků v řadiči základnové stanice (BSC). Kanál funguje se specifickými charakteristikami fyzické vrstvy, včetně zkrácené délky burstu (přístupové bursty o 88 bitech oproti běžným burstům o 148 bitech) a prodloužených ochranných period pro kompenzaci časové nejistoty. BSS implementuje sofistikované mechanismy detekce a řešení kolizí, včetně analýzy kvality přijímaného signálu a odhadu časového předstihu pro rozlišení více současných přístupových pokusů.

CTSARCH hraje klíčovou roli v celkovém výkonu sítě GSM optimalizací využití rádiových prostředků pro služby s přepojováním okruhů. Jeho návrh vyvažuje poskytnutí dostatečných přístupových příležitostí pro mobilní stanice a zároveň minimalizaci rušení a kolizí. Parametry kanálu může síťový operátor dynamicky upravovat na základě zatížení provozem, konfigurace buňky a požadavků služeb. Správná konfigurace parametrů CTSARCH přímo ovlivňuje klíčové ukazatele výkonu, včetně úspěšnosti navazování hovorů, přístupového zpoždění a celkové kapacity systému pro hlasové služby.

## K čemu slouží

CTSARCH byl vytvořen k řešení specifických výzev v raných sítích GSM souvisejících s efektivním a spolehlivým přístupem ke službám s přepojováním okruhů. Před jeho standardizací používaly sítě GSM obecné kanály s náhodným přístupem, které zpracovávaly přístupové pokusy pro přepojování okruhů i paketů, což vedlo k problémům s kolizemi a suboptimálnímu výkonu pro časově citlivé služby, jako jsou hlasové hovory. Rostoucí poptávka po mobilní telefonii na konci 90. let si vyžádala vyhrazený přístupový mechanismus, který by mohl upřednostňovat požadavky na hlasové služby a poskytovat předvídatelnou přístupovou latenci.

Primární problém, který CTSARCH řeší, je efektivní správa rádiových prostředků během procedur navazování hovoru. Oddělením přístupových požadavků pro přepojování okruhů od jiných typů přístupu k síti umožňuje optimalizovanou alokaci prostředků specificky přizpůsobenou pro hlasové služby. Toto oddělení umožňuje síťovým operátorům implementovat různé přístupové strategie pro různé typy služeb, přičemž parametry CTSARCH jsou laděny pro specifické požadavky komunikací s přepojováním okruhů, včetně striktních omezení zpoždění a požadavků na spolehlivost.

Historický kontext ukazuje, že vývoj CTSARCH byl motivován omezeními dřívějších přístupových mechanismů, které zacházely se všemi servisními požadavky stejně. Jak se sítě GSM vyvíjely k podpoře hlasových i datových služeb, ukázalo se, že univerzální přístup k náhodnému přístupu je nedostatečný. Vytvoření CTSARCH v Release 8 představovalo významný vývoj v architektuře sítí GSM/EDGE, který umožnil sofistikovanější diferenciaci služeb a správu kvality služeb na úrovni rádiového přístupu. Tato specializace byla obzvláště důležitá, protože sítě potřebovaly podporovat rostoucí hlasový provoz a současně zavádět datové služby s přepojováním paketů.

## Klíčové vlastnosti

- Vyhrazený uplink kanál pro požadavky na služby s přepojováním okruhů
- Používá protokol slotted Aloha pro náhodný přístup s konfigurovatelnými parametry
- Podporuje více důvodů navázání včetně tísňových hovorů
- Implementuje mechanismy detekce a řešení kolizí
- Umožňuje konfiguraci přístupových parametrů specifických pro službu
- Poskytuje odhad časového předstihu během přístupové procedury

## Související pojmy

- [CCCH – Common Control Channel](/mobilnisite/slovnik/ccch/)
- [GERAN – GSM EDGE Radio Access Network](/mobilnisite/slovnik/geran/)

## Definující specifikace

- **TS 43.052** (Rel-19) — GSM Cordless Telephony System (CTS) Radio Interface

---

📖 **Anglický originál a plná specifikace:** [CTSARCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/ctsarch/)
