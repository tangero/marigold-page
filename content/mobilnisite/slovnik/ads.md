---
slug: "ads"
url: "/mobilnisite/slovnik/ads/"
type: "slovnik"
title: "ADS – Access Domain Selection"
date: 2025-01-01
abbr: "ADS"
fullName: "Access Domain Selection"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ads/"
summary: "Access Domain Selection (ADS) je mechanismus 3GPP, který umožňuje síti vybrat nejvhodnější přístupovou doménu (přepojovanou okruhy nebo přepojovanou pakety) pro hlasové a zprávové služby. Zajišťuje op"
---

ADS je mechanismus 3GPP, při kterém síť vybere nejvhodnější přístupovou doménu, přepojovanou okruhy nebo přepojovanou pakety, pro doručování hlasových a zprávových služeb na základě schopností zařízení a stavu sítě.

## Popis

Access Domain Selection (ADS) je síťová rozhodovací funkce definovaná v architektuře IP Multimedia Subsystem (IMS). Funguje na rozhraní Evolved Packet Core (EPC) a jádra IMS, konkrétně zahrnuje Proxy-Call Session Control Function ([P-CSCF](/mobilnisite/slovnik/p-cscf/)) a Serving-Call Session Control Function ([S-CSCF](/mobilnisite/slovnik/s-cscf/)). Když User Equipment (UE) zahájí relaci (např. hlasové volání nebo zprávovou službu), jádro IMS obdrží požadavek na relaci a musí rozhodnout, zda směrovat relaci přes doménu přepojovanou pakety ([PS](/mobilnisite/slovnik/ps/)) (jako LTE/5G NR) nebo přes doménu přepojovanou okruhy ([CS](/mobilnisite/slovnik/cs/)) (jako 2G/3G). Toto rozhodnutí nečiní UE, ale síť na základě politik a podmínek v reálném čase.

Funkce ADS primárně spoléhá na informace poskytnuté během procesu registrace IMS a následného zahájení relace. Klíčové vstupy zahrnují registrační stav UE v obou doménách CS i PS, její podporované schopnosti (indikované pomocí IMS Communication Service Identifier, [ICSI](/mobilnisite/slovnik/icsi/)), politiky operátora sítě a aktuální typ přístupové sítě. Například, pokud je UE registrována v IMS přes LTE (což indikuje schopnost VoLTE) a síť podporuje hlas přes IMS, ADS typicky vybere PS doménu. Pokud UE není v IMS registrována nebo se nachází v oblasti bez podpory hlasu přes PS, ADS může přepnout zpět na CS doménu, aby zajistila kontinuitu služby. Logika rozhodování je implementována v S-CSCF, která konzultuje data o předplatném a operátorem nakonfigurované Service Point Triggers ([SPT](/mobilnisite/slovnik/spt/)).

Architektonicky je ADS úzce spojena s konceptem Single Radio Voice Call Continuity ([SRVCC](/mobilnisite/slovnik/srvcc/)) a enhanced SRVCC (eSRVCC). Zatímco SRVCC řeší předání hlasového hovoru z PS do CS domény během mobility, ADS řeší počáteční výběr domény před zřízením hovoru. P-CSCF hraje roli tím, že přeposílá počáteční [SIP](/mobilnisite/slovnik/sip/) požadavek (jako INVITE) do S-CSCF, která poté provede logiku ADS. S-CSCF může pro složitější servisní logiku vyvolat Application Server (AS). Výstup ADS určuje směrování SIP signalizace a následné mediální cesty – buď zůstane v jádru IMS/PS, nebo je ukotvena k CS síti přes Media Gateway Control Function (MGCF).

ADS je klíčová pro fázované nasazení VoLTE a případné vyřazení starších CS sítí. Umožňuje operátorům zachovat konzistentní uživatelský zážitek při migraci služeb na plně IP sítě. Mechanismus zajišťuje, že služby jako nouzová volání jsou vždy dostupné na nejspolehlivějším přístupu, v souladu s regulatorními požadavky. Centralizací výběru domény v síti poskytuje ADS operátorům kontrolu nad využitím zdrojů, kvalitou služeb a interoperabilitou mezi různými generacemi síťové technologie.

## K čemu slouží

Access Domain Selection byl vytvořen k řešení zásadní výzvy zavádění hlasových služeb založených na IP (VoLTE) v sítích LTE při zachování bezproblémové interoperability se stávajícími hlasovými sítěmi přepojovanými okruhy. Před LTE byly hlasové služby poskytovány výhradně přes CS doménu v sítích 2G a 3G. LTE bylo navrženo jako čistě paketová síť bez nativní CS funkčnosti, což vytvořilo 'hlasovou mezeru'. Počáteční řešení, Circuit Switched Fallback (CSFB), vyžadovalo, aby UE dočasně přepadla do sítě 2G/3G pro všechny hlasové hovory, což bylo neefektivní a prodlužovalo dobu zřizování hovoru. ADS, jako součást řešení VoLTE založeného na IMS, byl vyvinut tak, aby síti umožnil inteligentně zvolit nejlepší doménu pro poskytování hlasové služby od samého počátku, což umožňuje skutečný hlas přes IP, když je dostupný, a přepádá pouze v případě nutnosti.

Primární problém, který ADS řeší, je kontinuita služeb a optimální využití zdrojů během přechodného období, kdy koexistují domény CS i PS. Bez ADS by UE mohla činit neoptimální volby nebo by služby mohly v okrajových oblastech pokrytí zcela selhat. ADS dává síťovým operátorům centralizovanou kontrolu politik nad výběrem domény na základě faktorů, jako je profil účastníka, zatížení sítě, typ služby (např. nouzové volání vs. běžný hovor) a schopnosti UE. Tato kontrola je zásadní pro správu kvality uživatelského zážitku, zajištění spolehlivých nouzových služeb a efektivní směrování provozu k cílové plně IP síti.

Historicky motivace pro ADS vycházela z vize 3GPP pro IMS jako jedinou platformu pro řízení služeb pro všechny multimediální služby ve verzi Release 8 a novějších. ADS je klíčovým enablerem této vize pro hlas, umožňující IMS stát se sjednocující vrstvou, která abstrahuje podkladovou přístupovou technologii. Vyřešila omezení dřívějších přístupů s duálním rádiem a CSFB tím, že poskytla hladší, síťově řízenou migrační cestu. ADS také položila základy pro pokročilejší funkce mobility, jako je SRVCC, které řeší přenos domény během hovoru, zatímco ADS řeší počáteční výběr.

## Klíčové vlastnosti

- Síťově řízený výběr mezi přístupovými doménami přepojovanými okruhy (CS) a přepojovanými pakety (PS) pro hlasové a zprávové služby
- Rozhodování založené na stavu registrace UE v IMS, schopnostech sítě, politikách operátora a typu služby
- Těsná integrace s prvky jádra IMS (P-CSCF, S-CSCF) a daty o předplatném
- Umožňuje Voice over LTE (VoLTE) výběrem PS domény, když je podporována
- Poskytuje přepádání na CS doménu pro zajištění dostupnosti služby a zpětné kompatibility
- Podporuje regulatorní požadavky na nouzová volání zajištěním spolehlivého výběru domény

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [SRVCC – Single Radio Voice Call Continuity](/mobilnisite/slovnik/srvcc/)
- [P-CSCF – Proxy Call Session Control Function](/mobilnisite/slovnik/p-cscf/)
- [S-CSCF – Serving Call Session Control Function](/mobilnisite/slovnik/s-cscf/)

## Definující specifikace

- **TS 23.292** (Rel-19) — IMS Centralized Services (ICS) Architecture
- **TS 24.292** (Rel-19) — IMS Centralized Services (ICS) Protocol

---

📖 **Anglický originál a plná specifikace:** [ADS na 3GPP Explorer](https://3gpp-explorer.com/glossary/ads/)
