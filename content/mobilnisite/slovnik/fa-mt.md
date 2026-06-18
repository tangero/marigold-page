---
slug: "fa-mt"
url: "/mobilnisite/slovnik/fa-mt/"
type: "slovnik"
title: "FA/MT – Fax Adaptor / Mobile Terminal"
date: 2025-01-01
abbr: "FA/MT"
fullName: "Fax Adaptor / Mobile Terminal"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/fa-mt/"
summary: "FA/MT je funkce Faxového adaptéru umístěná v mobilním terminálu (např. v ručním přístroji nebo datové kartě). Spolupracuje se síťovou jednotkou FA/IWF na odesílání a přijímání faxů přes paketová datov"
---

FA/MT je funkce Faxového adaptéru (Fax Adaptor) v rámci mobilního terminálu, která přizpůsobuje faxová data pro rozhraní terminálu za účelem odesílání a přijímání faxů přes paketová datová připojení 3GPP ve spolupráci se síťovou jednotkou FA/IWF.

## Popis

Faxový adaptér na straně mobilního terminálu ([FA](/mobilnisite/slovnik/fa/)/[MT](/mobilnisite/slovnik/mt/)) je funkční komponenta na straně klienta, která umožňuje zařízení v mobilní síti 3GPP účastnit se relací faxu skupiny 3 přes paketově orientované síťové připojení. Je protějškem síťové jednotky [FA/IWF](/mobilnisite/slovnik/fa-iwf/) (Fax Adaptor at the Interworking Function). FA/MT je implementován v softwaru a/nebo hardwaru uživatelského zařízení (UE), například v chytrém telefonu s faxovým softwarem, v dedikovaném faxovém modemu nebo v datové kartě v notebooku.

Z architektonického hlediska se FA/MT nachází nad paketovým datovým protokolovým zásobníkem zařízení (např. [PPP](/mobilnisite/slovnik/ppp/) nad datovým přenosem 3GPP) a komunikuje s uživatelskou faxovou aplikací nebo ovladačem virtuálního faxového modemu. Když uživatel zahájí operaci odesílání faxu, aplikace vygeneruje standardní signály faxového modemu. FA/MT tyto signály zachytí, digitalizuje a zabalí faxová obrazová data a řídicí signály podle protokolu pro přenos faxu T.38 nebo podobného schématu. Tyto IP pakety pak přenáší přes zřízený kontext paketového datového protokolu ([PDP](/mobilnisite/slovnik/pdp/)) k síťové jednotce FA/[IWF](/mobilnisite/slovnik/iwf/). Pro příchozí faxové zprávy je proces opačný: FA/MT přijímá pakety T.38 od FA/IWF, rekonstruuje signály faxového modemu a předává je faxové aplikaci, jako by přicházely z přímého analogového připojení.

Klíčem k jeho činnosti je řízení faxové relace v reálném čase přes potenciálně nestabilní IP připojení. FA/MT zahrnuje vyrovnávací paměť pro potlačení kolísání zpoždění (jitter buffer) a implementuje techniky spoofingu, aby přesvědčil místní faxovou aplikaci, že má stabilní okruhové připojení s nízkou latencí. Zpracovává procedury protokolu T.38, včetně režimu opravy chyb ([ECM](/mobilnisite/slovnik/ecm/)), pokud je podporován, a komunikuje s telefonní vrstvou zařízení pro řízení hovoru (zahájení datového hovoru pro fax). Jeho úlohou je poskytovat kompletní emulaci faxového modemu lokálně, skrýt před uživatelským faxovým softwarem složitost paketové sítě a propojení, a tím umožnit bezproblémovou funkci mobilního faxu bez nutnosti tradičního okruhově přepínaného hlasového hovoru.

## K čemu slouží

[FA](/mobilnisite/slovnik/fa/)/MT byl vyvinut proto, aby umožnil mobilnímu uživatelskému zařízení fungovat jako faxový terminál v prostředí paketově orientované sítě. Před jeho standardizací vyžadovalo odeslání faxu z mobilního zařízení okruhově přepínaný datový hovor (CSD), který blokoval hlasový kanál a nabízel nízké přenosové rychlosti (např. 9,6 kbps). To bylo neefektivní a často vyžadovalo specifickou hardwarovou podporu. FA/MT, zavedený spolu s FA/IWF, tento problém vyřešil využitím vysokorychlostních paketových datových připojení (GPRS, EDGE, UMTS) pro přenos faxů.

Vznik byl motivován potřebou, aby mobilní datové služby plně nahradily starší okruhově přepínané služby, včetně faxu, který zůstával důležitý pro obchodní dokumenty, právní smlouvy a zdravotnictví. Řešil omezení spočívající v nutnosti mít v terminálu dedikovaný modem podporující CSD a špatný uživatelský zážitek z pomalých přenosových rychlostí faxu.

Implementací logiky faxového adaptéru v terminálu umožnil flexibilnější a softwarově aktualizovatelná faxová řešení. Uživatelé mohli potenciálně používat jediné mobilní zařízení pro hlas, internet a fax přes sdílené paketové datové předplatné. FA/MT a FA/IWF společně usnadnily migraci faxu z okruhově přepínané telefonní služby na aplikaci běžící přes mobilní širokopásmový přístup, což odpovídalo trendu průmyslu směrem k plně IP sítím.

## Klíčové vlastnosti

- Funkce faxového adaptéru na straně klienta zabudovaná v uživatelském zařízení (UE)
- Komunikuje s faxovou aplikací terminálu nebo ovladačem virtuálního modemového COM portu
- Zabaluje a rozbaluje faxová data pomocí protokolu T.38 pro přenos přes IP
- Implementuje spoofing a správu kolísání zpoždění (jitter) pro emulaci stabilního okruhového připojení
- Spolupracuje se síťovou jednotkou FA/IWF k dokončení faxové relace
- Umožňuje odesílání/přijímání faxů využitím datového přenosu zařízení (např. PDP kontextu)

## Související pojmy

- [FA/IWF – Fax Adaptor / Interworking Function](/mobilnisite/slovnik/fa-iwf/)

## Definující specifikace

- **TS 23.045** (Rel-4) — GSM Group 3 Facsimile Service Procedures
- **TS 43.045** (Rel-19) — Group 3 Fax Service in A/Gb Mode PLMN

---

📖 **Anglický originál a plná specifikace:** [FA/MT na 3GPP Explorer](https://3gpp-explorer.com/glossary/fa-mt/)
