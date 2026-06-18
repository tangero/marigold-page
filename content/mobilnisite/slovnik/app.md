---
slug: "app"
url: "/mobilnisite/slovnik/app/"
type: "slovnik"
title: "APP – Application-defined RTCP packet"
date: 2025-01-01
abbr: "APP"
fullName: "Application-defined RTCP packet"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/app/"
summary: "Rozšiřující mechanismus pro protokol RTCP (Real-time Transport Control Protocol), který umožňuje aplikacím definovat vlastní typy paketů pro řídicí informace specifické pro danou relaci. Umožňuje boha"
---

APP je rozšiřující mechanismus RTCP, který umožňuje aplikacím definovat vlastní typy paketů pro řídicí informace specifické pro danou relaci, což umožňuje bohatší řízení mediální relace.

## Popis

Aplikačně definovaný paket [RTCP](/mobilnisite/slovnik/rtcp/) (APP) je typ paketu v protokolu RTCP (Real-time Transport Control Protocol), standardizovaný [IETF](/mobilnisite/slovnik/ietf/) a přijatý ve specifikacích 3GPP pro služby IP Multimedia Subsystem (IMS) a Packet-Switched Streaming ([PSS](/mobilnisite/slovnik/pss/)). RTCP je doplňkový protokol k [RTP](/mobilnisite/slovnik/rtp/) (Real-time Transport Protocol), který poskytuje řídicí informace pro mediální relaci mimo přenosovou cestu, včetně zpětné vazby o kvalitě služeb (prostřednictvím Sender a Receiver Reports), identifikace účastníků a časování relace. Typ paketu APP poskytuje standardizovaný, rozšiřitelný kontejner pro data specifická pro aplikaci, která je třeba přenášet spolu se standardním řídicím provozem RTCP. Jeho struktura je definována v IETF [RFC](/mobilnisite/slovnik/rfc/) 3550 a následných aktualizacích a specifikace 3GPP podrobně popisují jeho použití v telekomunikační architektuře.

Paket APP se skládá ze standardní hlavičky [RTCP](/mobilnisite/slovnik/rtpcp/), která jej identifikuje jako typ paketu APP ([PT](/mobilnisite/slovnik/pt/)=204), následované polem podtypu, 4oktetovým polem name (sloužícím jako jedinečný identifikátor aplikace) a daty závislými na aplikaci. 32bitové pole name, typicky složené ze čtyř znaků ASCII, umožňuje různým aplikacím nebo výrobcům definovat vlastní sémantiku paketů bez rizika kolize. Následující data závislá na aplikaci mohou nést jakékoli informace, které aplikace považuje za nezbytné, jako jsou vlastní metriky, synchronizační signály, řídicí příkazy nebo proprietární mechanismy zpětné vazby nepokryté standardními reportovacími bloky RTCP.

V ekosystému 3GPP se pakety APP používají ve službách jako IMS Multimedia Telephony (MMTel) a Packet-Switched Streaming pro přenos rozšířených řídicích informací relace. Mohou například nést informace související s rozšířeními reportování kvality médií, řízení forward error correction ([FEC](/mobilnisite/slovnik/fec/)) na aplikační vrstvě nebo specifické příkazy pro adaptaci médií. Protokol funguje tak, že odesílající aplikační entita zapouzdří svá vlastní data do formátu paketu APP a přenese je stejným komunikačním kanálem jako ostatní pakety RTCP, typicky pomocí stejné transportní asociace (např. páru UDP portů) jako RTP mediální proud. Přijímající entity, které znají konkrétní 'jméno' a formát paketu APP, data interpretují a podle toho jednají, což umožňuje uzavřený řídicí mechanismus s ohledem na aplikaci.

Úlohou paketů APP v síti je překlenout propast mezi standardizovanou, obecnou zpětnou vazbou základního RTCP a specifickými, často proprietárními potřebami pokročilých multimediálních aplikací. Umožňují poskytovatelům služeb a vývojářům aplikací inovovat a optimalizovat mediální relace bez nutnosti změn základních standardů RTP/RTCP. Tato rozšiřitelnost je klíčová pro nasazování nových funkcí, provádění podrobných diagnostik výkonu a implementaci složité logiky zpracování médií zpětně kompatibilním způsobem, protože starší implementace RTCP, které konkrétní paket APP nerozumí, jej mohou na základě pravidel pro typy paketů RTCP bezpečně ignorovat.

## K čemu slouží

Paket APP byl vytvořen, aby odstranil omezení původní specifikace RTCP, která definovala pevnou sadu typů paketů (SR, RR, SDES, BYE) pro standardizované řídicí funkce. Zatímco tyto byly dostačující pro základní reportování kvality a správu relací, vznikající multimediální aplikace vyžadovaly možnost vyměňovat si vlastní řídicí informace specifické pro jejich provoz. Například aplikace mohla potřebovat signalizovat změnu specifického režimu kodeku, přenášet proprietární metriky kvality nebo synchronizovat pomocné datové toky. Bez standardizovaného rozšiřujícího mechanismu vývojáři přistupovali k nestandardním metodám, jako bylo používání nedefinovaných typů paketů nebo vkládání dat do jiných polí, což vedlo k problémům s interoperabilitou a kolizím.

Zavedení typu paketu APP v IETF RFC 3550 poskytlo formální, budoucně bezproblémový rozšiřující mechanismus. Vyřešilo problém vyhrazením specifického identifikátoru typu paketu (204) pro použití aplikací a definováním jednoduché struktury s jmenným prostorem pro prevenci konfliktů. To umožnilo různým aplikacím, dokonce i v rámci stejné relace, definovat a používat vlastní řídicí pakety bez vzájemného rušení nebo narušení základních funkcí RTCP. Motivací bylo zachovat stabilitu a interoperabilitu základního protokolu RTP/RTCP a zároveň umožnit inovace a přizpůsobení na aplikační vrstvě.

V kontextu 3GPP bylo přijetí a specifikace použití paketů APP v dokumentech jako TS 26.114 (IMS Multimedia Telephony) a TS 26.234 (PSS) hnáno potřebou rozšířeného řízení médií v službách úrovně operátora. Jak se služby IMS vyvíjely pro podporu bohaté komunikace, jako je videotelefonie a streamování s adaptivním datovým tokem, standardní hlášení RTCP byla nedostatečná pro přenos všech potřebných řídicích parametrů. Pakety APP poskytly standardizované médium pro rozšíření definovaná 3GPP, jako je přenos specifických metrik kvality uživatelského prožitku (QoE) z uživatelského zařízení (UE) na server, což umožňuje inteligentnější doručování médií a optimalizaci sítě v rámci infrastruktury telekomunikačního operátora.

## Klíčové vlastnosti

- Poskytuje standardizovaný rozšiřující mechanismus pro RTCP využívající typ paketu 204
- Obsahuje 4oktetové pole name s kódováním ASCII pro jedinečnou identifikaci aplikace a oddělení jmenných prostorů
- Přenáší data závislá na aplikaci proměnné délky pro vlastní řídicí informace
- Zachovává zpětnou kompatibilitu, protože nerozpoznané pakety APP mohou být staršími implementacemi ignorovány
- Umožňuje specifické inovace výrobců a aplikací bez modifikace základních standardů RTP/RTCP
- Používá se ve službách 3GPP IMS a PSS pro rozšířené řízení a reportování mediální relace

## Související pojmy

- [RTCP – Real-time Transport Control Protocol](/mobilnisite/slovnik/rtcp/)
- [RTP – Real-time Transport Protocol](/mobilnisite/slovnik/rtp/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TS 23.333** (Rel-19) — MRFC-MRFP Mp Interface Requirements
- **TS 23.334** (Rel-19) — IMS-ALG to IMS-AGW Interface (Iq) Stage 2
- **TS 26.114** (Rel-19) — IMS Multimedia Telephony Media Handling
- **TS 29.162** (Rel-19) — IMS-IP Network Interworking
- **TS 29.163** (Rel-19) — Interworking between 3GPP IM CN and CS networks
- **TS 29.205** (Rel-19) — BICC Protocols for Bearer-Independent CS Core Network
- **TS 36.750** (Rel-14) — Study on enhancement of VoLTE

---

📖 **Anglický originál a plná specifikace:** [APP na 3GPP Explorer](https://3gpp-explorer.com/glossary/app/)
