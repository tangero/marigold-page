---
slug: "chp"
url: "/mobilnisite/slovnik/chp/"
type: "slovnik"
title: "CHP – Constrained High Profile"
date: 2025-01-01
abbr: "CHP"
fullName: "Constrained High Profile"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/chp/"
summary: "Profil audio kodeku 3GPP navržený pro přenos vysoce kvalitní řeči v prostředích s omezenou šířkou pásma. Optimalizuje efektivitu přenosové rychlosti při zachování vynikající kvality hlasu, což je zvlá"
---

CHP je profil audio kodeku 3GPP pro vysoce kvalitní řeč v prostředích s omezenou šířkou pásma, který optimalizuje efektivitu přenosové rychlosti pro robustní hlasové služby v mobilních sítích.

## Popis

Profil Constrained High Profile (CHP) je standardizovaný profil audio kodeku v rámci specifikací 3GPP, konkrétně navržený jako součást rodin kodeků Adaptive Multi-Rate Wideband ([AMR-WB](/mobilnisite/slovnik/amr-wb/)) a později Enhanced Voice Services ([EVS](/mobilnisite/slovnik/evs/)). Funguje jako specifický provozní režim nebo konfigurace těchto kodeků a definuje sadu omezení kódovacích parametrů pro dosažení optimálního výkonu za specifických síťových a koncových omezení. Profil stanovuje pravidla pro alokaci přenosové rychlosti, algoritmickou složitost a mechanismy odolnosti proti chybám, které jsou přizpůsobeny scénářům, kde jsou omezené výpočetní zdroje nebo šířka pásma, ale vysoká percepční kvalita zvuku zůstává prioritou.

Z architektonického hlediska CHP funguje tak, že ukládá selektivní omezení na plné možnosti nadřazeného kodeku (např. AMR-WB nebo EVS). Tato omezení typicky zahrnují fixaci nebo vymezení určitých parametrů kodéru a dekodéru, jako jsou povolené přenosové rychlosti, složitost určitých algoritmických modulů (jako je redukce šumu nebo rozšíření šířky pásma) a zpracování vymazaných rámců. Například v rámci kodeku EVS může CHP omezit provoz na konkrétní podmnožinu dostupných přenosových rychlostí (např. režimy 13,2 kbps a 24,4 kbps) a vyžadovat použití robustnější, ale méně složité strategie maskování chyb. Tím je zajištěn předvídatelný výkon a interoperabilita mezi zařízeními, která podporu CHP deklarují.

Klíčové součásti specifikace CHP zahrnují definovanou sadu přenosových rychlostí, povinné a volitelné nástroje kodeku, formát paketizace (často sladěný s formátem RTP payload specifikovaným v 3GPP TS 26.445 pro EVS) a požadované chování dekodéru při ztracených nebo poškozených rámcích. Profil je těsně integrován s rámcem přenosu a QoS 3GPP, což umožňuje síti signalizovat použití CHP během procedur sestavování hovoru nebo vyjednávání kodeku, například při výměnách SIP/SDP pro služby VoLTE nebo VoNR založené na IMS. Jeho úlohou je zaručit konzistentní, vysokokvalitní hlasový zážitek i na zařízeních nižší třídy nebo v síťových buňkách s vysokou vytížeností, čímž slouží jako kvalitativní minimum pro prémiové hlasové služby.

Při provozu, když je relace sestavena s CHP, se jak koncové body, tak síťové prvky (např. mediální brány, aplikační servery IMS) řídí omezenou sadou parametrů. Kodér používá pouze povolené režimy, což snižuje výpočetní zátěž a spotřebu energie na zařízení. Transportní vrstva zabalí zakódované rámce podle pravidel profilu a dekodér, který zná používaný profil, aplikuje odpovídající omezené algoritmy pro syntézu a maskování chyb. Tato konzistence od konce ke konci je zásadní pro udržení cílové kvality uživatelského zážitku (QoE) a pro síťové plánování, protože operátoři mohou přesně modelovat kapacitu a výkon při nasazení CHP.

## K čemu slouží

Profil Constrained High Profile byl vytvořen, aby řešil výzvu poskytování vysokokvalitních, širokopásmových (nebo super-širokopásmových) hlasových služeb napříč velmi heterogenním ekosystémem mobilních zařízení a síťových podmínek. Rané širokopásmové kodeky jako [AMR-WB](/mobilnisite/slovnik/amr-wb/) nabízely výrazné zlepšení kvality oproti úzkopásmové řeči, ale jejich plná flexibilita v přenosových rychlostech a režimech mohla vést k nekonzistentní kvalitě, vyššímu odběru baterie u nízkorozpočtových zařízení a nepředvídatelnému síťovému zatížení. CHP poskytuje standardizovanou, optimalizovanou podmnožinu provozu kodeku, která zajišťuje garantovanou minimální úroveň kvality pro služby uváděné jako '[HD](/mobilnisite/slovnik/hd/) Voice' nebo 'Enhanced Voice', bez ohledu na konkrétní telefon nebo momentální rádiové podmínky.

Historicky, jak 3GPP vyvíjelo hlasové služby od okruhově přepínaného [AMR](/mobilnisite/slovnik/amr/) k paketově přepínanému VoLTE s AMR-WB a později k [EVS](/mobilnisite/slovnik/evs/) pro VoLTE a VoNR, vznikla potřeba udržet kvalitu služby a zároveň vyhovět obrovskému rozsahu možností zařízení – od vlajkových smartphonů po nízkonákladová IoT zařízení nebo starší telefony s omezeným výpočetním výkonem. Bez omezeného profilu čelili síťoví operátoři dilematu: buď vyžadovat podporu plného, komplexního kodeku (čímž by vyloučili nízkorozpočtová zařízení), nebo povolit přepínání na méně kvalitní kodeky, což by fragmentovalo uživatelský zážitek. CHP to řeší definováním 'vysokokvalitního, ale zvládnutelného' provozního bodu, který může být univerzálně vyžadován pro danou úroveň služeb.

CHP navíc pomáhá při optimalizaci a plánování sítě. Omezením rozsahu proměnlivé přenosové rychlosti a algoritmické složitosti snižuje poměr špičkové a průměrné přenosové rychlosti hlasového provozu, čímž činí provoz předvídatelnějším pro plánování paketů a správu rádiových zdrojů. Také zjednodušuje testování a certifikaci, protože zařízení a síťové prvky mohou být ověřovány vůči konkrétnímu, dobře definovanému profilu namísto celého prostoru kodeků. Tím se řeší omezení předchozích přístupů, kdy byla kvalita buď negarantovaná (plně adaptivní kodeky), nebo nedostatečná (pevné, starší kodeky), což umožňuje škálovatelné nasazení prémiových hlasových služeb.

## Klíčové vlastnosti

- Definovaná podmnožina přenosových rychlostí nadřazeného kodeku (např. specifické režimy AMR-WB nebo EVS) pro předvídatelné využití šířky pásma
- Omezená algoritmická složitost pro umožnění podpory na zařízeních s omezenými výpočetními možnostmi
- Standardizované postupy odolnosti proti chybám a maskování ztráty rámců pro robustní výkon v nepříznivých rádiových podmínkách
- Požadavky na povinnou podporu pro interoperabilitu v certifikovaných službách HD Voice nebo Enhanced Voice Services
- Integrace s procedurami vyjednávání kodeku a sestavování relace 3GPP (např. prostřednictvím SDP)
- Poskytuje konzistentní kvalitativní minimum pro prémiové hlasové služby napříč různými typy zařízení a sítí

## Související pojmy

- [AMR-WB – Adaptive Multi-Rate Wideband Speech Codec](/mobilnisite/slovnik/amr-wb/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 26.223** (Rel-19) — IMS Telepresence Client Specification
- **TS 26.281** (Rel-19) — MCVideo Codecs and Media Handling
- **TS 26.880** (Rel-14) — MBMS Enhancements for Mission Critical Video
- **TR 26.923** (Rel-19) — Study on IMS-based Telepresence Media Handling
- **TR 26.955** (Rel-19) — Video Codec Analysis for 5G Services

---

📖 **Anglický originál a plná specifikace:** [CHP na 3GPP Explorer](https://3gpp-explorer.com/glossary/chp/)
