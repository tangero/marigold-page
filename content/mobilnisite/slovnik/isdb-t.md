---
slug: "isdb-t"
url: "/mobilnisite/slovnik/isdb-t/"
type: "slovnik"
title: "ISDB-T – Integrated Services Digital Broadcasting – Terrestrial"
date: 2025-01-01
abbr: "ISDB-T"
fullName: "Integrated Services Digital Broadcasting – Terrestrial"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/isdb-t/"
summary: "Standard pro digitální terestriální televizní vysílání, používaný primárně v Japonsku a některých dalších zemích. Specifikace 3GPP se na něj odkazují v souvislosti se studiemi koexistence a potenciáln"
---

ISDB-T je standard pro digitální terestriální televizní vysílání používaný v Japonsku a dalších zemích, na který se 3GPP odkazuje ve studiích koexistence a integrace s mobilními vysílacími službami, jako je eMBMS.

## Popis

Integrated Services Digital Broadcasting – Terrestrial (ISDB-T) je standard pro digitální televizní vysílání vyvinutý v Japonsku a přijatý v několika zemích Jižní Ameriky a Asie. V kontextu specifikací 3GPP nejde o technologii definovanou 3GPP, ale je na ni odkazováno v technických zprávách a specifikacích, zejména těch souvisejících se studiemi koexistence, sdílením spektra a vylepšeními vysílacích služeb. Dokumenty 3GPP, jako jsou TR 36.792 a TS 36.104, zkoumají ISDB-T ve scénářích, kdy mobilní sítě (jako LTE nebo 5G NR) fungují na sousedních nebo stejných kmitočtových kanálech jako služby ISDB-T vysílání. Tyto studie jsou klíčové pro zajištění, že mobilní služby nezpůsobují škodlivé rušení stávajícím vysílacím službám a naopak.

Z architektonického hlediska ISDB-T používá přenosové schéma založené na ortogonálním frekvenčním multiplexu s dělením pásma (Band Segmented Transmission – BST [OFDM](/mobilnisite/slovnik/ofdm/)). Vysílací kanál dělí na 13 segmentů (nebo 12 segmentů plus jeden částečný segment pro mobilní příjem ve variantě ISDB-Tmm). Tato segmentace umožňuje flexibilní konfiguraci služeb: například některé segmenty lze použít pro televizi s vysokým rozlišením ([HDTV](/mobilnisite/slovnik/hdtv/)), jiné pro televizi se standardním rozlišením (SDTV) a jeden segment (obvykle středový) může být vyhrazen pro služby mobilní televize (známé jako 1seg). Každý segment se skládá ze sady OFDM subnosných a systém podporuje více modulačních schémat ([QPSK](/mobilnisite/slovnik/qpsk/), [16QAM](/mobilnisite/slovnik/16qam/), [64QAM](/mobilnisite/slovnik/64qam/)) a kódovacích poměrů pro přizpůsobení různým podmínkám příjmu. Vysílání probíhá v pásmu [UHF](/mobilnisite/slovnik/uhf/) (např. 470-710 MHz), které je také zajímavé pro služby mobilního širokopásmového přístupu díky svým dobrým šířicím vlastnostem.

Co se týče provozu, vysílač ISDB-T multiplexuje audio, video a datové toky do transportních proudů, které jsou následně kanálově kódovány, modulovány pomocí OFDM a vysílány vzduchem. Příjemci, jako jsou televizory nebo mobilní zařízení s tunery ISDB-T, signál dekódují. Služba 1seg je speciálně navržena pro mobilní příjem, využívá robustní modulaci (QPSK) a kódování pro zvládání výzev mobilního prostředí, jako je útlum a Dopplerův jev. Když 3GPP zvažuje ISDB-T, zaměřuje se na to, jak by základnové stanice LTE nebo 5G NR a uživatelská zařízení mohla interagovat s těmito vysílacími signály. To zahrnuje analýzu nežádoucích emisí mimo pásmo, poměru úniku do sousedního kanálu ([ACLR](/mobilnisite/slovnik/aclr/)) a blokovacích charakteristik za účelem definice potřebných ochranných pásem nebo požadavků na filtry.

Klíčovými komponentami v analýze koexistence jsou výkonová spektrální hustota vysílače ISDB-T, jeho obsazená šířka pásma (typicky 6 MHz na kanál, segmentovaná) a citlivost jeho přijímače. Specifikace 3GPP definují limity nežádoucích emisí pro mobilní stanice a základnové stanice za účelem ochrany přijímačů ISDB-T. Dále studie mohou zkoumat potenciál konvergence, kde by vysílací obsah dodávaný přes ISDB-T mohl být doplněn nebo integrován s mobilními unikastními službami, ačkoli to je spíše konceptuální. Odkazy ve specifikacích 3GPP zajišťují, že nasazení sítí, zejména v regionech používajících ISDB-T, splňují regulatorní požadavky a udržují kvalitu služeb jak pro vysílací, tak pro mobilní uživatele.

## K čemu slouží

Samotný ISDB-T byl vytvořen za účelem modernizace terestriálního televizního vysílání, přechodu z analogového na digitální, aby poskytoval vyšší kvalitu videa, více kanálů a další datové služby. Jeho účel v dokumentaci 3GPP je však odlišný. 3GPP odkazuje na ISDB-T primárně pro studie koexistence a kompatibility. Jak se mobilní sítě rozšiřují do nových kmitočtových pásem, včetně těch tradičně používaných pro vysílací [TV](/mobilnisite/slovnik/tv/) (např. pásmo 600 MHz po digitální dividendě), je nezbytné zajistit, aby nové mobilní přenosy nerušily stávající služby, jako je ISDB-T. Jedná se o regulatorní a technickou nutnost, aby nedošlo ke zhoršení služeb pro diváky vysílání.

Motivace pro zahrnutí ISDB-T do specifikací 3GPP vychází z globální povahy telekomunikací. Různé regiony přijímají různé vysílací standardy (např. DVB-T v Evropě, ATSC v Severní Americe, ISDB-T v Japonsku/Brazílii). Aby bylo zajištěno, že mobilní zařízení 3GPP může být nasazeno po celém světě, musí 3GPP zvažovat všechny hlavní stávající systémy. Release 18, kde se ISDB-T v 3GPP objevuje, odráží pokračující snahy studovat a definovat požadavky pro provoz 5G NR ve sdíleném a sousedním spektru. Omezeními, která jsou řešena, je potenciál škodlivého rušení, které by mohlo narušit jak vysílací služby (způsobit ztrátu obrazu televizním divákům), tak služby mobilní (pokud by vysílače vysílání přetížily mobilní přijímače).

Historicky se dřívější releasy 3GPP zaměřovaly na koexistenci s jinými mobilními systémy nebo specifickými vysílacími standardy, jako je DVB-H. Zahrnutí ISDB-T v Release 18 naznačuje rozšíření záběru na pokrytí více regionálních standardů, protože 5G usiluje o využití nižších kmitočtových pásem pro pokrytí širokých oblastí. Tyto studie pomáhají definovat technické parametry, jako je maximální povolená výkonová spektrální hustota pro základnové stanice NR v blízkosti přijímačů ISDB-T, potřebná ochranná pásma a požadavky na blokování přijímače. To zajišťuje, že nasazení 5G může plynule pokračovat v regionech s ISDB-T bez nákladných problémů s rušením, což usnadňuje globální harmonizaci využití spektra a chrání stávající investice do vysílací infrastruktury.

## Klíčové vlastnosti

- Využívá ortogonálního frekvenčního multiplexu s dělením pásma (BST OFDM), který rozděluje kanál na 13 segmentů pro flexibilitu služeb
- Podporuje vyhrazenou službu 1seg pro mobilní příjem využívající robustní modulaci QPSK
- Funguje v pásmech UHF (např. 470-710 MHz), která jsou také cílena pro mobilní širokopásmový přístup
- Umožňuje simultánní přenos služeb HDTV, SDTV a datových služeb v rámci jednoho RF kanálu
- Je odkazován v 3GPP v souvislosti se studiemi koexistence za účelem prevence rušení provozu LTE/5G NR
- Zahrnuje možnosti hierarchické modulace pro uspokojení podmínek příjmu jak pevného, tak mobilního

## Související pojmy

- [DVB-T – Digital Video Broadcasting - Terrestrial](/mobilnisite/slovnik/dvb-t/)
- [ATSC – Advanced Television Systems Committee](/mobilnisite/slovnik/atsc/)

## Definující specifikace

- **TS 36.104** (Rel-19) — Base Station (BS) radio transmission and reception
- **TR 36.792** (Rel-18) — Technical Report

---

📖 **Anglický originál a plná specifikace:** [ISDB-T na 3GPP Explorer](https://3gpp-explorer.com/glossary/isdb-t/)
