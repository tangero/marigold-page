---
slug: "tty"
url: "/mobilnisite/slovnik/tty/"
type: "slovnik"
title: "TTY – Text Telephone or TeletYpewriter"
date: 2025-01-01
abbr: "TTY"
fullName: "Text Telephone or TeletYpewriter"
category: "Services"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/tty/"
summary: "Telekomunikační služba pro osoby neslyšící, nedoslýchavé nebo s řečovým postižením, umožňující konverzaci pomocí textu v reálném čase prostřednictvím hlasových kanálů. Jde o klíčovou funkci zpřístupně"
---

TTY je telekomunikační služba pro osoby se sluchovým nebo řečovým postižením, která umožňuje konverzaci pomocí textu v reálném čase prostřednictvím kanálu hovoru.

## Popis

Text Telephone (TTY), známý také jako TeletYpewriter nebo telekomunikační zařízení pro neslyšící ([TDD](/mobilnisite/slovnik/tdd/)), je služba umožňující textovou komunikaci v reálném čase prostřednictvím tradičních kanálů hlasového pásma. V systémech 3GPP podpora TTY umožňuje mobilním zařízením generovat, přenášet a zobrazovat textové znaky během hovoru v přepojování okruhů. Text je převáděn na tóny v audio frekvencích (pomocí Baudotova nebo jiných protokolů), které jsou přenášeny v rámci hlasového kanálu. Příjemné zařízení tyto tóny zpětně dekóduje na text pro zobrazení. To umožňuje dvěma uživatelům TTY, nebo uživateli TTY a přepojovací službě, vést psanou konverzaci.

Z architektonického hlediska funkce TTY v mobilní síti zahrnuje jak koncové zařízení, tak síť. Uživatelské zařízení (UE) musí mít aplikaci nebo modem s podporou TTY, který dokáže zakódovat/dekódovat text do specifického schématu audio modulace (např. Baudotův kód 45,45 baudů). Během hovoru v přepojování okruhů UE zachází s daty TTY jako se speciální formou hlasového provozu. Role sítě je primárně transparentní; musí zachovat integritu audiofrekvenčních tónů při jejich průchodu hlasovou cestou. To vyžaduje pečlivé zacházení s hlasovými kodeky a vyvarování se signálového zpracování (jako je potlačení ozvěn nebo detekce hlasové aktivity), které by mohlo zkreslit TTY tóny. Specifikace 3GPP definují specifické režimy provozu (např. TTY přes GSM Full Rate, TTY přes UMTS [AMR](/mobilnisite/slovnik/amr/)) a požadavky na UE, aby signalizovalo síti svou schopnost a režim TTY.

Klíčové komponenty zahrnují TTY terminál (který může být externím zařízením připojeným k mobilnímu telefonu přes adaptér nebo vestavěným softwarem), přepojovací služby používané pro komunikaci mezi uživateli TTY a hlasovými uživateli a síťové plánování kodeků a přenosu. Služba funguje v reálném čase, přičemž znaky jsou odesílány během psaní. Kritickým aspektem je vyjednávání a konfigurace při sestavování hovoru. UE signalizuje svou schopnost TTY ústředně [MSC](/mobilnisite/slovnik/msc/), což může ovlivnit výběr vhodného hlasového kodeku a deaktivaci určitých vylepšení hlasu v přenosové cestě, aby bylo zajištěno spolehlivé rozpoznání TTY tónů.

Role TTY spočívá v tom, že jde o základní službu zpřístupnění. Nejde o datovou službu jako [SMS](/mobilnisite/slovnik/sms/) nebo instant messaging; je to konverzační služba v reálném čase, která využívá infrastrukturu hlasových hovorů. To zajišťuje její fungování i v oblastech bez pokrytí paketovými daty a poskytuje přímou, spojově orientovanou relaci. S vývojem směrem k plně IP sítím (VoLTE, VoNR) standardizoval 3GPP také Real-Time Text ([RTT](/mobilnisite/slovnik/rtt/)) jako modernějšího, IP-based nástupce, ale podpora TTY zůstává klíčová pro zpětnou kompatibilitu a interoperabilitu se staršími TTY zařízeními a službami veřejné telefonní sítě ([PSTN](/mobilnisite/slovnik/pstn/)).

## K čemu slouží

Podpora TTY v mobilních sítích byla zavedena za účelem zajištění přístupnosti telekomunikací pro osoby se sluchovým nebo řečovým postižením. Před jejím zavedením byly mobilní telefony pro konverzaci pomocí textu v reálném čase z velké části nepřístupné, což vytvářelo významnou digitální propast. Problém, který řeší, je poskytnout těmto uživatelům funkční ekvivalenci k hlasové telefonii, což jim umožňuje používat primární mobilní službu – hlasové hovory – ke komunikaci.

Historický kontext je takový, že TTY zařízení se na pevných linkách [PSTN](/mobilnisite/slovnik/pstn/) používají po desetiletí. Jak se mobilní telefonie stala všudypřítomnou, bylo nezbytné rozšířit tuto funkci zpřístupnění i do mobilní domény. Regulační požadavky v mnoha zemích, jako je Americans with Disabilities Act (ADA) v USA, poháněly potřebu standardizované implementace. Bez standardizované podpory TTY by výrobci a operátoři vytvářeli nekompatibilní řešení, což by poškozovalo interoperabilitu a uživatelský zážitek.

Standardizace 3GPP řešila technickou výzvu přenosu úzkopásmových TTY tónů přes digitální hlasové kodeky navržené pro lidskou řeč, které mohou zkreslovat jiné než řečové signály. Účelem bylo definovat spolehlivou metodu fungující napříč různými technologiemi radiového přístupu (GSM, UMTS) a základními sítěmi, která zajistí, že TTY hovor může být předán mezi buňkami a dokonce mezi sítěmi 2G/3G bez přerušení služby. Také musela umožňovat připojení ke starším TTY zařízením PSTN a přepojovacím službám. Zatímco novější technologie jako [RTT](/mobilnisite/slovnik/rtt/) nabízejí lepší funkce, TTY zůstává klíčovou přechodovou technologií a jeho podpora je dokladem závazku odvětví k inkluzivní komunikaci.

## Klíčové vlastnosti

- Umožňuje konverzaci pomocí textu v reálném čase přes hlasové kanály s přepojováním okruhů
- Používá modulaci audiofrekvenčními tóny (např. Baudotův kód) k reprezentaci textových znaků
- Vyžaduje transparentnost sítě k zachování integrity tónů při průchodu hlasovými kodeky
- Podporuje připojení ke starším TTY zařízením PSTN a telefonním přepojovacím službám
- Zahrnuje signalizaci schopností UE směrem k síti pro správnou konfiguraci hovoru
- Definuje provozní režimy pro kompatibilitu s kodeky GSM Full Rate a UMTS AMR

## Definující specifikace

- **TS 26.226** (Rel-19) — Cellular Text Telephone Modem (CTM)
- **TS 26.230** (Rel-19) — CTM C Code Implementation for Text Transmission
- **TS 26.231** (Rel-19) — CTM Minimum Performance Requirements Testing
- **TS 43.318** (Rel-19) — Generic Access Network (GAN) Stage 2
- **TR 43.902** (Rel-19) — GAN Enhancements Feasibility Study
- **TS 44.318** (Rel-19) — Generic Access Network (GAN) Interface Procedures

---

📖 **Anglický originál a plná specifikace:** [TTY na 3GPP Explorer](https://3gpp-explorer.com/glossary/tty/)
