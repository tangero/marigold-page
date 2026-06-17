---
slug: "hrp"
url: "/mobilnisite/slovnik/hrp/"
type: "slovnik"
title: "HRP – High Reliability Protocol"
date: 2025-01-01
abbr: "HRP"
fullName: "High Reliability Protocol"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/hrp/"
summary: "Transportní protokol navržený pro ultra-spolehlivou komunikaci s nízkou latencí (URLLC) v 5G sítích. Funguje nad IP vrstvou a poskytuje zvýšenou spolehlivost pomocí mechanismů, jako je duplikace paket"
---

HRP je transportní protokol pro 5G URLLC, který funguje nad vrstvou IP a poskytuje zvýšenou spolehlivost prostřednictvím duplikace paketů a korekce předem přenášených chyb (FEC) pro kritické průmyslové a vozidlové aplikace.

## Popis

Protokol vysoké spolehlivosti (High Reliability Protocol, HRP) je vylepšení protokolového zásobníku specifikované 3GPP, navržené k dosažení extrémních požadavků na spolehlivost (např. 99,9999 %) a nízkou latenci (např. 1 ms) služeb URLLC. Funguje jako mezivrstva (shim layer) mezi aplikací a standardními transportními vrstvami IP/UDP, přidávající spolehlivostní mechanismy, které jsou agresivnější a determinističtější než ty, které poskytuje TCP nebo konvenční protokoly založené na UDP. Architektonicky se entity HRP nacházejí v uživatelském zařízení (UE) a ve funkci uživatelské roviny ([UPF](/mobilnisite/slovnik/upf/)) nebo na vyhrazeném aplikačním serveru. Je navržen tak, aby pracoval v součinnosti s mechanismy 5G QoS a využíval toky QoS se zaručenou přenosovou rychlostí ([GBR](/mobilnisite/slovnik/gbr/)) a prioritním označením.

HRP funguje implementací souboru technik zvyšujících spolehlivost. Základním mechanismem je duplikace paketů, při které jsou identické datové pakety odesílány přes více nezávislých cest (např. různé PDU relace, různé rádiové nosiče nebo dokonce různé přístupové technologie jako 5G NR a LTE). Přijímající entita HRP provádí detekci duplicit a zahazuje redundantní kopie. HRP také využívá pokročilá schémata korekce předem přenášených chyb ([FEC](/mobilnisite/slovnik/fec/)), která přidávají redundantní paritní informace k datovým blokům, takže přijímač může rekonstruovat původní data i při ztrátě některých paketů, aniž by musel čekat na retransmise. Pro kontrolu latence používá HRP přísné časovače a může implementovat mechanismus selektivního opakování [ARQ](/mobilnisite/slovnik/arq/) s očekáváním velmi krátkého času odezvy, ale primárně spoléhá na FEC a duplikaci, aby se kdekoliv to bylo možné vyhnul latenci spojené s retransmisemi.

Protokol je definován jako konfigurovatelný na základě konkrétních cílů spolehlivosti a latence aplikace. Síťové funkce, jako je funkce správy relací ([SMF](/mobilnisite/slovnik/smf/)), mohou konfigurovat parametry HRP (např. faktor duplikace, schéma FEC) jako součást zřizování nebo modifikace PDU relace na základě přihlášeného profilu QoS. HRP také zahrnuje číslování sekvencí a časové značky pro řazení paketů a monitorování latence. Jeho fungování je podrobně popsáno ve specifikacích, jako je TS 23.725 pro architekturu, TS 26.260 pro doručování médií a TS 38.825 pro rádiové aspekty. Poskytnutím těchto funkcí na vyšší vrstvě přidává HRP záruku spolehlivosti end-to-end, která doplňuje spolehlivost poskytovanou na nižších vrstvách rozhraním 5G New Radio (NR) a protokoly RLC/[MAC](/mobilnisite/slovnik/mac/), čímž vytváří vícevrstvou obranu proti ztrátě paketů pro komunikace s vysokou mírou důležitosti.

## K čemu slouží

HRP byl vytvořen k vyplnění mezery mezi spolehlivostí poskytovanou tradičními internetovými protokoly (TCP/IP) a extrémními požadavky vznikajících vertikálních aplikací 5G, jako je automatizace továren, vzdálená chirurgie a koordinace autonomních vozidel. TCP se svou spolehlivostí založenou na retransmisích a řízením zahlcení zavádí nepředvídatelnou a často nadměrnou latenci, což jej činí nevhodným pro aplikace s latencí pod 10 ms. UDP nabízí nízkou latenci, ale žádnou spolehlivost. Zatímco rozhraní 5G NR a rámec QoS poskytují silné základy pro URLLC, ke ztrátě paketů může stále docházet v důsledku zahlcení v transportní síti (např. mezi [UPF](/mobilnisite/slovnik/upf/) a aplikačním serverem) nebo vzácných, ale katastrofických selhání rádiového spojení.

Motivace pro HRP vychází z potřeby end-to-end řešení na transportní vrstvě, které bezproblémově funguje v 5G sítích včetně segmentů jádra a transportu. Předchozí průmyslová řešení často používala proprietární protokoly vrstvy 2 nebo rigidní kabelové sítě (např. PROFINET, EtherCAT). HRP poskytuje standardizovaný protokol založený na IP, který může využít flexibilitu a škálovatelnost 5G při splnění tvrdých časových omezení reálného času. Řeší problém dosažení spolehlivosti 'šesti devítek' přes bezdrátové spoje a potenciálně ztrátové IP sítě tím, že proaktivně odesílá redundantní informace (pomocí duplikace a [FEC](/mobilnisite/slovnik/fec/)) namísto reaktivního přeposílání ztracených dat. Tento posun paradigmatu od reaktivního k proaktivnímu zotavení po chybě je klíčový k současnému dosažení vysoké spolehlivosti i ultra-nízké latence, což umožňuje bezdrátovou náhradu kritických kabelových spojení v průmyslovém a vozidlovém prostředí.

## Klíčové vlastnosti

- Duplikace paketů přes více nezávislých přenosových cest
- Pokročilá korekce předem přenášených chyb (FEC) pro obnovu ze ztráty bez retransmise
- Konfigurovatelné profily spolehlivosti a latence sladěné s toky 5G QoS
- End-to-end provoz mezi UE a aplikačním serverem/UPF
- Číslování sekvencí a detekce duplicit pro integritu dat
- Těsná integrace se správou 5G PDU relací a QoS pro rezervaci prostředků

## Definující specifikace

- **TS 23.725** (Rel-16) — Study on URLLC Architecture Enhancements
- **TS 26.260** (Rel-19) — Immersive Audio Objective Test Methods
- **TR 38.825** (Rel-16) — Study on NR Industrial IoT

---

📖 **Anglický originál a plná specifikace:** [HRP na 3GPP Explorer](https://3gpp-explorer.com/glossary/hrp/)
