---
slug: "omr"
url: "/mobilnisite/slovnik/omr/"
type: "slovnik"
title: "OMR – Optimal Media Routeing"
date: 2025-01-01
abbr: "OMR"
fullName: "Optimal Media Routeing"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/omr/"
summary: "Optimal Media Routeing (OMR) je funkce 3GPP, která optimalizuje cestu mediálních proudů (hlas, video) v rámci IP Multimedia Subsystem (IMS) a dalších paketových sítí. Jejím cílem je vybrat nejefektivn"
---

OMR je funkce 3GPP, která optimalizuje cestu mediálního proudu v sítích IMS tak, aby byl vybrán nejefektivnější směrovací postup, což minimalizuje latenci a zlepšuje kvalitu hovoru pro služby jako VoLTE.

## Popis

Optimal Media Routeing (OMR) je síťový optimalizační mechanismus definovaný v několika specifikacích 3GPP (např. TS 23.894, TS 24.229), který určuje nejefektivnější cestu pro mediální provoz (např. RTP proudy pro hlas a video) v relaci založené na IP. Jeho hlavním cílem je zabránit zbytečnému průchodu provozu přes prvky core sítě, zejména přes mediální brány a session border controllery, tím, že umožní přímější mediální cestu mezi dvěma komunikujícími koncovými body, je-li to možné a povoleno dle politik. Toho se často dosahuje tzv. "local switching" nebo "direct media path".

Z architektonického hlediska se OMR účastní několik klíčových síťových funkcí v rámci IMS a paketového jádra. Hlavní rozhodovací bod typicky sídlí v Proxy-Call Session Control Function ([P-CSCF](/mobilnisite/slovnik/p-cscf/)) nebo v Service Centralization and Continuity Application Server (SCC [AS](/mobilnisite/slovnik/as/)), které analyzují signalizaci pro zřízení relace (SIP/SDP). Tyto funkce zkoumají parametry, jako jsou IP adresy a čísla portů nabízené koncovými body ve výměně SDP offer/answer. Na základě znalosti topologie sítě, operátorských politik a potenciálně vstupu z Policy and Charging Rules Function (PCRF) rozhodnou, zda je přímá mediální cesta optimální a povolená. Pokud ano, signalizační cesta může být upravena tak, aby koncovým bodům nařídila odesílat mediální pakety přímo na vzájemné IP adresy, čímž se obejdou mezilehlé uzly pro zpracování médií.

Jak to funguje, zahrnuje koordinovaný proces během zřizování relace. Když je zahájen hovor, volající UE odešle SIP INVITE s SDP nabídkou obsahující své mediální schopnosti a navrhovanou IP adresu/port pro příjem médií. Tato signalizace prochází IMS jádrem (P-CSCF, S-CSCF atd.). Funkce s podporou OMR tyto informace analyzuje. Po přijetí SDP odpovědi z ukončující strany porovná obě IP adresy. Pokud se zjistí, že jsou ve stejné nebo úzce propojené IP podsíti (např. v rámci stejné sítě operátora nebo obě za stejným [NAT](/mobilnisite/slovnik/nat/)), a politika to povoluje, síť se může rozhodnout povolit přímou mediální cestu. Síťové funkce pak mohou potenciálně upravit těla SDP ve signalizačních zprávách tak, aby odrážela optimální cestu, nebo jednoduše umožní koncovým bodům používat adresy, které si již vyměnily. Médium (RTP/RTCP) pak proudí přímo mezi UE, zatímco řídicí signalizace (SIP) nadále prochází IMS jádrem pro řízení relace a servisní logiku.

## K čemu slouží

OMR byl vyvinut k řešení významných neefektivit v raných nasazeních VoIP a IMS, kde mediální provoz často "trombonoval" přes centrální mediální brány nebo session border controllery, i když obě komunikující strany byly geograficky blízko nebo v rámci stejné sítě. Toto trombonování zvyšovalo latenci, chvění (jitter) a ztrátu paketů, což zhoršovalo uživatelský komfort služeb v reálném čase, jako jsou hlasové a videohovory. Také to spotřebovávalo zbytečnou šířku pásma na přenosových linkách a přidávalo zátěž drahým prostředkům pro zpracování médií, čímž se zvyšovaly jak kapitálové, tak provozní výdaje operátorů.

Motivace pro OMR vycházela z komerčního nasazení služeb jako Voice over LTE (VoLTE), kde je vysoká kvalita hlasu klíčovým požadavkem. Tradiční model ukotvování veškerého média v centrálním bodě (jako Media Gateway Control Function – [MGCF](/mobilnisite/slovnik/mgcf/) nebo Media Resource Function – [MRF](/mobilnisite/slovnik/mrf/)) byl pro mnoho scénářů hovoru neoptimální, zejména pro mobilní hovory v rámci stejné sítě. OMR to řeší tím, že umožňuje inteligenci ve vrstvě řízení relace analyzovat umístění koncových bodů a dynamicky vybírat mediální cestu, která minimalizuje počet skoků a využití síťových prostředků. To přímo zlepšuje dobu zřizování hovoru, snižuje celkovou latenci a zvyšuje kvalitu hlasu/videa. Také umožňuje operátorům škálovat své sítě efektivněji přesunutím mediálního provozu z core uzlů na distribuovanější IP přenosovou síť.

## Klíčové vlastnosti

- Dynamicky vybírá nejefektivnější mediální cestu na základě IP adres koncových bodů
- Umožňuje přímý přenos médií mezi koncovými body, je-li to možné (local switching)
- Snižuje latenci, chvění (jitter) a ztrátu paketů u médií pro služby v reálném čase
- Snižuje spotřebu šířky pásma a zatížení uzlů core sítě
- Funguje na základě operátorem definovaných politik a topologie sítě
- Integruje se s řízením IMS relací (P-CSCF, SCC AS) a řízením politik (PCRF)

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [P-CSCF – Proxy Call Session Control Function](/mobilnisite/slovnik/p-cscf/)

## Definující specifikace

- **TS 23.894** (Rel-10) — IMS Local Breakout & Optimal Media Routing Study
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 24.802** (Rel-12) — IMS II-NNI Traversal Scenario Determination Study
- **TS 29.079** (Rel-19) — Optimal Media Routeing (OMR) Procedures
- **TS 29.162** (Rel-19) — IMS-IP Network Interworking
- **TS 29.165** (Rel-19) — Inter-IMS Network to Network Interface (NNI)
- **TR 29.949** (Rel-19) — VoLTE IMS Roaming Architecture & Procedures
- **TS 32.240** (Rel-19) — Charging Management Architecture & Principles
- **TS 32.260** (Rel-19) — IMS Charging Management

---

📖 **Anglický originál a plná specifikace:** [OMR na 3GPP Explorer](https://3gpp-explorer.com/glossary/omr/)
