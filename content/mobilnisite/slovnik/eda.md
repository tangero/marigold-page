---
slug: "eda"
url: "/mobilnisite/slovnik/eda/"
type: "slovnik"
title: "EDA – Extended Dynamic Allocation"
date: 2025-01-01
abbr: "EDA"
fullName: "Extended Dynamic Allocation"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/eda/"
summary: "Mechanismus přidělování zdrojů v sítích GSM/EDGE, který mobilní stanici umožňuje dynamicky využívat více časových slotů v rámci TDMA rámce pro uplinkový přenos dat. Významně zvyšuje uplinkovou propust"
---

EDA je mechanismus přidělování zdrojů v sítích GSM/EDGE, který mobilní stanici dynamicky přiřazuje více časových slotů na TDMA rámec pro uplinkový přenos, čímž zvyšuje propustnost a efektivitu přizpůsobením potřebám datového toku.

## Popis

Extended Dynamic Allocation (EDA, rozšířené dynamické přidělování) je schéma přidělování kanálů definované ve specifikacích GSM/[EDGE](/mobilnisite/slovnik/edge/) Radio Access Network ([GERAN](/mobilnisite/slovnik/geran/)), zejména v dokumentu 3GPP TS 45.912. Funguje v rámci struktury Time Division [Multiple Access](/mobilnisite/slovnik/multiple-access/) (TDMA) systému GSM, kde je rádiový kanál rozdělen na opakující se rámce o osmi časových slotech. EDA určuje, jak jsou mobilní stanici ([MS](/mobilnisite/slovnik/ms/)) přidělovány časové sloty pro uplinkový přenos paketových dat při použití technologií jako [GPRS](/mobilnisite/slovnik/gprs/) nebo EDGE. Na rozdíl od základních metod přidělování umožňuje EDA síti dynamicky přiřadit MS sadu časových slotů, které nemusí být v rámci TDMA rámce nutně souvislé. Toto přidělení je signalizováno pomocí řídicích zpráv na Packet Associated Control Channel (PACCH).

Mechanismus funguje tak, že Packet Control Unit (PCU) sítě vyhodnotí možnosti MS, aktuální rádiové podmínky a dostupné síťové zdroje. Poté odešle přiřazovací zprávu specifikující sadu uplinkových časových slotů (identifikovaných čísly TDMA rámce a indexy slotů), které může MS použít. MS pak musí sestavit své uplinkové přenosové bursty napříč těmito přidělenými, potenciálně nesousedícími sloty. Klíčové provozní pravidlo spočívá v tom, že MS nesmí vysílat v časovém slotu, který se v rámci nachází dříve než slot, který jí již byl přidělen pro monitorování downlinku kvůli možným řídicím zprávám, což zajišťuje, že transceiver má čas přepnout mezi režimem příjmu a vysílání.

Z architektonického hlediska se EDA týká koordinace mezi Base Station Subsystem ([BSS](/mobilnisite/slovnik/bss/)), konkrétně Base Transceiver Station ([BTS](/mobilnisite/slovnik/bts/)) a PCU, a MS. BTS je zodpovědná za fyzický přenos a příjem burstů v přidělených slotech, zatímco PCU zvládá logické přidělování zdrojů a plánování. Úlohou EDA je maximalizovat využití vzácných TDMA zdrojů tím, že umožňuje flexibilnější zabalení uživatelských dat, čímž se zvyšuje celková uplinková datová rychlost pro jednoho uživatele. Jde o klíčovou funkci pro zlepšení výkonu paketových dat ve vývoji GSM, která přímo přispívá k vyšší uživatelské propustnosti a lepší podpoře asymetrických datových aplikací, kde může být poptávka po uplinku značně proměnlivá.

## K čemu slouží

Extended Dynamic Allocation byl vytvořen, aby překonal omezení dřívějších, rigidnějších schémat přidělování zdrojů v GSM/[GPRS](/mobilnisite/slovnik/gprs/), jako jsou Fixed Allocation a Dynamic Allocation. Před zavedením EDA umožňovalo Dynamic Allocation více uživatelům sdílet uplinkové zdroje, ale s omezeními, která snižovala efektivitu a špičkové datové rychlosti. Hlavním problémem bylo neefektivní využití TDMA rámce, když MS měla nárazový uplinkový datový tok, ale dostupné sloty byly rozptýleny nesouvisle; starší schémata jejich použití nemusela povolit, což vedlo k plýtvání kapacitou a nižší propustnosti.

Zavedení EDA ve vydání 8 (Release 8) bylo motivováno rostoucí poptávkou po mobilních datových službách a potřebou vytěžit maximální výkon z existujícího GSM spektra a infrastruktury, zejména před rozsáhlým nasazením LTE. Řešilo konkrétní potřebu vyšších uplinkových rychlostí pro aplikace jako nahrávání fotografií, videokonference a reportování dat z zařízení v reálném čase. Tím, že síti umožnilo přidělit uživateli jakýkoli dostupný uplinkový časový slot (s ohledem na možnosti zařízení a časová omezení), EDA dramaticky zlepšilo zisk statistického multiplexování a spektrální účinnost.

Historicky bylo EDA součástí kontinuálního vývoje GERAN pro podporu Enhanced Data rates for GSM Evolution (EDGE) a dalších vylepšení. Vyřešilo kritický problém asymetrických datových potřeb tím, že poskytlo flexibilní nástroj pro řízení uplinkových zdrojů řízený poptávkou. To umožnilo operátorům nabízet vylepšené paketové datové služby bez nutnosti okamžité modernizace síťového hardwaru, čímž prodloužili komerční životnost a užitečnost svých investic do GSM. Představovalo významné vylepšení vrstvy řízení rádiových zdrojů, které lze realizovat softwarovou aktualizací, a optimalizovalo síť pro éru paketového přepojování.

## Klíčové vlastnosti

- Dynamické přiřazování nesousedících uplinkových TDMA časových slotů
- Signalizováno řídicími zprávami na Packet Associated Control Channel (PACCH)
- Zvyšuje propustnost a spektrální účinnost uplinkového paketového přenosu
- Podléhá časovým omezením transceiveru MS (žádný přenos dříve než v monitorovaném downlinkovém slotu)
- Zpětně kompatibilní s MS podporujícími tuto funkci
- Řízeno Packet Control Unit (PCU) v BSS

## Související pojmy

- [GERAN – GSM EDGE Radio Access Network](/mobilnisite/slovnik/geran/)
- [GPRS – CSI GPRS CAMEL Subscription Information](/mobilnisite/slovnik/gprs/)
- [EDGE – Enhanced Data rates for Global Evolution](/mobilnisite/slovnik/edge/)

## Definující specifikace

- **TR 45.912** (Rel-19) — GERAN Evolution Feasibility Study

---

📖 **Anglický originál a plná specifikace:** [EDA na 3GPP Explorer](https://3gpp-explorer.com/glossary/eda/)
