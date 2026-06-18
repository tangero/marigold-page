---
slug: "ipbcp"
url: "/mobilnisite/slovnik/ipbcp/"
type: "slovnik"
title: "IPBCP – IP Bearer Control Protocol"
date: 2025-01-01
abbr: "IPBCP"
fullName: "IP Bearer Control Protocol"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/ipbcp/"
summary: "Protokol používaný v rámci 3GPP IMS architektury pro vyjednávání a řízení charakteristik IP médiových přenosových kanálů (např. hlasových toků VoIP) mezi koncovými body nebo síťovými uzly. Umožňuje dy"
---

IPBCP je protokol používaný v rámci 3GPP IMS architektury pro vyjednávání a řízení charakteristik IP médiových přenosových kanálů (IP-based media bearers) mezi koncovými body za účelem umožnění dynamické rezervace zdrojů.

## Popis

IP Bearer Control Protocol (IPBCP) je protokol typu klient-server definovaný 3GPP pro řízení zdrojů IP přenosových kanálů, primárně v kontextu IP Multimedia Subsystem (IMS) a rozhraní mezi sítěmi. Funguje jako rozšiřující mechanismus v rámci modelu nabídky/odpovědi Session Description Protocol ([SDP](/mobilnisite/slovnik/sdp/)). V podstatě IPBCP umožňuje dvěma entitám účastnícím se relace (jako Media Gateway Control Function – [MGCF](/mobilnisite/slovnik/mgcf/) a Media Gateway – [MGW](/mobilnisite/slovnik/mgw/), nebo mezi MGCF navzájem) vyjednat a nastavit specifické parametry IP transportní vrstvy, která bude nést mediální tok (např. [RTP](/mobilnisite/slovnik/rtp/) toky pro hlas), nad rámec toho, co je možné se standardním SDP.

Architektonicky se IPBCP používá spolu s řídicími protokoly hovorů jako [SIP](/mobilnisite/slovnik/sip/) nebo BICC. Je přenášen jako atribut SDP v těle zpráv SIP (INVITE, 200 OK apod.) nebo v rámci BICC aplikačních transportních zpráv. Protokol definuje sadu zpráv a procedur pro zřízení, modifikaci a uvolnění přenosového kanálu. Klíčovou aplikací je kontext TrFO (Transcoder Free Operation) a [TFO](/mobilnisite/slovnik/tfo/) (Tandem Free Operation), kde pomáhá vyjednat použití specifických kodeků a vyhnout se zbytečnému překódování na síťové cestě. Může být také použit k vyjednání a řízení síťových zdrojů jako IP adresy, čísla portů, QoS označení, a dokonce ke spuštění zřízení vyhrazených přenosových kanálů v podřízených přístupových sítích (ačkoliv toto je často řízeno jinými mechanismy, jako je [PCC](/mobilnisite/slovnik/pcc/)).

Jak pracuje, následuje model žádost-odpověď vložený do SDP. Jedna entita (klient) zahrne IPBCP SDP atribut ve své SDP nabídce, navrhující určité charakteristiky přenosového kanálu. Vzdálená entita (server) zpracuje tuto žádost a zahrne odpovídající IPBCP atribut ve své SDP odpovědi, naznačující přijetí, odmítnutí nebo alternativní návrh. Toto vyjednávání může pokrývat aspekty jako model spojení (např. použití Media Gateway, nebo přímé spojení koncový bod–koncový bod), přidělení IP adres a portů a dohoda na jediném kodeku pro eliminaci překódování. Ve scénářích zahrnujících Media Gateways používá MGCF IPBCP k příkazu MGW, aby otevřel specifické porty a připravil se na příjem/přenos média s dohodnutými parametry, čímž odděluje signalizaci hovoru od přímého řízení médiové roviny.

## K čemu slouží

IPBCP byl vytvořen, aby řešil potřebu explicitní, dynamické kontroly nad médiovou rovinou přenosových kanálů v IP telekomunikacích, kterou samotné protokoly popisu relace dostatečně nepokrývaly. Standardní [SDP](/mobilnisite/slovnik/sdp/) dokázal popsat média formáty (kodeky), ale měl omezené možnosti v řízení, jak jsou nastaveny podkladové IP transportní zdroje pro toto médium, zvláště v síťově řízených scénářích zahrnujících média brány a rozhraní mezi operátory. Protokol řeší problém koordinovaného zřizování médiových přenosových kanálů mezi síťovými uzly, které jsou pod kontrolou různých funkčních entit (např. řízení hovoru v MGCF, zpracování média v MGW).

Jeho vývoj byl motivován snahou o efektivní zpracování média a optimální využití zdrojů. Například bez IPBCP by mohlo vyjednávání kodeku vést k suboptimální volbě vyžadující překódování na cestě, které by spotřebovávalo extra výpočetní výkon a potenciálně degradovalo kvalitu. IPBCP umožňuje explicitní dohodu na použití společného kodeku end-to-end (TrFO). Dále, v raném IMS a CS-IMS propojení poskytoval standardizovaný způsob, jakým MGCF instruuje MGW k alokaci konkrétních IP/port zdrojů, nahrazující proprietární řídicí protokoly dodavatelů. Toto zajišťovalo interoperabilitu mezi více dodavateli a umožňovalo inteligentnější uplatňování síťových médiových politik, což přispívá k celkové efektivitě sítě a kvalitě služeb.

## Klíčové vlastnosti

- Vyjednávání přenosových kanálů vložené do modelu SDP nabídky/odpovědi
- Podpora TrFO/TFO prostřednictvím explicitní dohody kodeků
- Řízení zdrojů média brány (IP, porty)
- Vyjednávání modelů spojení (přímé/nepřímé)
- Dynamické zřízení, modifikace a uvolnění přenosového kanálu
- Umožňuje síťově řízené přidělování médiových zdrojů

## Související pojmy

- [SDP – Service Discovery Protocol](/mobilnisite/slovnik/sdp/)
- [MGCF – Media Gateway Control Function](/mobilnisite/slovnik/mgcf/)

## Definující specifikace

- **TS 23.231** (Rel-19) — SIP-I based CS core network stage 2
- **TS 29.414** (Rel-19) — Nb Interface Bearer Transport & Control Protocols

---

📖 **Anglický originál a plná specifikace:** [IPBCP na 3GPP Explorer](https://3gpp-explorer.com/glossary/ipbcp/)
