---
slug: "aal1"
url: "/mobilnisite/slovnik/aal1/"
type: "slovnik"
title: "AAL1 – ATM Adaptation Layer type 1"
date: 2025-01-01
abbr: "AAL1"
fullName: "ATM Adaptation Layer type 1"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/aal1/"
summary: "AAL1 je protokol přizpůsobovací vrstvy ATM navržený pro služby s konstantním přenosovým tokem (CBR), které vyžadují časovou synchronizaci mezi zdrojem a cílem. Poskytuje emulaci okruhu v sítích ATM, c"
---

AAL1 je protokol přizpůsobovací vrstvy ATM navržený pro služby s konstantním přenosovým tokem vyžadující časovou synchronizaci, který poskytuje emulaci okruhu v sítích ATM pro přenos tradičního TDM provozu, jako je hlas a video.

## Popis

ATM Adaptation Layer type 1 (AAL1) je specifický protokol přizpůsobovací vrstvy v rámci zásobníku protokolů ATM, standardizovaný ITU-T a přijatý 3GPP pro určitá síťová rozhraní. Funguje jako mezivrstva mezi vrstvou ATM a aplikacemi vyšších vrstev a je speciálně navržen pro podporu služeb s konstantním přenosovým tokem (CBR), které vyžadují přesný časový vztah mezi zdrojem a cílem. Protokol je definován ve specifikaci 3GPP 29.163, která podrobně popisuje jeho implementaci pro interoperabilitu mezi IP sítěmi a legacy okruhově přepínanými sítěmi.

AAL1 funguje tak, že segmentuje a znovu skládá spojité bitové toky ze zdrojů CBR do buněk ATM pro přenos přes sítě ATM. Používá strukturovaný přístup s hlavičkou SAR-PDU o velikosti 1 bajtu, která obsahuje sekvenční čísla, bity ochrany sekvenčního čísla a indikátor konvergenční podvrstvy. Protokol podporuje dva provozní režimy: nestrukturovaný přenos dat (kde je celý tok CBR považován za spojitou bitovou sekvenci) a strukturovaný přenos dat (kde je tok CBR rozdělen do bloků odpovídajících konkrétním časovým slotům). Pro obnovu časování implementuje AAL1 několik mechanismů včetně synchronního reziduálního časového razítka (SRTS) a metod adaptivní obnovy hodin pro udržení synchronizace mezi vysílačem a přijímačem.

Architektura protokolu se skládá ze dvou podvrstev: podvrstvy segmentace a opětovného složení (SAR) a konvergenční podvrstvy (CS). Podvrstva SAR se zabývá rozdělením dat CBR na 47bajtové užitečné zatížení pro buňky ATM a jejich opětovným složením v cíli. CS vykonává funkce jako zpracování kolísání zpoždění buněk, číslování sekvencí a obnova časování. AAL1 také zahrnuje schopnosti dopředné korekce chyb (FEC) pomocí Reedova-Solomonova kódování pro ochranu před ztrátou buněk v síti ATM, což je zvláště důležité pro služby v reálném čase, jako je přenos hlasu a videa.

V sítích 3GPP hraje AAL1 klíčovou roli v službách emulace okruhu, což umožňuje přenos tradičních TDM okruhů (jako jsou linky E1/T1) přes paketově přepínané páteřní sítě ATM. To umožňuje mobilním operátorům integrovat legacy zařízení a služby s moderní infrastrukturou založenou na paketech. Protokol zajišťuje, že časově citlivé aplikace dostávají předvídatelný přenos s nízkým jitterem, který vyžadují, a zároveň využívá výhod statistického multiplexování sítí ATM. Návrh AAL1 řeší specifické výzvy přenosu izochronního provozu přes asynchronní sítě při zachování záruk kvality služby nezbytných pro komunikaci v reálném čase.

## K čemu slouží

AAL1 byl vytvořen, aby řešil základní výzvu přenosu provozu s konstantním přenosovým tokem a citlivého na časování přes sítě ATM, které jsou ze své podstaty paketové a asynchronní. Tradiční telekomunikační služby, jako je hlas, videokonference a okruhově přepínaná data, vyžadovaly přesnou časovou synchronizaci mezi koncovými body, kterou přenos založený na buňkách ATM nativně nepodporoval. AAL1 tento problém vyřešil tím, že poskytl schopnosti emulace okruhu, které umožnily legacy TDM zařízením a službám fungovat přes efektivnější infrastrukturu ATM.

Vývoj AAL1 byl motivován přechodem telekomunikačního průmyslu od čistě okruhově přepínaných sítí k hybridním sítím začleňujícím technologie paketového přepínání. V 90. letech a na počátku 21. století se ATM ukázalo jako slibná páteřní technologie nabízející výhody statistického multiplexování oproti tradičním TDM sítím. Operátoři však potřebovali zachovat stávající výnosné služby při migraci infrastruktury. AAL1 umožnil tento postupný přechod tím, že poskytl standardizovanou metodu pro zapouzdření a přenos TDM okruhů přes ATM s minimálním zhoršením kvality.

Předchozí přístupy k přenosu provozu v reálném čase přes paketové sítě trpěly časovým jitterem, citlivostí na ztrátu paketů a složitými požadavky na synchronizaci. AAL1 tyto nedostatky řešil prostřednictvím svého strukturovaného návrhu přizpůsobovací vrstvy, který zahrnoval číslování sekvencí, mechanismy obnovy časování a dopřednou korekci chyb. To umožnilo mobilním operátorům využívat výhody efektivity ATM při zachování kvality služeb očekávané od tradičních okruhově přepínaných sítí, což usnadnilo vývoj směrem ke konvergované infrastruktuře založené na paketech.

## Klíčové vlastnosti

- Podpora služeb s konstantním přenosovým tokem (CBR)
- Emulace okruhu v sítích ATM
- Mechanismy časové synchronizace včetně SRTS
- Dopředná korekce chyb pomocí Reedova-Solomonova kódování
- Strukturované a nestrukturované režimy přenosu dat
- Číslování sekvencí pro detekci ztráty buněk

## Definující specifikace

- **TS 29.163** (Rel-19) — Interworking between 3GPP IM CN and CS networks

---

📖 **Anglický originál a plná specifikace:** [AAL1 na 3GPP Explorer](https://3gpp-explorer.com/glossary/aal1/)
