---
slug: "evs-cmr"
url: "/mobilnisite/slovnik/evs-cmr/"
type: "slovnik"
title: "EVS-CMR – EVS Codec Mode Request"
date: 2025-01-01
abbr: "EVS-CMR"
fullName: "EVS Codec Mode Request"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/evs-cmr/"
summary: "Řídicí mechanismus používaný během hovoru kódovaného kodekem EVS k dynamickému vyžádání změny konfigurace kodeku vysílajícího koncového bodu (např. přenosová rychlost, šířka pásma, režim). To umožňuje"
---

EVS-CMR je řídicí mechanismus používaný během hovoru kódovaného kodekem EVS k dynamickému vyžádání změny konfigurace kodeku vysílajícího koncového bodu, což umožňuje adaptaci na síťové podmínky nebo optimalizaci výkonu v reálném čase.

## Popis

[EVS](/mobilnisite/slovnik/evs/) Codec Mode Request (EVS-CMR) je signalizační funkce definovaná v rámci specifikace kodeku Enhanced Voice Services (EVS) od 3GPP. Jedná se o řídicí protokol fungující v pásmu (in-band) v rámci datového proudu protokolu Real-time Transport Protocol ([RTP](/mobilnisite/slovnik/rtp/)) během aktivního hovoru. Jeho primární funkcí je umožnit jednomu koncovému bodu (příjemci) vyžádat si od druhého koncového bodu (vysílatele) přepnutí na jiný režim nebo konfiguraci kodeku EVS v reálném čase, aniž by bylo nutné provést úplnou novou [SIP](/mobilnisite/slovnik/sip/) dohodu o relaci.

Z architektonického hlediska je EVS-CMR přenášen v hlavičce RTP paketů EVS. Konkrétní pole v hlavičce je vyhrazeno pro Codec Mode Request. Příjemce, kterým může být uživatelské zařízení (UE) nebo síťový uzel (např. Media Resource Function Processor - [MRFP](/mobilnisite/slovnik/mrfp/) v IMS), monitoruje kvalitu hovoru a/nebo síťové podmínky. Na základě této analýzy (např. vysoká ztrátovost paketů indikující zahlcení nebo dobré podmínky umožňující vyšší kvalitu) rozhodne o optimálním režimu kodeku pro příchozí datový proud. Tento požadavek pak odešle zpět vysílateli nastavením pole [CMR](/mobilnisite/slovnik/cmr/) v RTP paketech, které posílá v opačném směru.

Jak to funguje, zahrnuje kontinuální zpětnovazební smyčku. Vysílatel po přijetí RTP paketu s platnou hodnotou CMR od svého protějšku to interpretuje jako žádost o změnu svých kódovacích parametrů pro následující pakety odesílané *směrem* k tomuto protějšku. Pokud je například detekováno síťové zahlcení, může příjemce odeslat CMR žádající o nižší přenosovou rychlost, robustnější režim (jako je Channel Aware mode) nebo přepnutí na interoperabilní režim [AMR-WB](/mobilnisite/slovnik/amr-wb/) IO. Vysílatel by měl této žádosti vyhovět, aby se zlepšil výkon na koncích. Změna je typicky plynulá, nový režim kodeku se uplatní na vhodné hranici rámce, čímž je zajištěna kontinuita zvuku.

Jeho role v síti je klíčová pro udržení kvality služeb (QoS) a optimalizaci využití zdrojů. V dynamickém rádiovém prostředí, jako je LTE nebo 5G, se podmínky mohou rychle měnit. EVS-CMR poskytuje rychlý mechanismus s nízkou režií pro přizpůsobení hlasového kodeku těmto změnám, mnohem rychleji, než by umožňovala signalizace SIP na aplikační vrstvě. To pomáhá předcházet přerušení hovoru, snižuje vnímatelné zhoršení zvuku při zahlcení a může být také použito k úspoře životnosti baterie v UE žádostí o režim kodeku s nižší složitostí, když vysoká kvalita není nutná. Je to klíčová součást 'channel aware' provozu moderních hlasových služeb.

## K čemu slouží

EVS-CMR byl vytvořen, aby řešil základní omezení statického vyjednávání kodeku používaného v dřívějších hlasových službách. V zastaralých systémech byl kodek a jeho parametry (přenosová rychlost) vyjednány pouze jednou při sestavení hovoru prostřednictvím [SIP](/mobilnisite/slovnik/sip/)/[SDP](/mobilnisite/slovnik/sdp/). Jakmile hovor začal, kodek pracoval v pevném režimu bez ohledu na měnící se síťové podmínky, jako je zvýšený jitter, ztrátovost paketů nebo proměnlivá dostupná šířka pásma. To mohlo vést ke špatnému uživatelskému zážitku při zhoršení síťových podmínek, protože kodek se nemohl adaptovat v reálném čase.

Problém, který řeší, je potřeba dynamické adaptace během hovoru. Bezdrátové sítě jsou ze své podstaty proměnlivé. Uživatel se může přesunout z oblasti s vynikajícím pokrytím na přetížený okraj buňky. Statický kodek s vysokou přenosovou rychlostí by generoval pakety, které by pravděpodobně byly ztraceny, což by způsobilo výrazné přerušování zvuku. Naopak statický kodek s nízkou přenosovou rychlostí za vynikajících podmínek promrhá příležitost pro vyšší věrnost. EVS-CMR poskytuje potřebnou uzavřenou smyčku řízení k optimalizaci kompromisu mezi kvalitou hlasu a odolností pro každý datový proud paketů.

Motivace byla přímo spojena s cíli EVS: poskytnout nejlepší možnou kvalitu hlasu za všech podmínek. Samotný EVS zavedl více provozních režimů (Primary, AMR-WB IO, Channel Aware) s různými přenosovými rychlostmi a profily odolnosti. EVS-CMR je 'mozek', který vybírá optimální režim na základě zpětné vazby v reálném čase. Umožňuje systému být proaktivní – například síťový uzel může požádat o robustnější režim dříve, než se ztrátovost paketů stane pro uživatele slyšitelnou. Tento koncept adaptace režimu kodeku existoval již u dřívějších kodeků (např. u AMR prostřednictvím signalizace v pásmu), a EVS-CMR je jeho evolucí přizpůsobenou bohatšímu souboru režimů a schopností, které kodek EVS nabízí, což z něj činí základní kámen inteligentní správy hlasových služeb v sítích 4G a 5G.

## Klíčové vlastnosti

- Signalizace v pásmu (in-band) v hlavičce RTP datové části pro minimální latenci
- Umožňuje dynamické přepínání mezi režimy EVS Primary, AMR-WB IO a Channel Aware
- Umožňuje adaptaci přenosové rychlosti nahoru nebo dolů na základě zpětné vazby příjemce
- Podporuje žádosti o specifické typy rámců (např. žádost o rámce komfortního šumu)
- Funguje obousměrně; oba konce hovoru mohou odesílat CMR
- Umožňuje plynulou adaptaci bez přerušení hovoru nebo SIP re-INVITE

## Související pojmy

- [EVS – Enhanced Voice Services (specifically, the AMR-WB IO mode: AMR-WB Interoperable)](/mobilnisite/slovnik/evs/)
- [RTP – Real-time Transport Protocol](/mobilnisite/slovnik/rtp/)

## Definující specifikace

- **TS 26.103** (Rel-19) — 3GPP Codec Lists for OoBTC and TrFO
- **TS 26.453** (Rel-19) — EVS Codec Generic Frame Format for 3G CS Networks
- **TS 26.454** (Rel-19) — EVS Codec Mapping for 3G CS Networks
- **TS 29.163** (Rel-19) — Interworking between 3GPP IM CN and CS networks
- **TS 29.414** (Rel-19) — Nb Interface Bearer Transport & Control Protocols
- **TS 29.415** (Rel-19) — Nb User Plane Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [EVS-CMR na 3GPP Explorer](https://3gpp-explorer.com/glossary/evs-cmr/)
